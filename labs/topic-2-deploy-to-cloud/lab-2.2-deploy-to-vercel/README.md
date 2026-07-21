# Lab 2.2 — Deploy to Vercel

> **Topic 2** · ~40 min · Builds on Lab 2.1 (your project is on GitHub)

### 📖 The build so far
By the end of the last lab, Cook & Bake Academy lived in a GitHub repository. **In this lab you add:** a real deployment — you connect the repo to Vercel and ship the landing page to the public internet. By the end you'll have Cook & Bake Academy live at a shareable `*.vercel.app` URL that redeploys on every push.

## What you will build

You will first understand what "building" a React app actually means by running
the production build locally and previewing it. You will then **grep a value out
of the shipped bundle with your own eyes** to prove why the `VITE_` prefix is a
security rule, not a naming convention. Then you will deploy Cook & Bake Academy
to Vercel by importing your GitHub repo — no servers, no config uploads, just a
few clicks. Vercel will rebuild and redeploy automatically every time you push,
give every branch its own preview URL, and serve your app worldwide over HTTPS.
You will also add the real `vercel.json` so client-side routing (Topic 6) and the
serverless API (Topic 5) both work.

## Concepts you will meet

| Concept | In one line |
|---|---|
| Build step | Compiling your `src/` into static `dist/` files a browser can run. |
| Static hosting | Serving plain HTML/CSS/JS files — no running server needed. |
| `npm run preview` | Serve the built `dist/` locally to test the production output. |
| Production deployment | The live site at your project's main URL, built from `main`. |
| Preview deployment | A separate throwaway URL built from a branch or pull request. |
| `VITE_` prefix | The rule that decides which env vars get baked into the public browser bundle. |
| Server secret | A value read with `process.env.*` inside `api/` only — never prefixed `VITE_`. |
| SPA rewrite | Sending non-`/api/` URLs to `index.html` so the client-side router can handle them. |

## Before you start

Your `cookbake` repo must be on GitHub (Lab 2.1). You need a free Vercel account:
sign up at <https://vercel.com> with **"Continue with GitHub"** so Vercel can see
your repos.

Run everything in `cookbake/`:

```bash
cd cookbake
```

> This is a config lab. The only file you create is `vercel.json`; the rest is
> understanding the build and clicking through the Vercel dashboard.

---

## Step 1 — Understand the build: `npm run build`

Your `src/App.jsx` uses JSX and ES modules. A browser cannot run JSX directly.
When you ran `npm run dev` in Topic 1, Vite compiled your code on the fly. For a
real deployment you compile it **once, ahead of time**, into plain files:

```bash
npm run build
```

Vite reads `index.html`, follows the `<script src="/src/main.jsx">`, bundles your
whole component tree plus its dependencies, minifies it, and writes the result to
a new `dist/` folder. Look inside:

```bash
ls dist
ls dist/assets
```

You will see `index.html` and an `assets/` folder holding a hashed `.js` bundle
and a `.css` file — for example `assets/index-a1b2c3d4.js`. The hash in the name
changes whenever the content changes, which lets browsers cache the file forever
and still pick up new versions instantly. **This `dist/` folder is your entire
app.** There is no React, no Node, no server inside it — just static assets.

That is the key idea: **a React app compiles down to static HTML, CSS, and
JavaScript.** Hosting it needs nothing more than a place that serves files.

## Step 2 — Preview the production build locally

`dist/` is what the world will download, so test *that*, not just the dev server:

```bash
npm run preview
```

