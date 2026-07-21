# Lab 2.3 — GitHub Pages with GitHub Actions

> **Topic 2** · ~40 min · Builds on Lab 2.2 (you understand the build and `dist/`)

### 📖 The build so far
By the end of the last lab, Cook & Bake Academy was live on Vercel. **In this lab you add:** a second, do-it-yourself deployment path — a GitHub Actions workflow that builds the app and publishes `dist/` to GitHub Pages. By the end you'll have Cook & Bake Academy deploying through your own CI/CD pipeline as well as Vercel.

## What you will build

You will deploy the same Cook & Bake Academy app a second time, to **GitHub
Pages**, using a **GitHub Actions** workflow that builds your app in the cloud and
publishes it — entirely inside GitHub, no third-party service. Along the way you
will meet the two things that trip up every first-time Pages deployment: the
**base path** (a different config knob than Vercel needed) and **SPA deep-link
404s**. You will make one `vite.config.js` serve both Vercel and Pages from a
single source.

## Concepts you will meet

| Concept | In one line |
|---|---|
| GitHub Actions | GitHub's built-in CI/CD: run steps in a cloud container on events like "push". |
| Workflow file | A `.yml` in `.github/workflows/` describing jobs and steps. |
| Job / step | A job runs on one machine; steps are the commands and actions it runs. |
| Action (`uses:`) | A reusable, versioned building block, e.g. `actions/checkout@v4`. |
| `permissions` | The exact access a workflow is granted — least privilege. |
| Artifact | A file bundle one job produces and another consumes; here, your `dist/`. |
| `base` path | The URL prefix Vite bakes into asset links — `/` for Vercel, `/<repo>/` for Pages. |
| `npm ci` | A clean, lock-file-exact install for CI — stricter than `npm install`. |

## Before you start

Your repo is on GitHub (Lab 2.1) and you understand `npm run build` → `dist/`
(Lab 2.2). This lab assumes your repository is named **`cookbake`**. If yours has
a different name, change **`cookbake`** to your repo name in two places below: the
`VITE_BASE` value in the workflow and (only if you test locally) the `VITE_BASE`
you pass to `npm run build`.

Two files from this lab go into your project:

```bash
cd cookbake
mkdir -p .github/workflows
cp ../labs/topic-2-deploy-to-cloud/lab-2.3-github-pages-actions/.github/workflows/deploy.yml .github/workflows/deploy.yml
cp ../labs/topic-2-deploy-to-cloud/lab-2.3-github-pages-actions/vite.config.js vite.config.js
```

> Config-only lab: you write no application code, but you do author a YAML
> workflow and edit `vite.config.js`.

---

## Step 1 — Make one `vite.config.js` work for both hosts

Open the `vite.config.js` you just copied:

```js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  base: process.env.VITE_BASE ?? '/',
  plugins: [react()],
})
```

The only change from the Topic 1 config is the `base` line. `base` is the URL
prefix Vite writes into every asset link in the built `index.html`. Vercel and
local dev serve your site from the domain root, so they need `base: '/'`. GitHub
Pages serves your site from a **sub-path** — `https://<user>.github.io/cookbake/`
— so on Pages the assets must be requested from `/cookbake/`, not `/`. Get this
wrong and you get a blank page: the HTML loads but the browser looks for the JS
bundle at the wrong URL and 404s.

Reading `base` from `process.env.VITE_BASE` keeps a **single config** honest for
both hosts. When the env var is unset (local dev, `npm run preview`, Vercel) it
falls back to `'/'`. The Pages workflow sets `VITE_BASE=/cookbake/` only for its
build. No `if HOST === …` branching, no second config file.

> `VITE_BASE` is a *public* value — a URL prefix, not a credential — so it is fine
> to have Vite bake it into the bundle. That is the one legitimate use of a `VITE_`
> variable. Your server secrets from Topic 5 (`DATABASE_URL`, `JWT_SECRET`) are the
> opposite and never appear here (Lab 2.2).

## Step 2 — Read the workflow file

Open `.github/workflows/deploy.yml`. It is the correct, current shape for
deploying a static build to Pages. Walk through it:

