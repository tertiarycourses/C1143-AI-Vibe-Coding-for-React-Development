# Lab 6.4 — Capstone: Assemble the Full-Stack App

> **Topic 6** · ~75 min · Builds on Lab 6.3 · The capstone

### 📖 The build so far
By the end of Lab 6.3, every major Cook & Bake Academy feature existed: the routed catalogue, dynamic course pages, the `/api` backend over Neon, bcrypt + JWT auth, and a protected dashboard. **In this lab you add:** nothing new to *invent* — this is where you **assemble** the whole three-tier app into one coherent product, run it end-to-end against your Neon database, and **grade it yourself** against every concept the course taught, pointing at the exact file in your own project where each one lives. Lab 6.5 takes this same app all the way to a public production deployment.

## What you will build

The **complete, assembled Cook & Bake Academy 🍞** — the three tiers wired into one running product:

```
React (browser)  --fetch-->  /api/* (Vercel serverless functions)  --sql-->  Neon Postgres
```

This lab's `src/` is the **entire finished front end**: every component, page, layout, context and hook, wired into one routed, authenticated app that reads and writes through `src/lib/api.js`. The `api/` folder and your `.env.local` already live in `cookbake/` from Topic 5. You will run the whole stack locally with **both** dev servers (`vercel dev` for the API, `npm run dev` for React), walk a full smoke test, and self-grade the app against the course rubric.

## Concepts you will meet

| Concept | In one line |
|---|---|
| The assembled three tiers | Browser → your `/api/*` functions → Postgres; the browser holds no database credential and reaches the DB only through `src/lib/api.js`. |
| Provider + router order | `BrowserRouter` outermost, then Theme/Auth/Cart providers, then `<App/>` — so every route can read routing, theme, auth and basket. |
| Two dev servers | `vercel dev` runs the `/api` functions on `:3000`; `npm run dev` serves React on `:5173` and proxies `/api` across — one origin, no CORS, and dev matches prod. |
| The AI React Bug Checklist | The six bugs AI-generated React quietly ships — run it over every feature before you accept it. |
| Self-check | Mapping each concept to the real file in your project that proves it. |
| A clean build is the gate | `npm run lint && npm run build` must pass before Lab 6.5 can deploy it. |

## Before you start

You need a completed Lab 6.3 app in `cookbake/` — the `api/` folder from Topic 5, a Neon project with `neon/schema.sql` applied (the 20 seeded courses), and `.env.local` holding `DATABASE_URL` and `JWT_SECRET` (with **no** `VITE_` prefix). This lab's `src/` is the **entire finished front end** — copy it whole over `cookbake/src/`, and copy the SPA rewrite config:

```bash
cp -R "labs/topic-6-react-router/lab-6.4-capstone/src/." cookbake/src/
cp    "labs/topic-6-react-router/lab-6.4-capstone/vercel.json" cookbake/vercel.json
```

Your `index.css`, `src/data/courses.js` and the whole `api/` folder are already in the app and are not included here because they don't change. (`data/courses.js` is effectively unused now that Postgres is the source of truth, except that `CategoryFilter` still imports the `categories` list from it — that is fine.)

---

## The finished file map

```
src/
  main.jsx                     BrowserRouter > ThemeProvider > AuthProvider > CartProvider > App
  App.jsx                      the <Routes> map
  lib/api.js                   the ONE fetch wrapper: attaches the Bearer token, checks res.ok
  layouts/RootLayout.jsx       Navbar + <Outlet/> + Footer
  context/    AuthContext.jsx  ThemeContext.jsx  CartContext.jsx
  hooks/      useCourses.js  useCourse.js  useEnrollments.js  useReviews.js
              useDebounce.js  useLocalStorage.js  useFetch.js
  components/ Navbar Hero Footer Section SearchBar CategoryFilter
              CourseGrid CourseCard CartSummary Chefs StarRating
              EnrollButton EnrollmentList ReviewForm ReviewList AuthForm ProtectedRoute
  pages/      HomePage CoursesPage CourseDetailPage AboutPage
              LoginPage DashboardPage NotFoundPage
              dashboard/MyCoursesPage  dashboard/ProfilePage

api/  (already in cookbake/ from Topic 5 — the server tier)
  _lib/db.js                   sql = neon(process.env.DATABASE_URL) — the only door to Postgres
  _lib/auth.js                 signToken / requireAuth / toClientUser / sendError
  auth/       signup.js login.js me.js        courses/  index.js [slug].js
  enrollments/ index.js [id].js               reviews/  index.js [id].js
```

`index.css` and `data/courses.js` live in the app already and are unchanged.

