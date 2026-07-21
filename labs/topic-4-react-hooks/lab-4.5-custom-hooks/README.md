# Lab 4.5 — Write your own hooks

> **Topic 4** · ~45 min · Builds on Lab 4.4 (Context + reducer)

### 📖 The build so far
By the end of the last lab, Cook & Bake Academy kept theme and shortlist in Context. **In this lab you add:** your own reusable logic — you extract `useLocalStorage` and `useDebounce` custom hooks and wire the debounced hook into the search box. By the end you'll have the exact hooks the finished app ships, powering a debounced search and a persistent shortlist.

## What you will build

You will extract two reusable hooks and wire them in — the same two files that live
in `cookbake/src/hooks/`. `useLocalStorage(key, initial)` is a drop-in replacement
for `useState` that also persists to storage; you will plug it into `CartContext`,
which lets you **retire the reducer** from Lab 4.4 in favour of plain immutable
setters — the simpler form the finished app actually uses. `useDebounce(value,
delay)` returns a value that only updates after typing pauses; you will feed the
search box through it so the grid filters 300 ms after you stop, not on every
keystroke. This is the payoff of the whole topic: once you understand the built-in
hooks, you can package logic into your own.

## Concepts you will meet

| Concept | In one line |
|---|---|
| Custom hook | A function named `useX` that calls other hooks to package reusable logic. |
| Logic reuse, not state reuse | Two components calling the same hook get **separate** state. |
| Return-shape conventions | Tuple `[value, setValue]` like `useState`; object `{ a, b }` for many named fields. |
| Debouncing | Delay reacting to a fast-changing value until it settles. |
| Spotting extractable logic | `useState` + `useEffect` that recur together are a hook waiting to be named. |

## Before you start

You need your finished Lab 4.4 app. Copy this lab's files:

```bash
cp -R labs/topic-4-react-hooks/lab-4.5-custom-hooks/src/. cookbake/src/
npm run dev
```

Adds `hooks/useLocalStorage.js` and `hooks/useDebounce.js`; updates `App.jsx`,
`SearchBar.jsx` and `context/CartContext.jsx`. `main.jsx` and everything else are
unchanged.

---

## Step 1 — `useDebounce`

Open `hooks/useDebounce.js`. It is `useState` + `useEffect` + cleanup — the exact
ingredients from Lab 4.2, now packaged behind a name:

```jsx
export function useDebounce(value, delay = 300) {
  const [debounced, setDebounced] = useState(value)
  useEffect(() => {
    const id = setTimeout(() => setDebounced(value), delay)
    return () => clearTimeout(id)   // cancel the pending update if value changes first
  }, [value, delay])
  return debounced
}
```

Every keystroke changes `value`, which re-runs the effect; the cleanup cancels the
previous pending timer, so only the *last* keystroke's timer ever fires.

## Step 2 — Wire debounce into search

In `App.jsx`:

```jsx
const [query, setQuery] = useState('')       // updates instantly (input stays snappy)
const debounced = useDebounce(query, 300)     // catches up 300 ms after you stop
const pending = query !== debounced
// filter on `debounced`, and show a "Searching…" hint while pending
```

The input still updates on every keystroke (so it feels instant), but the
*filtering* waits for you to pause. This is exactly what the finished
`CoursesPage` does — there, the debounced value is also what gets written to the
URL, so you don't push a history entry per keystroke.

## Step 3 — `useLocalStorage`

Open `hooks/useLocalStorage.js`. It mirrors `useState`'s `[value, setValue]` shape,
adding a lazy read on init and a persisting setter that accepts a value *or* an
updater function:

```jsx
export function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    try {
      const stored = window.localStorage.getItem(key)
      return stored !== null ? JSON.parse(stored) : initialValue
    } catch { return initialValue }
  })

  const set = (next) => {
    setValue((prev) => {
      const resolved = typeof next === 'function' ? next(prev) : next
      try { window.localStorage.setItem(key, JSON.stringify(resolved)) } catch { /* ignore */ }
      return resolved
    })
  }

  return [value, set]
}
```

## Step 4 — Use it in `CartContext` (and retire the reducer)

Swap Lab 4.4's `useReducer` for `useLocalStorage`, and replace the reducer with
plain immutable setters. This *is* the finished-app `CartContext`:

