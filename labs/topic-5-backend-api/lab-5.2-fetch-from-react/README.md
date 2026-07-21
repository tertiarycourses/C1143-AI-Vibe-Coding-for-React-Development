# Lab 5.2 — Fetch the Catalogue From React

> **Topic 5** · ~50 min · Builds on Lab 5.1 (the serverless API over Neon)

### 📖 The build so far
By the end of Lab 5.1, your `/api/courses` and `/api/courses/:slug` routes served the catalogue out of Neon — but you only ever called them with `curl`. The React app still renders the hardcoded `src/data/courses.js` array. **In this lab you add:** the browser tier — a tiny `api` client that is the app's only door to the server, and two hooks (`useCourses`, `useCourse`) that fetch live data with proper loading and error states. By the end, Cook & Bake Academy renders its catalogue straight from Postgres, over the network.

## What you will build

The **browser tier** that closes the loop:

```
React (this lab)  --fetch-->  /api/* (Lab 5.1)  --sql-->  Neon Postgres
```

`src/lib/api.js` — one `fetch` wrapper (`api.get/post/patch/del`) that the browser
uses for *every* server call; it checks `res.ok`, parses JSON, and carries the
status code on errors. Then `useCourses()` (the whole catalogue) and
`useCourse(slug)` (one course, with a real 404 → "not found"). You'll wire the
Vite dev proxy so the app and the API feel like one origin, and swap the
hardcoded array for the live read.

## Concepts you will meet

| Concept | In one line |
|---|---|
| The `api` client | The browser's **only** door to the server — no SQL, no credentials, just `/api/*` calls. |
| `res.ok` | `fetch` does **not** reject on 404/500; the wrapper checks `res.ok` and throws so callers can `catch`. |
| The three states | Every remote read is **loading**, then **error** or **success** — model all three or the UI feels broken. |
| Two dev servers + proxy | `vercel dev` (:3000) runs `api/`; Vite (:5173) serves React and proxies `/api` to :3000. |
| Status-aware errors | `err.status` lets `useCourse` turn a 404 into "not found" but a 500 into a red error. |
| Cleanup flag (`active`) | Guard against setting state after the component unmounted or the slug changed. |

## Before you start

Have Lab 5.1 working (the API answers `curl`). Copy this lab in:

```bash
cp -R "labs/topic-5-backend-api/lab-5.2-fetch-from-react/src/." cookbake/src/
```

That adds `src/lib/api.js`, `src/hooks/useCourses.js` and `src/hooks/useCourse.js`.
Your Topic 3–4 pages already render from a `courses` array with these fields, so
switching the source is a one-line change per page (Step 5).

> **No `VITE_` database variable — still.** Nothing in this lab (or any file under
> `src/`) touches `DATABASE_URL` or imports `@neondatabase/serverless`. The
> browser's only knowledge of the server is the string `'/api'`. If a suggestion
> ever puts a connection string in `src/`, it is wrong — that is the two-tier
> mistake Lab 5.1 exists to avoid.

---

## Step 1 — Run BOTH servers

In development there are **two** servers, and you need both running:

```bash
npx vercel dev --listen 3000   # terminal 1 — the api/ functions, reads .env.local
npm run dev                    # terminal 2 — Vite / React on :5173
```

`vercel dev` runs your serverless functions (and reads `DATABASE_URL` /
`JWT_SECRET` from `.env.local`). `npm run dev` serves and hot-reloads React.

## Step 2 — Understand the proxy (why it's one origin)

Your React code fetches a **relative** URL like `/api/courses`. Without help,
that request hits Vite on `:5173`, which knows nothing about `api/` and answers
with `index.html` — so `await res.json()` blows up trying to parse a page of HTML.
(If you ever see **`Unexpected token '<'`**, this is exactly why: you fetched a
URL and got a web page back.)

`vite.config.js` (shipped in Lab 5.1) fixes it with a proxy:

```js
server: {
  proxy: { '/api': 'http://localhost:3000' },
}
```

Now anything starting with `/api` is forwarded to `:3000`. The browser still only
ever sees **one origin** (`localhost:5173`), so there is no CORS to configure —
and in production it really *is* one origin, because Vercel serves the built site
and the functions from the same domain. **Dev matches prod.**

## Step 3 — Read `src/lib/api.js` — the only door to the server

Open `src/lib/api.js`. Notice what is **not** in it: no connection string, no
password, no SQL. The browser knows one thing — how to call `/api/*` URLs:

```js
const BASE = '/api'

async function request(method, path, body) {
  const res = await fetch(`${BASE}${path}`, { method, headers: {/*…*/}, body: /*…*/ })
  const data = res.status === 204 ? null : await res.json().catch(() => null)

  if (!res.ok) {
    const err = new Error(data?.error ?? `Request failed (${res.status})`)
    err.status = res.status   // carry the status so callers can branch on it
    throw err
  }
  return data
}

export const api = {
  get:  (path)       => request('GET', path),
  post: (path, body) => request('POST', path, body),
  patch:(path, body) => request('PATCH', path, body),
  del:  (path)       => request('DELETE', path),
}
```

