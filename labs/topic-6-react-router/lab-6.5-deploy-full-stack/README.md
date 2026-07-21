# Lab 6.5 — Deploy the Full-Stack App to Vercel + Neon

> **Topic 6** · ~60 min · Builds on Lab 6.4 · The final lab

### 📖 The build so far
By the end of the last lab, the complete Cook & Bake Academy ran on your laptop against a dev database — React on Vite, the `api/` serverless functions, and Neon Postgres. **In this lab you add:** a production deployment — the whole three-tier app on Vercel, a production Neon database with the schema, working auth, and server-side secrets that never reach the browser. By the end you'll have the full-stack Cook & Bake Academy live on the public internet at a `*.vercel.app` URL.

## What you will build

You will take the assembled Cook & Bake Academy app from Lab 6.4 and put it on the
public internet as **one deployment on Vercel**: the React SPA served as static
files, the `api/` functions running as **serverless functions on the same
domain**, and a production **Neon** Postgres database behind them. Back in Lab 2.2
you deployed a static page; this app is different — it has a database, an API and
user accounts — so deployment now means three tiers staying in sync:

```
React (browser) --fetch--> /api/* (Vercel serverless functions) --sql--> Neon Postgres
```

Vercel serves the built front-end *and* runs the functions on the same origin, so
the browser's relative `/api/*` calls just work in production — same-origin, no
CORS — exactly like the dev proxy in `vite.config.js` did on your laptop.

This is a **configuration lab**. It creates no React code — only the `vercel.json`
your app already ships, plus a series of dashboard settings. Everything else is
done in the Vercel and Neon consoles.

## Concepts you will meet

| Concept | In one line |
|---|---|
| Build-time vs server env | `VITE_*` values are baked into the public bundle at build; un-prefixed vars stay on the server and are read by `api/` via `process.env`. |
| Serverless functions | Vercel runs each file in `api/` as its own function on the same domain — no server to manage, no CORS. |
| SPA deep-link rewrite | `vercel.json` serves `index.html` for every non-API path so `/courses/:slug` doesn't 404 on refresh. |
| Negative lookahead | `(?!api/)` in the rewrite excludes `/api/`, so the rewrite forwards page routes but lets API calls reach the functions. |
| Same-origin in prod | The SPA and the functions share one domain, so relative `/api/*` fetches need no CORS — dev matches prod. |
| Preview deployments | Vercel builds a throwaway URL per branch/PR; every push redeploys automatically. |

## Before you start

You need a completed **Lab 6.4** app that runs locally: `npm run build` is clean,
the two-terminal dev setup works against your Neon database, and `vercel.json` sits
at `cookbake/vercel.json`. You also need:

- the project pushed to a **GitHub** repo,
- a **Vercel** account (free Hobby tier is enough),
- your **Neon** project from `topic-5-backend-api`, with its connection string.

Copy this lab's `vercel.json` to your app root (it is identical to Lab 6.4's — the
lab repeats it so 6.5 is self-contained):

```bash
cp labs/topic-6-react-router/lab-6.5-deploy-full-stack/vercel.json cookbake/vercel.json
```

---

## What Lab 2.2 did, and what is different now

In **Lab 2.2** you deployed a **static** Cook & Bake Academy landing page. The
whole app was HTML, CSS and a little JS; the host had one job — serve those files.
There was no server-side anything, no database, no secrets, no per-user state.
Deployment was "upload the folder."

This app is a **full-stack** app now, and two things changed:

1. **It has an API and a database.** The front-end is still static files served by
   Vercel, but it now fetches its own `/api/*` routes, and those functions talk to
   **Neon**. The browser never touches Postgres — it only ever calls your own API.
   That means deployment isn't done when the files are uploaded: the functions have
   to run, and the database they talk to has to have the schema.

2. **It has server-side secrets.** The API reads `DATABASE_URL` and `JWT_SECRET`
   from `process.env`. Locally those live in `.env.local`; in production they must
   be set in Vercel — and they must **not** have a `VITE_` prefix, or Vite would
   compile them into the public bundle. Get this wrong and you ship your database
   password to every visitor.

The SPA-rewrite lesson from Lab 2.2/2.3 still applies (Step 5), but it now has a
twist — it must *not* swallow the `/api/*` routes. Everything else is new because
the app grew a back end.

---

## Step 1 — Provision a production Neon database

Open the Neon Console → your project → **Connect** and copy the connection string
(it looks like `postgresql://USER:PASSWORD@ep-….neon.tech/neondb?sslmode=require`).
This is your production `DATABASE_URL`. It is the same **kind** of string you used
in `.env.local` for Lab 6.4, just pointing at the database you want to be live.

You can use your existing Neon project. If you want production data kept separate
from your local experiments, create a second Neon project (or database) for
production and copy *its* connection string instead. Either way, keep this string
secret — it carries the password with full read **and** write access.