---

## Ship checklist

### Step 1 — Confirm the schema and secrets are in place

The 20 courses must be seeded and the server secrets must be set from Topic 5:

```bash
psql "$DATABASE_URL" -c 'select count(*) from courses;'   #  -> 20
```

`cookbake/.env.local` holds exactly these two, **neither** with a `VITE_` prefix:

```
DATABASE_URL=postgresql://USER:PASSWORD@ep-xxx.region.aws.neon.tech/neondb?sslmode=require
JWT_SECRET=<32 random bytes from: node -e "console.log(require('crypto').randomBytes(32).toString('hex'))">
```

This is the rule that matters most in the whole course. A `VITE_` prefix would compile the value straight into the JavaScript every visitor downloads; `DATABASE_URL` carries the database password with read **and** write. It belongs only where `process.env` can reach it — inside the `api/` functions, never in `src/`.

### Step 2 — Run BOTH dev servers

Unlike the earlier front-end-only labs, this app needs its `/api` functions running alongside Vite — so in development there are **two** servers, not one:

```bash
cd cookbake
npx vercel dev --listen 3000   # terminal 1 — the api/ functions, reads .env.local
npm run dev                    # terminal 2 — Vite/React on :5173
```

Open `http://localhost:5173`. The browser fetches relative URLs like `/api/courses`; `cookbake/vite.config.js` proxies `/api` to `:3000`, so the browser only ever sees **one origin** (`:5173`) and there is no CORS to configure. In production Vercel serves the built site and the functions from the same domain — so dev matches prod. (If you ever see `Unexpected token '<'`, you fetched `/api/...` with no `vercel dev` running and got `index.html` back instead of JSON.)

### Step 3 — Confirm the SPA rewrite excludes `/api`

`cookbake/vercel.json` must send every non-API path to `index.html` so a deep-link refresh doesn't 404 — while leaving `/api/*` alone so API calls reach the functions:

```json
{ "rewrites": [{ "source": "/((?!api/).*)", "destination": "/index.html" }] }
```

The `(?!api/)` is load-bearing. Drop it and every `/api/courses` call falls through to `index.html` and comes back as HTML — the classic `Unexpected token '<'` in the console.

### Step 4 — Build it clean

```bash
npm run lint && npm run build     # bundles into dist/
```

A warning today is a broken deploy tomorrow. A clean `lint && build` is the gate Lab 6.5 walks through.

### Step 5 — Smoke test the whole stack locally

1. Load `/` — the catalogue renders from Postgres (public read; you are signed out).
2. Open a course, e.g. `/courses/artisan-sourdough-bread-baking`.
3. Sign up with a real email. A display **name** is required — the server rejects a sign-up missing any of email, name or password.
4. Sign in. The Navbar now shows **Dashboard** and **Sign out**.
5. Open a course, click **Enrol now**. It appears under `/dashboard/my-courses`.
6. On `/dashboard/my-courses`, **refresh**. You stay signed in and on the page (the `loading` gate in `ProtectedRoute` waits for `/api/auth/me` to verify your token).
7. Mark the enrollment complete, then remove it. Both persist across refresh — they live in Postgres.
8. Sign out. `/dashboard` now redirects to `/login`, and the catalogue on `/` still renders — but enrollments do not.

If all eight pass, your app is assembled and correct. **Lab 6.5 deploys it.**

---

## 📊 Grade your own app

For each concept, open the listed file and find it. If you can point at the line and explain it in a sentence, tick it. This is your exit rubric — every row maps to a **real file in your own project**.

