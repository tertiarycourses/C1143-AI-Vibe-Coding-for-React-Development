# Lab 4.1 — State with `useState`

> **Topic 4** · ~45 min · Builds on Topic 3 (your componentised Cook & Bake Academy catalogue)

### 📖 The build so far
By the end of the last lab, Cook & Bake Academy had a searchable, filterable catalogue. **In this lab you add:** a shortlist — `useState` in `App` tracks which courses a visitor has shortlisted, and each card gets an Add / Remove button. By the end you'll have a working in-memory shortlist at the top of the site.

## What you will build

You will make Cook & Bake Academy *interactive* for the first time. Each course card gets
an **Add to shortlist** button; clicking it drops the course into a shortlist, and the
button flips to **Remove**. A `CartSummary` panel above the grid shows the courses
on the shortlist and the running total price in S$. Nothing is saved yet (that is
Lab 4.2) — this lab is entirely about state that lives in memory while the page is
open.

## Concepts you will meet

| Concept | In one line |
|---|---|
| Hook | A function starting with `use` that lets a component "remember" things and tap into React features. |
| `useState` | Returns `[value, setter]`; calling the setter re-renders the component with the new value. |
| Rules of Hooks | Call hooks only at the top level of a component, in the same order every render. |
| State is a snapshot | Inside one render, a state variable is a fixed value, not a live changing one. |
| Updater form | `setX(prev => …)` reads the latest state — the safe way to update from the previous value. |
| Immutable update | Replace arrays/objects with new ones (`[...]`, `filter`, `map`); never mutate in place. |
| Lifting state up | Put shared state in the closest common parent, pass it down as props. |

## Before you start

You need the finished Topic 3 app in `cookbake/`, where `App.jsx` already owns
`query` and `category` state and renders `<CourseGrid courses={visible} />`. Work
inside `cookbake/`:

```bash
cd cookbake
npm run dev
```

Copy this lab's four files over your app (from the repo root):

```bash
cp -R labs/topic-4-react-hooks/lab-4.1-usestate/src/. cookbake/src/
```

That overwrites `App.jsx`, `CourseCard.jsx`, `CourseGrid.jsx` and adds a new
`CartSummary.jsx`. Your Topic 3 `Navbar`, `Hero`, `Footer`, `SearchBar` and
`CategoryFilter` are untouched.

---

## Step 1 — Give `App` a shortlist

Open `src/App.jsx`. Alongside the existing `query` and `category` state, add a
third piece of state — an array of the course **objects** currently shortlisted:

```jsx
const [items, setItems] = useState([])
```

This is the single most important decision in the lab, and it is a *design*
decision, not a syntax one: the shortlist lives in `App`, not in `CourseCard`.
`App` is the closest component that sits above **both** the cards (which add/remove)
and the `CartSummary` (which displays). That is "lifting state up" — more on why in
**Why it works**.

## Step 2 — Write immutable add / remove

Still in `App`, add the handlers:

```jsx
function addItem(course) {
  setItems((prev) =>
    prev.some((c) => c.id === course.id) ? prev : [...prev, course],
  )
}

function removeItem(id) {
  setItems((prev) => prev.filter((c) => c.id !== id))
}
```

Notice what you do **not** do: `items.push(course)`. Mutating the existing array
would not tell React anything changed, so the screen would not update. Instead you
build a **new** array with the spread `[...prev, course]` (add) or `filter`
(remove). The shortlist stores whole course objects, so `CartSummary` has the price
and title it needs without re-looking them up.

## Step 3 — Pass the shortlist down and report clicks up

`App` hands the data down through `CourseGrid` to each `CourseCard`:

```jsx
<CourseGrid courses={visible} items={items} onAdd={addItem} onRemove={removeItem} />
```

`CourseCard` does not own any shortlist state. It receives `enrolled` (a boolean)
and two callbacks, and calls them on click. Data flows **down** as props; events
flow **up** as function calls. This one-way loop is the whole mental model of React.

## Step 4 — Show the shortlist total

`CartSummary` takes `items` and computes the total **during render** — no extra
state:

```jsx
const total = items.reduce((sum, c) => sum + Number(c.fee), 0)
```

Shortlist a couple of courses and watch the `Total: S$…` update live.

---

## 🎤 Vibe prompt

Paste this into Claude Code / Cursor with your Topic 3 project open:

```text
In my React 19 + Vite app (plain JS, no TypeScript), add a course shortlist to
Cook & Bake Academy. The shortlist state must live in App.jsx as an array of the
full course OBJECTS, managed with useState. Requirements:
- App has addItem(course) and removeItem(id). Both use the updater form
  setItems(prev => ...) and update immutably (spread / filter). Never mutate the
  array. addItem must not add a duplicate (match on course.id).
- CourseCard receives { course, enrolled, onAdd, onRemove } and shows an
  "Add to shortlist" button, or a "Remove" button when enrolled. It holds NO
  state of its own. Show S${course.fee} and use the existing .card classes.
- CourseGrid passes shortlist data through to each CourseCard and computes
  enrolled={items.some(c => c.id === course.id)}.
- A new CartSummary component receives { items, onRemove, onClear }, titled
  "Your shortlist", and derives the total (sum of fee) DURING render — no useState,
  no useEffect. Use the .panel / .row / .row--between / .stack classes.
Keep search and category filtering exactly as they are.
```

## 🔍 Read what the AI wrote

Before you trust the generated code, check these — they are the exact places AI
agents slip:

- **Did it mutate?** Search the diff for `.push(`, `.splice(`, or `items[i] =`.
  Any of those mutate state in place and the UI will not re-render. The fix is
  always a new array (`[...prev, course]`, `filter`, `map`).
- **Updater vs. bare value.** Did it write `setItems([...items, course])` or
  `setItems(prev => [...prev, course])`? The bare `items` version reads a *snapshot*
  and breaks if the setter is ever called twice in a row. Prefer the `prev =>`
  form.
- **Where did the state land?** If the agent put `useState` inside `CourseCard`,
  each card gets its own private shortlist and the summary can never see them.
  State must be lifted to `App`. This is the most common structural mistake.
- **Duplicate guard.** Does `addItem` prevent adding the same course twice? Without
  the `some(c => c.id === …)` check, double-clicking shortlists a course twice and
  the total is wrong.
- **Derived, not stored.** Did it add `useState` for the total and a handler to
  keep it in sync? It should not — the total is derived during render. Extra state
  here is a bug waiting to go stale.

## 🧠 Why it works

A **hook** is a function React gives you whose name starts with `use`. It lets a
plain function component do things a plain function cannot: remember a value
between renders, run code after the screen paints, reach into the DOM. `useState`
is the first and most important one.

When you call `const [items, setItems] = useState([])`, React does two things. It
hands back the *current* value of this piece of state (on the very first render,
the `[]` you passed as the initial value). And it hands back a *setter* — a
function that, when called, tells React "this state changed; render this component
again." That re-render is the entire point: your UI is a function of your state,
so to change the UI you change the state and let React re-run your component.

Here is the idea that trips up almost everyone: **state is a snapshot, not a live
variable.** Within a single render, `items` is a frozen value — a photograph taken
at the top of the function. Calling `setItems(...)` does *not* change the `items`
variable you are currently looking at; it schedules a *new* render where `items`
will have a new value. This is why the updater form matters. If you write
`setItems([...items, course])` twice in a row, both calls read the same snapshot of
`items` and the second overwrites the first — you lose one. But `setItems(prev =>
[...prev, course])` asks React "give me the *latest* value and let me compute from
it," so stacked updates compose correctly. Reach for `prev =>` whenever the next
state depends on the previous state.

The second non-negotiable rule is **immutability**. React decides whether to
re-render by comparing the *reference* of the new state to the old one. If you do
`items.push(course)`, the array's contents change but it is the *same array object* —
same reference — so React sees no change and skips the re-render. Your click
appears to do nothing. Building a new array (`[...prev, course]`, `prev.filter(...)`,
`prev.map(...)`) gives React a new reference, so it knows to update. Treat every
piece of state as read-only and always replace it.

