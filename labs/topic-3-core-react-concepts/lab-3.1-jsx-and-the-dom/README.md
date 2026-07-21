# Lab 3.1 — JSX, the Real DOM and the Virtual DOM

> **Topic 3** · ~40 min · Builds on Topic 2 (the deployed landing page)

### 📖 The build so far
By the end of the last lab, Cook & Bake Academy was a deployed landing page you built by prompting — but the course cards were still hand-typed markup. **In this lab you add:** the understanding beneath the whole app — what the *real DOM* is and how you would update it without React, how React's *Virtual DOM* diffs and patches only what changed, and how *Babel* turns your JSX into plain JavaScript before the browser ever sees it. You explore all three with a small live demo, `DomVsReact`. By the end you'll have a solid mental model of how your JSX becomes the page you see — the model the next three labs (real components, `.map()`, the filter) all rest on.

## What you will build

A single teaching component, `DomVsReact`, with two side-by-side panels that both
count loaves out of the oven. The left panel increments the number the old-fashioned
way — by reaching into the live page and overwriting a DOM node by hand
(`document.getElementById(...).textContent = ...`). The right panel does the same
thing with React state. Same feature, two completely different philosophies. You will
render it on its own so you can study one idea without the rest of the app in the way —
and then you will look at the *compiled* output of your own JSX and see the Virtual DOM
object with your own eyes.

## Concepts you will meet

| Concept | In one line |
|---|---|
| The real DOM | The browser's live object tree of the page — what you see **is** the DOM |
| Imperative DOM updates | `getElementById(...).textContent`/`innerHTML` — you patch nodes by hand |
| The Virtual DOM | A lightweight plain-JS object tree describing the UI you want right now |
| Reconciliation | React diffs the new tree against the old and patches only the difference |
| Babel | The compiler (run for you by `@vitejs/plugin-react`) that turns JSX into JS |
| `React.createElement` / `jsx()` | What a JSX tag actually compiles to — a function call returning an object |
| `className` | JSX uses `className`, not `class` (because `class` is a reserved word in JS) |
| One root element | A component returns one value, so its JSX has one root (or a Fragment `<>…</>`) |
| `{expression}` | Curly braces embed a JS *expression* (a value), not a statement |
| XSS escaping | JSX escapes interpolated text automatically; `innerHTML` is the classic hole |

## Before you start

You need the working `cookbake` app from Topic 2 (Vite + React 19). From the repo root:

```bash
cd cookbake
npm install   # if you have not already
```

Copy this lab's snapshot over your app's `src/`:

```bash
cp -R labs/topic-3-core-react-concepts/lab-3.1-jsx-and-the-dom/src/. cookbake/src/
```

That drops in a temporary `src/App.jsx` (it renders only `DomVsReact`) and the new
`src/components/DomVsReact.jsx`. Then run `npm run dev` and open the local URL
(`http://localhost:5173`).

> The next lab rebuilds `App.jsx` into the real landing page. This throwaway `App.jsx`
> just lets you look at one component in isolation.

---

## Step 1 — Render one component in isolation

Open `src/App.jsx`. It is deliberately tiny:

```jsx
import DomVsReact from './components/DomVsReact'

export default function App() {
  return (
    <main className="section">
      <DomVsReact />
    </main>
  )
}
```

Notice `<DomVsReact />` — you use your own component with the same angle-bracket syntax
as a built-in tag. That is the whole mental model of React: your UI is a tree of
components, and components are just functions that return description-of-UI (JSX).

## Step 2 — Meet the real DOM, and update it by hand

Run the app. Click **+1 by hand** and **+1 with state**. Both numbers go up. From the
user's point of view they are identical. The difference is entirely in *how the code
gets there*.

Open DevTools (F12) → **Elements**. What you are looking at is the **DOM** — the
Document Object Model, the browser's live tree of objects, one per element on the page.
The page you see *is* a rendering of this tree; there is no separate "the page." When
anything on screen changes, it is because a node in this tree changed.

Now read the imperative panel's handler in `DomVsReact.jsx`:

```jsx
function bake() {
  const node = document.getElementById('loaf-count')
  node.textContent = String(Number(node.textContent) + 1)
}
```

This is how you update a page **without React**. You (1) find a specific node by its
`id`, (2) read the current number back *out of the DOM text*, (3) add one, and (4) write
it back in. There is no `count` variable holding the truth anywhere in your JavaScript —
**the DOM node itself is the storage**. You are giving the browser step-by-step
instructions: *how* to update.

