# Lab 4.3 — Escape hatches with `useRef`

> **Topic 4** · ~45 min · Builds on Lab 4.2 (persistent shortlist + countdown)

### 📖 The build so far
By the end of the last lab, Cook & Bake Academy had a persistent shortlist and a countdown. **In this lab you add:** direct DOM access with `useRef` — the search box focuses itself the moment the page opens, the caret snaps back to it after you click a category chip, and a "Browse courses" button smooth-scrolls the grid into view. By the end you'll have the two refs the *real* finished app uses, in the two places it uses them.

## What you will build

You will add the small touches that make an app feel finished, all powered by one
hook doing two very different jobs. **Job one — reach into the DOM.** The finished
Cook & Bake app uses a ref in exactly two places, and you build both here:

- **A self-focusing search box.** `CoursesPage` holds `const searchInput = useRef(null)`,
  passes it to `<SearchBar … inputRef={searchInput} />` (which puts it on its
  `<input ref={inputRef} />`), then focuses it on mount — and again after you click
  a Bakery/Cooking chip, so the caret returns to the box.
- **Scroll-to-grid.** `HomePage` holds `const popularRef = useRef(null)` on its
  courses `<section>`, and passes `scrollToCourses` to the hero as
  `<Hero onBrowse={scrollToCourses} />`. Clicking "Browse courses" smooth-scrolls
  the grid into view.

**Job two — remember a value without re-rendering:** a little `RenderCounter` badge
that shows how many times a component has rendered, updating without ever *causing*
a render itself.

> **Topics 1–4 have no router yet** — pages arrive in Topic 6. So in this lab you
> build both behaviours in the components you already have: the search-focus ref
> lives in `App`, and the scroll ref goes on the courses `<section>` in `App`. In
> Topic 6 these exact refs move into `src/pages/CoursesPage.jsx` and
> `src/pages/HomePage.jsx` — which is where they live in the finished app. You'll
> see that finished-app code in **Why it works**.

## Concepts you will meet

| Concept | In one line |
|---|---|
| `useRef` | Returns a stable `{ current }` box that persists for the component's whole life. |
| Ref vs. state | Changing `ref.current` does **not** re-render; calling a state setter **does**. |
| DOM ref | Put a ref on a JSX element and React fills `ref.current` with the real DOM node. |
| Imperative escape hatch | Refs let you call browser methods directly: `.focus()`, `.scrollIntoView()`. |
| Ref is null on first render | The DOM node does not exist yet during render — so you read the ref in an effect. |
| Non-visual bookkeeping | Timer ids, previous values, render counts: things the UI never draws → a ref, not state. |

## Before you start

You need your finished Lab 4.2 app. Copy this lab's files:

```bash
cp -R labs/topic-4-react-hooks/lab-4.3-useref/src/. cookbake/src/
npm run dev
```

This overwrites `App.jsx`, `SearchBar.jsx`, `CourseGrid.jsx` and adds a new
`RenderCounter.jsx`. `CourseCard`, `CartSummary` and `Countdown` are unchanged.

---

## The one rule that decides everything

Before the steps, hold onto this. It is the whole lab:

> **If changing a value should redraw the screen, it is STATE. If it should not, it is a REF.**

Mutating `ref.current` does **not** re-render. That single fact is why a ref — not
state — is the right home for a DOM node handle, a `setInterval` id, or a render
count. Keep the rule in view as you go.

## Step 1 — A ref to the search input

In `App.jsx`, create a ref and hand it to `SearchBar` as an ordinary prop called
`inputRef`:

```jsx
const searchInput = useRef(null)
// ...
<SearchBar value={query} onChange={setQuery} inputRef={searchInput} />
```

`useRef(null)` gives you a box: `{ current: null }`. When React renders the
`<input>`, it sets `searchInput.current` to the actual DOM element.

## Step 2 — Focus on mount, and after a chip click

Focus the box once, on mount, in an effect:

```jsx
useEffect(() => {
  searchInput.current?.focus()   // element exists by the time effects run
}, [])
```

Then, when a category chip is clicked, return the caret to the search box. Wrap the
category setter:

