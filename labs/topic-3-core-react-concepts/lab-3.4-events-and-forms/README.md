# Lab 3.4 — Events and Forms

> **Topic 3** · ~55 min · Builds on Lab 3.3

### 📖 The build so far
By the end of the last lab, Cook & Bake Academy rendered all 20 courses from data. **In this lab you add:** interactivity — a controlled search box and the All / 🧁 Bakery / 🍳 Cooking filter chips that narrow the grid live as the user types and clicks. You introduce `useState` for the first time in earnest and learn the rule that trips up almost every AI agent: the filtered list is **derived data**, computed during render, and must **not** be stored in its own state. By the end you'll have the searchable, filterable catalogue from the real app.

## What you will build

You will make the catalogue interactive: the real `SearchBar` that filters courses as you
type, and the real `CategoryFilter` chips (All / 🧁 Bakery / 🍳 Cooking) that filter by
category. `App` owns two pieces of state — `query` and `category` — and computes the visible
list from them. You will build the exact `<SearchBar value onChange inputRef/>` and
`<CategoryFilter value onChange/>` the finished app uses.

## Concepts you will meet

| Concept | In one line |
|---|---|
| Synthetic events | React's cross-browser wrapper over native DOM events |
| `onClick` / `onChange` | Event handler props you attach in JSX |
| Passing arguments | Wrap in an arrow: `onClick={() => onChange(cat.value)}` |
| Controlled input | `value` + `onChange` make React the source of truth for an input |
| `useState` | The hook that gives a component a piece of remembered state |
| Lifting state up | State lives in the common parent (`App`); children get value + a setter |
| `e.preventDefault()` | Stop a real `<form>`'s default full-page reload on submit |
| Derived state | Data you can compute from existing state — so you must NOT store it |

## Before you start

Continue from Lab 3.3. Copy this lab's snapshot over `src/`:

```bash
cp -R labs/topic-3-core-react-concepts/lab-3.4-events-and-forms/src/. cookbake/src/
```

This replaces `src/App.jsx` and `src/components/CourseGrid.jsx`, and adds
`src/components/SearchBar.jsx` and `src/components/CategoryFilter.jsx`. `CategoryFilter`
imports the `categories` array from `src/data/courses.js` (already exists). Run
`npm run dev`.

---

## Step 1 — Give `App` two pieces of state

```jsx
const [query, setQuery] = useState('')
const [category, setCategory] = useState('All')
```

`useState('')` hands back the current value and a setter. Calling the setter
(`setQuery('sourdough')`) tells React the value changed, and React re-renders `App`. This is
the `useState` you previewed in Lab 3.1 — Topic 4 goes deep on how it actually works. Here,
treat it as: *a value React remembers between renders, plus a function to change it.* The
state lives in `App` because `App` is the common parent of both the inputs and the grid —
that is **lifting state up**.

## Step 2 — Derive the visible list during render

```jsx
const visible = courses.filter((course) => {
  const matchesCategory = category === 'All' || course.category === category
  const matchesQuery = course.title.toLowerCase().includes(query.trim().toLowerCase())
  return matchesCategory && matchesQuery
})
```

`visible` is a plain `const`, recomputed every render from `courses`, `query` and
`category`. It is **not** state. Then pass it down: `<CourseGrid courses={visible} />`. The
`category` values (`'All'`, `'Bakery'`, `'Cooking'`) match the `value` field of each
category chip and the `category` field on every course.

## Step 3 — Build the controlled `SearchBar`

```jsx
export default function SearchBar({ value, onChange, inputRef }) {
  return (
    <div className="search">
      <span className="search__icon" aria-hidden="true">🔎</span>
      <input
        ref={inputRef}
        type="search"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        aria-label="Search courses"
      />
    </div>
  )
}
```

`value={value}` binds the input to React state; `onChange` reports every keystroke up to the
parent. That pair is what makes the input **controlled**. `inputRef` is passed straight
through and unused for now — Topic 4 will hand in a `useRef` so the box can focus itself on
load.

## Step 4 — Build `CategoryFilter` and wire the handlers

```jsx
import { categories } from '../data/courses'

export default function CategoryFilter({ value, onChange }) {
  return (
    <div className="filters">
      {categories.map((cat) => (
        <button
          key={cat.value}
          className={cat.value === value ? 'chip is-active' : 'chip'}
          onClick={() => onChange(cat.value)}
        >
          {cat.label}
        </button>
      ))}
    </div>
  )
}
```

`onClick={() => onChange(cat.value)}` passes an argument by wrapping the call in an arrow. In
`App`, `onChange` is `setCategory`, so clicking a chip sets the category and the list
re-filters. The active chip gets `chip is-active`; the rest get `chip`.

---

## 🎤 Vibe prompt