That works for one number. It stops scaling almost immediately, and the panel's comment
names the traps:

- **The DOM becomes your database.** The current value lives in a text string on a node,
  not in your code, so every reader has to go dig it back out.
- **Every handler must know the exact node id.** Rename `loaf-count` and the feature
  breaks silently — no error, it just stops counting.
- **Two handlers fight over one node.** Add a second button that also writes
  `#loaf-count` and now two pieces of code both "own" that text; keeping them in agreement
  is manual and fragile.
- **`innerHTML` is the classic XSS hole.** The shortcut `node.innerHTML = someText`
  *parses that string as HTML*, so any user-supplied text can smuggle in a live
  `<img onerror=…>` or `<script>`. `textContent` (which the demo uses) always writes
  plain text and is safe.

## Step 3 — Meet the Virtual DOM, and watch React patch one node

Read the React panel:

```jsx
const [count, setCount] = useState(0)
// ...
<button onClick={() => setCount(count + 1)}>+1 with state</button>
// ...
Loaves baked: <span>{count}</span>
```

No `getElementById`, no `.textContent`, no `id` at all. You change a value (`count`) and
describe what the UI should look like for that value (`{count}`). React does the DOM
surgery for you.

Make React's cleverness **visible**:

1. Keep DevTools → **Elements** open and find the React panel's
   `Loaves baked: <span>0</span>`.
2. Click **+1 with state**. Chrome briefly **highlights** the node it just changed —
   watch closely and you will see *only the one text node* (the `0` → `1`) flash. The
   surrounding `<article>`, the heading, the button, the caption: none of them flash,
   because React did not touch them.
3. Now click **+1 by hand** on the left and watch the left panel — same single-node
   flash, except *you* wrote that DOM update by hand.

The difference is who computes that minimal update. On the left, you did. On the right,
React did — and that is the payoff of the Virtual DOM (the "Why it works" section
explains exactly how).

## Step 4 — See your JSX after Babel compiles it

The browser has **never seen JSX**. `<span>{count}</span>` is not valid JavaScript and
no browser can run it. Something has to translate it first, and that something is
**Babel** — run automatically for you by `@vitejs/plugin-react`. Let's look at what it
produces. Two routes, both concrete:

**Route A — the Babel REPL (fastest).** Open <https://babeljs.io/repl>, tick the
**React** preset in the left sidebar, and paste this JSX:

```jsx
function LoafCount({ count }) {
  return <span className="card__price">{count}</span>
}
```

Read the output on the right. Your `<span>` is gone. In its place is a function call —
something close to:

```js
import { jsx as _jsx } from "react/jsx-runtime";
function LoafCount({ count }) {
  return _jsx("span", { className: "card__price", children: count });
}
```

**Route B — the module Vite actually serves.** With `npm run dev` running, open a new
browser tab at:

```
http://localhost:5173/src/components/DomVsReact.jsx
```

Vite serves the **transformed** JavaScript, not your source file. Scroll through it: the
JSX has vanished, replaced by `jsxDEV(...)` calls importing from `react/jsx-dev-runtime`
(the dev build adds line/column info for better error messages; `_jsx` is the production
build). This is the exact code your browser runs. Your `.jsx` source is a convenience for
*you*; the browser only ever sees this.

*(CLI option, if you prefer a terminal: `npx babel --presets @babel/preset-react
src/components/DomVsReact.jsx` prints the same transformed output to stdout.)*

Look at the shape of what the call returns — a plain JavaScript object roughly like:

```js
{ type: 'span', props: { className: 'card__price', children: 1 }, /* … */ }
```

**That object tree is the Virtual DOM.** Hold onto that fact — the next section connects
it to everything.

---

## 🎤 Vibe prompt

```text
In my Vite + React 19 app (Cook & Bake Academy), create src/components/DomVsReact.jsx as
a default-exported function component that teaches the difference between the real DOM and
React's virtual DOM. Render two side-by-side panels using the existing CSS classes
(.section, .section__head, .eyebrow, .grid, .panel, .badge, .muted, .btn):

1. An "imperative / real DOM" panel with <span id="loaf-count">0</span> and a button whose
   onClick reads that node's textContent, adds 1, and writes it back — no React state.
2. A "declarative / Virtual DOM" panel that uses useState(0) and a button that calls
   setCount, showing the value with {count}.

Both count "Loaves baked". Add short captions explaining that the left panel says HOW to
update the DOM (find the node, rewrite its text) while the right panel says WHAT the UI
should be. Also give me a temporary src/App.jsx that renders only <DomVsReact />. No
TypeScript, 2-space indent, single quotes, no semicolons.
```

