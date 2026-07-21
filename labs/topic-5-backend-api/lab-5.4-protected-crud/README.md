# Lab 5.4 — Protected CRUD: Enrollments Scoped to the Signed-in User

> **Topic 5** · ~60 min · Builds on Lab 5.3 (accounts, bcrypt + JWT)

### 📖 The build so far
By the end of Lab 5.3, users could sign up, sign in, and carry a verified JWT. But the app still can't *do* anything as that user. **In this lab you add:** protected, per-user data — a full CRUD layer over the `enrollments` table where every read and write is scoped to *you* by the id in your token. You'll build the enrol button, the "My learning" list, and the route guard — then attack the API by asking to delete **someone else's** enrollment and watch it return 404. By the end, each signed-in student has their own enrolments, and no one can touch anyone else's.

## What you will build

The **protected write side** of the app:

- **Server:** `api/enrollments/index.js` (GET my enrolments joined to their course;
  POST to enrol me) and `api/enrollments/[id].js` (PATCH the status, DELETE — each
  scoped by the token). Both derive the user id from `requireAuth(req)`.
- **Browser:** `src/hooks/useEnrollments.js` (the CRUD verbs, with optimistic UI),
  `EnrollButton` (on each course), `EnrollmentList` (mark complete / remove), and
  `ProtectedRoute` (the dashboard is signed-in only).

## Concepts you will meet

| Concept | In one line |
|---|---|
| The WHERE clause **is** the access control | No hidden database policy here — `where user_id = ${userId}` is what keeps users' data apart. |
| Identity from the token | The browser sends `{ courseId }`, never a user id; the server supplies it from the verified JWT. |
| IDOR | An **Insecure Direct Object Reference** — an id in the URL is a *request*, not a *permission*. |
| Ownership in SQL | `where id = ${id} and user_id = ${userId}` — a row you don't own simply doesn't match → 404. |
| `unique (user_id, course_id)` | The database, not the UI, guarantees you can't enrol twice (409 on conflict). |
| Optimistic UI | Update local state first for an instant feel; snapshot and roll back if the server says no. |

## Before you start

Have Lab 5.3 working (you can sign in and stay signed in). Copy this lab in:

```bash
cp -R "labs/topic-5-backend-api/lab-5.4-protected-crud/api/." cookbake/api/
cp -R "labs/topic-5-backend-api/lab-5.4-protected-crud/src/." cookbake/src/
```

That adds `api/enrollments/index.js`, `api/enrollments/[id].js`,
`src/hooks/useEnrollments.js`, `src/components/EnrollButton.jsx`,
`src/components/EnrollmentList.jsx` and `src/components/ProtectedRoute.jsx`. Wire
`<EnrollButton course={course} />` into `CourseDetailPage`, and render
`<EnrollmentList …>` on the dashboard's "My courses" page. (The full route map —
`ProtectedRoute` guarding `/dashboard` — is assembled in Topic 6; this lab ships
the guard and the data.)

---

## Step 1 — Protect the route, and derive identity from the token

Open `api/enrollments/index.js`. The first real line inside the handler:

```js
const userId = requireAuth(req)   // the verified `sub` of a signed JWT — not req.body, not a query param
```

This is **the** important line. `userId` is the cryptographically verified id from
the token (Lab 5.3). It is *not* `req.body.userId` and *not* a query string —
those are just things the caller typed. This is the only identity we trust, and
everything below scopes to it.

## Step 2 — The WHERE clause is the access control

GET returns *my* enrolments, joined to their course so the "My learning" card can
show the title and emoji in one request:

```js
const enrollments = await sql`
  select e.id::int as id, e.course_id::int as course_id, e.status, e.notes, e.created_at,
         json_build_object('id', c.id::int, 'title', c.title, 'emoji', c.emoji, /* … */) as courses
  from enrollments e
  join courses c on c.id = e.course_id
  where e.user_id = ${userId}
  order by e.created_at desc
`
```

There is **no hidden database policy** behind this API doing the scoping for us. This
`where e.user_id = ${userId}` **is** the access control. Forget it and every user
sees everyone's data. Say that out loud: in this architecture, the security is a
line of SQL you wrote, not a database feature you switched on. That's the whole
point of the three tiers — it lives on the server, where the user can't edit it.

## Step 3 — The caller chooses the COURSE, not the USER

POST enrols me. Look at what the browser sends and what the server supplies:

```js
const { courseId, notes = '' } = readBody(req)   // caller chooses the course
// …
insert into enrollments (user_id, course_id, status, notes)
values (${userId}, ${courseId}, 'active', ${notes})   // server supplies the user
on conflict (user_id, course_id) do nothing
returning …
```

The `${userId}` comes from the token, never from the body. This is the difference
between "enrol **me** in course 7" and "enrol **anyone I like** in course 7". If
the body could carry a user id, so could curl — and it would carry *yours*.

Zero rows back means the `unique (user_id, course_id)` constraint fired — you're
already enrolled — which is a **409**, guaranteed by the **database**, not the UI:

```js
if (rows.length === 0) throw new HttpError(409, 'You are already enrolled in this course.')
```

Two fast clicks can't create two rows, because the constraint, not a client check,
is the guarantee.

## Step 4 — IDOR: an id in the URL is a REQUEST, not a PERMISSION

Open `api/enrollments/[id].js` and read the header comment — it's the lesson of the
whole lab. `id` comes from the address bar, so anyone can change a `4` to a `5` and
ask to delete enrollment #5, which may belong to another student. So the id alone
must **never** be enough. Every statement carries **two** conditions:

```js
update enrollments set status = ${status}
where id = ${id} and user_id = ${userId}
                    ^^^^^^^^^^^^^^^^^^^^^ from the verified JWT — the caller can't influence it
returning …
```

```js
delete from enrollments where id = ${id} and user_id = ${userId} returning id::int as id
```

The ownership check lives in the **SQL**, not in an `if` in JavaScript. A row you
don't own simply doesn't match, so Postgres updates/deletes **nothing** and we
report **404** — telling a prober nothing about what exists. Getting this wrong is
called an **Insecure Direct Object Reference (IDOR)**, and it is one of the most
common real-world API vulnerabilities.

PATCH also **whitelists** the status so a caller can't set it to anything:

```js
if (!['active', 'completed', 'cancelled'].includes(status)) throw new HttpError(400, 'status must be active, completed or cancelled.')
```

## Step 5 — The browser never sends a user id (`useEnrollments`)

Open `src/hooks/useEnrollments.js`. Look at what's **missing** from every call: a
user id. `GET /api/enrollments` takes no "whose?" parameter, and `enroll()` sends
just `{ courseId }`:

```js
const data = await api.get('/enrollments')                 // no user id
const created = await api.post('/enrollments', { courseId, notes })   // no user id
```

The browser says **what** it wants; the server decides **who** is asking. If this
hook *could* pass a user id, then so could anyone with curl — and they'd pass
yours.

`updateStatus` and `remove` are **optimistic**: they change local state first so
the click feels instant, then roll back if the server disagrees:

```js
const previous = enrollments
setEnrollments(prev => prev.map(e => e.id === id ? { ...e, status } : e))  // optimistic
try { await api.patch(`/enrollments/${id}`, { status }); return {} }
catch (err) { setEnrollments(previous); return { error: { message: err.message } } }  // roll back
```

The trade-off: optimistic UI is snappy but you must snapshot the previous state and
restore it on failure. `enroll` uses a middle path — it takes the created row back
from the API and prepends it, no full refetch.

## Step 6 — Guard the dashboard (`ProtectedRoute`)

`ProtectedRoute` gates everything nested inside it:

```jsx
const { user, loading } = useAuth()
if (loading) return <p className="section muted">Checking your session…</p>
if (!user)   return <Navigate to="/login" replace state={{ from: location }} />
return <Outlet />
```

The `loading` check is the important line: on a hard refresh the auth provider
needs a tick to verify the stored token (via `/auth/me`), and during that tick
`user` is null. Redirect on `!user` **without** waiting for `loading` and a
signed-in user gets bounced to `/login` on every refresh. Wait first. `state.from`
remembers where they were headed so `/login` can send them back.

## Step 7 — Enrol, then attack your own API (the IDOR probe)

With both servers running and signed in, click **Enrol** on a course — it appears
in "My learning". Mark it complete, remove it, sign out and back in: your
enrolments persist because they live in Postgres, scoped to your user.

Now **prove the ownership check**. Sign in as user A, note one of your enrolment
ids and your token, then try to delete an id you don't own (or use A's token
against B's enrolment id):

```bash
TOKEN='<paste user A's JWT from localStorage: cookbake.token>'

# your own enrolment id -> 200 deleted
curl -s -X DELETE http://localhost:3000/api/enrollments/1 -H "Authorization: Bearer $TOKEN"

# an id that isn't yours -> 404, and the row is untouched
curl -s -X DELETE http://localhost:3000/api/enrollments/999 -H "Authorization: Bearer $TOKEN"
# {"error":"Enrollment not found."}
```

