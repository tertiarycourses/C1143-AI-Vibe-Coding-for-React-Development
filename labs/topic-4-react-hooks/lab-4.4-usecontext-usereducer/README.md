# Lab 4.4 — Global state with `useContext` + `useReducer`

> **Topic 4** · ~55 min · Builds on Lab 4.3 (refs, focus, scroll)

### 📖 The build so far
By the end of the last lab, Cook & Bake Academy managed shortlist state by passing props down through `App`. **In this lab you add:** global state — a dark-mode `ThemeContext` and a `CartContext` whose shortlist is driven by a `useReducer`, removing the prop-drilling. By the end you'll have theme and shortlist shared from Context anywhere in the tree.

## What you will build

You will lift the two pieces of truly *global* state — the theme and the shortlist —
out of prop chains and into React **Context**, so any component can read them
directly. A dark/light toggle in the `Navbar` themes the whole app (and remembers
your choice). The shortlist moves out of `App` and into a `useReducer` with named
actions `ADD`, `REMOVE`, `CLEAR`. When you are done, `CourseCard` and `CartSummary`
reach into the shortlist by themselves and `App` stops passing shortlist props
around entirely.

> **A note on the finished app.** The real `cookbake` keeps its `CartContext`
> *simpler* — plain immutable setters over a `useLocalStorage` hook, not a reducer
> (you'll build that exact version in Lab 4.5). We use `useReducer` here because it
> is the best possible teacher of *named state transitions*, and knowing it is what
> lets you decide, honestly, when a reducer is worth it and when it is overkill.
> The `useCart()` API you expose — `items`, `addItem`, `removeItem`, `clear`,
> `total`, `count` — is exactly the finished app's, so every consumer you write
> here survives the swap unchanged.

## Concepts you will meet

| Concept | In one line |
|---|---|
| Prop drilling | Passing a prop through components that don't use it, just to reach a deep child. |
| Context | A channel: `createContext` → `<Provider value>` → `useContext` reads it anywhere below. |
| Custom hook guard | Wrap `useContext` in a `useX()` that throws if used outside its Provider. |
| `useReducer` | State via a pure `(state, action) => newState` function you `dispatch` actions to. |
| Reducer purity | A reducer must not mutate or cause side effects — same inputs, same new state. |
| `useMemo` on provider value | Memoise the value object so consumers don't re-render needlessly. |

## Before you start

You need your finished Lab 4.3 app. This lab adds a `context/` folder and rewires
`main.jsx`, so copy carefully:

```bash
cp -R labs/topic-4-react-hooks/lab-4.4-usecontext-usereducer/src/. cookbake/src/
npm run dev
```

Files changed/added: `main.jsx`, `App.jsx`, `Navbar.jsx`, `CourseCard.jsx`,
`CourseGrid.jsx`, `CartSummary.jsx`, and the new `context/ThemeContext.jsx` +
`context/CartContext.jsx`. `SearchBar`, `Countdown` and `RenderCounter` are
unchanged.

> **Why `CourseGrid` changed too.** In Labs 4.1–4.3 the grid carried
> `items`/`onAdd`/`onRemove` props just to hand them to each card — textbook prop
> drilling. Now the card reads the shortlist itself, so the grid sheds those props.
> That deletion *is* the lesson; the lab includes the updated grid so it stays
> runnable.

---

## Step 1 — A theme Context

Open `context/ThemeContext.jsx`. Three moving parts: `createContext`, a
`ThemeProvider` that holds the `theme` state and themes the page in an effect, and
a `useTheme()` hook to read it:

```jsx
const ThemeContext = createContext(null)

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState(() => localStorage.getItem('theme') || 'light')
  useEffect(() => {
    document.documentElement.dataset.theme = theme   // index.css reads this
    localStorage.setItem('theme', theme)
  }, [theme])
  const value = useMemo(() => ({ theme, toggle: () => setTheme(t => t === 'dark' ? 'light' : 'dark') }), [theme])
  return <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>
}

export function useTheme() {
  const ctx = useContext(ThemeContext)
  if (!ctx) throw new Error('useTheme must be used inside <ThemeProvider>')
  return ctx
}
```

The `data-theme` attribute on `<html>` flips the CSS variables already defined in
`index.css` (`:root[data-theme='dark']`). This mirror-onto-the-DOM effect is exactly
what the finished app does.

## Step 2 — A shortlist Context backed by a reducer

Open `context/CartContext.jsx`. The shortlist's logic is a **pure reducer**. The
shortlist holds full course **objects**, so `ADD` carries the whole course and
`REMOVE` carries an id:

```jsx
function cartReducer(state, action) {
  switch (action.type) {
    case 'ADD':    return state.some((c) => c.id === action.course.id) ? state : [...state, action.course]
    case 'REMOVE': return state.filter((c) => c.id !== action.id)
    case 'CLEAR':  return []
    default:       throw new Error(`Unknown cart action: ${action.type}`)
  }
}
```

`CartProvider` runs it with `useReducer` and exposes friendly `addItem` /
`removeItem` / `clear` methods, plus the derived `total` and `count`, through
`useCart()`.

## Step 3 — Wrap the app in both Providers

Open `main.jsx`. The Providers must sit *above* everything that reads them:

```jsx
<StrictMode>
  <ThemeProvider>
    <CartProvider>
      <App />
    </CartProvider>
  </ThemeProvider>
</StrictMode>
```

(In Topic 5 an `AuthProvider` joins them, and in Topic 6 a `<BrowserRouter>` wraps
the lot — the same nesting, more layers.)

## Step 4 — Consume the contexts

- `Navbar` calls `useTheme()` for a toggle button and `useCart()` for the `count` badge.
- `CourseCard` calls `useCart()`, reads `enrolled = items.some(c => c.id === course.id)`,
  and calls `addItem` / `removeItem`.
- `CartSummary` calls `useCart()` for the list, `total` and a "Clear" button.
- `App` now only reads `const { count } = useCart()` for the tab-title count, and
  passes **no** shortlist props to `CourseGrid`.

Toggle the theme, shortlist courses, clear the shortlist — all with zero prop
drilling.

---

## 🎤 Vibe prompt

```text
In my React 19 + Vite Cook & Bake Academy app, introduce global state with Context.
1) context/ThemeContext.jsx: export ThemeProvider and a useTheme() hook.
   ThemeProvider holds theme ('light'|'dark') in state, lazily initialised from
   localStorage['theme']. An effect sets
   document.documentElement.dataset.theme = theme and persists it. Expose { theme,
   toggle } and wrap the value in useMemo([theme]). useTheme must throw if called
   outside the provider.
2) context/CartContext.jsx: export CartProvider and useCart(). The shortlist is an
   array of full course OBJECTS, managed with useReducer + a PURE reducer handling
   ADD (carries the course), REMOVE (carries an id), CLEAR (default: throw). Expose
   { items, addItem, removeItem, clear, total, count } via useMemo([items]), where
   total = items.reduce((sum, c) => sum + Number(c.fee), 0). useCart must throw
   outside the provider.
3) Wrap <App/> in <ThemeProvider><CartProvider> in main.jsx.
4) Navbar: a theme toggle button (useTheme) and a shortlist count badge (useCart).
   CourseCard and CartSummary: read the shortlist via useCart instead of props. App
   reads only { count } for the tab title and passes no shortlist props to
   CourseGrid; update CourseGrid to drop them.
```

## 🔍 Read what the AI wrote

- **Is the value memoised?** The Provider's `value` should be a `useMemo`. If the
  agent wrote `value={{ items, addItem, removeItem }}` inline, a brand-new object is
  created every render, so *every* consumer re-renders every time — the classic
  Context performance trap.
- **Is there a guard hook?** Check for the `if (!ctx) throw …` inside `useCart` /
  `useTheme`. Without it, forgetting the Provider gives a cryptic "cannot read
  property of null" far from the real mistake.
- **Is the reducer pure?** It must **return new state** and never mutate — no
  `state.push(...)`, no `state[i] = …`, no `console.log`/`fetch` inside. A `default`
  case that throws on unknown actions is a good sign.
- **Did it over-reach for Context?** Context is for *global* concerns (theme,
  shortlist, auth). If the agent moved `query` or `category` into Context too, push
  back — those are local to `App` and belong in `useState`. Context is not a state
  manager; it is dependency injection.
- **Provider placement.** The Providers must wrap `<App/>` in `main.jsx`. A Provider
  rendered *inside* App, below a consumer, means that consumer reads `null` and the
  guard throws.

## 🧠 Why it works

By Lab 4.3 the shortlist had to travel `App → CourseGrid → CourseCard`, and the grid
carried `items`, `onAdd` and `onRemove` props it never used itself — it just passed
them along. That is **prop drilling**: threading data through intermediaries purely
to reach a deep descendant. It is verbose, and it couples every layer in between to
data it does not care about. A theme toggle in the `Navbar` would be even worse —
the theme would have to be drilled down and back up through half the tree.

**Context** solves exactly this. Think of it as a channel that runs vertically
through your component tree. You open the channel with `createContext()`. You
broadcast a value onto it by wrapping part of the tree in
`<SomeContext.Provider value={…}>`. And *any* component inside that Provider —
however deep — tunes into the channel with `useContext(SomeContext)` and reads the
value directly, with no props in between. The intermediate components (`CourseGrid`)
neither know nor care that the data exists. That is why the grid could shed its
shortlist props entirely: the cards now tune into the shortlist channel themselves.

It is worth being precise about what Context *is not*. Context is not a state
manager and it does not, by itself, hold or update state — notice that our
`ThemeProvider` still uses plain `useState` and `CartProvider` still uses
`useReducer` to *hold* the data. Context only **distributes** whatever value you
put on it. The accurate phrase is **dependency injection**: it delivers a
dependency (the current theme, the shortlist API) to the components that need it,
without those components having to receive it hand-to-hand. Reach for it for a
small number of genuinely app-wide concerns — theme, current user, shortlist. Do
*not* sweep every piece of state into Context; `query` and `category` are local to
`App` and belong in `useState` right there. There is a performance reason on top of the tidiness one:
**every** component reading a context re-renders whenever that context's value changes. Put a
fast-changing value on a context — the live contents of a text input, a mouse position, an animation
frame — and you force *every* consumer to re-render on every keystroke or frame, however little of
the value they actually use. Keep high-frequency values in local state next to where they are used,
and reserve context for things that change occasionally: the theme, the signed-in user, the shortlist.

Two patterns make Context pleasant to use. The first is the **custom-hook guard**.
Instead of exporting the raw context and having every component call
`useContext(CartContext)`, you export a `useCart()` hook that calls
`useContext` for them and *throws a clear error* if the value is `null` — which
only happens when a component is rendered outside the Provider. This turns a
confusing, far-away "cannot read properties of null" into an immediate, honest
"useCart must be used inside <CartProvider>." The second is a **performance
caveat**: every component that reads a context re-renders whenever the Provider's
`value` changes *by reference*. If you write `value={{ items, addItem }}` inline, you
mint a fresh object every render, so all consumers re-render every time the
Provider's parent renders — even when nothing they use actually changed. Wrapping
the value in `useMemo([items])` (or `[theme]`) keeps the same object identity until
the underlying data really changes, so consumers only re-render when they must.

Now, **`useReducer`**, and when to prefer it over `useState`. `useReducer` manages
state through a **pure function** — `reducer(state, action) => newState` — that you
never call yourself; instead you `dispatch(action)` and React runs the reducer for
you. For a single boolean or string, `useState` is simpler and you should keep it.
Reach for `useReducer` when: several fields **change together** as a unit; the next
state **depends on the previous** state in non-trivial ways; or you have a set of
distinct operations you want to **name and test**. Our shortlist hits the third —
`ADD`, `REMOVE` and `CLEAR` are named operations, each computes the next array from
the previous one, and the logic is now one pure function you could unit-test with
zero React involved: `cartReducer([], { type: 'ADD', course })` must return
`[course]`. That testability is the quiet superpower of reducers.

**Being honest about the trade-off.** Is a reducer *worth it* for this shortlist?
Not really — and the finished app agrees. Three tiny operations over one array is
comfortably within `useState`'s reach, which is why Lab 4.5 rewrites this same
`CartContext` as plain immutable setters (`addItem`/`removeItem`/`clear`) over a
`useLocalStorage` hook, and it reads more simply. We taught the reducer first
because *recognising when to reach for it* is the real skill: the day your actions
grow to eight, carry payloads, and depend on each other, the reducer's named,
testable, pure transitions stop being ceremony and start being the clearest way to
write it. Know both; pick the smaller one until the bigger one earns its place.

The reducer's one ironclad rule is **purity**. Given the same state and action it
must always return the same new state, it must not mutate the state it was handed
(build a new array with `filter`/spread, exactly as in Lab 4.1), and it must not
perform side effects — no logging, no storage writes, no network calls inside the
reducer. Side effects live in effects; the reducer only computes. Keep it pure and
your state transitions become predictable, replayable, and trivial to reason about.

## ✅ Check your work

- [ ] The `Navbar` toggle switches the whole app between light and dark.
- [ ] The theme choice survives a page refresh (it is in `localStorage`).
- [ ] Add / remove works from the cards and the summary with no props threaded
      through `CourseGrid`.
- [ ] "Clear" empties the shortlist in one click (the `CLEAR` action).
- [ ] `useCart()` / `useTheme()` throw a clear error if you temporarily render a
      consumer outside its Provider.
- [ ] Both Providers wrap `<App/>` in `main.jsx`.

## 🛠 Your turn

1. Add a `TOGGLE` action to the shortlist reducer that adds a course if absent and
   removes it if present, then have `CourseCard` dispatch that single action
   instead of choosing between `addItem` and `removeItem`.
2. Add a `system` option to the theme (follow the OS setting via
   `window.matchMedia('(prefers-color-scheme: dark)')`). Notice this is real logic
   that would bloat the toggle — a hint that the theme, too, might one day deserve a
   reducer.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| "useCart must be used inside <CartProvider>" | A consumer renders outside the Provider, or the Provider is nested below it. | Move `<CartProvider>` up so it wraps `<App/>` in `main.jsx`. |
| Every component re-renders on any change | The Provider's `value` is an inline object, new every render. | Wrap it in `useMemo([...deps])`. |
| `Cannot read properties of null (reading 'items')` | No guard in the hook and the Provider is missing. | Add the `if (!ctx) throw` guard; add the Provider. |
| The shortlist "resets" unexpectedly | The reducer mutated state (`state.push`) instead of returning new state. | Return a new array from every case; never mutate. |
| Theme toggles but the page doesn't change | The effect didn't set `document.documentElement.dataset.theme`, or the CSS var block is missing. | Set the attribute in the effect; confirm `:root[data-theme='dark']` in `index.css`. |
| "Unknown cart action" thrown | A typo'd `action.type`, or a component dispatches a string, not `{ type }`. | Dispatch `{ type: 'ADD', course }`; match the case strings exactly. |

---
### ✅ Cook & Bake Academy after this lab
Theme and shortlist live in Context — dark mode works everywhere and the shortlist runs through a reducer instead of prop-drilling.