| # | Concept | Point at it in… |
|---|---|---|
| 1 | Components | any file in `components/` (e.g. `Footer.jsx`) |
| 2 | Props | `CourseCard.jsx` (`{ course }`), `SearchBar.jsx` (`{ value, onChange, inputRef }`) |
| 3 | JSX compiles via Babel | any `.jsx` — `className`, camelCase, `{}` for expressions (`CourseCard.jsx`) |
| 4 | `children` / composition | `Section.jsx` (renders `{children}`), `RootLayout.jsx` (`<Outlet/>`) |
| 5 | createRoot / Virtual DOM | `main.jsx` (the one place React touches the real DOM) |
| 6 | Lists + stable keys | `CourseGrid.jsx` (`key={course.id}` — never the index) |
| 7 | Conditional rendering | `HomePage.jsx` (loading/error/data), `EnrollButton.jsx` (`already`) |
| 8 | The `0 &&` footgun, done right | `CourseDetailPage.jsx` (`count > 0 && …`, not `count && …`) |
| 9 | Events | `SearchBar.jsx` (`onChange`), `Navbar.jsx` (`onClick`), `EnrollButton.jsx` |
| 10 | Controlled forms | `AuthForm.jsx` (email/password `value` + `onChange`), `ReviewForm.jsx` |
| 11 | `useState` | `CoursesPage.jsx` (`query`), `AuthForm.jsx` |
| 12 | `useEffect` + cleanup | `useDebounce.js` (`clearTimeout`), `useCourse.js` (`active` flag), `ThemeContext.jsx` |
| 13 | `useRef` (DOM escape hatch) | `CoursesPage.jsx` (focus the search input), `HomePage.jsx` (`scrollIntoView` the grid) |
| 14 | `useContext` | `AuthContext.jsx`, `ThemeContext.jsx`, `CartContext.jsx` + their `use*` hooks; `Navbar.jsx` reads all three |
| 15 | `useReducer` | *see "Your turn" — refactor `CartContext` to a reducer; the app ships without one* |
| 16 | Custom hooks | `useCourses.js`, `useCourse.js`, `useEnrollments.js`, `useReviews.js`, `useLocalStorage.js`, `useFetch.js` |
| 17 | Derived state (never stored) | `useReviews.js` (`count`/`average` at render), `CartContext.jsx` (`total`) |
| 18 | Immutable updates | `CartContext.jsx` (`[...prev, course]`), `useEnrollments.js` (`map`/`filter`) |
| 19 | Three tiers / no DB in the browser | `src/lib/api.js` (browser side, holds no SQL), `api/_lib/db.js` (`neon(process.env.DATABASE_URL)`) |
| 20 | `fetch` + `res.ok` + three states | `src/lib/api.js` (`if (!res.ok) throw`), `useCourses.js` (loading/error/success + `finally`) |
| 21 | Parameterised SQL | `api/courses/index.js`, `api/enrollments/[id].js` (tagged-template `sql\`… ${value}\``) |
| 22 | Password hashing (bcrypt) | `api/auth/signup.js` (`bcrypt.hash`; `password_hash` never in the `returning` list) |
| 23 | JWT issue + verify | `api/_lib/auth.js` (`signToken` / `requireAuth`) |
| 24 | Identity from the token, ownership in SQL | `api/_lib/auth.js` → `requireAuth(req)`; `api/enrollments/[id].js` → `where id = ${id} and user_id = ${userId}` |
| 25 | Routing (SPA) | `main.jsx` (`BrowserRouter`), `App.jsx` (`Routes`), `RootLayout.jsx` (`Outlet`) |
| 26 | `<Link>` not `<a>` | `CourseCard.jsx`, `Navbar.jsx` (`NavLink`) |
| 27 | Dynamic params | `CourseDetailPage.jsx` (`useParams`), `App.jsx` (`courses/:slug`) |
| 28 | URL state | `CoursesPage.jsx` (`useSearchParams`) |
| 29 | 404 / catch-all | `App.jsx` (`path="*"`), `NotFoundPage.jsx`, `useCourse.js` (404 → `course: null`) |
| 30 | Protected routes (UX) vs the real boundary (SQL) | `ProtectedRoute.jsx` (`loading` gate + `Navigate` — UX) vs `api/enrollments/[id].js` (`where user_id = ${userId}` — the security) |
| 31 | Imperative navigation | `EnrollButton.jsx` / `CourseDetailPage.jsx` (`useNavigate`), `LoginPage.jsx` (redirect-after-login) |

> **Row 15 (`useReducer`)** is the one your shipped app doesn't force you to use. Do the matching "Your turn" task to close the rubric.

> **Say row 30 out loud.** `ProtectedRoute` is a convenience: it stops a signed-out visitor from seeing the dashboard shell. It is **not** security — anyone can delete it in devtools. The real boundary is `where user_id = ${userId}` in the API, keyed off the id in the *verified* JWT. Bypass the client guard and `/dashboard/my-courses` still renders — but the list is empty, because `GET /api/enrollments` answered 401.

---

## 🎤 Vibe prompt

By now you can prompt for a *whole feature* and audit it. Try one:

```text
Add a "Recommended for you" strip to the Cook & Bake Academy dashboard home
(/dashboard/my-courses), above the enrollment list. It should:
- read the student's enrollments (already available via useEnrollments),
- read all courses via useCourses,
- show up to 3 courses in categories the student is enrolled in (Bakery or
  Cooking) but hasn't enrolled in yet, each as the existing <CourseCard/>,
- render nothing if there are no recommendations,
- reuse existing components and the .grid/.card classes; add no dependencies,
- send NO user id anywhere — enrollments already come scoped to the token.
Then explain which existing files you reused and why.
```