## 🔍 Read what the AI wrote

- **Did it reach for `innerHTML`?** The most common AI shortcut for the imperative panel
  is `node.innerHTML = ...`. Prefer `textContent`: `innerHTML` parses its input as HTML
  and is the classic cross-site-scripting (XSS) hole. Flag it every time.
- **Did it write `className`, not `class`?** In JSX the attribute is `className`. If the
  agent emitted `class="panel"`, React 19 warns in the console and may drop it. Search the
  file for ` class=` and fix any it left behind.
- **Is there exactly one root element per return?** Each component returns one value, so
  its JSX must have one root. This file uses a Fragment `<>…</>` for `DomVsReact` and a
  `<main>` inside `App`. If an agent returns two sibling elements with no wrapper, it must
  use a Fragment or the file will not compile.
- **Did it put a statement inside `{}`?** `{}` in JSX accepts an *expression* (something
  that has a value), not a statement. `{if (x) …}` is invalid; the ternary `{x ? a : b}`
  is the expression form. Check the captions.
- **Is `useState` imported from `react`?** It should be `import { useState } from 'react'`
  — no default `React` import is needed under React 19's automatic JSX transform.

## 🧠 Why it works

**Start with the real DOM.** When the browser loads your page it parses the HTML into a
tree of objects — the **DOM** (Document Object Model). Every element is a node; the page
you see is just the browser painting that tree. Change a node and the screen changes.
Without React, updating the UI *means* writing DOM code by hand, exactly like the left
panel: `document.getElementById('loaf-count')` to find a node, `.textContent = …` to
overwrite it. This is **imperative** — you spell out *how* to mutate the page, step by
step. It works, but the state of your app ends up scattered across DOM nodes: the current
loaf count lives in a text string, every handler has to know the right `id`, two handlers
editing one node drift out of sync, and `innerHTML` quietly opens an XSS hole. In a page
with dozens of interdependent values, keeping every node correct by hand is where bugs
breed.

**JSX is not HTML — it is JavaScript in disguise, and Babel does the translating.** The
browser cannot run `<span>{count}</span>`; it is not valid JS. So before your code ever
reaches the browser, **Babel** (bundled into `@vitejs/plugin-react`) compiles every JSX
tag into a plain function call. You saw this in Step 4:

```js
jsx('span', { className: 'card__price', children: count })
```

That call does not touch the page. It **returns an ordinary JavaScript object** —
something like `{ type: 'span', props: { className: 'card__price', children: 1 } }`. Your
whole component, when called, returns a *tree* of these objects. **That tree is the
Virtual DOM**: a lightweight, in-memory description of what you want the screen to look
like right now. It is cheap because it is just objects, not real DOM nodes.

One naming note so the docs and every AI agent make sense. Under React 19's **automatic
JSX transform**, Babel emits `jsx(...)` and `jsxs(...)` (the `s` variant is for an element
with multiple children) imported from `react/jsx-runtime`. You will also constantly see
the older form **`React.createElement('span', { className: 'card__price' }, count)`** in
documentation, Stack Overflow answers, and AI output — that is the *classic* transform,
and it means exactly the same thing and produces the same object. `jsx(...)` and
`React.createElement(...)` are two spellings of one idea: *a JSX tag is a function call
that returns a Virtual-DOM object.*

**Now the payoff — reconciliation.** When state changes (you call `setCount(1)`), React
calls your component again and gets a **new** Virtual-DOM tree. It compares (diffs) the
new tree against the previous one — this is **reconciliation** — finds the single thing
that changed (the text `0` became `1`), and issues the one minimal real-DOM operation
needed to make the browser match. That is the single node you watched flash in DevTools.
It does not rebuild the page and it does not ask you which node to touch. You described
*what* the UI should be for `count === 1`; React figured out *how*. That is the whole
difference between **declarative** (React) and **imperative** (the left panel) code — and
it removes the entire class of "I forgot a `getElementById`" and "two handlers fought over
one node" bugs, because state is the single source of truth and the DOM is re-derived from
it every render.

**The JSX rules all fall out of "JSX compiles to function calls."** You are not
memorising arbitrary syntax; each rule is a direct consequence:

- **`className`, not `class`** — the compiled call is `jsx('span', { className: … })`, and
  `class` is a reserved word in JavaScript, so the prop is named `className`. The same
  goes for **`htmlFor`** (the HTML `for`, since `for` is reserved too).