```jsx
export function CartProvider({ children }) {
  const [items, setItems] = useLocalStorage('cart', [])

  const addItem = (course) =>
    setItems((prev) => (prev.some((c) => c.id === course.id) ? prev : [...prev, course]))
  const removeItem = (id) => setItems((prev) => prev.filter((c) => c.id !== id))
  const clear = () => setItems([])

  const total = items.reduce((sum, c) => sum + Number(c.fee), 0)
  const value = { items, addItem, removeItem, clear, total, count: items.length }
  return <CartContext.Provider value={value}>{children}</CartContext.Provider>
}
```

The shortlist persists again — and the whole provider got *shorter*. Refresh: your
shortlist is still there. The `useCart()` API is unchanged, so every consumer from
Lab 4.4 keeps working untouched.

---

## 🎤 Vibe prompt

```text
In my React 19 + Vite Cook & Bake Academy app, extract two custom hooks.
1) hooks/useDebounce.js — export useDebounce(value, delay = 300). Return a
   debounced copy of value using useState + useEffect + a setTimeout whose cleanup
   clearTimeouts on change. Deps [value, delay].
2) hooks/useLocalStorage.js — export useLocalStorage(key, initialValue). Same
   [value, setValue] shape as useState. Lazily initialise from localStorage[key]
   (JSON.parse, fall back to initialValue). The setter accepts a value OR an updater
   function and writes JSON to localStorage. Wrap storage reads/writes in try/catch.
Then: in App.jsx run `query` through useDebounce(query, 300) and filter on the
debounced value; show a "Searching…" hint while query !== debounced. In
context/CartContext.jsx replace the Lab 4.4 useReducer with useLocalStorage('cart',
[]) and plain immutable setters addItem(course)/removeItem(id)/clear, keeping the
same useCart() API: { items, addItem, removeItem, clear, total, count }.
```

## 🔍 Read what the AI wrote

- **Does `useDebounce` clean up?** The effect must `return () => clearTimeout(id)`.
  Without it, every keystroke leaves a pending timer and the value updates in a
  burst instead of debouncing. Same cleanup lesson as Lab 4.2 — recognise it.
- **Return shape.** `useLocalStorage` should return the tuple `[value, setValue]`
  so it is a true drop-in for `useState`. If the agent returns an object or only
  the value, calling code cannot update it the familiar way.
- **Lazy init, not eager.** The initial `useState(() => …)` must be a function, or
  storage is re-read and re-parsed on every render.
- **"Shares state" misconception.** If the agent's comments or code imply two
  components using `useDebounce` will somehow share a value, that is wrong — each
  call has its own independent state (see Why it works). Watch for a module-level
  variable used to "cache" across components; that is a bug.
- **Name starts with `use`.** A hook that calls other hooks *must* be named `useX`,
  or React's lint rules can't enforce the Rules of Hooks on it. `getDebounce`
  would silently lose that safety net.

## 🧠 Why it works

A **custom hook is nothing more exotic than a function whose name starts with
`use` and which calls other hooks.** There is no special API, no registration, no
base class. `useDebounce` is a plain function that happens to call `useState` and
`useEffect` inside it. Because it calls hooks, the Rules of Hooks apply to it — it
must be called at the top level of a component or another hook, never conditionally
— and the `use` prefix is what lets React's linter *see* that it is a hook and
enforce those rules. Rename it `getDebounce` and the safety net silently
disappears.

The single most important thing to understand — and a near-universal
misconception, including in AI-generated code — is that **a custom hook shares
*logic*, never *state*.** When two different components each call
`useDebounce(...)`, they do **not** share a debounced value. Each call runs the
hook's body fresh and creates its *own* `useState` inside *that* component. A hook
is a recipe, not a shared jar: every kitchen that follows the recipe bakes its own
loaf. This is exactly the opposite of Context, which *does* share one value across
components. If you actually want shared state, you put it in Context (Lab 4.4) or
lift it up (Lab 4.1); a custom hook only lets many components run the *same setup
steps* over their *own* separate state. Keep that distinction sharp and hooks stop
being mysterious.