Then **read the diff before you accept it**, using the checklist below.

## 🔍 Read what the AI wrote — the AI React Bug Checklist

Run this list over any feature an AI adds to this three-tier app. These are the bugs this course trained you to catch — the six React ones first, then the three-tier ones:

- **`key={index}`?** Lists use a stable id as the key (`key={course.id}`), never the array index. An index key corrupts row state when the list is filtered, reordered or deleted.
- **A missing effect cleanup?** Every `useEffect` that subscribes, fetches or sets a timer returns a cleanup — `clearTimeout`, an `active` flag, an unsubscribe. `StrictMode` double-invokes effects precisely to expose the ones that leak.
- **`{count && …}` rendering a literal `0`?** `0` is falsy but not `false`, so `{count && <Badge/>}` renders a bare `0` when the count is zero. Write `count > 0 && …` (see `CourseDetailPage.jsx`).
- **A `fetch` with no `res.ok` check?** `fetch` does **not** reject on 404 or 500 — only a network failure rejects. Every call must check `res.ok` (our `src/lib/api.js` does it once for the whole app), or an error payload sails into the UI and renders as data.
- **State mutated with `push`?** `arr.push(x)` mutates in place and does not re-render. Build a new value: `[...prev, x]`, `prev.map(...)`, `prev.filter(...)` (see `CartContext.jsx`, `useEnrollments.js`).
- **A stored derived value?** Anything you can compute from existing state during render — a count, an average, a filtered list — belongs in the render body, not mirrored into `useState` where it can drift. `useReviews.js` derives `count` and `average`; it never stores them.

Then the boundary bugs, unique to a real backend:

- **User id from the body instead of the token?** Grep the new route for `req.body.userId` / `req.query.userId`. Identity must come from `requireAuth(req)`, which reads the *verified* JWT. If the body could carry a user id, so could curl — and it would carry yours.
- **Ownership check in JavaScript instead of SQL?** A `[id]` write must carry `and user_id = ${userId}` in the WHERE clause, not an `if (row.user_id !== userId)` after fetching. Fetching first already exposed a row you shouldn't have read.
- **SQL built by concatenation?** Every query is a tagged template — `sql\`… where slug = ${slug}\``. A value glued into a plain string is injectable.
- **A secret with a `VITE_` prefix?** `DATABASE_URL` and `JWT_SECRET` never carry `VITE_` and never appear under `src/`. A `VITE_` prefix publishes them to every visitor.

## 🧠 Why it works — the shape of the whole app

Read `main.jsx` top to bottom and you can see the architecture in one screen. `BrowserRouter` connects the app to the address bar. Inside it, three context providers make cross-cutting state — theme, auth, cart — available to any component without prop-drilling. Inside those, `<App/>` is nothing but a `<Routes>` map: URLs to components. `RootLayout` is the frame every page shares; its `<Outlet/>` is where the current page mounts. Pages are thin — they call a custom hook for data (`useCourses`, `useCourse`, `useEnrollments`, `useReviews`), render loading/error/empty/data, and delegate the pixels to presentational components.

The hooks never touch Postgres. They call `src/lib/api.js`, which attaches `Authorization: Bearer <token>` from `localStorage`, checks `res.ok`, and returns JSON — that one wrapper is the browser's entire relationship with the server. On the other side of that `fetch`, the `api/*` serverless functions are the only code that holds `DATABASE_URL`, the only code that runs SQL, and the only place identity is decided: `requireAuth(req)` reads the user id from the *verified* JWT, and `where user_id = ${userId}` in the SQL is the real boundary that keeps one student's data apart from another's. Every idea in the course is one of those layers, and they compose — that composability is the point.

## ✅ Check your work

- [ ] Both dev servers run (`vercel dev` on `:3000`, `npm run dev` on `:5173`); loading `http://localhost:5173` shows the catalogue and `/api/courses` returns the 20-course array from Postgres.
- [ ] `.env.local` holds `DATABASE_URL` and `JWT_SECRET` and **neither** carries a `VITE_` prefix; you can explain why a `VITE_` prefix would be a breach.
- [ ] `cookbake/vercel.json` rewrites every non-`/api/` path to `index.html`, and `/api/*` still reaches the functions.
- [ ] `npm run lint && npm run build` completes with no errors or warnings.
- [ ] The full smoke test passes locally (sign up → enrol → refresh → stay signed in → dashboard → sign out; a signed-out visitor still sees the catalogue but no enrollments).
- [ ] You can point at the real file for every rubric row (after the one "Your turn" task, all rows without an asterisk).