```text
Add search and category filtering to my Cook & Bake Academy catalogue.

In src/App.jsx: add two useState hooks — query (''), and category ('All'). Import
{ courses } from './data/courses'. Compute a derived array `visible` by filtering courses
where the category matches (or category === 'All') AND the lowercased title includes the
lowercased trimmed query. Render <SearchBar value={query} onChange={setQuery} /> and
<CategoryFilter value={category} onChange={setCategory} /> inside a <div className="toolbar">,
then <CourseGrid courses={visible} />.

Create src/components/SearchBar.jsx: props { value, onChange, inputRef }. A <div
className="search"> with a search icon and a controlled <input type="search"> that has
ref={inputRef}, value={value}, and onChange={(e) => onChange(e.target.value)}.

Create src/components/CategoryFilter.jsx: import { categories } from '../data/courses'; props
{ value, onChange }. Map categories to <button className="chip"> (the selected one adds
is-active); onClick calls onChange(cat.value); the button text is cat.label.

IMPORTANT: `visible` must be a plain const computed during render. Do NOT store the filtered
list in useState and do NOT sync it with useEffect.

No TypeScript, 2-space indent, single quotes, no semicolons, reuse existing CSS classes
(.toolbar .search .search__icon .filters .chip .grid .muted).
```

## 🔍 Read what the AI wrote

- **The big one: did it store derived state?** Watch for the agent adding
  `const [visible, setVisible] = useState([])` plus a `useEffect(() => setVisible(…),
  [query, category])`. That is the anti-pattern this lab exists to kill. The filtered list
  must be a plain `const` computed in the render body — no extra state, no effect.
- **Is the input controlled?** It needs **both** `value={query}` and `onChange`. With only
  `onChange`, it is uncontrolled and React does not own the value. With `value` but no
  `onChange`, React locks the input read-only and warns in the console.
- **Did it call the handler instead of passing it?** `onClick={onChange(cat.value)}` runs
  `onChange` *during render*, on every render — an immediate-fire / infinite-loop bug. It
  must be `onClick={() => onChange(cat.value)}` (a function React calls later, on click).
- **Did it filter by `cat.label` instead of `cat.value`?** The chips carry `label`
  (`'🧁 Bakery'`) for display and `value` (`'Bakery'`) for logic. The filter must compare
  `course.category` against the **value**, and the active chip against the **value**.
- **Do the chips have a `key`?** They are produced by `.map()`, so each needs
  `key={cat.value}` (the values are unique — a fine key here).

## 🧠 Why it works

**React events are declarative too.** Instead of `element.addEventListener('click', …)`, you
attach a handler as a prop in JSX: `onClick={handleClick}`. React wires up a single listener
at the root and dispatches a **synthetic event** — a lightweight, cross-browser wrapper
around the native event with the same API (`e.target`, `e.preventDefault()`). You almost
never think about the wrapper; you just get consistent behaviour across browsers. Two details
matter. First, you pass the *function itself*, not its result:
`onChange={(e) => onChange(e.target.value)}`. Writing `onChange={onChange()}` calls it
immediately during render — a classic bug. Second, to pass an argument you wrap the call in
an arrow function that captures it: `onClick={() => onChange(cat.value)}`.

**Controlled inputs put React in charge of form state.** An `<input>` can hold its own value
in the DOM (uncontrolled), or it can be told its value by React (controlled). You make it
controlled by giving it both `value={query}` and `onChange={(e) => setQuery(e.target.value)}`.
Now the flow on each keystroke is: you type → `onChange` fires → `setQuery` updates state →
`App` re-renders → the input receives its new `value` from state. The DOM input never holds
the truth on its own; React state does, and the input is just a view of it. That is what
"controlled" means and why the two attributes always travel together. It is also what lets
`App` *use* the query to filter — the value lives in state, where the rest of the component
can read it. And because both the search box and the grid read from state that lives in their
common parent `App`, they stay in sync automatically: that is **lifting state up**.

**`e.preventDefault()` and real forms.** The `SearchBar` is a bare `<input>`, not a
`<form>`, so pressing Enter does nothing special. But the moment you build a real
`<form>` — the sign-in form (`AuthForm`) or the `ReviewForm` you meet in Topic 5 — the
browser's default is to *submit and reload the whole page*, which throws away all your React
state. You stop it with `onSubmit={(e) => e.preventDefault()}`, then handle the submit in
JavaScript. Keep that reflex ready; every form in this app uses it.

**One state object for a whole form.** The search box needs a single `useState`, but a real
form — the sign-up in `AuthForm`, or the review editor in `ReviewForm` — has many fields, and
one `useState` per field gets noisy fast. The tidier pattern is a single object in state and
one handler for every input:

```jsx
const [form, setForm] = useState({ email: '', name: '', password: '' })

function handleChange(e) {
  setForm((prev) => ({ ...prev, [e.target.name]: e.target.value }))
}
```

