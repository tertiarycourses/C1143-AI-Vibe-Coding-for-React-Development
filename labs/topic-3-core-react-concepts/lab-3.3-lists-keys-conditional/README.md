# Lab 3.3 — Lists, Keys and Conditional Rendering

> **Topic 3** · ~50 min · Builds on Lab 3.2

### 📖 The build so far
By the end of the last lab, Cook & Bake Academy rendered six hand-written `CourseCard` elements. **In this lab you add:** data-driven rendering — you replace them with `courses.map(course => <CourseCard key={course.id} course={course} />)` over the full 20-course catalogue in `src/data/courses.js`, add conditional badges and a "Free" price branch, and give the grid an empty state. By the end you'll have a catalogue that grows and shrinks with its data — the exact behaviour the search and filter in Lab 3.4 rely on.

## What you will build

You will delete the six hand-written `<CourseCard>` elements and render the whole
catalogue from data instead: `courses.map(course => <CourseCard key={course.id}
course={course} />)`. All 20 real courses appear. Then you will make each card react to its
own data — an "Advanced · book early" badge, a "Free"/`S$` price branch, a pluralised
"weeks" — and give the grid an empty state for when there are no courses. Along the way you
will meet the single most-misunderstood prop in React: `key`.

## Concepts you will meet

| Concept | In one line |
|---|---|
| Rendering a list | Turn an array of data into an array of elements with `.map()` |
| `key` | A stable per-item identity React uses to match old and new elements |
| The index-key bug | Using the array index as `key` corrupts state on reorder/delete |
| Conditional `&&` | `cond && <X />` renders `<X />` only when `cond` is true |
| Ternary in JSX | `cond ? <A /> : <B />` picks one of two things to render |
| Early return | `if (empty) return <Empty />` before the main JSX |
| The `0 &&` footgun | `count && <X />` renders a literal `0` when `count` is `0` |
| Derived value | Compute flags like `isAdvanced` in the body; don't store them |

## Before you start

Continue from Lab 3.2. Copy this lab's snapshot over `src/`:

```bash
cp -R labs/topic-3-core-react-concepts/lab-3.3-lists-keys-conditional/src/. cookbake/src/
```

This replaces `src/App.jsx`, `src/components/CourseGrid.jsx` and
`src/components/CourseCard.jsx`, and adds `src/components/KeyBugDemo.jsx`. It imports the
shared catalogue from `src/data/courses.js` (which **already exists** in `cookbake` — do not
recreate it). Run `npm run dev` — you should now see all 20 courses.

---

## Step 1 — Move the data into `App` and pass it down

`App.jsx` now imports the array and hands it to the grid as a prop:

```jsx
import { courses } from './data/courses'
// ...
<CourseGrid courses={courses} />
```

This continues the one-way data flow from Lab 3.2: `App` owns the data, `CourseGrid`
receives it. `courses` is the same 20-object array the real app ships — and in Topic 5 the
same shape arrives from a Postgres table instead of a file.

## Step 2 — Replace six cards with one `.map()`

`CourseGrid` becomes tiny:

```jsx
export default function CourseGrid({ courses }) {
  if (courses.length === 0) {
    return <div className="card"><p className="muted">No courses to show yet.</p></div>
  }
  return (
    <div className="grid">
      {courses.map((course) => (
        <CourseCard key={course.id} course={course} />
      ))}
    </div>
  )
}
```

`.map()` turns the array of 20 course objects into an array of 20 `<CourseCard>` elements.
React renders arrays of elements natively — you just drop the array inside `{}`.

## Step 3 — Give every element a `key`

Notice `key={course.id}`. The `key` is not shown anywhere; it is a hint *to React*. Use the
data's own stable id. **Never** use the array index (`key={index}`) unless the list never
reorders, filters, or deletes — the "Why it works" section and `KeyBugDemo` show the exact
bug. And a searchable catalogue absolutely filters (Lab 3.4), so index keys are a latent bug
here.

## Step 4 — Make the card conditional on its data

Open `CourseCard.jsx`:

```jsx
const isBakery = category === 'Bakery'
const isAdvanced = level === 'Advanced'
// ...
<span className="card__tag">{isBakery ? '🧁 Bakery' : '🍳 Cooking'}</span>
{isAdvanced && <span className="badge">🔥 Advanced · book early</span>}
<span>🕒 {weeks} week{weeks > 1 ? 's' : ''}</span>
<span className="card__price">{fee === 0 ? 'Free' : `S$${fee}`}</span>
```

Three forms of conditional rendering: `&&` (show or nothing), ternary (one or the other),
and — in `CourseGrid` — early return for the empty case.

---

## 🎤 Vibe prompt

```text
In my Cook & Bake Academy app, replace the six hardcoded <CourseCard> elements in
src/components/CourseGrid.jsx with a data-driven list. CourseGrid should take a `courses`
prop and render courses.map(course => <CourseCard key={course.id} course={course} />)
inside <div className="grid">. Use course.id as the key, NOT the array index. If courses is
empty, return an empty-state card with a muted message instead.

Update src/App.jsx to `import { courses } from './data/courses'` and pass
<CourseGrid courses={courses} /> — all 20 courses.

In src/components/CourseCard.jsx (which imports { campuses, courseImage } from
'../data/courses') add conditional rendering:
- a category tag: category === 'Bakery' ? '🧁 Bakery' : '🍳 Cooking' (a ternary),
- an "Advanced · book early" badge with && ONLY when level === 'Advanced',
- "🕒 {weeks} week" with an "s" appended when weeks > 1,
- price: fee === 0 ? 'Free' : `S$${fee}` (use a ternary, not an if).

No TypeScript, 2-space indent, single quotes, no semicolons, reuse existing CSS classes
(.card .card__img .card__tag .card__lvl .card__body .card__meta .card__foot .card__price
.card__ask .badge .grid .muted).
```

## 🔍 Read what the AI wrote

- **Check the `key`.** The most common AI mistake here is `key={index}` (from
  `courses.map((course, index) => … key={index})`). It silences React's warning but plants
  the reorder/delete bug described below. Insist on `key={course.id}`.
- **Watch for the `0 &&` footgun.** This card guards with real booleans (`isAdvanced`,
  `weeks > 1`), so it is safe — but the moment an agent writes `{count && <p/>}` where
  `count` can be `0` (e.g. a future "{spotsLeft} spots left" line), a course with
  `spotsLeft === 0` renders a stray **0**. `&&` returns its left side when that side is
  falsy, and React renders the number `0` (it only skips `false`, `null`, and `undefined`).
  Always write `{spotsLeft > 0 && …}`.
- **Is the empty state an early return or buried in a ternary?** Either works, but an early
  `if (courses.length === 0) return …` is easier to read than a giant
  `courses.length === 0 ? <Empty/> : <div>…</div>`.
- **Did it keep `key` on the outermost mapped element?** `key` goes on the element returned
  by `.map()` (the `<CourseCard>`), not on some `<div>` inside `CourseCard`.
- **Free vs S$fee — did it use a ternary or an `if`?** You cannot put an `if` statement
  inside JSX. It must be an expression: `{fee === 0 ? 'Free' : `S$${fee}`}`.

## 🧠 Why it works

**Rendering a list is just mapping data to elements.** `courses.map(…)` produces an array
of `<CourseCard>` elements, and React knows how to render an array dropped inside `{}`.
There is no special "list component" — it is ordinary JavaScript `.map()` returning ordinary
JSX. This is why designing `CourseCard` to take a single `course` object (Lab 3.2) paid off:
the map body is a clean one-liner because each element needs exactly one thing.

**`key` exists so React can track identity across renders — it is not just "an id React
wants."** Remember from Lab 3.1 that on every render React builds a new virtual tree and
diffs it against the old one. For a *list*, it needs to answer a specific question: "is the
third card in the new list the *same* card as the third card in the old list, or a different
one that happens to sit in that slot?" `key` answers it. With `key={course.id}`, React
matches elements by their stable id no matter where they move. Without a good key — or with
`key={index}` — React matches by *position*, and position lies the moment the list changes.