## 🛠 Your turn — close the rubric

1. **`useReducer` (row 15):** refactor `CartContext` from its three setter helpers (`addItem` / `removeItem` / `clear`) to a single `useReducer` with `ADD` / `REMOVE` / `CLEAR` actions. Keep the public API identical, so no other file changes — a clean demonstration of why a hook encapsulates its state. (Persisting through `useLocalStorage` can stay; wrap the reducer or sync in an effect.)
2. **`useRef`, said out loud (row 13):** open `CoursesPage.jsx` and `HomePage.jsx` and explain, in one sentence each, why "is focused" and "scroll here" are refs and not state — *redraw the screen → state; don't redraw → ref.*

## The vibe-coding retrospective

You started this course typing prompts and hoping. You finish it able to *read the output* — which changes how you should prompt.

**How to prompt for a whole feature now.** Give the agent the four things it can't infer: the **files it may reuse** (name them), the **data source** ("via the existing `useEnrollments` hook — it sends no user id"), the **states to handle** ("loading, error, empty, data"), and the **constraints** ("no new dependencies; use `.grid`/`.card`; default exports; parameterised SQL only; identity from `requireAuth`, never the body"). Then ask it to *explain what it reused and why* — that explanation is your fastest audit. A vague prompt gets you a plausible-looking feature with an index key, a missing cleanup, and a `fetch` that renders an error page as data. A specific prompt plus a read-through gets you code you'd sign your name to.

**The bugs this course taught you to catch in AI-generated React over a real backend** — keep this list; it's the difference between "the AI did it" and "I shipped it":

1. Array index used as a list `key`.
2. `useEffect` with no cleanup (subscriptions, timers, fetches on unmount).
3. `useEffect` used to compute derived state that should be plain render logic.
4. `{count && …}` rendering a literal `0` instead of `{count > 0 && …}`.
5. `<a href>` for internal navigation instead of `<Link>` (full reload, lost state).
6. Auth guard that redirects before `loading` resolves — logs signed-in users out on refresh.
7. Mutating state in place (`push`, `splice`, direct assignment).
8. `fetch` with no `res.ok` check — an error payload gets parsed and rendered as data.
9. A user id read from `req.body`/`req.query` instead of the verified JWT (`requireAuth`).
10. An ownership check in a JS `if` instead of `and user_id = ${userId}` in the SQL WHERE.
11. SQL built by string concatenation instead of a parameterised tagged template.
12. A secret shipped to the client under a `VITE_` prefix (`DATABASE_URL`, `JWT_SECRET`).
13. `password_hash` selected into a response instead of whitelisting safe fields.
14. Data views with no loading / error / empty states.
15. Missing the `/api`-excluding SPA rewrite, so deep links or API calls break in production (fixed in Lab 6.5).

You can build the feature *and* you can prove it's right. That's vibe coding done properly. **Now go to Lab 6.5 and ship it.**

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `/api/courses` returns an HTML page / `Unexpected token '<'` | Only `npm run dev` is running, so the Vite proxy has no target, or the SPA rewrite doesn't exclude `/api`. | Start `npx vercel dev --listen 3000` in a second terminal so the proxy has a target; ensure `vercel.json` source is `/((?!api/).*)`. |
| Blank catalogue, `DATABASE_URL is not set` | `.env.local` missing or `vercel dev` not restarted after editing it. | Set `DATABASE_URL` (no `VITE_`) in `cookbake/.env.local`; restart `vercel dev`. |
| `JWT_SECRET is not set` thrown on an auth call | `JWT_SECRET` missing from `.env.local`. | Generate 32 random bytes and set `JWT_SECRET` (no `VITE_`); restart `vercel dev`. |
| Sign-up rejected with 400 | The request is missing email, name **or** password. | Provide all three; the server requires a display name and an 8+ char password. |
| Refresh on `/dashboard` logs you out | `ProtectedRoute` lost its `loading` gate and redirected before `/api/auth/me` resolved. | Restore `if (loading) return …` before the `!user` check. |
| Enrollments never load for a signed-in user | The token isn't attached, or the route didn't reach `requireAuth`. | Confirm `src/lib/api.js` sends `Authorization: Bearer` and the route calls `requireAuth(req)`. |

---
### ✅ Cook & Bake Academy after this lab
The full Cook & Bake Academy is assembled end-to-end — React Router front end, `/api` serverless backend over Neon, bcrypt + JWT auth and a private dashboard — measured against a self-grading rubric where every concept points at a real file in your own project.
</content>
</invoke>