The second returns **404** even though the row exists — because
`and user_id = ${userId}` removed it from the match. Try the same in DevTools by
editing the id `useEnrollments.remove` sends: still 404. The URL let you *ask*; the
token decided you *couldn't*.

---

## 🎤 Vibe prompt

```text
In my three-tier app (React -> /api/* serverless -> Neon) with JWT auth, add
protected CRUD for enrollments. api/_lib/auth.js exports requireAuth(req) (returns
the user id from a VERIFIED JWT), sendError, readBody, requireMethod, HttpError.
Table: enrollments(id, user_id, course_id, status check active|completed|cancelled,
notes, created_at) with unique(user_id, course_id).

1. api/enrollments/index.js — requireMethod(req,'GET','POST'); userId =
   requireAuth(req). GET: return MY enrollments joined to courses via
   json_build_object(...) as courses, `where e.user_id = ${userId}` order by
   created_at desc. POST {courseId, notes?}: insert (user_id=${userId} FROM THE
   TOKEN, course_id=${courseId}, 'active', notes) `on conflict (user_id, course_id)
   do nothing`; zero rows -> 409; else return the joined row, 201. NEVER read the
   user id from the body or query.

2. api/enrollments/[id].js — requireMethod(req,'PATCH','DELETE'); userId =
   requireAuth(req); id = req.query.id. PATCH {status}: whitelist status to
   active|completed|cancelled (else 400); `update ... where id = ${id} and user_id =
   ${userId}`; zero rows -> 404. DELETE: `delete ... where id = ${id} and user_id =
   ${userId}`; zero rows -> 404. The ownership check MUST be in the SQL WHERE, not a
   JS if.

3. src/hooks/useEnrollments.js — useEnrollments() -> { enrollments, loading, error,
   enroll, updateStatus, remove, reload }. Load GET /enrollments when a user is
   signed in. enroll(courseId, notes) POSTs { courseId, notes } (NO user id) and
   prepends the returned row; on failure return { error }. updateStatus/remove apply
   optimistically and roll back on error. Never send a user id anywhere.

Return { data } / { error } from the mutations (never throw). Use existing CSS.
```

## 🔍 Read what the AI wrote

- **Does every `[id]` statement carry `and user_id = ${userId}`?** The single most
  important check in this lab. An `update`/`delete` filtered by `id` alone is a
  textbook IDOR — anyone can edit the number and touch another user's row.
- **Is the user id read from the token, never the body/query?** Grep for
  `req.body.userId` / `req.query.userId`. Identity must come from `requireAuth(req)`.
- **Is the ownership check in SQL or in JavaScript?** A JS `if (row.user_id !==
  userId)` still *fetched* the other user's row first (and might leak it). Put the
  condition in the WHERE so the row never comes back.
- **Is `409` handled via the unique constraint?** Enrolling twice should be a clean
  409 from `on conflict`, not a 500 or a duplicate row.
- **Does the browser ever send a user id?** If `enroll`/`GET` includes one, it's
  both pointless and a red flag — the server ignores it, and the instinct to send
  it is the bug to unlearn.
- **Optimistic rollback present?** Local state changed with no snapshot/restore on
  error leaves the UI showing a change that didn't happen.
- **Does `ProtectedRoute` wait for `loading`?** Redirecting on `!user` before the
  session resolves bounces signed-in users on every refresh.

## 🧠 Why it works

**Access control is a line of SQL, and it's yours.** With no database-enforced row
policy in this architecture, nothing scopes a query to the current user unless *you* write it.
`where user_id = ${userId}` on every read, and `and user_id = ${userId}` on every
write, is the entire boundary. That sounds fragile, but it's actually the honest
version of security: it's visible, it's in one place per route, and it runs on the
server where the client can't reach it. A database-enforced row policy would move this
into the database; here it lives in the function. Either way the rule is the same — *the server, keyed off
the verified token, decides which rows you may touch.*

**Identity is supplied, never accepted.** The browser is allowed to choose the
*object* of an action (which course, which enrollment id) but never the *subject*
(which user). The subject always comes from `requireAuth(req)`. This inversion is
what makes the API safe against its own clients: it doesn't matter what a malicious
browser sends, because the one field that decides *whose data this is* is the one
field the browser can't set. `{ courseId }` is a request; `${userId}` is the
answer to "and who are you?" — and only the token can answer that.

