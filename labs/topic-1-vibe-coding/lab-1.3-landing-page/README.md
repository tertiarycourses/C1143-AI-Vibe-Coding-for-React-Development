# Lab 1.3 — Vibe-Code the Cook & Bake Landing Page

> **Topic 1** · ~50 min · Builds on Lab 1.2

### 📖 The build so far
By the end of the last lab, Cook & Bake could render a single `CourseCard`. **In this lab you add:** the rest of the landing page around it — a navbar, a hero, a grid of six hand-written course cards and a footer. By the end you'll have a complete Cook & Bake Academy landing page in one file.

## What you will build

The full Cook & Bake Academy landing page: a **Navbar** (🍞 Cook & Bake Academy),
a **Hero** banner ("Master the art of cooking & baking"), a **CourseGrid** showing
six course cards, and a **Footer** — a real, presentable page you could show
someone. You will vibe-code it as one monolithic `App.jsx` with the six cards
written out by hand. That is deliberate: it works today, and Topic 3 turns this
exact code into the clean, reusable components the finished app actually ships
(`Navbar.jsx`, `Hero.jsx`, `CourseGrid.jsx`).

## Concepts you will meet

| Concept | In one line |
|---|---|
| Composition | Building a page by nesting small components inside a bigger one. |
| Multiple components per file | Several function components can live in one file (fine for now, not forever). |
| Fragment `<>…</>` | An invisible wrapper that lets `App` return several siblings with no extra `<div>`. |
| Layout classes | `.nav`, `.hero`, `.section`, `.grid`, `.card` from `index.css` arrange the page. |
| Reuse vs. repetition | The same `<CourseCard>` used six times — working code that is begging to be refactored. |

## Before you start

You need Lab 1.2's `CourseCard` component working. This lab keeps that component
(unchanged) and rewrites `App.jsx` into the full page. Copy this lab's `src/`
over your app's `src/`:

```bash
# from the cookbake/ folder
cp -R ../labs/topic-1-vibe-coding/lab-1.3-landing-page/src/. src/
```

This replaces `src/App.jsx` and refreshes `src/components/CourseCard.jsx`. It does
not touch `index.css`.

---

## Step 1 — Sketch the page as four sections

A landing page is just a stack of sections. You will define four small
components — `Navbar`, `Hero`, `CourseGrid`, `Footer` — **all inside `App.jsx`**,
and have `App` render them in order. Defining them in one file is not best
practice, but it keeps everything in view while you learn composition. (In the
real app each of these is its own file under `src/components/` — Topic 3.2 splits
them out.)

## Step 2 — Build the Navbar and Hero

Each section is a function returning JSX. `Navbar` uses the `.nav` / `.brand`
helpers; `Hero` is the full-bleed banner with a headline and a call-to-action:

```jsx
function Navbar() {
  return (
    <header className="nav">
      <div className="nav__inner">
        <span className="brand">
          <span className="brand__mark">🍞</span>
          <span className="brand__text">
            Cook &amp; Bake<small>Academy</small>
          </span>
        </span>
        <nav className="nav__links">
          <a href="#courses" className="nav__link">Courses</a>
          <a href="#about" className="nav__link">About</a>
        </nav>
        <div className="nav__actions">
          <button className="btn btn--sm">Sign in</button>
        </div>
      </div>
    </header>
  )
}

function Hero() {
  return (
    <section className="hero">
      <div className="hero__bg" />
      <div className="hero__overlay" />
      <div className="hero__content">
        <p className="eyebrow">Singapore&apos;s hands-on culinary studio</p>
        <h1>
          Master the art of <span>cooking</span> &amp; <span>baking</span>
        </h1>
        <p className="hero__sub">
          From artisan sourdough to French pastry, sushi to street food — learn
          practical, job-ready skills from professional chefs in small classes.
        </p>
        <div className="hero__cta">
          <a href="#courses" className="btn btn--lg">Browse courses</a>
        </div>
      </div>
    </section>
  )
}
```

## Step 3 — Build the CourseGrid with six cards

`CourseGrid` wraps six `<CourseCard>` elements in a `.grid` container. Each card
gets its data as **one hardcoded `course` object** — you write all six objects out
by hand, from the real catalogue:

```jsx
function CourseGrid() {
  return (
    <section id="courses" className="section">
      <div className="section__head">
        <p className="eyebrow">Our catalogue</p>
        <h2>Popular courses</h2>
      </div>
      <div className="grid">
        <CourseCard
          course={{
            code: 'BAK-101',
            title: 'Artisan Sourdough Bread Baking',
            category: 'Bakery',
            level: 'Beginner',
            weeks: 4,
            fee: 680,
            campus: 'Bakehouse',
            emoji: '🍞',
            summary:
              'Grow your own starter, master hydration and bake a crackling open crumb loaf.',
          }}
        />
        {/* …five more cards, each with its own hardcoded course object… */}
      </div>
    </section>
  )
}
```

Use these six real courses (fees are Singapore dollars, whole numbers):