```yaml
on:
  push:
    branches: [main]     # deploy whenever main changes
  workflow_dispatch:     # ...and let you trigger it by hand

permissions:
  contents: read         # read your code
  pages: write           # publish to Pages
  id-token: write        # prove identity to Pages via OIDC (required by deploy-pages)

concurrency:
  group: pages
  cancel-in-progress: false   # never interrupt a running publish
```

Then two jobs. **`build`** compiles the app and uploads the result as a Pages
artifact:

```yaml
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm            # cache ~/.npm so npm ci is fast on repeat runs
      - run: npm ci
      - env:
          VITE_BASE: /cookbake/   # <-- your repo name, with leading+trailing slash
        run: npm run build
      - uses: actions/upload-pages-artifact@v3
        with:
          path: dist            # upload the build output
```

**`deploy`** takes that artifact and publishes it:

```yaml
  deploy:
    needs: build                # wait for build to finish
    runs-on: ubuntu-latest
    environment:
      name: github-pages        # required: this is the Pages deploy environment
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - uses: actions/configure-pages@v5
      - id: deployment
        uses: actions/deploy-pages@v4
```

Every `uses:` is pinned to a current major version: `checkout@v4`,
`setup-node@v4`, `upload-pages-artifact@v3`, `configure-pages@v5`,
`deploy-pages@v4`. Pinning to a major keeps the workflow working while still
receiving patch fixes.

## Step 3 — Turn on Pages and point it at Actions

1. On GitHub, open your repo → **Settings → Pages**.
2. Under **Build and deployment → Source**, choose **GitHub Actions** (not
   "Deploy from a branch"). This tells Pages to accept deployments from the
   workflow instead of serving a branch directly.

You do not upload anything here — the workflow does the publishing.

## Step 4 — Commit, push, and watch it run

```bash
git add vite.config.js .github/workflows/deploy.yml
git commit -m "Add GitHub Pages deploy via Actions"
git push
```

Open the repo's **Actions** tab. You will see the "Deploy to GitHub Pages" run
start: the `build` job installs and builds, then `deploy` publishes. When both
jobs go green, the `deploy` job shows the live URL — typically
`https://<your-username>.github.io/cookbake/`. Open it: Cook & Bake Academy is
now served from GitHub's own infrastructure.

> **Vercel is still live too.** You now have the same landing page deployed two
> ways. That is the point — you have seen both a managed platform (Vercel) and a
> raw CI/CD pipeline (Actions), and one `vite.config.js` feeds both.

## Step 5 — Meet the SPA deep-link 404 (and how Pages handles it)

Cook & Bake Academy is one page today, so you will not hit this yet — but you
must know it before Topic 6. GitHub Pages, like any plain static host, maps URLs
to files. It has your `index.html`, but once you add React Router and a user
refreshes on `/courses/artisan-sourdough-bread-baking`, Pages looks for a file at
that path, finds none, and returns **404**. Vercel solved this with the
`vercel.json` rewrite (Lab 2.2). Pages has **no rewrite feature**, so you use one
of two workarounds:

- **The `404.html` copy trick.** Add a build step that copies `dist/index.html`
  to `dist/404.html`. Pages serves `404.html` for any unknown path, so your app
  boots and the router takes over. It works, but it is a hack — the server still
  thinks it served an error page.
- **`HashRouter`.** Put the route in the URL *fragment*:
  `.../#/courses/artisan-sourdough-bread-baking`. The part after `#` never reaches
  the server, so there is nothing to 404 on. The cost is uglier URLs with a `#` in
  them.

Both work; neither is as clean as Vercel's rewrite, where the host natively
understands "send everything to `index.html`." This trade-off is a big reason
this course treats Vercel as the primary deploy target and Pages as the free
alternative for the *static* site. You will revisit this in Topic 6 when routing
actually exists.

> **The bigger reason Pages cannot host the finished app.** From Topic 5 on, Cook
> & Bake Academy is a **full-stack** app: the React front end calls serverless
> functions under `api/`, which talk to a Neon Postgres database:
>
> ```
> React (browser) --fetch--> /api/* (Vercel serverless functions) --sql--> Neon Postgres
> ```
>
> GitHub Pages is a **static file host** — it can serve your `dist/`, but it
> **cannot run the `api/` functions at all**. There is no server to execute
> `api/courses/index.js`, so every `/api/*` call on a Pages deployment just 404s.
> That is why the full-stack deploy in Topic 6 targets **Vercel**, which serves the
> built site *and* runs the functions from one origin. Treat this Pages deploy as
> practice with CI/CD on the static landing page — a great skill, but not where the
> database-backed app will live.