Vite serves `dist/` on a local URL (usually <http://localhost:4173>). Open it.
It should look and behave exactly like `npm run dev` did — the 🍞 Cook & Bake
Academy navbar, the "Master the art of cooking & baking" hero, and the grid of
course cards — but this is the minified, production output. If something works in
`dev` but breaks in `preview`, it will break in production too; this is where you
catch it first.

Stop the preview server with `Ctrl+C` when you are done. `dist/` is git-ignored
(Lab 2.1) — you never commit it. The cloud builds its own copy.

## Step 3 — See a `VITE_` value inside the shipped bundle (do this once)

Everyone *tells* you that a `VITE_` variable is public. Prove it to yourself so
you never forget. This takes two minutes and you will undo it at the end.

**a.** Create a `.env.local` in `cookbake/` with one demo variable:

```bash
echo 'VITE_DEMO_PUBLIC=super-not-a-secret-12345' > .env.local
```

**b.** Reference it once in your code so Vite has a reason to inline it. Add this
line near the top of `src/main.jsx` (just below the imports):

```js
console.log('build-time demo value:', import.meta.env.VITE_DEMO_PUBLIC)
```

**c.** Build, then grep the compiled bundle for the value:

```bash
npm run build
grep -r "super-not-a-secret-12345" dist/assets
```

It **prints a match.** Your "env variable" is sitting in plain text inside
`dist/assets/index-*.js` — the exact file every visitor downloads. Vite did not
hide it; it *substituted the literal string into the code* at build time. Open
the file if you like: `grep -o "super-not-a-secret[^\"']*" dist/assets/index-*.js`.

**d.** Now undo the experiment — this is exactly the Lab 2.1 workflow:

```bash
git restore src/main.jsx        # throw away the console.log edit
rm .env.local                   # delete the demo file (it was git-ignored anyway)
```

You just watched the security boundary with your own eyes: **anything named
`VITE_*` is compiled into the public bundle. It is not a secret. It never can
be.** Hold on to that mental image for Step 5.

## Step 4 — Add the real `vercel.json`

Copy the `vercel.json` from this lab into the root of `cookbake/`:

```bash
cp ../labs/topic-2-deploy-to-cloud/lab-2.2-deploy-to-vercel/vercel.json vercel.json
```

It contains one rule — and this is the exact file the finished `cookbake` ships:

```json
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "rewrites": [
    { "source": "/((?!api/).*)", "destination": "/index.html" }
  ]
}
```

Read the `source` pattern in two halves:

- **`(.*)` — "match every path"** is the SPA half. It tells Vercel: for any
  incoming URL, serve `index.html`. That is what makes a deep link like
  `/courses/artisan-sourdough-bread-baking` survive a browser refresh instead of
  returning a 404 (full explanation in **Why it works**).
- **`(?!api/)` — "…except anything starting with `api/`"** is a **negative
  lookahead**. Without it, the rewrite would swallow your API too: a request to
  `/api/courses` would be answered with `index.html` instead of running the
  serverless function. In Topic 5 you add real functions under `api/`; this guard
  is what lets both live in one project. `/api/*` runs as functions; everything
  else falls through to the React app.

Right now Cook & Bake Academy is a single page with no `api/` folder yet, so you
will not *see* either half do anything. It is here so the app is ready for
Topic 5 (the backend) and Topic 6 (the router). Commit and push it so Vercel
picks it up:

```bash
git add vercel.json
git commit -m "Add Vercel SPA rewrite that spares /api routes"
git push
```

## Step 5 — Environment variables: the rule that keeps your database safe

Before you deploy, open the **Environment Variables** section on the import
screen. Cook & Bake Academy needs **no variables yet** — the database and the
`api/` functions arrive in Topic 5 — but this is where they go, and Step 3 just
showed you exactly why the rule matters.

From Topic 5, the app has **two server secrets**:

| Name | What it is | Where it lives |
|---|---|---|
| `DATABASE_URL` | Your Neon Postgres connection string (`postgresql://user:password@…`). Full read/write to every row. | **Vercel → Project → Settings → Environment Variables**, read with `process.env.DATABASE_URL` inside `api/` only. |
| `JWT_SECRET` | The key the API signs and verifies login tokens with. Anyone who has it can forge a token for any user. | Same place; read with `process.env.JWT_SECRET` inside `api/` only. |

**Notice what is missing: neither name has a `VITE_` prefix — and that is the
whole design.** You proved in Step 3 that `VITE_*` values are compiled into the
public bundle. So if you ever "fixed" a connection error by renaming
`DATABASE_URL` to `VITE_DATABASE_URL`, you would publish your database password —
with full read *and* write access — to every visitor of the site, exactly the way
`super-not-a-secret-12345` ended up in `dist/assets/index-*.js`.

That is why the architecture keeps the browser away from the database entirely:

```
React (browser) --fetch--> /api/* (Vercel serverless functions) --sql--> Neon Postgres
```

The browser never holds a database credential. It calls your own `/api/*` URLs.
Only the serverless functions — running in Node on Vercel, reading
`process.env.DATABASE_URL` — ever touch Postgres. The connection string belongs
**only** in Vercel's server-side environment settings, never in a file the
browser downloads, never behind a `VITE_` prefix. Remember: **`VITE_` means
"shipped to the browser."**

> **Forward look — Topic 5.** That is where you actually paste `DATABASE_URL` and
> `JWT_SECRET` into Vercel → Settings → Environment Variables and mark them for
> Production (and Preview, if you want previews to hit a database).

For this lab, leave the variables empty and continue.

## Step 6 — Import the repo into Vercel

1. In the Vercel dashboard, click **Add New… → Project**.
2. Find **cookbake** in your list of GitHub repositories and click **Import**.
   (If you do not see it, click **Adjust GitHub App Permissions** and grant
   Vercel access to the repo.)
3. Vercel inspects the repo and **auto-detects the framework preset as Vite**.
   Confirm these settings — they should already be filled in correctly:

   | Setting | Value |
   |---|---|
   | Framework Preset | **Vite** |
   | Build Command | `npm run build` |
   | Output Directory | `dist` |
   | Install Command | `npm install` (or `npm ci`) |

   You do not need to change anything. Vercel knows how to build a Vite app.

## Step 7 — Deploy

Click **Deploy**. Vercel clones your repo, runs `npm install` then
`npm run build`, and publishes the resulting `dist/` to its global CDN. After a
minute you get a live URL like `https://cookbake-<hash>.vercel.app`. Open it —
your Cook & Bake Academy landing page is now on the public internet over HTTPS.

## Step 8 — Watch automatic redeploys

This is the payoff of connecting Git to Vercel. Make a visible change locally:

```bash
# edit the hero headline in src/App.jsx, then:
git add src/App.jsx
git commit -m "Update hero headline"
git push
```

Within seconds Vercel notices the push to `main`, rebuilds, and updates your
production URL — no button to click. Every push to `main` becomes a new
**production deployment**. If you push a *different* branch or open a pull
request, Vercel builds a separate **preview deployment** at its own URL and (for
PRs) comments the link right on GitHub. You can click that link to review the
change live before it ever reaches production. This per-branch preview is how
teams review UI changes; you get it for free.

---

## 🎤 Vibe prompt

Deployment mostly goes right — until a build fails in the cloud with a wall of
log output. That is where an AI agent earns its keep. When a Vercel build fails,
copy the failing log and paste it in:

```text
My Vercel deployment of a Vite + React app (project name cookbake) failed. Here
is the end of the build log:

<paste the red error lines from the Vercel build log here>

Tell me the single most likely cause and the exact fix. It builds fine locally
with `npm run build`, so focus on what differs in CI: case-sensitive import paths
(Linux vs macOS — e.g. importing CourseCard from './components/coursecard'), a
dependency in devDependencies that should be in dependencies, or an out-of-date
lock file. Do not rewrite my app — just diagnose the build.
```

You can also ask an agent to write the `vercel.json` rewrite — but be specific
about the `/api` exception, or it will give you the naive version that breaks the
backend:

```text
Write a vercel.json for a Vite single-page app that ALSO has serverless
functions under an /api folder. Any deep-link page URL (e.g.
/courses/artisan-sourdough-bread-baking) must serve index.html so the
client-side router handles it, but requests to /api/* must NOT be rewritten —
they have to reach the serverless functions. Use a single rewrite with a negative
lookahead. Just the rewrite, nothing else.
```

Then compare its output to the `vercel.json` in this lab — check the `(?!api/)`
is present.

## 🔍 Read what the AI wrote

No app code changed, but you changed how the project is built and served. An
agent gets these details wrong constantly — check each one:

- **`dist/` is real and complete.** After `npm run build`, `dist/index.html`
  exists and references a hashed file under `dist/assets/`. If `dist/` is empty
  or missing, the build failed — read the terminal output.
- **`preview` matches `dev`.** The site at `npm run preview` behaves like the dev
  server. A difference here (e.g. a broken course image) is a real production bug.
- **The `vercel.json` rewrite keeps the `(?!api/)` guard.** Agents love to
  "simplify" it to `"/(.*)"`. That version works today (no API yet) and silently
  breaks every `/api/*` route the moment you add the backend in Topic 5 — the
  functions get answered with `index.html` and `res.json()` chokes on a page of
  HTML. Confirm your file matches this lab's exactly.
- **`vercel.json` is valid JSON and committed.** Run
  `node -e "JSON.parse(require('fs').readFileSync('vercel.json'))"` — no output
  means it parsed. A trailing comma is the classic mistake AI and humans both make.
- **No secret got a `VITE_` prefix.** If an agent adds env vars for you, scan
  them: `DATABASE_URL` and `JWT_SECRET` must **never** start with `VITE_`. You saw
  in Step 3 where a `VITE_` value ends up.

## 🧠 Why it works

**A React app is a build artifact, not a running program.** In development, Vite
runs a server that compiles your JSX on every request so you get instant hot
reload. That server is a *dev* convenience; it is not what ships. `npm run build`
does the compilation once — transforming JSX into plain JavaScript, bundling all
your modules and their dependencies into a few files, minifying them, and adding
content hashes to the filenames — and drops the result in `dist/`. What comes out
is ordinary static assets: an `index.html`, a JavaScript bundle, a stylesheet.
There is no React "running" on a server anywhere. React runs entirely in the
visitor's browser, downloaded as that JS bundle.

Because the output is just static files, hosting is trivial and cheap: any
service that can serve files over HTTP can serve your whole app. That is why
Vercel can put it on a global CDN and why it loads fast everywhere. Vercel's real
value is not the hosting — it is the pipeline. By watching your GitHub repo, it
turns `git push` into "build in a clean Linux container, then publish." The build
happens on *their* machine from *your* committed source, which is exactly why you
never commit `dist/` (Lab 2.1): the source is the single truth, and the artifact
is regenerated on demand. It also explains a whole class of "works on my machine,
fails in CI" bugs — the cloud build starts from your lock file on a clean Linux
box, so a dependency you only have installed locally, or an import whose
capitalization is wrong (Linux filesystems are case-sensitive; macOS is not),
fails there and not on your laptop.

### Why the `VITE_` rule is a security boundary, not a naming convention

Vite deliberately refuses to expose most environment variables to browser code,
because browser code is public by definition — anyone can read it in DevTools, or
just `grep` the shipped bundle the way you did in Step 3. The one exception is
variables you *explicitly* opt in by prefixing with `VITE_`. Those get **inlined
into the bundle** at build time: the literal string value is written directly
into the JavaScript every visitor downloads. So the prefix is a promise you are
making — "this value is safe for the whole world to see." A public URL prefix
like `VITE_BASE` (Lab 2.3) keeps that promise; it is an address, not a credential.

Your two real secrets are the opposite. `DATABASE_URL` carries the database
password and grants full read/write to every row of every user. `JWT_SECRET` lets
its holder forge a login token for anyone. Give either a `VITE_` prefix and you
have published an admin credential to the internet. That is why they live only in
Vercel's **server-side** environment settings and are read with `process.env.*`
**inside `api/` functions**, which run in Node on Vercel and never ship to the
browser. The mental model that keeps you safe: **anything named `VITE_*` is
shipped to, and readable by, every browser. A server secret never gets that
prefix — it lives only in Vercel's Settings → Environment Variables and in
`process.env` on the server.**

Because a `VITE_` value is frozen into the bundle at build time, it is also *not*
something you can flip at runtime: change one in the Vercel dashboard and nothing
updates until the next build. That is why editing a `VITE_` env var on Vercel
always means "redeploy." A server secret like `DATABASE_URL` is different — it is
read fresh from `process.env` each time a function runs, so changing it takes
effect on the next request (Topic 5).

### Why the SPA rewrite is needed

Your built app has exactly **one** HTML file: `dist/index.html`. When React
Router (Topic 6) shows a page at, say, `/courses/artisan-sourdough-bread-baking`,
it is not loading a new file — it is JavaScript swapping components while updating
the URL bar. That works fine as long as the browser already has `index.html`
loaded. But if a user **refreshes** on that URL, or pastes the deep link into a
fresh tab, the browser asks the *server* for a file at that path. There is no
`courses/artisan-sourdough-bread-baking.html` in `dist/` — so a naive static host
returns **404**.

The rewrite fixes this at the host: `{ "source": "/((?!api/).*)", "destination":
"/index.html" }` tells Vercel to answer *every path except `/api/*`* with
`index.html`. The app boots, React Router reads the URL, and renders the right
page. The `(?!api/)` lookahead is what keeps that generosity from eating your
backend: `/api/courses` is left alone so its serverless function can run. One
config line turns a pile of static files into something that behaves like a
multi-page app on refresh and deep-link, while still hosting a real API in the
same project. This is also why Vercel is the primary target in this course: a
rewrite is a first-class feature here, whereas on GitHub Pages (Lab 2.3) you
resort to a `404.html` copy trick or a `HashRouter`, and Pages cannot host the
`api/` functions at all.

## ✅ Check your work

- [ ] `npm run build` completes and creates `dist/index.html` + `dist/assets/…`.
- [ ] `npm run preview` serves the built site and it looks correct.
- [ ] You saw a `VITE_` demo value with `grep` inside `dist/assets/`, then undid the experiment.
- [ ] `vercel.json` exists in the project root, matches this lab (with `(?!api/)`), is valid JSON, and is committed.
- [ ] Your Vercel project's live `.vercel.app` URL loads Cook & Bake Academy over HTTPS.
- [ ] The import screen showed **Framework Preset: Vite** auto-detected.
- [ ] A `git push` to `main` triggers a new production deployment automatically.
- [ ] You can explain why `DATABASE_URL` and `JWT_SECRET` must never carry a `VITE_` prefix.

## 🛠 Your turn

1. Create a branch (`git checkout -b tweak-hero`), change the hero text, push it,
   and open a pull request on GitHub. Find the **preview deployment** URL Vercel
   posts and open it. Confirm production is unchanged. Then merge the PR and watch
   production update.
2. Redo the Step 3 experiment, but this time try to prove a *server* secret would
   leak: set `VITE_FAKE_DB_URL=postgresql://user:hunter2@host/db` in `.env.local`,
   reference it once in `src/main.jsx`, build, and `grep` for `hunter2` in
   `dist/assets`. Watch the password appear in the bundle — then `git restore` and
   delete the file. This is the mistake the `VITE_` rule exists to prevent.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| Build fails in Vercel but works locally | CI runs a clean install on Linux from your lock file. | Commit an up-to-date `package-lock.json`; check for import paths whose capitalization differs from the real filename (case-sensitive on Linux). |
| Page is blank; console shows a 404 for the JS asset | Wrong base path — Vite built assets at `/` but they are served elsewhere. | On Vercel the base is `/`, so leave `vite.config.js` alone. (The `base` setting is a *Pages* concern — see Lab 2.3.) |
| Refresh on `/courses/<slug>` returns 404 (once you add Router in Topic 6) | No SPA rewrite. | Add the `vercel.json` rewrite from Step 4 and redeploy. |
| `/api/*` calls return HTML / `Unexpected token '<'` (Topic 5+) | The rewrite was simplified to `"/(.*)"`, so it swallows the API and serves `index.html`. | Restore the `(?!api/)` negative lookahead exactly as in this lab. |
| Database/auth calls fail in production but work locally (Topic 5+) | `DATABASE_URL` / `JWT_SECRET` set in `.env.local` are not uploaded to Vercel. | Add them in Vercel **Settings → Environment Variables** (no `VITE_` prefix), then redeploy. |
| `vercel.json` ignored | Invalid JSON (often a trailing comma) or not committed/pushed. | Validate the JSON and confirm it is in the pushed commit. |

---
### ✅ Cook & Bake Academy after this lab
Cook & Bake Academy is live on a public Vercel URL and auto-deploys whenever you push to GitHub.
