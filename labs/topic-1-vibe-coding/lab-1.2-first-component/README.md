# Lab 1.2 — Vibe-Code Your First Component

> **Topic 1** · ~45 min · Builds on Lab 1.1

### 📖 The build so far
By the end of the last lab, Cook & Bake was a running Vite dev server showing a single heading. **In this lab you add:** your first real React component — a `CourseCard` that displays one course's emoji, category, level, price and duration. By the end you'll have one hand-built card rendering on the page.

## What you will build

Your first real React component: a `CourseCard` that displays one course from the
Cook & Bake catalogue — its emoji, a 🧁 Bakery / 🍳 Cooking tag, the level, title,
summary, price and duration — styled with the design classes already in
`index.css`. You will then render that card from `App.jsx`. One card, one course
object, done properly.

## Concepts you will meet

| Concept | In one line |
|---|---|
| Component | A JavaScript function that returns JSX (a chunk of UI). |
| JSX | HTML-like syntax you write inside JavaScript; it compiles to function calls. |
| `className` | JSX's name for the HTML `class` attribute (`class` is a reserved word in JS). |
| Single root element | Everything a component returns must sit under exactly one parent tag. |
| `{ }` in JSX | Curly braces drop a JavaScript **expression** into the markup. |
| Props | The inputs to a component — passed like HTML attributes, received as a function argument. |
| The `course` object prop | The whole card is driven by ONE prop, an object with the same shape as a catalogue row. |

## Before you start

You need the running `cookbake` app from Lab 1.1. Confirm `npm run dev` still
serves it. This lab adds two files. Copy this lab's `src/` over your app's `src/`:

```bash
# from the cookbake/ folder
cp -R ../labs/topic-1-vibe-coding/lab-1.2-first-component/src/. src/
```

(Adjust the path to wherever you keep the `labs/` folder.) This creates
`src/components/CourseCard.jsx` and replaces `src/App.jsx`. It does **not** touch
`src/index.css` — you keep the shared styles from the course.

---

## Step 1 — Create the component file

Make a `src/components/` folder and add `CourseCard.jsx` inside it. Grouping
components in their own folder keeps `src/` tidy as the app grows — it is exactly
where the finished app keeps `Navbar.jsx`, `Hero.jsx`, `CourseCard.jsx` and the
rest.

## Step 2 — Write the component

`CourseCard` takes **one prop** — a `course` object — and returns JSX. It reuses
the shared `.card`, `.card__body`, `.card__tag`, `.card__price` and `.card__meta`
classes so it looks right without any new CSS:

```jsx
export default function CourseCard({ course }) {
  const { title, category, level, weeks, fee, campus, emoji, summary } = course
  const isBakery = category === 'Bakery'

  return (
    <article className="card">
      <div
        className="card__img"
        style={{
          display: 'grid',
          placeItems: 'center',
          fontSize: '3.5rem',
          background: 'var(--brand-soft)',
        }}
      >
        <span className="card__tag">{isBakery ? '🧁 Bakery' : '🍳 Cooking'}</span>
        <span className="card__lvl">{level}</span>
        {emoji}
      </div>

      <div className="card__body">
        <h3>{title}</h3>
        <p className="muted small">{summary}</p>

        <div className="card__meta">
          <span>🕒 {weeks} week{weeks > 1 ? 's' : ''}</span>
          <span>📍 {campus}</span>
        </div>

        <div className="card__foot">
          <span className="card__price">S${fee}</span>
          <span className="card__ask">View &amp; enrol →</span>
        </div>
      </div>
    </article>
  )
}
```

> The real app puts a course **photo** in `.card__img`. We don't have the data
> file (with its image ids) until Topic 3, so for now the course emoji stands in
> for the photo. The rest of the markup is the finished card, trimmed.

## Step 3 — Render it from App.jsx

A component that nobody uses shows nothing. In `App.jsx`, import `CourseCard`,
write one `course` object, and pass it as a single prop:

```jsx
import CourseCard from './components/CourseCard'

const sourdough = {
  code: 'BAK-101',
  slug: 'artisan-sourdough-bread-baking',
  title: 'Artisan Sourdough Bread Baking',
  category: 'Bakery',
  level: 'Beginner',
  weeks: 4,
  fee: 680,
  campus: 'Bakehouse',
  emoji: '🍞',
  summary:
    'Grow your own starter, master hydration and bake a crackling open crumb loaf.',
}

export default function App() {
  return (
    <div className="grid">
      <CourseCard course={sourdough} />
    </div>
  )
}
```

Save and check the browser — one styled course card appears.

---

## 🎤 Vibe prompt

Instead of typing the component yourself, let the agent draft it. Paste this into
Claude Code (or Cursor / Copilot) from inside the `cookbake` folder:

```text
Create a React component at src/components/CourseCard.jsx for the Cook & Bake
Academy app.

- It is a function component with a default export.
- It receives a SINGLE prop named `course` — an object with these fields:
  code, slug, title, category ('Bakery' | 'Cooking'), level, weeks, fee,
  campus, emoji, summary. Destructure the fields you need off `course` on the
  first line. Do NOT accept a flat list of separate props.
- Return one root <article className="card"> and use ONLY existing CSS classes
  from index.css: card, card__img, card__tag, card__lvl, card__body, card__meta,
  card__foot, card__price, card__ask, muted, small. Do not invent classes and do
  not add a stylesheet. Do NOT import react-router — there is no routing yet.
- Show: the emoji large inside .card__img, a .card__tag reading "🧁 Bakery" when
  category is 'Bakery' otherwise "🍳 Cooking", the level in .card__lvl, the title
  as an <h3>, the summary, a .card__meta line with "🕒 {weeks} week(s)" (singular
  when weeks === 1) and "📍 {campus}", and a .card__foot with "S${fee}" in
  .card__price.

Then update src/App.jsx to import CourseCard and render ONE card for the
Artisan Sourdough Bread Baking course (code BAK-101, category Bakery, level
Beginner, weeks 4, fee 680, campus Bakehouse, emoji 🍞) inside a <div className="grid">.

Do not use useState or any hook. Do not import a data file yet.
```

## 🔍 Read what the AI wrote

Do not accept the code just because the card renders. Check these specific things —
they are where agents slip up:

- **One `course` object, not a flat prop list.** Confirm the signature is
  `CourseCard({ course })` and the fields are destructured off `course` inside.
  If the agent wrote `CourseCard({ title, fee, … })` with nine separate props,
  correct it — the whole app passes courses as one object, and matching that shape
  now is what lets this card drop straight into Topic 3's `.map()` and Topic 5's
  database rows unchanged.
- **`className`, never `class`.** Every styling attribute must be `className`.
  If the agent wrote `class="card"`, React warns in the console and the class may
  not apply. This is the single most common JSX mistake.
- **Exactly one root element.** The `return` must wrap everything in one tag
  (here, `<article>`). Two sibling tags with no parent won't compile — a fragment
  `<>…</>` or a wrapping element is required.
- **No react-router yet.** If the agent wrapped the card in `<Link to=...>` and
  imported `react-router-dom`, remove it — that package isn't installed until
  Topic 6. For now the card is a plain `<article>`. (Topic 6 turns this exact
  `<article>` into a `<Link>` so the whole card becomes clickable.)
- **`S${fee}`, whole dollars.** Prices are Singapore dollars written `S$680`, not
  `$680`, `SGD 680` or `680.00`. Watch for the agent "helpfully" reformatting.
- **The week suffix is conditional.** `{weeks} week{weeks > 1 ? 's' : ''}` must
  read "1 week" but "4 weeks". An agent often hardcodes "weeks" and gets "1 weeks".
- **Only existing classes.** The agent should reuse the `.card*` classes from
  `index.css`. If it added a `<style>` block or a new `.css` file, delete it — the
  design system is already provided.

## 🧠 Why it works

**A component is just a function.** `CourseCard` is an ordinary JavaScript
function whose job is to return a description of some UI. React calls your
function, takes what it returns, and turns it into real DOM nodes. That is the
whole idea: your interface is built out of functions that return markup, and you
compose them like Lego. The name must start with a **capital letter** —
`CourseCard`, not `courseCard` — because React uses the capital to tell your
components apart from built-in HTML tags like `<article>`.