The same "replace, never mutate" rule covers **objects**, not just arrays. When a piece of state is
an object — say a `{ title, level }` filter — you never assign to a field (`filter.level =
'Beginner'`); you spread a fresh object with the one field changed: `setFilter(prev => ({ ...prev,
level: 'Beginner' }))`. A mutated object keeps the same reference, so React skips the render, exactly
as a `push` does. And there is a name for *why* the updater form is not merely a nicety here:
**batching**. Inside a single event handler React groups your setter calls and applies them together
before one re-render, so two calls that each read the plain `items` snapshot collapse into a single
change — the classic "I added twice but only one landed" bug. Passing `prev =>` hands each call the
result of the previous one, so stacked updates in the same tick actually compose.

Finally, **the Rules of Hooks**, and *why* they exist. You must call hooks only at
the top level of a component — never inside an `if`, a loop, or a nested function —
and only from React components or other hooks. The reason is delightfully simple:
React does not know the *names* of your hooks. It tracks them purely by **call
order**. The first `useState` in a component is "state slot 1," the second is
"slot 2," and so on, every render. If you hid a `useState` behind an `if` that is
sometimes false, the slots would shift and React would hand `items`'s value to the
wrong variable. Calling hooks unconditionally, in the same order every time, is
what keeps that bookkeeping correct.

**Lifting state up** ties it together. The shortlist is needed in two places: the
cards change it, the summary displays it. Sibling components cannot pass data to
each other directly, so the state moves *up* to their nearest common parent —
`App` — which then passes the data down as props and the change-handlers down as
callbacks. Data flows down, events flow up. When you feel the urge to "share"
state between two components, the answer is almost always: move it to the parent
they both live under. (When that parent gets *too* far from the components that
need it, you reach for Context — Lab 4.4.)

### Lazy initial state (preview)

`useState([])` runs the initial value on every render but only *uses* it the first
time — cheap for `[]`. When the initial value is *expensive* to compute, pass a
function instead: `useState(() => expensiveThing())`. React calls it only on the
first render. You will use this for real in Lab 4.2 to read the saved shortlist out
of `localStorage` exactly once.

## ✅ Check your work

- [ ] Clicking **Add to shortlist** adds the course and the button becomes **Remove**.
- [ ] The `CartSummary` total updates immediately on every add/remove.
- [ ] Double-clicking **Add** does **not** add the course twice.
- [ ] Removing from either the card or the summary updates both places at once.
- [ ] Searching / filtering still works and does not disturb the shortlist.
- [ ] There is no `useState` inside `CourseCard` or `CartSummary`.

## 🛠 Your turn

1. Show the **count** in the shortlist heading — e.g. "Your shortlist (3)".
   (Hint: derive it during render from `items.length`; do not add state.)
2. Add a **"Clear"** button to `CartSummary` that empties the shortlist in one
   click. Decide where the handler lives and how the button reaches it — this is
   the lifting-state-up decision again. (The starter already wires `onClear`; make
   sure you understand why the handler lives in `App`, not `CartSummary`.)

## Common errors

| Error | Cause | Fix |
|---|---|---|
| Clicking Add does nothing | You mutated state (`items.push(course)`) so the reference never changed. | Build a new array: `setItems(prev => [...prev, course])`. |
| Course adds twice on fast clicks | Missing duplicate guard, or you used `setItems([...items, course])` reading a stale snapshot. | Use the updater form and the `some(c => c.id === …)` check. |
| "Rendered more hooks than during the previous render" | A `useState` is inside an `if`/loop/early return. | Move every hook to the top level, called unconditionally. |
| The summary shows a stale total | You stored the total in its own `useState`. | Delete that state; derive `total` during render from `items`. |
| Each card has its own separate shortlist | `useState` was placed inside `CourseCard`. | Lift the shortlist to `App`; pass `enrolled` and callbacks down as props. |
| Changing a field on an object in state does nothing | Mutated the object in place (`obj.x = …`) — same reference. | Spread a new object: `setObj(prev => ({ ...prev, x }))`. |

---
### ✅ Cook & Bake Academy after this lab
The site tracks shortlisted courses in `App` state, with Add and Remove buttons on every card.
