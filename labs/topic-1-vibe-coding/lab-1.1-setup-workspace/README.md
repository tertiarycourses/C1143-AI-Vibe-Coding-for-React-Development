# Lab 1.1 — Set Up Your Vibe-Coding Workspace

> **Topic 1** · ~40 min · Builds on nothing (this is the very first lab)

### 📖 The build so far
Nothing exists yet — this is the very first lab, so Cook & Bake Academy starts as just an idea. **In this lab you add:** the toolchain (Node 22, VS Code, an AI coding agent) and a freshly scaffolded Vite + React project. By the end you'll have a running dev server showing your first Cook & Bake heading at `http://localhost:5173`.

## What you will build

A working React development environment and a freshly scaffolded Vite + React
app called **Cook & Bake Academy** — the cooking & bakery course catalogue you
will grow across all six topics of this course. By the end you will have Node 22,
VS Code and an AI coding agent installed, the app running live at
`http://localhost:5173`, and a clear mental model of what every generated file does.

## Concepts you will meet

| Concept | In one line |
|---|---|
| Node.js + npm | The JavaScript runtime and package manager that run your tools and install libraries. |
| Vite | The build tool that serves your app instantly in dev and bundles it for production. |
| Scaffolding | Generating a ready-to-run project skeleton with one command. |
| Vibe coding | Building software by **prompting** an AI agent, then **reading, understanding and correcting** what it writes. |
| The entry point | How `index.html` → `main.jsx` → `App.jsx` hand off to put React on the page. |
| Dev server (HMR) | `npm run dev` serves the app and hot-reloads it the instant you save. |

## Before you start

You need a computer where you can install software and use a terminal. This
course assumes you already know modern JavaScript (arrow functions, destructuring,
`map`/`filter`, template literals, `async`/`await`) — every minute here goes to
React, not JS basics. This lab creates the project from scratch, so there is no
previous lab's code to copy.

---

## Step 1 — Install Node 22

React tooling runs on **Node.js**. This course targets **Node 22 LTS**.

1. Download the **LTS** installer from <https://nodejs.org> (or use a version
   manager like `nvm` / `fnm` if you have one).
2. Verify it in a terminal:

```bash
node -v   # should print v22.x.x
npm -v    # should print 10.x or newer
```

`npm` (Node Package Manager) ships with Node. It installs libraries and runs the
scripts defined in `package.json`.

> If `node -v` shows an older major version (18, 20…), upgrade before continuing.
> Vite 8 and React 19 assume a modern Node.

## Step 2 — Install VS Code

Download **Visual Studio Code** from <https://code.visualstudio.com>. It is the
editor this course assumes. After installing, add two extensions from the
Extensions panel (the square icon in the sidebar):

- **ESLint** — surfaces mistakes as you type.
- **Prettier** — formats your code on save so you never argue about spacing.

Open VS Code's built-in terminal with **View → Terminal** (or `` Ctrl+` ``). You
will run every command in this course from there.

## Step 3 — Install an AI coding agent