---

## 🎤 Vibe prompt

Hand-writing correct CI YAML from memory is exactly the kind of fiddly,
version-sensitive task an AI agent is good at — and exactly where it also tends
to produce *out-of-date* action versions. Use the agent, then verify the versions.

```text
Write a GitHub Actions workflow at .github/workflows/deploy.yml that deploys a
Vite + React app (plain JavaScript, Node 22, project name cookbake) to GitHub
Pages on every push to main. Requirements:
- Use the official Pages actions: actions/checkout, actions/setup-node (with npm
  cache), actions/configure-pages, actions/upload-pages-artifact (path: dist),
  and actions/deploy-pages.
- Two jobs: a build job that runs `npm ci` then `npm run build` and uploads the
  dist folder as the Pages artifact, and a deploy job that needs build and
  publishes it.
- Set permissions to contents: read, pages: write, id-token: write.
- Add concurrency group "pages" with cancel-in-progress: false.
- The deploy job must use environment: github-pages.
- Set VITE_BASE=/cookbake/ as an env var on the build step only.
Use the current latest MAJOR version of each action and tell me which versions
you used so I can confirm they are current.
```

When a run fails, feed the log back in:

```text
My GitHub Pages deploy failed. Here is the failing step's log:

<paste the red lines from the Actions log>

The app builds fine locally with `npm run build`. Diagnose the CI-specific
cause — a missing permission, Pages source not set to "GitHub Actions", an
out-of-date action version, or a wrong VITE_BASE — and give me the exact fix.
```

## 🔍 Read what the AI wrote

No app code, but a YAML workflow and a config edit — both easy to get subtly
wrong, and both places agents reliably slip up. Check:

- **The YAML parses.** Run `npx js-yaml .github/workflows/deploy.yml` (or paste
  into the Actions tab, which lints on push). Indentation errors are the number
  one cause of a workflow that silently never runs.
- **Action versions are current.** Confirm `checkout@v4`, `setup-node@v4`,
  `upload-pages-artifact@v3`, `configure-pages@v5`, `deploy-pages@v4`. AI agents
  frequently emit stale ones (e.g. `deploy-pages@v2`, `checkout@v3`) that fail or
  warn. If an agent wrote your workflow, this is the first thing to audit.
- **Permissions are exactly these three.** `contents: read`, `pages: write`,
  `id-token: write`. Missing `id-token: write` makes `deploy-pages` fail with an
  OIDC error; a too-broad `contents: write` is an unnecessary risk.
- **`base` reads the env var, with a `/` fallback.**
  `grep base vite.config.js` should show `process.env.VITE_BASE ?? '/'`. A
  hard-coded `base: '/cookbake/'` would break local dev and Vercel.
- **`VITE_BASE` matches your repo name** and has both a leading and trailing
  slash (`/cookbake/`). No leading slash, or a missing trailing slash, and the
  asset URLs come out wrong.
- **Pages source is "GitHub Actions"**, not "Deploy from a branch" (Step 3).

## 🧠 Why it works

**GitHub Actions is CI/CD that lives in your repo.** A workflow is a YAML file
that says: on some event, spin up a fresh Linux container and run these steps.
Here the event is a push to `main`. The steps do exactly what you did by hand in
Lab 2.2 — check out the code, install dependencies, run `npm run build` — except
on GitHub's machine, reproducibly, every time. `npm ci` (rather than
`npm install`) is the CI-correct choice: it deletes any existing `node_modules`
and installs the **exact** versions pinned in `package-lock.json`, failing if the
lock file and `package.json` disagree. That determinism is the whole point of CI —
the build must not depend on whatever happens to be on someone's laptop.