## Step 2 — Run the schema against the production database

A fresh database has **no tables**. Run the migration once against production, from
your machine, using the production connection string:

```bash
psql "$DATABASE_URL" -f neon/schema.sql
```

(`schema.sql` is re-runnable — the seed uses `on conflict (code) do nothing`, so
running it twice is harmless.) Then verify it took:

```sql
-- tables exist
select tablename from pg_tables where schemaname = 'public';
-- the 20 courses seeded
select count(*) from courses;   -- expect 20
```

If `courses` is empty, your production catalogue will be empty even though it works
locally — you ran the schema against a different database than the one Vercel will
use. The `DATABASE_URL` you seed here in Step 2 **must be the same string** you
paste into Vercel in Step 4.

## Step 3 — Import the repo into Vercel

Vercel → **Add New… → Project** → import your GitHub repo.

- **Root Directory:** `cookbake` (the app is not at the repo root).
- **Framework Preset:** **Vite** (Vercel usually auto-detects it).
- **Build Command:** `npm run build`.
- **Output Directory:** `dist`.

Vercel also detects the `api/` folder next to your source and runs each file in it
as a **serverless function** on the same domain — you configure nothing for that.
Do **not** deploy yet — set the env vars first (Step 4), or the first build ships an
app whose API has no database and no signing key.

## Step 4 — Set the two server-side env vars

Vercel → your project → **Settings → Environment Variables**. Add both:

| Name | Value | Notes |
|---|---|---|
| `DATABASE_URL` | your production Neon connection string (from Step 1) | Server-side. **No `VITE_` prefix.** |
| `JWT_SECRET` | a long random string (`node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"`) | Server-side. **No `VITE_` prefix.** |

**Say it out loud: these are SERVER-SIDE variables, and the missing `VITE_` prefix
is the whole point.** Vite compiles every `VITE_*` variable straight into the
public browser bundle — so a `VITE_DATABASE_URL` would ship your database password,
with full read and write access, to every single visitor of your site. These two
variables have no `VITE_` prefix, so Vite never touches them; only your `api/`
functions read them, at runtime, via `process.env.DATABASE_URL` and
`process.env.JWT_SECRET`. The browser never sees either one.

Set them for **Production** (and Preview too, if you want previews to run). Now
trigger the first deploy (Deploy button, or push a commit).

## Step 5 — The SPA rewrite that spares the API

Your `cookbake/vercel.json` is exactly this:

```json
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "rewrites": [
    { "source": "/((?!api/).*)", "destination": "/index.html" }
  ]
}
```

There is one rewrite doing **two** jobs, and the regex is the whole story:

- **`destination: "/index.html"` — the SPA half.** On a static host the only real
  file is `index.html`; there is no file at `/courses/artisan-sourdough-bread-baking`
  or `/dashboard/my-courses`. Without a rewrite, clicking a `<Link>` works (React
  Router handles it in memory), but **hard-refreshing or sharing a deep link asks
  the server for a file that doesn't exist → a Vercel 404.** The rewrite says "serve
  `index.html` for this path", so the SPA boots and React Router shows the right page.
- **`(?!api/)` — the negative lookahead that saves the API.** `source` matches every
  path *except* those starting with `api/`. That exclusion matters: your API routes
  (`/api/courses`, `/api/auth/login`, …) must reach the **serverless functions**, not
  be rewritten to `index.html`. If the rewrite were the naïve `"/(.*)"`, every
  `/api/*` fetch would return your HTML page instead of JSON — and `await res.json()`
  would blow up on `Unexpected token '<'`. The lookahead lets page routes fall
  through to `index.html` while API routes fall through to the functions.

This is the same deep-link lesson as Lab 2.2/2.3, upgraded for a full-stack app that
now has its own API on the same domain. Commit it and redeploy.

## Step 6 — Push, deploy, and preview

Vercel is wired to your GitHub repo, so **every push redeploys automatically** —
pushes to your main branch update production, and every other branch or PR gets its
own **preview URL** at a throwaway address. This is your normal loop from now on:
edit, commit, push, watch Vercel build.

Because the SPA and the functions share one origin, there is nothing else to wire:
the browser's relative `/api/*` calls hit the functions on the same domain, so there
is no CORS to configure — the production setup mirrors the dev proxy from
`vite.config.js`. When the build goes green, open the deployment URL and run the
smoke test below. The finished reference app is live at
`https://cookbake-academy.vercel.app`.

---

## 🎤 Vibe prompt

Deployment config is a great use of an AI agent, as long as you verify it.

