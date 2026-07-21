# Lab 2.1 — Git and GitHub

> **Topic 2** · ~35 min · Builds on Lab 1.x (your finished Cook & Bake Academy landing page)

### 📖 The build so far
By the end of the last lab, Cook & Bake Academy was a complete landing page living only on your laptop. **In this lab you add:** version control — you initialise Git, make your first commits and push the project to a GitHub repository. By the end you'll have Cook & Bake Academy safely versioned and hosted on GitHub.

## What you will build

You will put your `cookbake` project under version control with Git, write a
`.gitignore` that keeps dependencies, build output, and secrets out of history,
make your first commit, and push the whole project up to a new GitHub repository.
By the end you will have a URL you can share and a safety net that makes the rest
of this course — including letting an AI agent rewrite your code — safe to do.

## Concepts you will meet

| Concept | In one line |
|---|---|
| Repository (repo) | The folder Git watches, plus the full history of every change. |
| Commit | A saved snapshot of your tracked files, with a message describing why. |
| `.gitignore` | A list of paths Git must never track — deps, build output, secrets. |
| Remote (`origin`) | A copy of your repo hosted elsewhere; here, on GitHub. |
| `git push` | Upload your local commits to the remote. |
| `git diff` / `git restore` | See what changed / throw away uncommitted changes — your undo button. |

## Before you start

You need the finished project from Topic 1 in `cookbake/`. Open a terminal
**inside that folder** — every command below runs from there:

```bash
cd cookbake
```

Check you have the tools:

```bash
git --version      # any 2.x is fine
node --version     # v22.x
gh --version       # GitHub CLI — optional but recommended; see Step 5
```

If `git` is missing, install it from <https://git-scm.com>. If `gh` is missing,
install it from <https://cli.github.com> (or use the web-UI path in Step 5b).

> This is a config lab: there is no application code to write. You will create
> one file — `.gitignore` — and run a handful of Git commands.

---

## Step 1 — Turn the folder into a Git repository

```bash
git init
```

This creates a hidden `.git/` sub-folder. That folder *is* your repository: it
holds every snapshot you will ever take. Deleting `.git/` deletes the history;
your working files are untouched. Nothing has been saved yet — `git init` only
sets up the machinery.

Newer versions of Git already name the first branch `main`. Confirm it:

```bash
git branch -M main
```

`main` is the branch GitHub, Vercel, and GitHub Actions all expect by default.
Setting it now avoids friction in Labs 2.2 and 2.3.

## Step 2 — See what Git wants to track

```bash
git status
```

Git lists everything in the folder as **untracked**, including `node_modules/`
(thousands of files) and possibly a `.env.local` if you created one. You do
**not** want those in your history. That is what `.gitignore` is for.

## Step 3 — Write `.gitignore`

Create a file named `.gitignore` in the root of `cookbake/`. Copy the version
in this lab folder (`labs/topic-2-deploy-to-cloud/lab-2.1-git-and-github/.gitignore`):

```bash
cp ../labs/topic-2-deploy-to-cloud/lab-2.1-git-and-github/.gitignore .gitignore
```

> Adjust the `../` if your `labs/` folder sits somewhere else relative to
> `cookbake/`. The Vite scaffold already ships a `.gitignore`; this one is the
> same idea with clearer comments — overwrite it.

The four categories that matter most, and **why each is excluded**:

| Ignored | Why it must never be committed |
|---|---|
| `node_modules` | Reinstallable from `package.json` + `package-lock.json`. It is hundreds of MB of machine-specific files. Committing it bloats the repo and causes endless merge conflicts. |
| `dist` (and `dist-ssr`) | Build **output**. It is generated from your source by `npm run build`. Committing generated files means they drift out of sync with the source they came from. The cloud rebuilds it fresh (Lab 2.2). |
| `.env` / `.env.local` / `.env.*.local` / `*.local` | **Secrets.** From Topic 5, your Neon connection string (`DATABASE_URL`) and your token signing key (`JWT_SECRET`) live here. A secret pushed to a public repo is a secret that has been leaked — bots scrape GitHub for exactly this within minutes. Once a secret is in history, deleting the file later does **not** remove it from past commits. |
| `.vercel` | The local link Vercel writes when you run `vercel link` / `vercel dev` (Topic 5). Machine-specific project metadata; nobody else needs it. |

Now re-run `git status`. `node_modules/` and any `.env.local` should be gone
from the list. If they are still there, you edited the wrong file or added a typo.

## Step 4 — Make your first commit