Here is the concrete bug. Imagine a list `[A, B, C]` rendered with `key={index}`, so the
keys are `0, 1, 2`. Now you delete `A`. The new list is `[B, C]` with keys `0, 1`. React
compares by key: key `0` used to be `A` and is now `B`, key `1` used to be `B` and is now
`C`, and key `2` is gone. So React thinks "item 0's content changed from A to B, item 1's
changed from B to C, and item 2 was removed" — it *reuses* the first two DOM nodes and just
edits their text. That sounds harmless until a card holds internal state: a typed-in note, a
focused input, a "selected" highlight, a play/pause toggle. That state is keyed to the DOM
node, so after deleting `A`, `B` inherits `A`'s half-filled input, and `C` inherits `B`'s.
The data says one thing, the on-screen state says another. Now give every item a stable
`key={id}`: React sees that key `A` disappeared and keys `B` and `C` simply moved up, so it
removes `A`'s node and keeps `B` and `C` (state intact) exactly right. That is why the rule
is *stable identity from your data*, not the loop counter.

**When is `key={index}` actually acceptable?** When the list is static: it never reorders,
never filters, never inserts or deletes in the middle, and the items have no internal state.
A fixed list of footer links, for example. But the moment a list can change — and a
searchable catalogue absolutely can (Lab 3.4 filters it) — index keys are a latent bug.
Prefer the data's id every time.

**Conditional rendering** has three idioms, each for a different shape of decision.
`cond && <X />` means "render `<X />` or nothing" — but mind the footgun: `&&` evaluates to
its *left operand* when that operand is falsy, and React renders the numbers `0` (and `NaN`)
as visible text while skipping `false`/`null`/`undefined`. So `{spotsLeft && <p/>}` prints a
literal `0` when `spotsLeft` is `0`; writing `{spotsLeft > 0 && <p/>}` makes the left side a
real boolean and the problem vanishes. This card sidesteps the trap by guarding with real
booleans throughout (`isAdvanced`, `weeks > 1`). Use `cond ? <A /> : <B />` (a ternary, an
*expression*) when you must choose between two things — that is why `fee === 0 ? 'Free' :
`S$${fee}`` works but an `if` statement cannot sit inside JSX. And use an **early return** for
a whole-component branch, like `CourseGrid`'s empty state: handle the special case first and
let the rest of the function assume the normal case. All three are just JavaScript
expressions producing values that React renders.

**Conditionally *styling* an element** is the same trick aimed at an attribute instead of a
whole element. Often a card should not appear or disappear — it should just *look* different
based on its data. Because `className` takes a plain string, you build that string with a
template literal and a ternary:

```jsx
<article className={`card ${isAdvanced ? 'card--featured' : ''}`}>
```

The `card` class is always applied; the second slot resolves to `'card--featured'` when
`isAdvanced` is true and to an empty string otherwise. Inline styles work the same way but
take an *object*, so the ternary chooses a value rather than a class:
`style={{ opacity: fee === 0 ? 0.6 : 1 }}`. Keep the distinction clear: conditional
*rendering* (`{cond && <X/>}`) decides whether an element exists at all, while a conditional
`className` or `style` keeps the element and changes how it looks. You will use both
constantly, sometimes on the very same element.

## 🔬 See the bug live

Reading about the index-key bug is one thing; watching your own typing jump to the wrong row
is another. This lab's snapshot ships a self-contained component,
`src/components/KeyBugDemo.jsx`, that lets you trigger the bug on demand and toggle the fix.

**Drop it into `App` temporarily.** At the top of `src/App.jsx`:

```jsx
import KeyBugDemo from './components/KeyBugDemo'
```

and render it once, above your grid:

```jsx
<KeyBugDemo />
```

**Now reproduce the bug:**

1. The demo shows three course rows, each with a plain text box (an **uncontrolled** input —
   the DOM node owns the text, not React). Type a different note into each row, e.g.
   `first`, `second`, `third`.
2. Leave the toggle on **`key={index}` — broken** and press **Move first to last**. The row
   *labels* rotate, but your notes **stay put** — `first` is now sitting next to the wrong
   course.