| Code | Title | Category | Level | Weeks | Fee | Campus | Emoji |
|---|---|---|---|---|---|---|---|
| BAK-101 | Artisan Sourdough Bread Baking | Bakery | Beginner | 4 | 680 | Bakehouse | 🍞 |
| BAK-102 | French Pastry & Viennoiserie | Bakery | Intermediate | 8 | 1480 | Bakehouse | 🥐 |
| BAK-104 | Macaron Masterclass | Bakery | Intermediate | 2 | 420 | Bakehouse | 🍬 |
| CUL-201 | Italian Cuisine Mastery | Cooking | Intermediate | 6 | 1180 | Culinary | 🍝 |
| CUL-203 | Japanese Sushi & Sashimi | Cooking | Intermediate | 4 | 980 | Culinary | 🍣 |
| CUL-210 | Knife Skills & Kitchen Essentials | Cooking | Beginner | 1 | 160 | Culinary | 🔪 |

See this lab's `src/App.jsx` for all six cards in full.

## Step 4 — Assemble the app

`App` returns the four sections in a fragment so there is no needless wrapper
`<div>`:

```jsx
export default function App() {
  return (
    <>
      <Navbar />
      <Hero />
      <CourseGrid />
      <Footer />
    </>
  )
}
```

Save and open the browser — the full landing page renders, six cards in a
responsive grid that reflows as you resize the window.

---

## 🎤 Vibe prompt

Paste this into your AI agent from inside the `cookbake` folder:

```text
Rewrite src/App.jsx into the Cook & Bake Academy landing page. Keep the existing
src/components/CourseCard.jsx component (it takes a single `course` object prop)
and import it.

In App.jsx, define four function components in this same file:
- Navbar: use <header className="nav"> with a .nav__inner. On the left a .brand
  showing "🍞" (.brand__mark) and "Cook & Bake" with a <small>Academy</small>
  (.brand__text). Then .nav__links with "Courses" (#courses) and "About" links
  using .nav__link, and a .nav__actions with a "Sign in" <button className="btn btn--sm">.
- Hero: <section className="hero"> containing a .hero__bg, a .hero__overlay, and a
  .hero__content with an eyebrow "Singapore's hands-on culinary studio", an <h1>
  "Master the art of <span>cooking</span> & <span>baking</span>", a .hero__sub
  paragraph, and a .hero__cta with a "Browse courses" link to #courses
  (className "btn btn--lg").
- CourseGrid: a <section id="courses" className="section"> with a .section__head
  (<h2>Popular courses</h2>) and a <div className="grid"> containing SIX
  <CourseCard course={{...}} /> elements. Write each course object out explicitly
  (code, title, category, level, weeks, fee, campus, emoji, summary). Use these
  six real courses: BAK-101 Artisan Sourdough Bread Baking (Bakery, Beginner, 4
  weeks, 680, Bakehouse, 🍞), BAK-102 French Pastry & Viennoiserie (Bakery,
  Intermediate, 8, 1480, Bakehouse, 🥐), BAK-104 Macaron Masterclass (Bakery,
  Intermediate, 2, 420, Bakehouse, 🍬), CUL-201 Italian Cuisine Mastery (Cooking,
  Intermediate, 6, 1180, Culinary, 🍝), CUL-203 Japanese Sushi & Sashimi (Cooking,
  Intermediate, 4, 980, Culinary, 🍣), CUL-210 Knife Skills & Kitchen Essentials
  (Cooking, Beginner, 1, 160, Culinary, 🔪).
- Footer: a <footer className="footer"> with a copyright line for Cook & Bake Academy.

App returns <Navbar/>, <Hero/>, <CourseGrid/>, <Footer/> inside a fragment.
Use only existing index.css classes (nav, brand, hero, section, grid, card, btn,
eyebrow, muted, footer). Do NOT use a .map() loop, do NOT import a data file, do
NOT import react-router, and do NOT use any hook — write the six cards out by hand
for now.
```

## 🔍 Read what the AI wrote

The agent will produce **working but repetitive** code — and that is exactly the
point of this lab. Recognising the smell is the skill; resist the urge to fix it
yet.

- **Six near-identical cards is intentional here.** You will notice the six
  `<CourseCard>` lines differ only in their `course` object. That repetition is
  real and it is a code smell — but do **not** refactor it now. Topic 3.3 replaces
  all six with a single `.map()` over the shared `data/courses.js`, and doing it
  by hand first is what makes that lesson land. Leave it repetitive.
- **Everything-in-one-file is also intentional.** `Navbar`, `Hero`, `CourseGrid`
  and `Footer` all sitting in `App.jsx` is fine for a first draft but won't scale.
  Topic 3.2 moves each into its own file under `src/components/` — the exact
  structure the finished app uses. Notice how big `App.jsx` is getting — that
  feeling is the motivation for the refactor.
- **Did it stay off `.map()` and off the data file?** For this lab the cards must
  be hardcoded objects. If the agent "helpfully" imported `courses.js` and looped,
  it jumped ahead of the syllabus — revert it to six explicit cards so the Topic 3
  progression works.