**JSX is HTML-flavoured JavaScript.** The stuff inside `return ( … )` looks like
HTML but it is not — it is JSX, which Vite compiles into plain function calls
before the browser sees it. Because it is really JavaScript, a few HTML habits
change:

- The attribute is `className`, not `class`, because `class` is a reserved word
  in JavaScript. Similarly `for` becomes `htmlFor`, and multi-word attributes are
  camelCase (`onClick`, `tabIndex`).
- A component must return a **single root element**. React needs one thing to
  render; if you want siblings with no wrapper, use an empty fragment `<>…</>`.
- To put a value into the markup, wrap a JavaScript **expression** in curly
  braces: `{title}`, `S${fee}`, `{weeks} week{weeks > 1 ? 's' : ''}`. Anything
  that produces a value works between `{ }` — a variable, a sum, a ternary, a
  function call. Statements like `if` or `for` do **not** go there; only
  expressions. That is why the singular/plural switch is written as a ternary.

**Props are the component's arguments — and here there is just one.** When you
write `<CourseCard course={sourdough} />`, React collects the attributes into a
single object — `{ course: sourdough }` — and passes it to your function as its
first argument. We **destructure** in the parameter list — `CourseCard({ course })`
— to pull that object into a local variable, then destructure again on the first
line to pull the fields off it. Driving the card from **one `course` object**
instead of nine loose props is a deliberate choice: it mirrors the shape of a row
in `data/courses.js` (Topic 3) and a row in the Postgres `courses` table (Topic 5),
so this component never has to change as the data source does. Props flow **one
way**: the parent (`App`) owns the course object and the child (`CourseCard`) just
displays it. A child never edits its own props. That one-way flow is what makes
React apps predictable — to change what a card shows, you change what the parent
passes in.

## ✅ Check your work

- [ ] `src/components/CourseCard.jsx` exists and default-exports a `CourseCard` function.
- [ ] `CourseCard` takes a **single** `course` prop and destructures its fields — not a flat list of props.
- [ ] The browser shows one card with the 🍞 emoji, a "🧁 Bakery" tag, a "Beginner" level chip, the title, summary, "S$680" and "4 weeks".
- [ ] The component uses `className` everywhere (no `class`), and the console shows no warnings.
- [ ] No `import ... from 'react-router-dom'` and no `<Link>` — the card is a plain `<article>`.
- [ ] No new CSS file or `<style>` block was added; only `index.css` classes are used.

## 🛠 Your turn

1. Render a **second** card for a cooking course, e.g. `CUL-210` Knife Skills &
   Kitchen Essentials (category `Cooking`, level `Beginner`, weeks `1`, fee `160`,
   campus `Culinary`, emoji `🔪`). Confirm the tag flips to "🍳 Cooking" and the
   meta line reads "1 week" (singular), proving your ternary works.
2. Change the sourdough course's `weeks` to `1` for a moment. Does the label read
   "1 week"? Set it back to `4` and watch it become "4 weeks".

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `Adjacent JSX elements must be wrapped in an enclosing tag` | The component returns two or more siblings with no parent. | Wrap them in one element or a fragment `<>…</>`. |
| Warning: `Invalid DOM property 'class'. Did you mean 'className'?` | Used `class` instead of `className`. | Rename every `class` attribute to `className`. |
| Card shows the word `[object Object]` | Put the whole object between `{ }`, e.g. `{course}`. | Render a field, e.g. `{course.title}`, after destructuring. |
| `Cannot destructure property 'title' of 'course' as it is undefined` | Rendered `<CourseCard />` with no `course` prop. | Pass the object: `<CourseCard course={sourdough} />`. |
| `Failed to resolve import 'react-router-dom'` | The agent added a `<Link>` and import that isn't installed yet. | Delete the import and `<Link>`; use a plain `<article className="card">`. Routing arrives in Topic 6. |
| Nothing renders / blank card | Component name is lowercase, so React treats `<courseCard>` as an unknown HTML tag. | Capitalise the component and the tag: `CourseCard`. |

---
### ✅ Cook & Bake Academy after this lab
A reusable `CourseCard` component renders one course’s details from a single `course` object prop.