```text
I have a full-stack app in the ./cookbake subfolder of my Git repo. It's a Vite +
React SPA (react-router-dom v7) that fetches its own relative /api/* routes. Those
routes are Vercel serverless functions in cookbake/api/ that talk to Neon Postgres
with the @neondatabase/serverless driver. The API reads DATABASE_URL and JWT_SECRET
from process.env. Deploying to Vercel:

1. Write cookbake/vercel.json that rewrites every path EXCEPT /api/ to /index.html,
   so deep links like /courses/artisan-sourdough-bread-baking and
   /dashboard/my-courses don't 404 on refresh — but /api/* still reaches the
   serverless functions and is NOT rewritten to index.html. Use the vercel.json
   $schema and explain the (?!api/) negative lookahead.
2. List the exact Vercel project settings: Root Directory, Framework Preset, Build
   Command, Output Directory.
3. List the environment variables I must set in Vercel and whether each is
   server-side or public. Explain why DATABASE_URL and JWT_SECRET must NOT have a
   VITE_ prefix, and what leaks if they do.
4. Give me the one-time command to run neon/schema.sql against the production
   database.

Do not put any secret in vercel.json, and never suggest a VITE_ prefix for
DATABASE_URL or JWT_SECRET.
```

## 🔍 Read what the AI wrote

No app code is generated here, so audit the *configuration* the agent hands you:

- **The rewrite excludes the API.** The `source` must be `"/((?!api/).*)"`, not
  `"/(.*)"`. Agents love the simpler `"/(.*)"` — but that swallows `/api/*`, and your
  fetches start returning HTML (`Unexpected token '<'`) instead of JSON. Prove the
  file parses: `cat cookbake/vercel.json | jq .`.
- **No `VITE_` on the secrets.** The agent must set `DATABASE_URL` and `JWT_SECRET`
  as plain, server-side variables. If it prefixes either with `VITE_`, or drops the
  connection string into `vercel.json`, reject it — that publishes your database
  password. AI sometimes "helpfully" suggests exposing the connection string; do not
  accept it.
- **Root Directory is `cookbake`.** If the agent or the Vercel importer leaves it at
  the repo root, the build won't find `package.json` and fails.
- **It says to seed production.** A correct answer reminds you to run
  `neon/schema.sql` against the production database once, or the live catalogue is
  empty while everything works locally.
- **No CORS theatre.** Because the SPA and API share one origin, there is nothing to
  allow-list. If the agent invents a CORS allow-list step for your own `/api/*`, it
  has misread the architecture.

## 🧠 Why it works

Deploying this app is really three tiers that must agree, on one domain.

**The build-time boundary.** Vite is a bundler: when `npm run build` runs on Vercel,
it reads every `import.meta.env.VITE_*` reference and *substitutes the literal value*
into the output JavaScript, which is then served to every browser as plain static
files. That is exactly why the `VITE_` / no-`VITE_` split is a security boundary, not
a style choice. `DATABASE_URL` and `JWT_SECRET` have **no** prefix, so Vite never
sees them; they live only in the serverless runtime, where `api/_lib/db.js` reads
`process.env.DATABASE_URL` and `api/_lib/auth.js` reads `process.env.JWT_SECRET`. A
`VITE_DATABASE_URL` would be inlined into `dist/assets/*.js` — a public file — handing
the password to anyone who opens DevTools. There is no server reading env vars for the
front-end; the front-end *is* the bundle.

**The routing boundary.** The browser's address bar can hold any path, but a static
host only has the files you uploaded. React Router runs in the browser, so once the
app is loaded it renders `/dashboard/my-courses` from memory — but the *first* request
for that URL (a refresh, a shared link, a bookmark) goes to Vercel, which has no such
file. The rewrite answers every page path with `index.html`; the app boots, reads the
real path from `window.location`, and React Router renders the matching route. The
`(?!api/)` lookahead is what keeps this from breaking the back end: `/api/*` is
excluded from the rewrite, so those requests fall through to the serverless functions
and return JSON. One rule serves the SPA *and* protects the API.

**The same-origin boundary.** In development, `vite.config.js` proxies `/api` from
:5173 to `vercel dev` on :3000, so the browser only ever sees one origin and there is
no CORS. In production Vercel serves the built site **and** the functions from the
same domain, so the browser's relative `/api/courses` fetch is same-origin again —
no CORS headers, no preflight, nothing to allow-list. Dev deliberately matches prod:
the relative-URL fetches in `src/lib/api.js` work identically in both places precisely
because both are one origin.

**And the API is the only door to the database.** The browser holds no credentials and
never opens a socket to Postgres — it calls your `/api/*` routes, and the functions run
parameterised SQL against Neon using a connection string that exists only in their
environment. Even if a user edits the JavaScript in their browser, they cannot reach
the database directly; they can only send requests to an API that sets `user_id` from a
verified JWT and refuses to touch anyone else's rows.

## ✅ Check your work

- [ ] The production site loads at your `*.vercel.app` URL and shows the 20-course
      catalogue (so the functions reached Neon and the schema is seeded).
