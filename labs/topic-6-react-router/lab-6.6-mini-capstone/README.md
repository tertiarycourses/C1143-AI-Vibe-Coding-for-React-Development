# Lab 6.6 — Mini-Capstone: Add Course Reviews, On Your Own

> **Topic 6** · ~60 min · Builds on Lab 6.5 (the whole app is deployed on Vercel + Neon)

### 📖 The build so far
By the end of Lab 6.5, the full **Cook & Bake Academy** 🍞 was live in production on Vercel + Neon — a three-tier app with a Postgres catalogue of 20 courses, real accounts (bcrypt + JWT), protected enrolments and a private student dashboard. Every earlier lab handed you the steps. **This one does not.** In this mini-capstone you add one brand-new **end-to-end** feature — star-rated **Course Reviews** — mostly by *vibe-coding it yourself*: you write the prompts, read the generated code against everything this course taught you, correct it, and redeploy. By the end, every course detail page shows real student reviews and a live average rating, in production. This is the payoff of the whole course.

## The brief

Ship a **Course Reviews** feature into the live Cook & Bake Academy app. When you are done:

- **any visitor** (even signed-out) can read a course's reviews and see its **average star rating** on the detail page;
- **any signed-in student** can post exactly **one** review per course (1–5 stars + text), **edit** it, or **delete** it;
- nobody can post, edit or delete a review as someone else — and you will prove it with `curl`.

You already have the pieces this rests on: a serverless API over Neon (Topic 5), the `requireAuth(req)` identity helper and the `and user_id = ${userId}` ownership pattern (Lab 5.4), custom hooks and derived state (Topic 4), controlled forms, keys and conditional rendering (Topic 3), and auth-gated routes (this topic). The reviews feature touches **all** of them.

Concretely, you will build:

- **The `/api/reviews` routes** — `api/reviews/index.js` (a **public** GET list + an auth'd POST that UPSERTs *your* one review) and `api/reviews/[id].js` (a DELETE scoped to your token). The **server** enforces everything: `requireAuth` on the writes, validation of `rating`/`body`, ownership in the SQL `where`, and one-per-course via the unique constraint.
- **A `useReviews(courseId)` hook** — loads `GET /api/reviews?courseId=`, exposes `submit`/`remove`, finds *your* review, and **derives** the count and average at render — the same data-layer shape as `useEnrollments`.
- **A `StarRating` component** — read-only when given only a `value`, and interactive (real keyboard-accessible `<button>`s) when also given `onChange`.
- **A `ReviewForm`** — a controlled form only signed-in students see, seeded from any existing review so it does double duty for *write* and *edit*.
- **A `ReviewList`** — renders the public list and shows a Delete button only on your own rows (UX only).
- **A DERIVED average** shown next to the course title — computed from the reviews array at render, **never stored** on the course row.
- **A redeploy** — a `git push` that puts the whole feature (front end *and* the new serverless function) live.

The `reviews` table is **already** in `neon/schema.sql`, so if you ran that against your database in Topic 5, it exists. A **model answer** lives in this lab's `src/` and `schema-reviews.sql`. Build it yourself first; only open those files to compare, or when you are truly stuck.

## Why this is the real test

A reviews feature is the whole course in one deliverable: a new API route with parameterised SQL, identity taken from the JWT (never the body), a custom hook with three states, a controlled form, a derived average, and a production redeploy. Your job is the real vibe-coding loop — **prompt, read what the AI wrote, correct it, run it.** The agent will happily write code that *looks* right and quietly opens a hole: it reads a `userId` out of the request body, forgets to check `rating`, gates deletion with a JavaScript `if` instead of the SQL `where`, or stores an average that drifts. Catching that is the skill this whole course has been building toward.

## Concepts you will meet

| Concept | In one line |
|---|---|
| Public read, protected write | `requireAuth(req)` is called **inside the POST branch**, so signed-out visitors can still READ but only a signed-in student can WRITE. |
| Identity from the token | The browser sends `{ courseId, rating, body }`, never a user id; the server supplies it from the verified JWT. |
| UPSERT on a unique key | One statement — `on conflict (user_id, course_id) do update` — makes POST do double duty for write **and** edit, race-free. |
| Ownership in SQL | `delete … where id = ${id} and user_id = ${userId}` — a review you don't own simply doesn't match → 404. |
| Server-side validation | `rating` 1–5 and `body` length are checked in the function *and* the schema — never trust the form. |
| Derived state | `average` and `count` fall out of the reviews array at render; storing them on the course is a bug waiting to drift. |
| A join is not a licence | GET joins `users` to show the reviewer's **name only** — never email, never `password_hash`. |

## Before you start

Have Lab 6.5 working — the app is deployed, you can sign in, enrol and reach `/dashboard`. Make sure the `reviews` table exists in your database (it ships in `neon/schema.sql`; the exact block is reproduced in this lab's `schema-reviews.sql` for reference):

```bash
psql "$DATABASE_URL" -c '\d reviews'   # the table is already there from Topic 5
```

This lab ships a **model answer** so you can check yourself:
`api/reviews/index.js`, `api/reviews/[id].js`, `src/hooks/useReviews.js`,
`src/components/StarRating.jsx`, `src/components/ReviewForm.jsx`,
`src/components/ReviewList.jsx`, and the reviews block wired into
`src/pages/CourseDetailPage.jsx`. **Try to build each one from the prompts below
first.** Only copy the model answer in to compare, or when you are stuck:

```bash
cp -R labs/topic-6-react-router/lab-6.6-mini-capstone/src/. cookbake/src/
```

---

## 🎤 The loop: Prompt → Read → Correct

Five prompts, roughly in build order. For each one: **prompt** the agent, **read**
every line it wrote against the checks that follow, and **correct** it before you
run it. The prompts deliberately name the traps — the reading is where you catch
the AI ignoring them.

### 1 — The API route (`api/reviews/index.js`)

The `reviews` table already exists — its `unique (user_id, course_id)` **is** the
feature spec (one review per student per course). Read it, then prompt for the route:

```text
Create api/reviews/index.js — a Vercel serverless function for my three-tier app
(React -> /api/* -> Neon). api/_lib/db.js exports `sql` (a tagged-template
function). api/_lib/auth.js exports requireAuth(req) (returns the user id from a
VERIFIED JWT), readBody, requireMethod, sendError, HttpError.

Table: reviews(id, user_id, course_id, rating int check 1..5,
body text check length 1..2000, created_at, unique(user_id, course_id)).

GET  /api/reviews?courseId=  : PUBLIC, no token. Return that course's reviews
     newest first, joined to users for the reviewer NAME only — select u.name and
     nothing else from that table (never email, never password_hash). Cast ids
     ::int.
POST /api/reviews {courseId, rating, body} : call requireAuth(req) INSIDE the POST
     branch for the user id — NEVER read a user id from the body. Validate rating
     is a whole number 1..5 and body length 1..2000 server-side. UPSERT with
     `on conflict (user_id, course_id) do update`. Tagged-template SQL only.

requireMethod(req,'GET','POST'); wrap in try/catch ending in sendError(res, err).
```

**Read what it wrote:**

- **Is `requireAuth` *inside* the POST branch, not at the top of the handler?**
  Call it at the top and you lock signed-out visitors out of *reading* reviews.
  Reads take no token; writes do. That asymmetry is the point.

  ```js
  if (req.method === 'GET') { /* no token needed — public list */ }

  const userId = requireAuth(req)   // only reached on POST — the write
  ```

- **Does the GET select only `u.name` from the join?** A join to `users` is not
  permission to expose every column you can now reach. `email` and
  `password_hash` must never appear in the select.

- **Is the write an UPSERT that can only touch *your* row?** One statement,
  race-free, `user_id` taken from the token:

  ```js
  insert into reviews (user_id, course_id, rating, body)
  values (${userId}, ${courseId}, ${rating}, ${body.trim()})
  on conflict (user_id, course_id) do update
    set rating = excluded.rating, body = excluded.body, created_at = now()
  returning id::int as id, user_id::int as user_id, rating, body, created_at
  ```

  Because `user_id` is `${userId}` from the JWT, there is no way to phrase this
  request so it overwrites someone else's review — and the unique constraint means
  two fast submissions can't create two rows.

- **Is `rating`/`body` validated in the function?** The schema's `check`
  constraints are the backstop; a clear 400 from the function is the friendly
  front. Do both — never rely on the form alone.

### 2 — The delete route (`api/reviews/[id].js`)

Same rule as `enrollments/[id].js` (Lab 5.4): the id in the URL says **which**
row, the token says **whose**. Both go in the WHERE.

```text
Create api/reviews/[id].js. requireMethod(req,'DELETE'); userId = requireAuth(req);
id = req.query.id. `delete from reviews where id = ${id} and user_id = ${userId}
returning id::int as id`. Zero rows -> throw HttpError(404). The ownership check
MUST be in the SQL WHERE, not a JavaScript if.
```

**Read what it wrote:** the statement must carry **both** conditions:

```js
delete from reviews
where id = ${id} and user_id = ${userId}   // id = which, token = whose
returning id::int as id
// 0 rows -> 404. You cannot delete someone else's review by guessing its id.
```

A review you don't own doesn't match the WHERE, so Postgres deletes **nothing** and
you report **404** — telling a prober nothing about what exists. Gating deletion
with a JavaScript `if` after fetching the row is a textbook Insecure Direct Object
Reference (IDOR): you already read a row you had no right to.

### 3 — The hook (`src/hooks/useReviews.js`)

```text
Write src/hooks/useReviews.js like useEnrollments. Load GET /api/reviews?courseId=
into state with loading/error. Expose submit({rating, body}) that POSTs
{courseId, rating, body} (NO user id) and refetches, and remove(id) that DELETEs
/reviews/:id. Find myReview = the signed-in user's own review or null. DERIVE
`count` and `average` from the reviews array at render — never store them. Return
{ data } / { error } from the mutations, never throw.
```

**Read what it wrote:**

- **Is the average *derived*, not stored?** It must be computed each render so it
  can't drift from the list, and it must be `null` — never `NaN` — on zero reviews:

  ```js
  const count = reviews.length
  const average = count
    ? Math.round((reviews.reduce((sum, r) => sum + r.rating, 0) / count) * 10) / 10
    : null   // derived at render, not stored on the course
  ```

- **Does `myReview` compare like-typed ids?** The API casts every id `::int`, so
  this is `3 === 3`, not `3 === "3"`. Get the cast wrong upstream and "my review"
  silently never matches — the form never switches to edit mode.

  ```js
  const myReview = reviews.find((r) => r.user_id === user?.id) ?? null
  ```

- **Does any call send a user id?** It must not. `submit` sends
  `{ courseId, rating, body }`; the server decides *who* from the token.

### 4 — The UI (`StarRating`, `ReviewForm`, `ReviewList`)

```text
Build three components with my existing CSS tokens (.panel, .row, .btn, .muted,
.error, .stars). 2-space indent, default exports.
- StarRating({value, onChange}): read-only stars when no onChange; when onChange
  is given, render real <button type="button"> stars (keyboard + screen-reader
  accessible via aria-label), never divs with onClick.
- ReviewForm({existing, onSubmit}): a CONTROLLED form (star rating + textarea)
  seeded from `existing` so it works for both write and edit; call
  e.preventDefault(); show any error onSubmit returns; disable submit while saving
  or when body is empty.
- ReviewList({reviews, currentUserId, onDelete}): map with key={r.id}; show a
  Delete button ONLY where r.user_id === currentUserId — a UX nicety, NOT the guard.
```

**Read what it wrote:**

- **Are the interactive stars real `<button>`s?** Keyboard and screen-reader users
  can't operate a `<div onClick>`. Accessibility is not optional.

  ```jsx
  <button type="button" onClick={() => onChange(n)} aria-label={`Rate ${n} star${n > 1 ? 's' : ''}`}>★</button>
  ```

- **Is the form controlled and seeded from `existing`?** One form for write and
  edit — the rating and textarea are React state, initialised from any current
  review.

- **Does every row use `key={r.id}`, not the array index?** (Lab 3.3.) And the
  Delete button is drawn only on your own rows — but that is **cosmetic**. Hiding a
  button stops nobody; the `and user_id = ${userId}` in the DELETE SQL is the real
  guard.

### 5 — Wire it into the course detail page, and redeploy

```text
In src/pages/CourseDetailPage.jsx call useReviews(course?.id) (a no-op until the
course id loads). Next to the title show the DERIVED average and count ONLY when
count > 0 (average must be hidden/null on zero reviews, never NaN). Show
<ReviewForm existing={myReview} onSubmit={submit} /> ONLY when a user is signed in;
otherwise show a "Sign in to write a review" Link. Render <ReviewList> below for
everyone.
```

```jsx
{average != null && (<><StarRating value={Math.round(average)} /> {average} ({count})</>)}

{user
  ? <ReviewForm existing={myReview} onSubmit={submit} />
  : <p className="muted"><Link to="/login">Sign in</Link> to write a review.</p>}

<ReviewList reviews={reviews} currentUserId={user?.id} onDelete={remove} />
```

Run it locally end to end, then **attack it** (below). When it holds, ship it:

```bash
git add -A && git commit -m 'feat: course reviews' && git push
```

Vercel rebuilds the front end **and** deploys `api/reviews/*` as new functions.
The feature is live at your Vercel URL — nothing extra to configure, because
`DATABASE_URL` and `JWT_SECRET` are already set as server-side environment
variables from Lab 6.5.

## 🔍 MANDATORY — attack your own endpoint before you ship

Two probes, the same pair from Topic 5, aimed at your new route. With
`npx vercel dev --listen 3000` running:

```bash
# 1) SQL injection through the query string — harmless, because the SQL is
#    parameterised. Returns a clean [] or the real list, never runs anything.
curl "http://localhost:3000/api/reviews?courseId=1'%20or%20'1'='1"

# 2) Delete a review with ANOTHER user's token — 404, because the row never
#    matches `and user_id = ${userId}`. Not a 403 from a JS if — a 404 from SQL.
curl -X DELETE http://localhost:3000/api/reviews/1 \
  -H "Authorization: Bearer <OTHER-USER-TOKEN>"
```

The first bounces because every value travels as a bound parameter, never as SQL
the database parses. The second returns **404** because the ownership check lives
in the WHERE clause, where the caller can't influence it. If either behaves
differently, you have a hole — fix it before you push.

## 🔍 Grade your own work

Tick each box — the right-hand column names the concept it proves.

- [ ] Signed-**out** visitors can **read** reviews and see the average → *`requireAuth` is inside the POST branch; GET is public*
- [ ] Only signed-**in** students see the review form → *conditional rendering gated on auth (`user ? … : …`)*
- [ ] A student can post **only one** review per course; a second submit **edits** the first → *UPSERT on `unique (user_id, course_id)`*
- [ ] The form pre-fills when you already have a review → *controlled form seeded from `myReview` (write/edit in one)*
- [ ] `rating` outside 1–5 is rejected even if the UI is bypassed → *server-side validation + the `check` constraint, not the form*
- [ ] The average updates the instant a review is added/removed and is **never `NaN`** on zero reviews → *derived state, computed at render*
- [ ] All data access goes through `useReviews(courseId)`, not inline fetches → *custom hook / separation of concerns*
- [ ] Every mapped review has `key={r.id}` (not the array index) → *stable keys (Lab 3.3)*
- [ ] You never send a `user_id` from the client anywhere → *identity comes from the verified JWT, not the browser*
- [ ] A Delete button appears only on your own reviews, **and** deleting someone else's returns **404** server-side → *the SQL `and user_id = ${userId}` is the guard, not the hidden button*
- [ ] The two attack probes bounce (empty/list, and a 404) → *parameterised SQL + ownership in the WHERE*
- [ ] The feature works on the **live** Vercel URL after `git push`, not just localhost → *the production redeploy of the front end and the new function*

## 🛠 Stretch goals

- **Sort & filter reviews** — add a control to sort by newest / highest / lowest
  rating (pure derived state over the same array — no new fetch).
- **Only enrolled students may review** — gate the form on an existing enrolment
  for that course, and enforce it **server-side** in the POST by checking the
  `enrollments` table before the UPSERT (the client gate is UX; the server check
  is the rule).
- **Rating breakdown** — show a small 5→1 star histogram derived from the reviews
  array.
- **Edit in place** — let the owner flip a review row into an inline edit form
  without leaving the page, reusing `ReviewForm`.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| Signed-out visitors get **401** trying to *read* reviews | `requireAuth(req)` was called at the top of the handler, so it gates the GET too. | Move `requireAuth` **inside** the POST branch; the GET must take no token. |
| A review shows the reviewer's **email** (or worse) | The GET joined `users` and selected `*` or too many columns. | Select `u.name` only from that table — a join is not permission to expose columns. |
| Posting a second review **500s** with a duplicate-key error | The write is a plain `insert` with no conflict clause. | UPSERT: `on conflict (user_id, course_id) do update set …` so the second submit edits your row. |
| Average shows `NaN` on a course with no reviews | Divided by a count of `0`, or rendered unconditionally. | Derive `average = count ? sum/count : null` and render it only when `count > 0`. |
| "My review" never pre-fills the form | `r.user_id === user?.id` compares a string to a number. | Cast ids `::int` in the SQL so both sides are numbers, then the `find` matches. |
| **Anyone** can delete anyone's review | Deletion was gated with a JavaScript `if`, or the `[id]` statement filtered by `id` alone. | Put `and user_id = ${userId}` in the DELETE SQL; the hidden button is cosmetic. |
| Insert writes the wrong / no `user_id` | The client sent a `user_id`, or the route read one from the body. | Never send a user id; take it only from `requireAuth(req)` and put `${userId}` in the SQL. |
| Feature works locally but not on the live site | The redeploy was skipped, or the `reviews` table isn't in the production database. | `git push` to redeploy, and confirm `neon/schema.sql` ran against the production branch. |

---
### ✅ Cook & Bake Academy after this lab
Learners can post star-rated reviews on any course and every detail page shows a live, derived average — a feature you built and deployed almost entirely on your own, with the server (not the browser) enforcing who may write and whose review is whose.
</content>
</invoke>