```jsx
const selectCategory = (cat) => {
  setCategory(cat)
  searchInput.current?.focus()   // leave the caret back in the search box
}
// ...
<CategoryFilter value={category} onChange={selectCategory} />
```

Reload: the cursor is already in the search box. Click a Bakery chip: focus snaps
back so you can keep typing. Note the `?.` — `current` could be `null` in the brief
window before the input mounts.

## Step 3 — `SearchBar` puts the ref on its `<input>`

Open `SearchBar.jsx`. It takes `inputRef` as a normal prop and attaches it:

```jsx
export default function SearchBar({ value, onChange, inputRef }) {
  return (
    <div className="search">
      <span className="search__icon" aria-hidden="true">🔎</span>
      <input ref={inputRef} type="search" value={value}
             onChange={(e) => onChange(e.target.value)} /* … */ />
    </div>
  )
}
```

Because the ref travels as a plainly-named prop (`inputRef`), you need **no**
`forwardRef` wrapper — see **Why it works**.

## Step 4 — Scroll the grid into view

Put a ref on the courses `<section>` (always rendered), and a button that calls the
browser's scroll method imperatively:

```jsx
const coursesRef = useRef(null)

const scrollToCourses = () => {
  coursesRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' })
}
// ...
<button className="btn btn--ghost btn--lg" onClick={scrollToCourses}>Browse courses ↓</button>
<section ref={coursesRef} className="section" id="courses"> … </section>
```

In the finished app this button *is* the hero's "Browse courses" button, wired via
`<Hero onBrowse={scrollToCourses} />` — but the hero uses the router, which arrives
in Topic 6, so for now the button lives in `App`.

## Step 5 — A ref that is *not* a DOM node

Open `RenderCounter.jsx`. Here `useRef` holds a plain number, not an element:

```jsx
const renders = useRef(0)
renders.current += 1   // survives renders, but bumping it does NOT re-render
```

The "re-render" button uses `useState` to force renders so you can watch the count
climb — proving the difference between the two hooks.

---

## 🎤 Vibe prompt

```text
In my React 19 + Vite Cook & Bake Academy app, use useRef for three things.
1) In App.jsx create searchInput = useRef(null) and pass it to SearchBar as a
   prop called inputRef. SearchBar puts it on its <input ref={inputRef} />. Do NOT
   use forwardRef — pass the ref as an ordinary named prop.
2) Focus the search input on mount via an effect with [] deps
   (searchInput.current?.focus()). Also refocus it inside the category-change
   handler, so clicking a Bakery/Cooking chip returns the caret to the search box.
3) Create coursesRef = useRef(null), put it on the courses <section>, and a
   "Browse courses" button that calls
   coursesRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' }).
Also add RenderCounter.jsx: a component using useRef to count how many times it has
rendered and display the count, with a button that forces a re-render via useState.
Remember: if changing a value should redraw the screen it is state; if not it is a
ref. Read refs in effects/handlers, never in the render body, and guard with ?..
```

## 🔍 Read what the AI wrote

- **Reading a ref during render.** The biggest one. If the agent writes
  `searchInput.current.focus()` in the render body, `current` is still `null` (the
  DOM does not exist yet) and it crashes. Focus belongs in a `useEffect`, which runs
  *after* the DOM is committed.
- **Ref where state was needed (or vice-versa).** If it stored the *search text* in
  a ref "to avoid re-renders," that is wrong — typing must update the screen, which
  needs state. Conversely, if it stored the *interval id* or the *render count* in
  `useState`, that re-renders on every tick. Apply the rule: screen redraw → state;
  no redraw → ref.
- **`forwardRef` in 2024-era code.** A tell that the AI is working from old training
  data: it wraps `SearchBar` in `forwardRef((props, ref) => …)`. You don't need it —
  the ref rides in as a normal prop named `inputRef`. It still *works*, but it is
  legacy noise.
- **Did it clean up any listener?** If the agent added a `window` keydown shortcut
  as an extra, its effect **must** return `() => window.removeEventListener(...)`,
  or every StrictMode double-mount leaves another listener attached.