The single most important line is `if (!res.ok)`. `fetch` **does not throw** on a
404 or 500 — a response arrived, so as far as `fetch` is concerned it worked. If
the wrapper didn't check `res.ok`, an error payload like `{ error: "..." }` would
sail into the UI and get rendered as if it were a course. Checking it once, here,
means every hook can just `try/catch`. (The `Authorization` header this wrapper
attaches is for Labs 5.3–5.4; the public catalogue doesn't send one.)

## Step 4 — Read the two hooks

**`useCourses()`** — `GET /api/courses`, the public catalogue:

```js
const data = await api.get('/courses')   // throws on network failure AND any non-2xx
setCourses(data)
```

It holds all **three** states — `courses`, `loading`, `error` — and clears
`loading` in a `finally` so one failed request can't leave the UI stuck on its
skeleton forever. Downstream components can't tell the difference from the old
hardcoded array: same shape, same fields. The only new thing is that the data now
**arrives over a network**, which can be slow (hence `loading`) or fail (hence
`error`).

**`useCourse(slug)`** — `GET /api/courses/:slug`, one course:

```js
try {
  const data = await api.get(`/courses/${slug}`)
  setCourse(data); setError(null)
} catch (err) {
  if (err.status === 404) { setCourse(null); setError(null) }  // a real 404, not a crash
  else setError(err.message)
} finally { setLoading(false) }
```

This is where `err.status` earns its keep. A **404** means "no such course" —
`course: null`, **no** error — which is what makes `CourseDetailPage` render its
"Course not found" page. A **500** is a real error and shows the red message. Two
different failures, two different screens; collapse them and you show "Something
went wrong" to a user who merely mistyped a URL.

## Step 5 — Swap the hardcoded array for the live read

Your Topic 3–4 pages import the local `courses` array. Change them to call the
hook. In `src/pages/CoursesPage.jsx` (and `HomePage.jsx`), replace the import and
add loading/error branches:

```jsx
import { useCourses } from '../hooks/useCourses'
// …
const { courses, loading, error } = useCourses()

if (loading) return <div className="grid">{Array.from({ length: 8 }).map((_, i) => <div key={i} className="skeleton" />)}</div>
if (error)   return <p className="error">Could not load courses: {error}</p>
// …then render <CourseGrid courses={courses} /> exactly as before
```

Do the same in `CourseDetailPage.jsx` with `useCourse(slug)`, rendering the
"Course not found" state when `!loading && !course`.

Reload. The catalogue now comes from Postgres. Prove it: change a course title in
the Neon **SQL Editor** (`update courses set title = '…' where code = 'BAK-101';`),
reload the app, and watch it change — with **no** code edit.

## Step 6 — See all three states

Open DevTools → Network, throttle to **Slow 3G**, reload: the skeletons are now
clearly visible. Then right-click the `/api/courses` request → **Block request
URL** and reload to see the red error branch. Visit `/courses/not-a-real-slug` to
see the 404 → "Course not found" page. All three states, on demand.

---

## 🎤 Vibe prompt

```text
In my Vite + React app (plain JSX) I have src/lib/api.js exporting an `api` object
with get/post/patch/del that call fetch on /api/* and THROW on any non-2xx
response (the thrown Error carries err.status). Create two hooks:

1. src/hooks/useCourses.js — export useCourses() returning { courses, loading,
   error }, loading true to start. In a useEffect with [] deps, call
   `await api.get('/courses')`, setCourses(data) on success, setError(err.message)
   on failure, and clear loading in a finally. Use a local `active` flag cleared
   in the cleanup so you never setState after unmount.

2. src/hooks/useCourse.js — export useCourse(slug) returning { course, loading,
   error }. Keyed on [slug]. Call `await api.get('/courses/'+slug)`. On success set
   the course. In catch, if err.status === 404 set course=null WITH NO error (a
   real not-found), otherwise set error. Clear loading in a finally; guard with an
   `active` flag.

Do NOT import @neondatabase/serverless or any DATABASE_URL in these files — the
browser only ever calls /api/*. Use existing CSS classes (grid, skeleton, error).
```

## 🔍 Read what the AI wrote

- **Did it re-check `res.ok` itself?** If the hook calls raw `fetch` instead of
  the `api` client, make sure it checks `res.ok` — otherwise a 500 error body
  renders as a course. Prefer going through `api.get`, which already does it.
- **Does `useCourse` treat 404 as data, not an error?** The tell of weak code is
  one `error` state for both "not found" and "server broke". Look for
  `if (err.status === 404)` setting `course = null` with **no** error.
- **Is there a `finally`?** Without it, a failed request leaves `loading` true and
  the skeleton shimmers forever under the (invisible) error.
- **Empty deps on `useCourses`, `[slug]` on `useCourse`?** No array re-runs every
  render and hammers the API; the detail hook must re-fetch when the slug changes.
- **`active` cleanup flag?** Rapidly changing the slug can let an old response set
  state after a newer one. The flag (or an `AbortController`) prevents it.
- **Any DB credential in `src/`?** If a "fix" ever imports `@neondatabase/serverless`
  or a `DATABASE_URL` into a browser file, reject it — that breaks the three tiers.

## 🧠 Why it works

**The `api` client is the boundary.** Everything the browser is allowed to do to
the server goes through one small file, and that file speaks only in `/api/*`
URLs. It has no idea Postgres exists. That is the payoff of Lab 5.1's design: the
security lives on the far side of `fetch`, in code the user can't edit, so the
worst a malicious browser can do is call your public API — which decides for
itself what to answer.

**`fetch` doesn't throw on HTTP errors — so we do.** `fetch` models "did the HTTP
conversation happen", not "did the server like your request". A 404 or 500 is a
*completed* conversation, so the promise resolves and `res.ok` is `false`. Only a
broken connection rejects. If you skip the `res.ok` check, `res.json()` happily
parses the error body and you render `{ error: "..." }` as data. The wrapper
throws on `!res.ok` and stamps `err.status` onto the error, converting HTTP's
"look at the status code" convention into JavaScript's "catch the exception" one —
so every hook handles success and failure the same familiar way.

**Three states, always.** A remote read is a tiny state machine: `loading →
success | error`. The trap is thinking of it as "get the data", but there is a
window with *no* data yet (loading) and a branch where you'll *never* get it
(error). Render something sensible in all three — a skeleton, a message, the
content — or the first network hiccup renders `undefined.map(...)` and crashes.
This isn't polish; it's correctness. And clearing `loading` belongs in a
`finally`, because it must run whether the request succeeded *or* threw.

**404 is an answer, not an exception.** The reason `useCourse` splits on
`err.status` is that "this course doesn't exist" and "the server fell over" are
*different facts* that deserve *different screens*. HTTP already encodes the
difference in the status line; `err.status` carries it up to React so the UI can
choose the not-found page or the error page. A hook that treats every failure as
one `error` state throws away information the server took care to send.

**Why the proxy makes dev match prod.** In production, Vercel serves your built
React *and* your `api/` functions from one domain, so `/api/courses` is same-origin
— no CORS. In dev they're two processes on two ports, which would be cross-origin.
The Vite proxy forwards `/api` to `:3000` so the browser still sees a single origin
(`:5173`). You develop against the same relative URLs and the same
no-CORS reality you'll deploy to — which is why "it worked locally" actually means
something here.

## ✅ Check your work

- [ ] Both servers run: `vercel dev` on :3000 and `npm run dev` on :5173.
- [ ] The catalogue renders from Neon; editing a title in the SQL Editor and
      reloading shows the change with no code edit.
- [ ] Slow-3G throttling shows the skeletons; blocking `/api/courses` shows the
      red error message, not a blank page or a crash.
- [ ] `/courses/not-a-real-slug` shows the "Course not found" page (a 404), **not**
      a red error.
- [ ] `useCourses` clears `loading` in a `finally`; `useCourse` branches on
      `err.status === 404`.
- [ ] No file under `src/` imports `@neondatabase/serverless` or references
      `DATABASE_URL`.

## 🛠 Your turn

1. Wire the existing `SearchBar` / `CategoryFilter` to the API: pass their values
   as `useCourses({ q, category })` and build the query string
   (`/courses?q=…&category=…`). The API already supports both params (Lab 5.1) —
   now the filtering happens in Postgres, not in the browser.
2. Add a `refetch` function to `useCourses` (extract the loader into a `useCallback`
   and return it) and a "Try again" button that appears in the error branch.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `Unexpected token '<'` when parsing JSON | The request hit Vite (:5173), not the API — no proxy, or `vercel dev` isn't running. | Start `npx vercel dev --listen 3000` and keep the `/api` proxy in `vite.config.js`. |
| Catalogue is blank, no error shown | The hook read `data` from a non-ok response without checking `res.ok`. | Go through `api.get` (it throws on non-2xx), or add the `res.ok` check. |
| Mistyped URL shows a red "Something went wrong" | `useCourse` treated the 404 as an `error`. | Branch on `err.status === 404` → `course = null`, no error. |
| Spinner never stops after a failure | `setLoading(false)` ran only on success. | Clear `loading` in a `finally` block. |
| React warning: state update on unmounted component | No cleanup guard; an old request resolved after unmount. | Use a local `active` flag set to false in the effect cleanup. |
| API fires on every keystroke/render | Missing or wrong dependency array. | `[]` for `useCourses`, `[slug]` for `useCourse`. |

---
### ✅ Cook & Bake Academy after this lab
The catalogue renders live from Neon Postgres through the app's own `/api/*` client, with real loading, error and not-found states.