Once you internalise "a hook is just a function that calls hooks," you start seeing
them everywhere in your existing code — specifically, wherever the **same `useState`
+ `useEffect` pair keeps recurring**. Look back at Lab 4.2: the shortlist used lazy
`useState` to read storage plus a `[items]` effect to write it. If you also
persisted the category filter (the Lab 4.2 "Your turn"), you wrote that pattern
*twice*. Two copies of the same `useState`-plus-effect shape is the smell that says
"extract a hook." `useLocalStorage` is that extraction: the read-on-init and
write-on-change logic, named once and reused. Notice how it *collapses*
`CartContext` — what took a `useReducer` plus (in the finished app's earlier drafts)
a persistence effect now takes one `useLocalStorage` line, and the reducer from Lab
4.4 disappears entirely. That is the honest end of the trade-off we flagged in Lab
4.4: for three small operations, plain immutable setters over `useLocalStorage` read
more simply than a reducer, so the finished app keeps this form. The reducer was the
better *teacher*; this is the better *code* for a shortlist this small.

`useDebounce` is the same idea aimed at a different problem. Its body — `useState`,
a `useEffect` that sets a `setTimeout`, and a cleanup that `clearTimeout`s — is
precisely the timer-with-cleanup pattern from Lab 4.2's `Countdown`, and the
cleanup does precisely the same job: because the effect re-runs every time `value`
changes, React runs the cleanup *first*, cancelling the previous pending timer. So
while you are typing "macaron", the timers for "m", "ma", "mac"… are each cancelled
in turn, and only the timer started after you stop typing ever fires. The result:
`query` updates instantly so the input feels responsive, but `debounced` — the value
the filter actually reads — settles only once, 300 ms after you pause. Debouncing
turns a value that changes too fast into one that changes when it matters, and
packaging it as a hook means the next search box, or autosave, or resize handler,
gets it for free.

Two small **conventions** make your hooks feel native. First, **return shape.** If
your hook manages one value you set, return a **tuple** `[value, setValue]` so it
reads like `useState` — that is why `useLocalStorage` returns an array and slots in
as a drop-in replacement. If it exposes several named things, return an **object**
`{ a, b, c }` so callers destructure by name (as our `useCart` does). Second,
**name the hook for what it gives you** (`useDebounce`, `useLocalStorage`,
`useCart`), always with the `use` prefix. Good names and predictable return shapes
are what let a teammate — or you, six months later, or an AI agent reading your
code — use the hook correctly without opening it. And that reading-your-code skill
cuts both ways: when an AI generates a component stuffed with a repeated
`useState`+`useEffect` block, or the same fetch-and-cache logic inline in three
places, you now recognise the shape and can prompt "extract that into a custom
hook" — turning a wall of generated code into something reusable and testable.

## ✅ Check your work

- [ ] Typing in the search box updates the input instantly, but the grid filters
      only after you pause (~300 ms); "Searching…" shows in between.
- [ ] The shortlist survives a page refresh, now via `useLocalStorage` in `CartContext`.
- [ ] `useLocalStorage` returns `[value, setValue]` and is used exactly like `useState`.
- [ ] `useDebounce`'s effect returns `() => clearTimeout(id)`.
- [ ] Both hook files live in `src/hooks/` and their names start with `use`.

## 🛠 Your turn

1. Add a `delay` control (a small `<select>` for 0 / 300 / 1000 ms) and pass it to
   `useDebounce(query, delay)`. Feel how the hook's second argument makes it
   configurable.
2. Write `useMediaQuery(query)` returning a boolean, and use it to hide the
   `RenderCounter` badge on narrow screens. It is `useState` + an effect that
   subscribes to `window.matchMedia(query)` and **cleans up** the listener — the
   same three ingredients, a brand-new hook.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| Filtering fires on every keystroke | You filtered on `query`, not `debounced`, or the debounce effect lacks cleanup. | Filter on the debounced value; `return () => clearTimeout(id)`. |
| `useLocalStorage` value won't update | The hook returns only the value, not `[value, setValue]`. | Return the tuple so callers can set it like `useState`. |
| Storage re-read on every render (jank) | Eager init: `useState(JSON.parse(localStorage...))`. | Use lazy init: `useState(() => …)`. |
| "Invalid hook call" | The hook is called conditionally, or isn't named `useX`. | Call it unconditionally at the top level; prefix the name with `use`. |
| Two components unexpectedly share a value | Assuming a custom hook shares state (it doesn't), or using a module-level variable. | For shared state use Context; a hook gives each caller its own state. |
| `JSON.parse` crashes on load | Corrupt or non-JSON value already in storage. | Wrap the read in `try/catch` and fall back to `initialValue`. |

---
### ✅ Cook & Bake Academy after this lab
Reusable `useDebounce` and `useLocalStorage` hooks power a debounced search and a persistent shortlist — the exact hooks the finished app ships.