This is a **vibe-coding** course, so you need an AI agent that can read and write
files in your project. We use **Claude Code** (Anthropic's official CLI) as the
primary agent throughout.

```bash
npm install -g @anthropic-ai/claude-code
claude          # first run walks you through signing in
```

Run `claude` from inside your project folder and it can see and edit your files.

**Alternatives** (any one of these works for the labs — the prompts are the same):

- **Cursor** — a VS Code fork with an AI chat + inline edit built in (<https://cursor.com>).
- **GitHub Copilot** — an extension that adds inline suggestions and a chat panel to VS Code.

Whichever you pick, the workflow in this course is identical: you write a prompt,
the agent writes code, and **you read and verify it**.

## Step 4 — Scaffold the Cook & Bake app

`cd` into the folder where you keep projects, then let Vite generate the skeleton:

```bash
npm create vite@latest cookbake -- --template react
```

`npm create vite@latest` downloads and runs Vite's project generator. `cookbake`
is the folder name. Everything after `--` is passed to the generator:
`--template react` selects the plain-JavaScript React template (no TypeScript).

Then install dependencies and start the dev server:

```bash
cd cookbake
npm install       # reads package.json, downloads React + Vite into node_modules/
npm run dev       # starts Vite's dev server
```

Vite prints a local URL — open <http://localhost:5173> in your browser. You should
see the spinning Vite + React starter page.

## Step 5 — Understand what Vite generated

Open the `cookbake` folder in VS Code. Here is what each file does — read this
before you touch anything:

| File | What it is |
|---|---|
| `index.html` | The **only** HTML page. It contains `<div id="root"></div>` — the empty box React fills — and a `<script type="module" src="/src/main.jsx">` that boots the app. |
| `src/main.jsx` | The **entry point**. It finds `#root` and tells React to render your `<App/>` into it. You rarely edit this. |
| `src/App.jsx` | Your **root component** — the top of the component tree. This is where your app actually starts. You will edit this constantly. |
| `src/index.css` | Global styles. In this course it already holds the Cook & Bake design tokens (`.card`, `.hero`, `.grid`, `.btn`…) — do not overwrite it. |
| `vite.config.js` | Vite's configuration. It enables the React plugin (JSX + fast refresh). You will barely touch it. |
| `package.json` | Lists your dependencies and the `scripts` you can run (`dev`, `build`, `preview`). |
| `node_modules/` | The actual downloaded library code. Never edit it; never commit it. |
| `public/` | Static files served as-is (e.g. `favicon.svg`). |

## Step 6 — Make it yours (optional smoke test)

Replace the contents of `src/App.jsx` with the minimal component in this lab's
`src/App.jsx`:

```jsx
export default function App() {
  return <h1>🍞 Cook &amp; Bake Academy is live 🎉</h1>
}
```

Save. Because the dev server does **Hot Module Replacement (HMR)**, the browser
updates instantly — no refresh. Seeing your heading appear confirms the whole
chain (`index.html` → `main.jsx` → `App.jsx`) is wired correctly.

---

## 🎤 Vibe prompt

You can even let your AI agent scaffold and explain the project. Open your agent
in an empty folder and paste:

```text
I'm starting a React course. In this folder, scaffold a new Vite + React
(JavaScript, not TypeScript) app named "cookbake" using
`npm create vite@latest`. Then install dependencies and start the dev server.
After that, explain in plain English what each of these files does and how they
connect: index.html, src/main.jsx, src/App.jsx, vite.config.js, package.json.
Do not add any libraries beyond what the template includes.
```

Then read the agent's explanation against Step 5 above. If it says something you
don't understand, ask it to go deeper — that back-and-forth *is* vibe coding.

## 🔍 Verify

This lab generates configuration, not app logic, so instead of auditing code you
verify the environment:

- Run `node -v` — it prints `v22.x.x`, not an older major version.
- `npm run dev` starts without errors and prints a `localhost:5173` URL.
- The browser shows the starter page (or your heading after Step 6).
- `src/main.jsx` imports `App` from `./App.jsx` and calls
  `createRoot(document.getElementById('root')).render(...)`.
- `index.html` contains exactly one `<div id="root">` and one `<script src="/src/main.jsx">`.
- Editing `App.jsx` and saving updates the browser **without a manual refresh**.

## 🧠 Why it works

**What is "vibe coding"?** It is building software by describing what you want to
an AI agent and letting it write the code — but it is *not* "type a prompt and
walk away". The skill this course teaches is a loop:

> **Prompt → Generate → Read → Understand → Correct.**

You *prompt* the agent, it *generates* code, you *read* every line, you make sure
you *understand* what it does and why, and where it is wrong or unclear you
*correct* it (by editing, or by prompting again). The AI is fast but not
trustworthy; you stay the engineer. Every lab in this course walks that loop
explicitly, and the `🔍 Read what the AI wrote` sections train the "Read" and
"Understand" steps — the ones beginners skip and later regret.

**How does React actually get onto the page?** A React app has a single HTML
file. Open `index.html` and the important line is:

```html
<div id="root"></div>
```

That `<div>` is empty. React does not write HTML files; it fills this one box at
runtime. The next line, `<script type="module" src="/src/main.jsx">`, tells the
browser to run your JavaScript entry point. Inside `main.jsx`:

```jsx
import { createRoot } from 'react-dom/client'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(<App />)
```

`document.getElementById('root')` grabs that empty `<div>`. `createRoot(...)`
hands it to React, and `.render(<App />)` tells React to build the output of your
`App` component and put it inside. So the chain is:
**`index.html` provides the box → `main.jsx` finds the box and starts React →
`App.jsx` is the content React renders into it.** Every component you write from
now on lives somewhere inside that `<App />` tree.

**Why Vite?** In development, Vite serves your files directly to the browser and
swaps changed modules in place (HMR) so saves feel instant. For production,
`npm run build` bundles and minifies everything into a `dist/` folder of plain
static files. You get a fast feedback loop now and an optimised app later, with
no configuration from you.

## ✅ Check your work

- [ ] `node -v` prints `v22.x.x`.
- [ ] VS Code is installed with the ESLint and Prettier extensions.
- [ ] An AI coding agent (Claude Code, Cursor, or Copilot) is installed and signed in.
- [ ] `npm create vite@latest cookbake -- --template react` created a `cookbake/` folder.
- [ ] `npm install` completed and `npm run dev` serves the app at `localhost:5173`.
- [ ] You can name what `index.html`, `main.jsx`, `App.jsx`, `vite.config.js` and `package.json` each do.
- [ ] Editing `App.jsx` and saving updates the browser with no manual refresh.

## 🛠 Your turn

1. In `package.json`, find the `scripts` block. Run `npm run build`, then
   `npm run preview`. What is the difference between `dev` and `preview`, and what
   new folder appeared? (Hint: look for `dist/`.)
2. Ask your AI agent: *"What would break if I deleted the `<div id="root">` from
   index.html?"* Predict the answer first, then try it (and put it back).

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `node: command not found` | Node isn't installed or the terminal was opened before install. | Install Node 22, then open a **new** terminal. |
| `npm error could not determine executable to run` | Typo in the create command or a very old npm. | Use exactly `npm create vite@latest cookbake -- --template react`; upgrade npm with `npm install -g npm`. |
| Blank white page, console says `Target container is not a DOM element` | `#root` is missing or renamed in `index.html`. | Restore `<div id="root"></div>`; the id must match `getElementById('root')` in `main.jsx`. |
| `Port 5173 is in use` | Another dev server is already running. | Stop the other server, or let Vite pick the next free port (it offers one). |
| Changes don't show in the browser | The dev server isn't running, or you edited a file outside `src/`. | Confirm `npm run dev` is still running in the terminal; edit files under `src/`. |

---
### ✅ Cook & Bake Academy after this lab
A Vite + React project called cookbake runs live at `localhost:5173` and hot-reloads every edit.