**IDOR, and why the fix is one clause.** The most common way apps leak data is
trusting an id in the URL. `DELETE /api/enrollments/5` looks innocent, but `5` is
attacker-controlled — increment it and you're asking about someone else's row. The
naive server does `delete where id = 5` and cheerfully deletes it. Adding
`and user_id = ${userId}` closes the hole completely: a row that isn't yours
doesn't match the WHERE, so nothing is deleted and Postgres reports zero affected
rows, which we surface as a **404**. Crucially the check is in the *query*, not a
JavaScript `if` after fetching the row — because fetching it first already exposed
data you shouldn't have read. The id says *which* row; the token says *whose*; both
go in the WHERE.

**The database guarantees "once", not the button.** `EnrollButton` disables itself
once you're enrolled — but that's a UX nicety, not a guarantee. Anyone can POST
twice with curl, and two fast clicks can race past a disabled button. The real
guarantee is `unique (user_id, course_id)` in the schema: the second insert
*cannot* create a row, it collides, and `on conflict do nothing` returns zero rows
which we turn into a 409. Correctness that must hold no matter what the client does
belongs in the database, as a constraint — not in the UI, as a hope.

**Optimistic UI, honestly.** Users feel an app as fast when it reacts the instant
they click. Optimistic updates deliver that by changing local state immediately and
talking to the server in the background. The price is correctness work: snapshot
the previous state and roll back if the server says no, because for a moment your
UI is *predicting* the outcome rather than reporting it. The simpler, slower
alternative is to `await` the write and refetch — always correct, never out of
sync, but every action has a visible pause. Knowing which to reach for is an
engineering judgement, not a default; `useEnrollments` picks optimistic for
status/remove and a return-the-row middle path for enrol.

## ✅ Check your work

- [ ] Signed in, you can enrol, mark complete, and remove — and the changes persist
      across sign-out/in (they're in Postgres).
- [ ] Enrolling in the same course twice returns a friendly "already enrolled"
      (409), not a duplicate row or a 500.
- [ ] `DELETE`/`PATCH` on an enrollment id you don't own returns **404** and leaves
      the row untouched (verify with curl or DevTools).
- [ ] Neither `useEnrollments` nor any request body sends a user id.
- [ ] Both `[id]` statements carry `and user_id = ${userId}` in the SQL.
- [ ] `ProtectedRoute` shows "Checking your session…" during `loading` and only
      redirects once it's false — a refresh on `/dashboard` keeps you there.

## 🛠 Your turn

1. **Reviews, the same pattern.** `api/reviews/*` mirrors enrolments: `GET
   ?courseId=` is public, `POST` is auth'd and UPSERTs your one review
   (`on conflict (user_id, course_id) do update`), and `DELETE /api/reviews/:id`
   carries `and user_id = ${userId}`. Wire `ReviewForm` / `ReviewList` into
   `CourseDetailPage` and confirm you can only delete your **own** review.
2. Add a `status` filter to the dashboard (`active` / `completed`) that narrows the
   list client-side, then move it server-side as `GET /api/enrollments?status=` —
   remembering to keep `where user_id = ${userId}` and add
   `(${status ?? null}::text is null or status = ${status ?? null})`.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| A user can delete/edit another user's enrollment | `[id]` statement filtered by `id` alone (IDOR). | Add `and user_id = ${userId}` to every `update`/`delete`. |
| `401` on enrol even though you're signed in | The token isn't attached, or the route wasn't reached through `requireAuth`. | Ensure `api.js` sends `Authorization: Bearer` and the route calls `requireAuth(req)`. |
| Enrolling twice 500s | Missing `on conflict (user_id, course_id) do nothing` / zero-rows check. | Use the conflict clause and throw 409 when no row returns. |
| Every user sees everyone's enrolments | The GET query dropped `where user_id = ${userId}`. | Scope the read to the token's user id — that clause *is* the access control. |
| Signed-in user bounced to `/login` on refresh | `ProtectedRoute` redirected before `loading` resolved. | Return a "checking session" state while `loading` is true. |
| Optimistic change sticks even though the server rejected it | No snapshot/rollback in `updateStatus`/`remove`. | Save `previous` and restore it in the `catch`. |

---
### ✅ Cook & Bake Academy after this lab
Each signed-in student has their own enrolments — created, updated and deleted through protected API routes where the token, not the request, decides whose data is whose.
