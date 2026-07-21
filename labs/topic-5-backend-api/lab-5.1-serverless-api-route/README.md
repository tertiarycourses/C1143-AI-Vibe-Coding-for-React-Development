# Lab 5.1 — The Three Tiers: Your First API Route over Neon

> **Topic 5** · ~55 min · Builds on Topic 4 (the app runs on hardcoded data)

### 📖 The build so far
By the end of Topic 4, Cook & Bake Academy was a polished front end running entirely on the hardcoded `courses` array in `src/data/courses.js`. **In this lab you add:** a real backend — a Neon Postgres database and your first two **serverless API routes** (`/api/courses` and `/api/courses/:slug`) that read from it. No React yet; you build and test the server tier on its own with `curl`. By the end you'll have a running API that serves the 20-course catalogue out of Postgres — and you'll fire a real SQL-injection attack at it and watch it bounce.

## What you will build

The **server tier** of a three-tier app:

```
React (browser)  --fetch-->  /api/* (Vercel serverless functions)  --sql-->  Neon Postgres
```

You provision a free Neon Postgres project, load `neon/schema.sql` (20 courses),
and write two serverless functions: `api/courses/index.js` (the whole catalogue,
with optional `?category=` / `?q=` filters) and `api/courses/[slug].js` (one
course or a 404). The database password lives **only** on the server, never in
the browser bundle. Then you attack your own API to prove the parameterised SQL
is injection-proof.

## Concepts you will meet