- **No react-router.** The navbar links are plain `<a href="#courses">` anchors and
  the "Browse courses" button is an anchor too — no `<Link>` / `NavLink`, no
  `react-router-dom` import (it isn't installed until Topic 6). If the agent added
  it, strip it out.
- **Data must match the catalogue.** The six courses, categories, levels, weeks and
  fees should match the table above exactly (they are real Cook & Bake courses).
  An agent may invent plausible-but-wrong numbers — verify each card, and confirm
  fees read `S$680`, `S$160` (Singapore dollars, whole numbers).
- **Check the fragment.** `App` should return the four sections wrapped in `<>…</>`,
  not an extra `<div>`. A stray wrapper `<div>` is harmless but unnecessary; a
  fragment adds no node to the DOM.

## 🧠 Why it works

**Composition: pages are trees of components.** `App` does not draw anything
itself — it returns four other components, and each of those returns more markup,
some of which (`CourseGrid`) returns yet more components (`CourseCard`). React
walks this tree from the top: it calls `App`, sees `<Hero/>`, calls `Hero`, and so
on down to the leaf `<article>` and `<h3>` tags, assembling the final HTML. This is
the mental model that makes React scale — you never build one giant blob of
markup; you build small, named pieces and nest them. A "page" is simply the
component at the top of the tree, and the real app's `HomePage` is that same idea
grown up: a `Hero`, then `Section`s of `CourseGrid`, `Chefs` and a `Footer`.

**Why `App` returns a fragment.** A component must return a single root element,
but the landing page is four siblings — navbar, hero, grid, footer — with no
natural wrapper. You *could* wrap them in a `<div>`, but that adds a meaningless
node to the page. A **fragment**, written `<>…</>`, groups siblings for React's
sake while rendering nothing itself. Use it whenever you need to return several
elements but don't want an extra box in the DOM.

**Reuse is the payoff of components — repetition is the warning sign.** Look at
`CourseGrid`: one `CourseCard` component, used six times with a different `course`
object each time. That is reuse working exactly as intended — you wrote the card's
markup once in Lab 1.2 and now you get six cards for free. But notice the *other*
thing: you typed the `<CourseCard course={{ … }} />` block out six times, changing
only the data. When you find yourself copy-pasting structure and editing only the
values, the code is telling you the data should live in a list and the structure
should be written once. That is precisely what Topic 3 does — it moves all twenty
courses into `data/courses.js` and renders them with
`courses.map(course => <CourseCard key={course.id} course={course} />)`, so adding a
course becomes a data change, not a copy-paste. Today you feel the pain on purpose;
later you earn the fix. Working code first, clean code next — that ordering is
itself a vibe-coding lesson: get it running, read it honestly, then improve it.

## ✅ Check your work

- [ ] The page shows the 🍞 navbar, a hero with "Master the art of cooking & baking" and a button, a grid of six cards, and a footer.
- [ ] All six courses appear with the correct titles, levels, durations and `S$` fees from the catalogue.
- [ ] The grid reflows into fewer columns as you narrow the browser window.
- [ ] `App.jsx` defines `Navbar`, `Hero`, `CourseGrid` and `Footer`, and `App` returns them in a fragment.
- [ ] The six cards are written out by hand — no `.map()`, no imported data file, no `react-router`, no hooks.
- [ ] The browser console shows no warnings or errors.

## 🛠 Your turn

1. Add a seventh course card by copy-pasting a `<CourseCard>` block and changing
   the `course` object (try `BAK-105` Chocolate & Confectionery Making, Bakery,
   Intermediate, 4 weeks, 760, Bakehouse, 🍫). Count how many lines that took —
   remember the number when you reach Topic 3.3.
2. The `Hero`'s "Browse courses" button already points at `#courses`. Click it and
   watch the page smooth-scroll to the grid (the CSS sets `scroll-behavior: smooth`).
   Give the navbar's "Courses" link the same behaviour if it doesn't already.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `Adjacent JSX elements must be wrapped in an enclosing tag` | `App` returns four siblings with no wrapper. | Wrap them in a fragment `<>…</>`. |
| Only one card, or cards overlap | The six `<CourseCard>` elements aren't all inside the `.grid` div, or `.grid` is missing. | Put all six cards inside one `<div className="grid">`. |
| A card is blank or shows `undefined` | A field was misspelled or omitted in that card's `course` object. | Compare that object against the working ones; every card needs the full set of fields. |
| `CourseCard is not defined` | Missing import at the top of `App.jsx`. | Add `import CourseCard from './components/CourseCard'`. |
| The page has no styling | `index.css` isn't imported (it's imported in `main.jsx`) or class names are misspelled. | Keep `import './index.css'` in `main.jsx`; use the exact class names from `index.css`. |
| `Failed to resolve import 'react-router-dom'` | The agent added `<Link>`/`NavLink` before Topic 6. | Use plain `<a href="#…">` anchors here; routing arrives in Topic 6. |

---
### ✅ Cook & Bake Academy after this lab
A full Cook & Bake Academy landing page — 🍞 navbar, hero, six course cards and footer — renders as a single page.
