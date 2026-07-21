# Lab 4.2 — Side effects with `useEffect`

> **Topic 4** · ~50 min · Builds on Lab 4.1 (the in-memory shortlist)

### 📖 The build so far
By the end of the last lab, Cook & Bake Academy's shortlist lived only in memory and vanished on refresh. **In this lab you add:** side effects with `useEffect` — the shortlist persists to `localStorage`, the document title reflects the shortlist count, and a class-intake countdown ticks down. By the end you'll have a shortlist that survives a page reload.

## What you will build

You will make the shortlist *persist* and give the site two live, self-updating
touches. Three concrete effects: (a) the browser tab title tracks the shortlist
count, (b) the shortlist is saved to `localStorage` and restored on reload so a
refresh no longer empties it, and (c) a "Next sourdough intake starts in HH:MM:SS"
countdown that ticks every second and — crucially — cleans up its timer. Along the
way you will meet the single most misused hook in React and learn when *not* to
reach for it.

## Concepts you will meet

| Concept | In one line |
|---|---|
| Side effect | Anything that reaches outside React to touch the world: the DOM title, storage, timers, network. |
| `useEffect` | Runs a function *after* render, so effects don't block painting. |
| Dependency array | Controls *when* the effect re-runs: omitted / `[]` / `[deps]`. |
| Cleanup function | The function you `return` from an effect; React runs it before the next effect and on unmount. |
| StrictMode double-invoke | In dev, React mounts→unmounts→remounts each component to surface missing cleanup. |
| Derived-state anti-pattern | Using `useEffect` to compute a value you could compute during render — avoid it. |

## Before you start

You need your finished Lab 4.1 app (shortlist in `App`). Then copy this lab's files:

```bash
cp -R labs/topic-4-react-hooks/lab-4.2-useeffect/src/. cookbake/src/
npm run dev
```

This overwrites `App.jsx` and `CartSummary.jsx` and adds a new `Countdown.jsx`.
`CourseCard.jsx` and `CourseGrid.jsx` from Lab 4.1 are unchanged.

---

## Step 1 — Sync the tab title to the shortlist (effect with `[items]`)

In `App.jsx`, add:

```jsx
useEffect(() => {
  document.title = items.length
    ? `Cook & Bake (${items.length})`
    : 'Cook & Bake Academy'
}, [items])
```

`document.title` is not a React thing — it belongs to the browser. Reaching out to
set it is a *side effect*, and side effects belong in `useEffect`, not in the body
of your component. The `[items]` dependency array means "re-run this only when
`items` changes." Shortlist a course and watch the tab title update.

## Step 2 — Persist and restore the shortlist (lazy init + effect)

Give the shortlist a **lazy initial value** that reads from storage once, and an
effect that writes on every change:

```jsx
const [items, setItems] = useState(() => {
  const saved = localStorage.getItem('cart')
  return saved ? JSON.parse(saved) : []
})

useEffect(() => {
  localStorage.setItem('cart', JSON.stringify(items))
}, [items])
```

The arrow function in `useState(() => …)` is the lazy form you previewed in Lab
4.1: it runs only on the first render, so you read storage exactly once. The effect
is the write side. Shortlist a course, **refresh the page** — it is still there.

## Step 3 — A countdown that cleans up (effect with a timer)

Open the new `Countdown.jsx`. It starts a `setInterval` and — this is the whole
lesson — **returns a cleanup function** that clears it:

```jsx
useEffect(() => {
  const id = setInterval(() => setRemaining(deadline - Date.now()), 1000)
  return () => clearInterval(id)
}, [deadline])
```

`CartSummary` renders `<Countdown hours={72} />` at the bottom of the shortlist
panel — "⏳ Next sourdough intake starts in …". Watch it tick down once per second.

---

## 🎤 Vibe prompt