- [ ] Opening `https://your-app.vercel.app/courses/artisan-sourdough-bread-baking`
      directly (new tab / hard refresh) loads the detail page, **not** a Vercel 404.
- [ ] `curl https://your-app.vercel.app/api/courses` returns **JSON**, not the HTML
      of `index.html` (the `(?!api/)` lookahead is working).
- [ ] You can **sign up** (with a display name) and **sign in** on the live site, and
      an enrolment on a course shows up under `/dashboard/my-courses`.
- [ ] After enrolling, refreshing `/dashboard/my-courses` keeps you signed in and on
      the page; signed out, `/dashboard` redirects to `/login`.
- [ ] `grep -r "postgresql://" cookbake/dist/` (after `npm run build`) prints
      **nothing** — the connection string is not in the browser bundle.

## 🛠 Your turn

1. **Prove the build-time trap (safely).** In a throwaway local build, rename
   `DATABASE_URL` to `VITE_DATABASE_URL` in `.env.local`, run `npm run build`, then
   `grep -r "postgresql://" dist/assets/*.js`. Watch your password appear inside a
   public JavaScript file — that is exactly what Vite does with any `VITE_*` value.
   Delete that build, restore the correct name, and **never** do this to production.
   You now understand why the prefix is a security boundary, not a naming style.
2. **Use a preview deployment.** Create a branch, change a bit of copy (say the Hero
   line), push it, and open the preview URL Vercel comments on your PR. Confirm it
   builds and runs against your API. Merge to update production and watch Vercel
   redeploy automatically.

## Production smoke test

Run this against the **live** URL, in order:

1. Load `/` — the 20-course catalogue renders while signed out.
2. Deep-link `/courses/artisan-sourdough-bread-baking` in a fresh tab — the detail
   page loads (rewrite works).
3. Hit `/api/courses` directly — it returns JSON (the API is not rewritten away).
4. **Sign up** with a real email and a display name; **sign in**.
5. Open a course and **enroll**; it appears under `/dashboard/my-courses`.
6. On `/dashboard/my-courses`, **refresh** — you stay signed in and on the page.
7. **Sign out.** As a signed-out visitor, `/` still shows the catalogue but
   `/dashboard` redirects to `/login`.

All seven passing on the deployed URL means you have shipped a full-stack React +
Neon app.

## Security review

Open the deployed site with DevTools open:

- **Network → an API request** (e.g. loading `/dashboard/my-courses` while signed in):
  expand it and confirm an **`Authorization: Bearer …`** header carries your JWT. The
  `api/` function verifies that token and reads the user id from its `sub` claim — it
  is how the server trusts "who is asking" without believing anything the browser says.
- **No connection string in the bundle.** After `npm run build`, run
  `grep -r "postgresql://" dist/` — it must return **nothing**. The browser only ever
  sees your own `/api/*` URLs; `DATABASE_URL` lives solely in the serverless runtime.
- **The route guard is UX, not security.** `ProtectedRoute` runs in the browser, which
  is the user's machine — they can edit the JS and delete the guard. It only decides
  what the UI *shows*. The real boundary is the **API on the server**: every
  enrollments/reviews statement carries `where … and user_id = ${userId}`, with
  `userId` taken from the *verified* JWT (which can't be forged in the browser), so the
  server refuses to return or modify another user's rows no matter what the client does.
  The guard makes the app pleasant; the API makes it safe.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `/api/*` returns HTML; `await res.json()` throws `Unexpected token '<'` | The rewrite is `"/(.*)"` and swallows the API. | Use `"/((?!api/).*)"` in `vercel.json` — the negative lookahead excludes `/api/`. |
| Catalogue empty in prod, fine locally | Production database never ran the schema, or you seeded a *different* database than Vercel uses. | `psql "$DATABASE_URL" -f neon/schema.sql` against the **same** string set in Vercel. |
| API 500s in prod: "DATABASE_URL is not defined" | The env var wasn't set in Vercel (or only in Preview, not Production). | Add `DATABASE_URL` and `JWT_SECRET` in Settings → Environment Variables, then redeploy. |
| The connection string is visible in `dist/assets/*.js` | A secret was named with a `VITE_` prefix, so Vite inlined it into the bundle. | Remove the `VITE_` prefix; secrets are read by `api/` via `process.env`, never by the browser. |
| Build fails: can't find `package.json` | Root Directory left at repo root. | Set Vercel Root Directory to `cookbake`. |
| Login "works" locally but every prod login is rejected | `JWT_SECRET` differs between where the token was signed and verified, or is unset in prod. | Set one stable `JWT_SECRET` in Vercel and redeploy. |

---
### ✅ Cook & Bake Academy after this lab
The full-stack Cook & Bake Academy — React SPA, `/api` serverless functions and Neon database — is live in production on Vercel at `https://cookbake-academy.vercel.app`.