```bash
git add .
git commit -m "Initial commit: Cook & Bake Academy landing page"
```

`git add .` **stages** every tracked, non-ignored file — marks it for the next
snapshot. `git commit` writes the snapshot with a message. That message is
permanent and public; treat it as a note to your future self.

### Commit message hygiene

A good message says **why**, in the imperative mood ("Add", "Fix", "Refactor"),
as if completing the sentence *"This commit will…"*.

```
Good:  Add Bakery/Cooking category filter to the course grid
Good:  Fix S$ price formatting on the course card
Bad:   stuff
Bad:   asdasd
Bad:   fixed it finally!!!
```

Keep the first line under ~50 characters. If a change needs more explanation,
leave a blank line and add a paragraph below. Small, focused commits with clear
messages are what make `git log` and `git diff` useful later — including in the
vibe-coding workflow you are about to learn.

## Step 5 — Create the GitHub repo and push

### 5a — With the GitHub CLI (recommended)

```bash
gh auth login          # one time, if you have not already
gh repo create cookbake --public --source=. --remote=origin --push
```

That one command creates the repo on GitHub, wires it up as your `origin`
remote, and pushes `main` — all at once. Skip to **Step 6**.

### 5b — With the GitHub website (no CLI)

1. Go to <https://github.com/new>.
2. Repository name: `cookbake`. Visibility: **Public**. Do **not** tick
   "Add a README", ".gitignore", or "license" — your local repo already has
   files, and pre-filling would cause a conflict on the first push.
3. Click **Create repository**. GitHub shows you an "…or push an existing
   repository" snippet. It is the two commands below — run them in `cookbake/`:

```bash
git remote add origin https://github.com/<your-username>/cookbake.git
git push -u origin main
```

`git remote add origin …` records where "the cloud copy" lives. `git push -u
origin main` uploads your commits and the `-u` sets `origin/main` as the default
upstream, so future pushes are just `git push`.

## Step 6 — Confirm it landed

Refresh your repo page on GitHub. You should see `src/`, `package.json`,
`index.html`, and your `.gitignore` — **but no `node_modules/` and no
`.env.local`**. That absence is the whole point of Step 3.

---

## 🎤 Vibe prompt

Even a `.gitignore` is a great small task to hand to an AI agent — it knows the
standard patterns for every framework. Use this in Claude Code / Cursor:

```text
I have a Vite + React project called cookbake (plain JavaScript, no TypeScript).
It will later be deployed on Vercel and will have serverless functions in api/
that read server-side secrets — DATABASE_URL (a Neon Postgres connection string)
and JWT_SECRET — from a .env.local file. Generate a .gitignore for it. It MUST
ignore node_modules, the dist build output, every local env file (.env,
.env.local, .env.*.local, *.local), the .vercel folder, and the usual log and
.DS_Store noise. Add a short comment above each group explaining why it is
ignored. Do NOT ignore package-lock.json — that file must be committed.
```

Then compare the agent's output to the `.gitignore` in this lab. This is the
vibe-coding loop in miniature: **prompt → generate → read → correct**.

## 🔍 Verify

You did not write application code here, but you did change what your project
tracks. Audit it before you trust it:

- **Nothing secret got committed.** Run `git ls-files | grep -i env` — it should
  return nothing, or only `.env.example` (a template with placeholder values,
  which is safe to commit). If `.env.local` shows up, it is now in history; you
  must remove it *and* rotate any real credentials it held.
- **`node_modules` is not tracked.** `git ls-files | grep node_modules` must be
  empty. If it is not, your `.gitignore` was added *after* you staged — run
  `git rm -r --cached node_modules` then commit.
- **The lock file IS tracked.** `git ls-files | grep package-lock.json` should
  return one line. It pins exact dependency versions so the cloud build matches
  your machine. AI-generated `.gitignore` files sometimes ignore it by mistake —
  a classic error; do not let it.
- **`.vercel` is ignored.** It does not exist yet, but the rule must already be
  there so it never sneaks in when you run `vercel dev` in Topic 5.
- **The remote is set.** `git remote -v` shows `origin` pointing at your GitHub
  URL for both `fetch` and `push`.

## 🧠 Why it works

Git is a **content tracker with history**. Every `commit` is a full, immutable
snapshot of the files you have staged, identified by a hash. Because each
snapshot is complete and permanent, Git gives you two superpowers: you can see
*exactly* what changed between any two points (`git diff`), and you can return to
*any* earlier state (`git restore`, `git checkout`). Your project stops being a
single fragile "current version" and becomes a timeline you can move along.