```text
In my React 19 + Vite Cook & Bake Academy app, add three side effects with
useEffect.
1) In App.jsx, sync document.title to the shortlist count: "Cook & Bake (n)" when
   the shortlist has items, "Cook & Bake Academy" when empty. Dependency array
   [items].
2) Persist the shortlist to localStorage under the key "cart". Restore it using
   LAZY initial state: useState(() => JSON.parse(localStorage...) ?? []). Add an
   effect with [items] that writes it back on change.
3) Create Countdown.jsx: a component that counts down to a deadline 72 hours from
   mount and shows HH:MM:SS ("Next sourdough intake starts in …"), updating every
   second with setInterval. It MUST return a cleanup function that clears the
   interval. Render it inside CartSummary using the .muted class.
Do NOT use useEffect to compute the shortlist total — keep deriving that during
render.
```

## 🔍 Read what the AI wrote

- **Is there a cleanup?** The countdown's effect **must** `return () =>
  clearInterval(id)`. AI agents forget this constantly. Without it, every re-run
  stacks another interval and the number starts jumping by 2, 3, 4… per second.
- **Right dependency array?** For the title and storage effects, `[items]` is
  correct. An **empty** `[]` there would run once and never update. **No** array
  at all would run after *every* render — wasteful, and for the storage write,
  harmless but pointless.
- **Lazy init, not eager.** Check the shortlist's initial state is `useState(() =>
  …)`, not `useState(JSON.parse(localStorage.getItem(...)))`. The eager version
  re-reads and re-parses storage on every render.
- **Did it "effect" the total?** If the agent added `useEffect(() =>
  setTotal(...), [items])`, reject it. The total is derived data — compute it in
  the render body. This is the number-one thing AI gets wrong with `useEffect`.
- **JSON round-trips.** Confirm it `JSON.stringify`s on write and `JSON.parse`s on
  read. Storing an array without stringifying saves the literal string
  `"[object Object]"`.

## 🧠 Why it works

React's job is to turn your state into a description of the UI. That description is
*pure*: given the same state, it produces the same output, and it should not touch
anything outside itself while rendering. But real apps must touch the outside
world — set the document title, read storage, start a timer, later fetch from a
server. Those are **side effects**, and `useEffect` is where they belong.

The mechanism is: React renders your component (builds the UI description and
paints it), and *then*, after the paint, runs your effects. Running effects after
paint is deliberate — it keeps side effects from blocking the screen from updating.
So the flow is always **render → commit to the DOM → run effects**.

It helps to name the three moments in a component's life that effects hook into: **mount** (it is
added to the screen for the first time), **update** (it re-renders because its state or props
changed), and **unmount** (it is removed). Older React expressed these as separate class methods —
`componentDidMount`, `componentDidUpdate`, `componentWillUnmount` — and you will still meet that
vocabulary in articles and in AI-generated code. `useEffect` folds all three into one API, and the
dependency array is how you choose which moments an effect cares about: `[]` runs on **mount** only;
`[items]` runs on mount *and* on every **update** where `items` changed; and the function you `return`
runs on **unmount** (and just before each re-run). So the countdown's `[deadline]` effect starts its
timer on mount and its returned `clearInterval` stops it on unmount — one hook expressing that
component's whole lifecycle. Reading an effect as *"which lifecycle moments does this dependency array
subscribe to?"* is the fastest way to tell at a glance whether it will run when you expect.

The **dependency array** is how you control *when* an effect re-runs, and it has
exactly three meaningful forms:

- **Omit it** — `useEffect(fn)` — and the effect runs after *every* render. Rarely
  what you want.
- **Empty `[]`** — the effect runs *once*, after the first render, and never
  again. Use it for one-time setup (a subscription, a "on mount" action).
- **`[a, b]`** — the effect re-runs whenever any listed value changes between
  renders. This is the common case. React compares each dependency to its previous
  value; if any differ, it runs the cleanup (if any) and then the effect again.

The **cleanup function** is the half beginners skip and the half that matters most.
When you `return` a function from an effect, React runs it in two situations:
*before it runs the effect again* (to undo the previous run), and *when the
component unmounts* (to undo the last run). A `setInterval` with no cleanup is a
classic leak: each time the effect runs it starts a fresh interval, but the old
ones are still firing — you now have several timers racing. `return () =>
clearInterval(id)` guarantees each timer is stopped before the next one starts and
when the component goes away. The mental rule: **if an effect *starts* something —
a timer, a subscription, an event listener — it must *stop* that same thing in its
cleanup.**

Which brings us to **StrictMode**. In development, React deliberately mounts each
component, immediately unmounts it, then mounts it again — so every effect runs
*twice* on first load, with a cleanup in between. This is not a bug; it is a
smoke-detector. If your countdown ends up with two intervals after that
double-mount, you know your cleanup is missing or wrong — in *development*, where
it is cheap to notice, rather than in production, where the leak is silent. Code
that survives StrictMode's double-invoke is code whose effects are correctly
paired with cleanups. (StrictMode only does this in dev; production mounts once.)

Finally, the **anti-pattern**, because it is the thing AI coding agents produce
more than any other `useEffect` mistake. It is tempting to write:

```jsx
// ❌ Don't do this.
const [total, setTotal] = useState(0)
useEffect(() => {
  setTotal(items.reduce(...))
}, [items])
```

This is wrong. It stores a value in state that is fully determined by *other*
state, then uses an effect to keep the two in sync. The result is an extra render
(state → effect → setState → render again), a moment where `total` is stale, and a
whole class of "why is my derived value one step behind?" bugs. If a value can be
computed from the state you already have, **compute it during render**:

```jsx
// ✅ Do this.
const total = items.reduce((sum, c) => sum + Number(c.fee), 0)
```

No effect, no extra state, never stale. The rule of thumb: reach for `useEffect`
only when you need to *synchronise with something outside React* — the DOM,
storage, a timer, the network. If you are only transforming state you already have
into other data for the screen, that is a render-time calculation, not an effect.

## ✅ Check your work

- [ ] The browser tab title shows `Cook & Bake (n)` and updates as you add/remove.
- [ ] Shortlist a course, refresh the page — it survives (it is in `localStorage`).
- [ ] The countdown ticks down smoothly by exactly one second at a time.
- [ ] In DevTools → Application → Local Storage you can see the `cart` key.
- [ ] There is no `useState` for the shortlist total anywhere; it is derived in render.

## 🛠 Your turn

1. Open DevTools and confirm the countdown really cleans up: temporarily **delete**
   the `return () => clearInterval(id)` line and watch the timer start skipping
   seconds after a hot reload (React re-runs the effect without cleaning up). Put
   the line back.
2. Add a `localStorage` persistence for the selected **category** filter too, so a
   refresh keeps the user on the same category. Reuse the same lazy-init +
   `[category]` effect pattern. (In Lab 4.5 you will factor this repetition into a
   `useLocalStorage` hook.)

## Common errors

| Error | Cause | Fix |
|---|---|---|
| Countdown jumps by 2+ seconds after a save/reload | The interval effect has no cleanup, so intervals stack up. | `return () => clearInterval(id)` from the effect. |
| Shortlist is empty after every refresh | You read storage but never wrote it, or wrote without `JSON.stringify`. | Add the `[items]` effect that `setItem`s the stringified array. |
| `localStorage` shows `"[object Object]"` | You stored the array without `JSON.stringify`. | Stringify on write, `JSON.parse` on read. |
| Tab title never changes | Empty `[]` dependency array on the title effect. | Use `[items]` so it re-runs when the shortlist changes. |
| Total is one click behind | You synced it into state with an effect. | Delete the state + effect; derive the total during render. |
| "Maximum update depth exceeded" | An effect calls `setState` with a dependency that the `setState` itself changes. | Remove the derived-state effect; compute during render instead. |

---
### ✅ Cook & Bake Academy after this lab
The shortlist persists across reloads via `localStorage`, and the tab title and a countdown stay in sync with state.