3. Press the toggle to switch to **`key={item.id}` — correct**, retype your notes, and
   reorder again. This time the notes **travel with their row**.

**Why you see exactly that.** This is the reconciliation story from *Why it works* made
visible. The typed text lives on a real DOM `<input>` node, and `key` is the only thing that
tells React which node belongs to which item across a render. With `key={index}`, React
matches by *position*: after the rotation, position 0 is still key `0`, so React **reuses**
the same DOM node — including the text you typed — and just swaps the label text beside it.
The note is stranded because the node never moved, only the data around it did. With
`key={item.id}`, React sees that the item with id `a` moved from position 0 to position 2, so
it **moves that node** (input and all) to follow it. Same list, same reorder — the single
line `key={useIndexKey ? index : item.id}` is the whole difference.

When you're done exploring, delete the `import` and the `<KeyBugDemo />` line — it is a
teaching aid, not part of Cook & Bake Academy.

## ✅ Check your work

- [ ] `CourseGrid` renders via `.map()` with `key={course.id}` — no hardcoded cards remain.
- [ ] `App.jsx` imports `courses` from `./data/courses` and passes `courses={courses}`.
- [ ] All 20 courses appear, and the one Advanced course (Wedding Cake Design & Decoration)
      shows the "🔥 Advanced · book early" badge; no other card does.
- [ ] Each card shows `S$` + fee (none of the seed courses are free — you test that in
      "Your turn").
- [ ] Temporarily pass `courses={[]}` and confirm the empty-state card appears.
- [ ] No stray `0` appears on any card, and the browser console shows **no** key warning.

## 🛠 Your turn

1. In `data/courses.js` (your local copy), set one course's `fee` to `0`. Confirm you see
   **Free** on that card instead of `S$0`.
2. Prove the index-key bug on the real grid. Temporarily change the map to `key={index}`
   (add `, index` to the map callback), give `CourseCard` a text `<input>`, type into the
   first card, then reverse the array (`[...courses].reverse()`) before mapping. Watch your
   typed text stick to the wrong card. Switch back to `key={course.id}` and see it follow the
   right one.
3. Add the `0 &&` footgun on purpose, then fix it. Give each course a `spotsLeft` number in
   your local data (set one to `0`), render `{spotsLeft && <p className="muted">{spotsLeft}
   spots left</p>}`, and watch the card with `0` print a bare **0**. Change it to
   `{spotsLeft > 0 && …}` and the 0 disappears.
4. Add a "Sort by fee" button in `App` that reorders the `courses` array before passing it
   down. With `key={course.id}` the cards rearrange cleanly.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| Console: `Each child in a list should have a unique "key" prop` | `.map()` without a `key` | Add `key={course.id}` to the element returned by `.map()` |
| A literal `0` shows on a card | Used `{count && …}` where `count` can be `0` | Guard with a boolean: `{count > 0 && …}` |
| Typed input / selection jumps to the wrong row after reordering | Used `key={index}` | Use a stable id: `key={course.id}` |
| `Unexpected token` near an `if` inside JSX | Tried to put an `if` statement in `{}` | Use a ternary expression, or an early `return` above the JSX |
| Every card is identical | Mapped but forgot to pass `course` (passed only `key`) | Pass both: `<CourseCard key={course.id} course={course} />` |
| `courses.map is not a function` | `courses` prop was undefined or not an array | Ensure `App` passes `courses={courses}` and the import path is `./data/courses` |
| `Cannot read properties of undefined (reading 'area')` | `campuses[campus]` — a course had a `campus` not in the map | Use `'Bakehouse'` or `'Culinary'` exactly; they are the two keys in `campuses` |
| A class won't apply conditionally | Tried to put an `if` inside `className={}` | Use a ternary in a template literal: `` className={`card ${on ? 'card--featured' : ''}`} `` |

---
### ✅ Cook & Bake Academy after this lab
The catalogue renders all 20 courses from the `courses` array with stable keys and conditional badges instead of hardcoded cards.