The workflow is split into two jobs for a reason. `build` produces the `dist/`
folder and hands it off with `upload-pages-artifact` as a named **artifact** — a
bundle that outlives the job. `deploy` declares `needs: build`, so it waits, then
`deploy-pages` takes that artifact and publishes it to Pages. Splitting build
from publish means the privileged publish step is small and isolated. That is
also why `permissions` is spelled out: by default a workflow gets a broad token,
but here you grant only what the deploy needs — `pages: write` to publish and
`id-token: write` so `deploy-pages` can use OIDC to prove to Pages that this run
is authorized. Least privilege: the workflow can publish the site and read the
code, and nothing more. The `concurrency` block with `cancel-in-progress: false`
ensures two rapid pushes do not race to publish and leave the site in a torn
state; the running deploy finishes, then the newest one runs. The
`environment: github-pages` on the deploy job is required — Pages only accepts
deployments that target that named environment, which is what your Step 3 setting
enables.

### The base-path gotcha, precisely

Vite writes asset URLs into the built `index.html` at build time, prefixed by
`base`. With the default `base: '/'`, the HTML asks for `/assets/index-abc.js` —
an *absolute* path from the domain root. On Vercel your app *is* at the domain
root, so that resolves. On GitHub Pages your app lives under `/cookbake/`, so the
browser dutifully requests `/assets/index-abc.js` from the domain root, where
nothing exists, and the page renders blank. Setting `base: '/cookbake/'` makes
Vite write `/cookbake/assets/index-abc.js` instead, which resolves under Pages.
Because that prefix is baked in **at build time**, it must be decided when the
build runs — which is exactly why the workflow sets `VITE_BASE` as an env var on
the build step, and why `vite.config.js` reads it. One source of truth, two
correct outputs: unset → `/` for Vercel and local dev, `/cookbake/` → correct for
Pages.

## ✅ Check your work

- [ ] `.github/workflows/deploy.yml` exists and is valid YAML.
- [ ] `vite.config.js` sets `base: process.env.VITE_BASE ?? '/'`.
- [ ] Repo **Settings → Pages → Source** is set to **GitHub Actions**.
- [ ] Pushing to `main` starts a run in the **Actions** tab; both jobs go green.
- [ ] The live site at `https://<user>.github.io/cookbake/` loads correctly —
      no blank page, no 404s for the JS/CSS in the browser console.
- [ ] `npm run dev` still works locally (base falls back to `/`).
- [ ] The action versions match the current majors listed in **Read what the AI wrote**.

## 🛠 Your turn

1. Add a build step that copies `dist/index.html` to `dist/404.html` so Pages is
   ready for deep links before Topic 6 adds routing. (Hint: a `run: cp
   dist/index.html dist/404.html` step after the build.) Push and confirm the
   workflow still goes green.
2. Break the base path on purpose: set `VITE_BASE` to `/wrong/` in the workflow,
   push, and open the deployed site. Read the browser console to see the 404s for
   the JS bundle, then fix it back. Seeing the failure mode makes the concept
   stick.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| Deployed page is blank; console shows 404 for the JS/CSS bundle | `base` is `/` but Pages serves under `/<repo>/`. | Set `VITE_BASE=/<repo>/` (leading **and** trailing slash) on the build step; confirm `vite.config.js` reads it. |
| Workflow never runs after push | YAML indentation error, or the file is not under `.github/workflows/`. | Validate the YAML; check the exact path and `.yml` extension. |
| `deploy-pages` fails with an OIDC / token error | Missing `id-token: write` permission. | Add all three permissions exactly as shown. |
| Run fails: "Pages site not configured" / environment error | Pages source is still "Deploy from a branch". | Settings → Pages → Source → **GitHub Actions**. |
| `npm ci` fails: "lock file and package.json are out of sync" | `package-lock.json` is stale or was not committed. | Run `npm install` locally to refresh the lock file, commit it, push. |
| A stale action version warning or failure | AI or an old tutorial emitted e.g. `deploy-pages@v2`. | Bump to the current majors listed above (`@v4`/`@v5`). |
| Refresh on a sub-route 404s (after Topic 6) | Pages has no rewrite; deep links map to missing files. | Use the `404.html` copy trick or `HashRouter` (Step 5). |
| `/api/*` calls fail on the Pages site (Topic 5+) | Pages is a static host and cannot run the serverless functions. | Deploy the full-stack app to Vercel (Topic 6); Pages only serves the static build. |

---
### ✅ Cook & Bake Academy after this lab
A GitHub Actions workflow builds Cook & Bake Academy and publishes it to GitHub Pages on every push.