The reason `.gitignore` matters so much is that Git tracks *content* faithfully —
including content you never wanted tracked. Three kinds of files are actively
harmful in history. **Dependencies** (`node_modules`) are derived from your lock
file, so tracking them is redundant and enormous. **Build output** (`dist`) is
derived from your source, so tracking it means two copies of the same truth that
inevitably disagree. **Secrets** (`.env.local`) are the dangerous one: Git's
permanence works against you. Deleting a leaked key file in a later commit leaves
the key sitting in every earlier commit, still readable by anyone who clones the
repo. **A leaked credential in git history is permanent.** The only real fix after
a leak is to rewrite history *and* rotate the credential at the provider — reset
the Neon database password, mint a new `JWT_SECRET`. Far easier to never commit it,
which is exactly what the ignore rule guarantees. The rule of thumb: **Git tracks
what you author, never what a tool generates or what must stay private.**

`origin` on GitHub adds the second half of the value: a durable off-machine copy
and a place other services can read from. In Lab 2.2, Vercel will *watch* this
repo and rebuild your site every time you push. In Lab 2.3, GitHub Actions will
do the same. Version control is not just backup — it is the interface every
deployment tool in this course plugs into.

### The vibe-coding safety net

Here is why this lab comes *before* every lab where you let an AI agent touch
your code. AI agents are fast and confident, and sometimes confidently wrong —
they will happily rewrite a working `CourseCard` into a broken one. Git is what
makes that risk affordable:

1. **Commit before you prompt.** Get to a known-good, committed state first.
2. **Let the agent make its changes.** Prompt away.
3. **Read the diff, do not just read the result.** `git diff` shows you *every*
   line the agent changed — including the ones it did not mention. This is how
   you catch the subtle regression it slipped in three files over: it "fixed" the
   price format and quietly dropped the campus name from every card.
4. **Keep the good, drop the bad.** Happy with everything? Commit it. Something
   broke? `git restore <file>` throws away the change to that file and snaps it
   back to your last commit — instantly, with no memory of what the agent did.

Without version control, "let the AI refactor it" is a gamble with your only
copy. With it, every AI edit is a proposal you review and can reject in one
command. That is what makes vibe coding *safe* rather than reckless, and it is
the single most important habit in this course.

## ✅ Check your work

- [ ] `git status` reports a clean tree ("nothing to commit, working tree clean").
- [ ] `git log --oneline` shows your initial commit.
- [ ] `git ls-files` lists your source but **not** `node_modules` or `.env.local`.
- [ ] `git ls-files | grep package-lock.json` returns exactly one line.
- [ ] Your `cookbake` repo is visible on github.com and shows the same files.
- [ ] `git remote -v` shows `origin` pointing at your GitHub URL.

## 🛠 Your turn

1. Make a tiny visible change to `src/App.jsx` (change the hero headline from
   "Master the art of cooking & baking" to anything else). Run `git diff` to see
   exactly what you changed, then `git restore src/App.jsx` to throw the change
   away. Confirm the headline is back. You just used the vibe-coding undo button
   on your own edit.
2. Add a real `README.md` to the project root describing Cook & Bake Academy in
   two sentences, then commit it with a clean message. Push, and watch it render
   on the GitHub repo home page.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `fatal: not a git repository` | You ran a `git` command outside a repo. | `cd` into `cookbake/`; make sure you ran `git init` there. |
| `node_modules` shows up on GitHub | You committed before adding `.gitignore`. | `git rm -r --cached node_modules`, commit, push. The ignore rule only affects *future* staging. |
| `.env.local` appears on GitHub | Same timing problem — secrets got committed. | `git rm --cached .env.local`, commit — **then rotate the leaked credentials**: reset the database password in the Neon Console and generate a new `JWT_SECRET`. Deleting the file does not scrub old commits. |
| `remote origin already exists` | You ran `git remote add origin …` twice. | `git remote set-url origin <url>` to update it instead. |
| `Updates were rejected … fetch first` | You ticked "Add a README" when creating the GitHub repo, so the remote has a commit yours does not. | `git pull --rebase origin main`, resolve if needed, then `git push`. Next time, create the repo empty. |
| `Authentication failed` on push (HTTPS) | GitHub no longer accepts account passwords over HTTPS. | Use `gh auth login`, or create a Personal Access Token and use it as the password. |

---
### ✅ Cook & Bake Academy after this lab
Cook & Bake Academy is tracked in Git and pushed to a GitHub repository with a clean commit history.