- **camelCase attributes** — `onClick`, `tabIndex`, `onChange`. They become object keys in
  the `props` argument, and that is the JS convention.
- **One root element per return** — a function returns one value, so a component returns
  one Virtual-DOM object. Genuine siblings get wrapped in a **Fragment** `<>…</>`, which
  groups them without adding a real `<div>` to the page.
- **Self-close void tags** — `<img />`, `<input />`, `<br />`. Each tag is a function call
  that has to be closed; a bare `<input>` is fine in HTML but a syntax error in JSX.
- **`{}` takes an expression, never a statement** — whatever is in the braces becomes an
  *argument value* to the `jsx()` call, so it has to *be* a value. `{count}`,
  `{fee === 0 ? 'Free' : `S$${fee}`}` and `{courses.map(...)}` all produce values;
  `{if (…)}` and `{for (…)}` are statements and cannot sit there.

And because interpolated text is passed as a *string value*, JSX **escapes it
automatically**: if `count` were the string `<img onerror=alert(1)>`, React would render
those characters as visible text, not as a live tag — the built-in XSS protection you gave
up the moment you used `innerHTML` on the left. Nesting is just nested calls
(`<article><h3>{title}</h3></article>` → `jsx('article', { children: jsx('h3', { children:
title }) })`), and a parent with several children gets a `children` **array** — which is
exactly why, once you render a *list* from an array in Lab 3.3, React needs a `key` to tell
those array entries apart across renders.

## ✅ Check your work

- [ ] Both counters increase by 1 on each click.
- [ ] The left panel uses `document.getElementById(...).textContent`; the right panel uses
      `useState` and `{count}` — no `getElementById` anywhere on the right.
- [ ] There is no ` class=` attribute in the file (only `className`).
- [ ] `App.jsx` renders `<DomVsReact />` and the page shows the two panels side by side.
- [ ] In DevTools → Elements, clicking **+1 with state** highlights only the one text node
      (it flashes), not the whole panel.
- [ ] You opened `http://localhost:5173/src/components/DomVsReact.jsx` (or the Babel REPL)
      and confirmed the JSX has become `jsx(...)` / `jsxDEV(...)` calls — no angle brackets.

## 🛠 Your turn

1. **Paste your own card into the Babel REPL.** Copy the real `<CourseCard>` markup shape
   — an `<article className="card">` with an `<h3>` and a `<span className="card__price">`
   — into <https://babeljs.io/repl> with the React preset on. Find the `jsx('article', …)`
   call and the nested `children` array. Then rewrite the same markup as raw
   `React.createElement('article', { className: 'card' }, …)` by hand and confirm you get
   the same object shape. This is the single best exercise for making JSX stop being magic.
2. **Make the imperative panel lie.** Add a second button to the *left* panel that also
   writes `#loaf-count`, then force a React re-render of the whole `DomVsReact` (e.g. add a
   `useState` toggle at the top and a button that flips it). Watch the hand-written DOM
   value survive or drift depending on when React re-renders — a whole category of bug that
   is impossible on the declarative side.
3. **Add a Reset button to each panel.** On the React side it is `setCount(0)`. On the
   imperative side you must find the node by id again. Which would you trust in a
   500-component app?

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `Adjacent JSX elements must be wrapped in an enclosing tag` | A component returned two sibling elements | Wrap them in a Fragment `<>…</>` or a single parent element |
| Console warning: `Invalid DOM property 'class'. Did you mean 'className'?` | Used HTML `class` in JSX | Rename every `class=` to `className=` |
| `Cannot read properties of null (reading 'textContent')` | `getElementById` ran before the node existed, or the id is misspelled | Make sure the `id` in the handler exactly matches the `id` on the `<span>` |
| `Unexpected token` around `{if (…)}` | Put a statement inside JSX braces | Use an expression: a ternary `{cond ? a : b}` or compute the value above the `return` |
| The React counter does not update | Read/wrote a plain variable instead of calling `setCount` | Only `setCount(...)` triggers a re-render; `count = count + 1` does nothing visible |
| Console warning: `Invalid DOM property 'for'. Did you mean 'htmlFor'?` | Used the HTML `for` attribute on a `<label>` | Rename `for` to `htmlFor` (as `class` becomes `className`) |
| Parsing error around an `<input>` or `<img>` | An empty (void) element was not self-closed | Self-close it: `<input />`, `<img />`, `<br />` |

---
### ✅ Cook & Bake Academy after this lab
A small demo makes the real DOM, the Virtual DOM and the Babel/JSX compile step visible — the foundation the real components, `.map()` and the filter all build on.