- **Optional chaining.** Good generated code writes `searchInput.current?.focus()`.
  The `?.` guards the brief window where `current` could be `null` (before mount,
  after unmount).

## 🧠 Why it works

`useRef` returns a single, stable object: `{ current: someValue }`. "Stable" means
React hands you the *exact same object* on every render for the life of the
component — it never gets a new identity the way a fresh `{}` literal would. You
read and write the value through `.current`. And here is the defining property:
**mutating `.current` does not trigger a re-render.** That is the opposite of state,
and it is the entire reason the hook exists. The contrast is worth a table:

| | `useState` | `useRef` |
|---|---|---|
| Read | `value` | `ref.current` |
| Change | `setValue(next)` | `ref.current = next` |
| Causes a re-render? | **Yes** | **No** |
| Value seen in render | The snapshot for *this* render | Always the latest `.current` |
| Use it for | Anything the UI displays | Anything the UI does *not* display |

That last row is the rule again, in table form: **screen redraw → state; no redraw
→ ref.** Everything below follows from it.

### Job one — a handle on a DOM node

When you pass a ref to a JSX element — `<input ref={searchInput} />` — React sets
`searchInput.current` to the real DOM node after it mounts. Now you can call the
imperative browser methods React deliberately hides from you: `.focus()`,
`.scrollIntoView()`, `.play()` on a `<video>`, `.getBoundingClientRect()` to
measure. React is *declarative* — you describe what the UI should look like and let
it update the DOM. But "is this input focused?" and "scroll this section into view"
have no declarative equivalent; they are imperative actions. Refs are the sanctioned
**escape hatch** from React's declarative world into the imperative DOM. Use them
for exactly those cases, and no more.

Two rules keep DOM refs safe. First, **refs are attached *after* the DOM is
committed, so `ref.current` is `null` during the first render.** React has not
created the `<input>` yet while your component function is running — it creates it,
paints it, *then* fills in `.current`. That is precisely why focus-on-mount lives in
a `useEffect([])`: effects run after the commit, when `current` points at a real
element. Read a ref in the render body and you get `null`. Second, guard with `?.` —
there are brief moments (before mount, after unmount) where `current` is `null`.

Here is the finished-app code you are building toward — the two real refs, in the
two real files they live in from Topic 6 onward:

```jsx
// src/pages/CoursesPage.jsx  — the self-focusing search box
const searchInput = useRef(null)

useEffect(() => {
  searchInput.current?.focus()          // focus the moment the page opens
}, [])

const setCategory = (cat) => {
  setSearchParams(/* … */)
  searchInput.current?.focus()          // caret returns after a chip click
}

<SearchBar value={query} onChange={setQuery} inputRef={searchInput} />
```

```jsx
// src/pages/HomePage.jsx  — "Browse courses" scrolls to the grid
const popularRef = useRef(null)

const scrollToCourses = () =>
  popularRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' })

<Hero onBrowse={scrollToCourses} />
<section ref={popularRef} className="section" id="courses"> … </section>
```

In this lab both live in `App` (there is no router yet); in Topic 6 they move,
unchanged, into those two pages. Same refs, same effects — a different home.

### Job two — a mutable box that survives renders without causing one

The `RenderCounter` keeps a count in `renders.current` and bumps it each render.
Because writing a ref does not re-render, this is a pure side-observation — it
counts renders without perturbing them. Try it the wrong way to feel the rule:
if you kept the count in `useState` and incremented it during render, each render
would schedule another render — an **infinite loop**. The count must *not* redraw
the screen, so by the rule it is a ref. (Incrementing a ref *during* render like
this is the one widely-accepted exception to "no refs during render," and only
because it is a diagnostic the UI logic does not depend on — never do it for real
data.)

The same "survives renders, causes none" property is why **a `setInterval` /
`setTimeout` id belongs in a ref**, not state. You need to remember the id between
renders so you can `clearInterval` it later — but the id is never *shown*, so
putting it in state would re-render on every tick for nothing. Here is the canonical
`useRef` example, a start/stop timer:

```jsx
const [seconds, setSeconds] = useState(0)   // displayed  → state
const timerRef = useRef(null)               // interval id → ref

function start() {
  if (timerRef.current) return              // already running
  timerRef.current = setInterval(() => setSeconds((s) => s + 1), 1000)
}
function stop() {
  clearInterval(timerRef.current)
  timerRef.current = null
}
```

Notice the split, and notice it *is* the rule. The *displayed* number is `useState`,
because changing it must re-render the screen. The *interval id* is `useRef`,
because you only need to remember it long enough to clear it later — the UI never
shows it. Why not a plain `let timerId` variable? Because a function component
re-runs top to bottom on every render, so a local variable is re-created (and reset
to `null`) each time — the next render would lose the id and you could never stop
the timer. A ref is the notebook React does not erase between renders; a plain
variable is a whiteboard wiped on every re-render. A **previous value** you want to
compare against next render, a DOM node handle, a timer id — all the same shape:
persists across renders, drawn by nobody, so all refs.

### `ref` as a prop, and why no `forwardRef`

For years a function component could not receive a `ref` — `ref` was a reserved
word React intercepted, so forwarding a ref to a child's DOM node meant wrapping the
child in `forwardRef((props, ref) => …)`. Two things make that unnecessary here.
First, our `SearchBar` receives the ref under an ordinary name — `inputRef` — so it
is just a normal prop with no special-casing at all. Second, even if you *did* name
it `ref`, React 19 removed the special-casing: `ref` is now an ordinary prop on
function components. Either way, `forwardRef` is obsolete ceremony. We call this out
because the vast majority of AI-generated code and online tutorials predate the
change and still reach for it — recognising that is a good example of reading
generated code against the *current* version of the framework rather than accepting
it blindly.

## ✅ Check your work

- [ ] On page load, the cursor is already in the search box.
- [ ] Clicking a Bakery/Cooking chip returns focus to the search box.
- [ ] "Browse courses ↓" smooth-scrolls the grid into view.
- [ ] The render badge increments when you click its "re-render" button.
- [ ] `SearchBar` takes `inputRef` as a plain prop — there is no `forwardRef` in the file.
- [ ] No ref is read in a render body; focus happens inside a `useEffect`.

## 🛠 Your turn

1. Add a **global `/` shortcut** that focuses the search box: an effect that adds a
   `window` keydown listener and **removes it in cleanup**. Ignore `/` when the
   input is already focused (`document.activeElement === searchInput.current`) and
   `preventDefault()` so `/` isn't typed. This is the same cleanup discipline as Lab
   4.2 — for an event listener this time.
2. Add a `previousCount` ref to `CartSummary` that remembers the shortlist count
   from the *last* render, and show "▲ added" or "▼ removed" based on whether the
   count went up or down. This is a value you want to remember across renders but
   never render directly — a perfect ref.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `Cannot read properties of null (reading 'focus')` | You read `ref.current` during render or before mount. | Do it in a `useEffect`, and guard with `?.`. |
| Focus never lands on the search box | You called `.focus()` in the render body, when `current` is still `null`. | Move it into `useEffect(() => …, [])`. |
| Caret does not return after a chip click | The category handler doesn't refocus. | Call `searchInput.current?.focus()` inside your `selectCategory`. |
| Search box does not update as you type | You stored the query in a ref instead of state. | The query is displayed, so it must be `useState`; keep refs for the DOM node. |
| "Too many re-renders" from the render counter | The count was kept in `useState` and set during render. | A render count must be a `useRef`; bumping `.current` never re-renders. |
| A timer can't be stopped / `clearInterval` does nothing | The interval id was kept in a plain variable, reset to `null` on every render. | Store the id in a `useRef` so it survives re-renders; clear `timerRef.current`. |
| `forwardRef is not defined` | Half-migrated code mixes the old wrapper with a `ref` prop. | Delete `forwardRef`; pass the ref as a normal prop (here, `inputRef`). |

---
### ✅ Cook & Bake Academy after this lab
`useRef` gives the site a self-focusing search box, focus-return after a chip click, and scroll-to-grid — the two refs the finished app really uses.