Each input carries a `name` that matches a key in the object and shares the one handler:
`<input name="email" value={form.email} onChange={handleChange} />`. Two details make it
work. The `[e.target.name]` is a **computed property key** — the square brackets tell
JavaScript "use the *value* of `e.target.name` as the key," so a change on the `email` input
writes to `form.email` and a change on the `password` input writes to `form.password`, all
through one function. And the `...prev` spread is not optional: a state update *replaces* the
object rather than merging into it, so without copying the existing fields first you would
wipe every field except the one that just changed. This keeps a many-field form down to one
piece of state and one handler — and on submit, `form` is already the shaped object you send
off (in Topic 5, straight to `api.post('/auth/signup', form)`).

**Now the lesson this whole lab is built around: derived state must not be stored.**
`visible` is *entirely determined* by three things you already have — the full `courses`
array and the two state values `query` and `category`. Anything you can compute from existing
state or props is **derived data**, and the rule is: *if you can calculate it during render,
calculate it during render.* So `visible` is a plain `const`:

```jsx
const visible = courses.filter(/* uses query + category */)
```

It is recomputed on every render, which means it is *always* correct and *always* in sync,
because it is never stored anywhere that could go stale. Compare that to what AI agents reach
for constantly — a second copy in state that they try to keep updated with an effect:

```jsx
// ❌ The anti-pattern. Do not do this.
const [visible, setVisible] = useState(courses)
useEffect(() => {
  setVisible(courses.filter(/* … */))
}, [query, category])
```

This is worse in every way. It creates a *second source of truth* that can disagree with the
first. It renders once with a **stale** list before the effect runs and re-renders it (a
visible flicker). It adds a dependency array you must maintain perfectly or it silently
desyncs. And it doubles the renders. The plain `const` has none of these problems — it cannot
be stale because it does not persist. Learn to spot this: whenever an agent pairs a `useState`
with a `useEffect` whose only job is to `setState` from other state or props, it has almost
certainly created derived state that should just be a variable. Reserve state for genuine
*inputs* the user changes (`query`, `category`); compute everything downstream.

Notice how cleanly this composes with the earlier labs. `App` owns two small bits of state
and passes data *down* (`courses={visible}`) and event handlers *down* (`onChange`); the
children send changes *up* by calling those handlers. Data down, events up — the exact
one-way-data-flow shape from Lab 3.2, now with interactivity added.

## ✅ Check your work

- [ ] Typing in the search box filters the cards live; clearing it restores all 20.
- [ ] Clicking a chip filters to that category; **All** shows everything.
- [ ] Search and category work **together** (e.g. "bread" + 🧁 Bakery narrows further).
- [ ] Searching for nonsense (e.g. "zzz") shows the empty-state message from Lab 3.3.
- [ ] `App.jsx` computes `visible` as a plain `const` — there is **no** `useState` holding the
      filtered list and **no** `useEffect` in the file.
- [ ] The selected chip shows `chip is-active` and looks different from the others.

## 🛠 Your turn

1. Add a live result count next to the section title: `{visible.length} of
   {courses.length} courses`. It is derived data too — just render `visible.length`, do not
   store it.
2. Make search match the summary as well as the title (`course.summary` too). One line in
   the filter; no new state.
3. Add a "Clear filters" button that calls both `setQuery('')` and `setCategory('All')`. Show
   it only when a filter is active: `{(query || category !== 'All') && <button/>}`.
4. Sort the visible list by `fee` with a toggle. Sorting is also derived — chain
   `.filter(…).sort(…)` in the render body; do not add a state array.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| The list flickers or shows stale results | Stored `visible` in `useState` and synced it with `useEffect` | Delete the state + effect; make `visible` a plain `const` computed in render |
| `Warning: You provided a 'value' prop … without an 'onChange' handler` | Controlled `value` but no `onChange` | Add `onChange={(e) => onChange(e.target.value)}` |
| Typing does nothing / input feels frozen | `value` is bound but `onChange` does not update the state it reads from | Ensure `onChange` calls the setter that feeds `value` |
| Clicking a chip does nothing / fires on load | Wrote `onClick={onChange(cat.value)}` (called it) | Wrap it: `onClick={() => onChange(cat.value)}` |
| The filter never matches | Compared `course.category` against `cat.label` (`'🧁 Bakery'`) | Compare against `cat.value` (`'Bakery'`) |
| `Too many re-renders` | Called a setter directly in the render body (not inside a handler) | Only call setters from event handlers or effects, never during render |
| Chips warn about missing `key` | `.map()` without a key | Add `key={cat.value}` to each button |
| Typing in one field of an object-form clears the others | Set state without spreading the previous object | `setForm(prev => ({ ...prev, [e.target.name]: e.target.value }))` |

---
### ✅ Cook & Bake Academy after this lab
Users can narrow all 20 courses with a live search box and the Bakery/Cooking filter chips — the searchable catalogue from the real app.