| Concept | In one line |
|---|---|
| Three-tier architecture | Browser → your `/api/*` functions → Postgres; the browser never holds a DB credential. |
| Serverless function | A file in `api/` that exports `handler(req, res)`; Vercel runs it on demand, no server to manage. |
| Dynamic route (`[slug].js`) | The `[slug]` in the **filename** matches `/api/courses/anything` and gives you `req.query.slug`. |
| `DATABASE_URL` (no `VITE_`) | The connection string is a **server** env var; a `VITE_` prefix would publish it to every visitor. |
| Tagged-template SQL | ``sql`... where slug = ${slug}` `` sends query text and values to Postgres **separately** — a parameterised query. |
| SQL injection (and why it can't happen here) | User input travels as a bound value, never as SQL the database parses. |

## Before you start

You should have the Topic 4 app in `cookbake/` (`npm run dev` works). This lab
adds the `api/` folder and three config files. Copy them in:

```bash
cp -R "labs/topic-5-backend-api/lab-5.1-serverless-api-route/api/." cookbake/api/
cp  "labs/topic-5-backend-api/lab-5.1-serverless-api-route/.env.example"  cookbake/.env.example
cp  "labs/topic-5-backend-api/lab-5.1-serverless-api-route/vercel.json"   cookbake/vercel.json
cp  "labs/topic-5-backend-api/lab-5.1-serverless-api-route/vite.config.js" cookbake/vite.config.js
```

That adds `api/_lib/db.js`, `api/_lib/auth.js`, `api/courses/index.js`,
`api/courses/[slug].js`, and the three config files. `api/_lib/auth.js` carries
shared plumbing (`sendError`, `requireMethod`, and the JWT helpers you'll use in
Lab 5.3) — the courses routes import `sendError` and `requireMethod` from it, so
it ships now.

---

## Step 1 — Draw the three tiers

Before any code, get the shape in your head. There are **three** tiers, and the
arrow only ever points one way:

```
┌──────────────────┐   fetch('/api/..')   ┌─────────────────────┐   sql`..`   ┌──────────────┐
│  React (browser) │ ───────────────────▶ │  /api/* functions   │ ──────────▶ │ Neon Postgres│
│  no credentials  │ ◀─────────────────── │  DATABASE_URL here   │ ◀────────── │  the data    │
└──────────────────┘       JSON           └─────────────────────┘   rows      └──────────────┘
```

The browser **never** talks to Postgres. It knows one thing: how to call our own
`/api/*` URLs. Everything about security — who may read, who may write, whose
data is whose — lives in the middle tier, on the server, where a visitor cannot
edit it. This is the single most important idea in the whole topic. If you ever
find yourself importing `@neondatabase/serverless` into a file under `src/`, stop:
that puts the database in the browser, which is the architecture we are
deliberately leaving behind.

## Step 2 — Create a Neon project and get the connection string

1. Go to <https://neon.tech>, sign in, and click **New project**. Name it
   `cookbake`, pick a region near you, create it. Neon is serverless Postgres, so
   provisioning takes seconds — there is no instance to wait for.
2. On the project dashboard click **Connect** and copy the **connection string**.
   It looks like:

   ```
   postgresql://USER:PASSWORD@ep-xxx.region.aws.neon.tech/neondb?sslmode=require
   ```

That string contains your database **password** with full read **and** write
access. Treat it like one. It belongs on the server and nowhere else — Step 4 is
about keeping it there.

## Step 3 — Load the schema and seed the 20 courses

`neon/schema.sql` (already in the repo) creates the `users`, `courses`,
`enrollments` and `reviews` tables and seeds the 20 courses. Run it once. Put
your connection string in a shell variable first so it isn't stored in your
history in plain sight:

```bash
export DATABASE_URL='postgresql://USER:PASSWORD@ep-xxx.region.aws.neon.tech/neondb?sslmode=require'
psql "$DATABASE_URL" -f neon/schema.sql
```

**No `psql`?** No problem — open the Neon **SQL Editor** in the Console, paste the
entire contents of `neon/schema.sql`, and click **Run**. The script uses
`if not exists` / `on conflict (code) do nothing`, so it is safe to run twice.

Verify 20 courses landed:

```bash
psql "$DATABASE_URL" -c 'select count(*) from courses;'   #  -> 20
```

## Step 4 — Install the server dependencies

The serverless functions run in Node and need three packages — the Neon driver,
and bcrypt + JWT (for Labs 5.3–5.4, installed now so you do it once):

```bash
cd cookbake
npm install @neondatabase/serverless bcryptjs jsonwebtoken
```

## Step 5 — Put the secrets in `.env.local` — with NO `VITE_` prefix

```bash
cp .env.example .env.local
```

Open `.env.local` and paste your real values:

```
DATABASE_URL=postgresql://USER:PASSWORD@ep-xxx.region.aws.neon.tech/neondb?sslmode=require
JWT_SECRET=  # generate one below
```

Generate a real `JWT_SECRET` (you'll use it in Lab 5.3):

```bash
node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
```

`.env.local` is **git-ignored** — never commit real secrets.

**Now the rule that matters most in this entire course.** Notice neither variable
has a `VITE_` prefix. That is not a style choice. Vite splits env vars into two
worlds:

- **`VITE_SOMETHING`** — Vite finds `import.meta.env.VITE_SOMETHING` in your
  source and **substitutes the value straight into the JavaScript it ships**.
  Anyone can open DevTools, or just read `dist/assets/index-*.js`, and see it. A
  `VITE_` variable is **public. Always. No exception.**
- **`SOMETHING`** (no prefix) — stays on the server. Vite never touches it. Only
  code running in Node (our `api/` functions) reads it, via `process.env.SOMETHING`.

So if you ever "fix" a connection error by renaming `DATABASE_URL` to
`VITE_DATABASE_URL`, you have just published your database password — with read
**and** write — to every visitor of your site. There is no safe way to put a
password in a `VITE_` variable. The whole three-tier design exists so the
password lives only where `process.env` can reach it.

## Step 6 — Read `api/_lib/db.js` — the one door to Postgres

Open `api/_lib/db.js`. It is short:

```js
import { neon } from '@neondatabase/serverless'

// runs on Vercel's servers, never in the browser
export const sql = neon(process.env.DATABASE_URL)
```

This is the **only** file in the whole app that holds a connection to Postgres,
and it reads the password from `process.env` — a value that only exists on the
server. `sql` is a **tagged-template function** (Step 9 is entirely about why
that word matters). Every query in `api/` goes through this one `sql`.

## Step 7 — Read the two course routes

**`api/courses/index.js`** — the public catalogue, `GET /api/courses`:

```js
const { category, q } = req.query ?? {}
const search = q ? `%${q}%` : null

const courses = await sql`
  select id::int as id, code, slug, title, category, level,
         fee::float8 as fee, weeks, campus, summary, emoji, image, created_at
  from courses
  where (${category ?? null}::text is null or category = ${category ?? null})
    and (${search}::text is null
         or title ilike ${search} or summary ilike ${search} or code ilike ${search})
  order by id
`
```

Two things to notice. First, **there is no `requireAuth()`** — the catalogue is
what a visitor sees before they have an account, so reads are public. Second, the
optional filters **switch themselves off** when the parameter is absent
(`${category ?? null} is null` is true for every row), so one query handles all
of `/api/courses`, `?category=Bakery` and `?q=sourdough` without gluing strings
together.

> **Why the casts?** Postgres `bigint` (our ids) and `numeric` (our fee) arrive
> in JavaScript as **strings** — a bigint can exceed `Number.MAX_SAFE_INTEGER`,
> so the driver refuses to guess. `id::int` and `fee::float8` hand the browser
> real numbers. Skip the cast and `course.id === enrollment.course_id` silently
> compares `1` with `"1"` and is always false. That bug is miserable to find.

**`api/courses/[slug].js`** — one course, `GET /api/courses/:slug`:

```js
const { slug } = req.query ?? {}
const rows = await sql`select ... from courses where slug = ${slug}`
if (rows.length === 0) throw new HttpError(404, `No course found at /courses/${slug}.`)
return res.status(200).json(rows[0])
```

The `[slug]` in the **filename** is what makes this a dynamic route: Vercel
matches `/api/courses/anything` and hands you the matched segment as
`req.query.slug`. No row means a real **404**, not a `200` with `null` — the
status code *is* the API's answer, and the frontend (Lab 5.2) renders its
"Course not found" page from it.

## Step 8 — Run it and hit it with curl

The API functions are run by `vercel dev`, which reads `.env.local`:

```bash
npx vercel dev --listen 3000
```

(The first time it asks to link the project — accept the defaults.) In another
terminal, call your API:

```bash
curl -s http://localhost:3000/api/courses | head
curl -s 'http://localhost:3000/api/courses?category=Bakery'
curl -s http://localhost:3000/api/courses/artisan-sourdough-bread-baking
```

The first returns the 20-course array, the second only the 10 Bakery courses, the
third one course object. A made-up slug returns a 404 body:

```bash
curl -s http://localhost:3000/api/courses/does-not-exist
# {"error":"No course found at /courses/does-not-exist."}
```

## Step 9 — MANDATORY: attack your own API and watch it bounce

You are about to fire a real SQL-injection payload at your own database. **Do
it.** Seeing the attack fail — and understanding *why it was never going to work*
— is the whole point of this lab.

The classic attack tries to smuggle SQL through a value. Try to drop the `users`
table through the slug, and try to bypass the search with `' OR 1=1 --`:

```bash
curl -s "http://localhost:3000/api/courses/x'%3B%20drop%20table%20users%3B%20--"
curl -s --get --data-urlencode "q=' OR 1=1 --" http://localhost:3000/api/courses
```

Expected result: the first returns a clean **404**, the second returns an **empty
array `[]`** (no course title/summary/code contains the literal text
`' OR 1=1 --`). Nothing executed. Now confirm your table is untouched:

```bash
psql "$DATABASE_URL" -c '\dt'                     # users is still listed
psql "$DATABASE_URL" -c 'select count(*) from users;'   # still there (0 rows, but the TABLE lives)
```

The `users` table is exactly where it was. **Prove to yourself it's not luck —
read the *Why it works* section, then try to reintroduce the hole and watch even
that get rejected.**

---

## 🎤 Vibe prompt

```text
I'm building the server tier of a three-tier app: React in the browser calls my
own /api/* serverless functions, which are the ONLY code that talks to Neon
Postgres. The browser holds no DB credentials. I already have api/_lib/db.js
exporting `sql = neon(process.env.DATABASE_URL)` (a tagged-template function) and
api/_lib/auth.js exporting sendError(res, err), requireMethod(req, ...verbs) and
an HttpError class. Create two Vercel serverless routes in plain ESM (each a
default `export default async function handler(req, res)`):

1. api/courses/index.js — GET /api/courses, PUBLIC (no auth). Optional query
   params ?category= and ?q=. Return all columns of `courses` with id cast to int
   and fee cast to float8, ordered by id. Build ONE parameterised query using the
   tagged template `sql`, where each filter switches off when its param is absent
   (e.g. `where (${category ?? null}::text is null or category = ${category ?? null})`
   and an ilike search on title/summary/code). NEVER concatenate values into the
   SQL string. Call requireMethod(req,'GET') and wrap everything in try/catch that
   ends in sendError(res, err).

2. api/courses/[slug].js — GET one course by slug from req.query.slug via a
   tagged-template query `where slug = ${slug}`. If no row, throw new HttpError(
   404, ...). Return the single row object, else sendError.

Do not use sql.unsafe or string concatenation anywhere.
```

## 🔍 Read what the AI wrote

- **Did it build SQL by concatenation?** The one fatal mistake. Grep the output
  for a backtick-or-quote query with `${` **inside a plain string** —
  ``sql(`... '${slug}'`)`` or `` `select ... ${slug}` `` passed to a normal
  function. That is string interpolation and it *is* injectable. Every query must
  be `` sql`...${value}...` `` — the value directly in a **tagged** template.
- **Did it reach for `sql.unsafe(...)`?** Some drivers expose an escape hatch that
  interpolates raw text. There is deliberately none in this codebase. If the AI
  suggests it, refuse — it reopens the exact hole you're closing.
- **Is `?category` / `?q` optional, or did it write two queries?** The tell of
  weaker code is an `if (category)` that concatenates a `WHERE` clause. One
  self-switching parameterised query is safer and simpler.
- **Are the casts there?** No `id::int` / `fee::float8` and the browser gets
  strings; `course.id === enrollment.course_id` breaks later.
- **404 vs 200-with-null.** A missing course must throw a 404, not return `null`
  with status 200 — the frontend keys its not-found page off the status.
- **Is `requireAuth` wrongly called on the public catalogue?** These are public
  reads. An auth check here locks out signed-out visitors.

## 🧠 Why it works

**The three tiers, and where the password lives.** In a two-tier design the
browser talks straight to the database, which means the database credential must
be *in the browser* — and anything in the browser is public. The third tier fixes
this: the browser calls `/api/*`, and only the server tier holds `DATABASE_URL`.
`sql = neon(process.env.DATABASE_URL)` reads that password from `process.env`,
which exists only in the Node process Vercel runs. Vite never sees it (no `VITE_`
prefix), so it is never compiled into anything a visitor downloads. The database
is genuinely unreachable from the browser, by construction.

**`sql` is a *tagged template*, and that is the entire security story.** Look
closely at the punctuation:

```js
await sql`select * from courses where slug = ${slug}`   //  ✅ tagged template
```

There are **no parentheses**. `sql` is not being *called* with a finished string;
it is *tagging* a template literal. That distinction changes everything. JavaScript
hands the `sql` function two things separately: the static text chunks
(`['select * from courses where slug = ', '']`) and the array of interpolated
values (`[slug]`). The Neon driver turns that into a **parameterised query** — it
sends Postgres the query text with a numbered placeholder (`... where slug = $1`)
and sends the value `$1 = slug` as a *separate* argument. Postgres **parses the
SQL first**, decides `$1` is a value slot in a `WHERE` comparison, and *only then*
binds your input into that slot. Your input arrives after parsing is done, so it
can never *become* SQL. A slug of `x'; drop table users; --` is looked up as one
absurd literal string, matches no row, and returns a 404. It is not that the driver
"escaped" the dangerous characters — it is that your input was never on the code
path where SQL grammar is interpreted at all.

**The one thing that would reintroduce the hole.** Build the string yourself and
you throw all of that away:

```js
await sql(`select * from courses where slug = '${slug}'`)   // ⛔ NEVER — string-built
```

Now `sql` is *called* (parentheses!) with a single finished string in which
`${slug}` was already glued in *before* Postgres ever saw it. There are no
separate values, no placeholders — just text. A slug of
`x' union select ... --` becomes part of the SQL the parser reads, and the attack
runs. Try it as an experiment on a throwaway query and you'll see the difference
immediately. The rule that follows is absolute: **never build SQL by
concatenation**, and there is **no `sql.unsafe()` anywhere in this codebase**,
deliberately — there is simply no door to walk user input through. Every query in
`api/` is a tagged template for exactly this reason.

**Why query-string filters are safe here.** `?category=` and `?q=` are
attacker-controlled — a visitor types whatever they like. They are also harmless,
because they only ever travel as `${}` placeholders inside a tagged template.
Postgres binds them as values, never parses them as SQL, so no `?q=` payload can
change what the query *does*; it can only change what it *searches for*.

**404 is data, not a crash.** The status code is part of the API's answer. A
missing course returns `404` with a small JSON body, not a `500` (that would say
"the server broke") and not a `200` with `null` (that would say "here's your
course: nothing"). Getting the status right here is what lets Lab 5.2's
`useCourse` render a clean "Course not found" page instead of a red error.

## ✅ Check your work

- [ ] `psql "$DATABASE_URL" -c 'select count(*) from courses;'` returns **20**.
- [ ] `.env.local` holds `DATABASE_URL` and `JWT_SECRET` and **neither** has a
      `VITE_` prefix; you can explain why a `VITE_` prefix would be a breach.
- [ ] `npx vercel dev --listen 3000` is running and
      `curl http://localhost:3000/api/courses` returns the 20-course array.
- [ ] `?category=Bakery` returns 10 courses; `/api/courses/does-not-exist`
      returns a **404** body.
- [ ] The SQL-injection probes returned a 404 and an empty `[]`, and
      `\dt` still lists the `users` table.
- [ ] You can point at a `` sql`...${x}...` `` and say why it is NOT string
      interpolation — and name the one rewrite (string-built SQL / `sql.unsafe`)
      that would reintroduce the hole.

## 🛠 Your turn

1. Add a `?level=` filter (Beginner/Intermediate/Advanced) to
   `api/courses/index.js`, using the same self-switching pattern
   (`(${level ?? null}::text is null or level = ${level ?? null})`). Test with
   `curl 'http://localhost:3000/api/courses?level=Beginner'`.
2. As a controlled experiment, add a **temporary** route that builds the query by
   concatenation (`` sql(`select * from courses where slug = '${slug}'`) ``), fire
   the `x'; drop table courses; --` payload at it against a **throwaway** copy of
   the table, and watch it actually execute. Then delete the route. Feeling the
   difference once is worth a hundred warnings — never ship it.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `DATABASE_URL is not set` thrown at startup | `.env.local` missing/mis-named, or `vercel dev` not restarted after editing it. | Create `.env.local` with `DATABASE_URL` (no `VITE_`) and restart `npx vercel dev`. |
| `curl` returns an HTML page / `Unexpected token '<'` | You hit Vite (`:5173`) instead of the API (`:3000`). | Call `http://localhost:3000/api/...`, or set up the proxy in Lab 5.2. |
| `permission denied` / relation "courses" does not exist | The schema wasn't run against this database. | `psql "$DATABASE_URL" -f neon/schema.sql`, or paste it into the Neon SQL Editor. |
| `course.id === x` is always false later | Missing `id::int` / `fee::float8` casts — Postgres returned strings. | Cast in the `select`, as the real routes do. |
| A missing course returns `200` with `null` | The route returned the row without checking `rows.length`. | `if (rows.length === 0) throw new HttpError(404, ...)`. |
| An attacker payload actually ran | You built SQL with string concatenation or `sql.unsafe()`. | Use a tagged template (`` sql`...${value}` ``) for every query; never concatenate. |

---
### ✅ Cook & Bake Academy after this lab
The 20-course catalogue is served by your own serverless API over Neon Postgres — and it shrugs off SQL injection because every query is a parameterised tagged template.
