# Lab 3.2 — Components and Props

> **Topic 3** · ~50 min · Builds on Lab 3.1

### 📖 The build so far
By the end of the last lab, Cook & Bake Academy's landing page was one big file and you understood how JSX compiles and how the Virtual DOM reconciles. **In this lab you add:** structure — you split the monolith into real component files (`Navbar`, `Hero`, `Section`, `CourseCard`, `CourseGrid`, `Footer`) and make `CourseCard` accept a single `course` object as a prop. By the end you'll have a properly componentised app whose files match the real `cookbake/src/components/` folder.

## What you will build

You will break the vibe-coded monolith apart. Right now the landing page is one giant
`App.jsx` with the navbar, hero, grid and footer all defined inline, and each course card
is spelled out with eight separate props. You will extract each piece into its own file,
add a reusable `Section` layout component that uses the `children` prop, and — the key
refactor — change `CourseCard` to take a **single `course` object** instead of eight flat
props. When you are done, `App.jsx` reads like a table of contents.

## Concepts you will meet

| Concept | In one line |
|---|---|
| Component | A function that returns JSX and can be reused like a tag |
| Default export | `export default function Foo()` — the file's one main thing |
| Named export | `export function bar()` — for utilities/hooks; import with `{ }` |
| Props | Read-only inputs a parent passes down to a child |
| One-way data flow | Data flows parent → child, never back up by mutation |
| Destructuring props | `function CourseCard({ course })` pulls fields straight out |
| Default parameter | `function Section({ title = 'Untitled' })` gives a prop a fallback |
| Function prop | Passing a function down (`onBrowse`) so a child can call back up |
| `children` | The special prop holding whatever you nest inside a component |
| Composition | Build UIs by nesting components, not by adding more config props |

## Before you start

Continue from the app you have. Copy this lab's snapshot over `src/`:

```bash
cp -R labs/topic-3-core-react-concepts/lab-3.2-components-and-props/src/. cookbake/src/
```

This replaces `src/App.jsx` and adds six files under `src/components/`:
`Navbar.jsx`, `Hero.jsx`, `Footer.jsx`, `Section.jsx`, `CourseGrid.jsx`, `CourseCard.jsx`.
Run `npm run dev` — the page should look like the Cook & Bake Academy landing page with a
hero and six course cards.

---

## Step 1 — Extract the layout pieces

`Navbar`, `Hero` and `Footer` each become their own file with a default export:

```jsx
// src/components/Hero.jsx
export default function Hero({ onBrowse }) {
  return (
    <section className="hero" id="top">
      {/* ... */}
      <button type="button" className="btn btn--lg" onClick={onBrowse}>
        Browse courses
      </button>
      {/* ... */}
    </section>
  )
}
```

`Navbar` and `Footer` take no props; `Hero` takes one — `onBrowse`, a **function** the
parent hands down. That is your first taste of "events up": the child does not decide what
the button does, it just calls the function it was given.

## Step 2 — Build `Section`, a component with `children`

`Section` is a *layout* component. It does not know what a course is; it only knows how to
frame a titled block of content. This is the exact `Section` the real app uses on every
page:

```jsx
export default function Section({ id, title, eyebrow, alt, children }) {
  return (
    <section id={id} className={alt ? 'section section--alt' : 'section'}>
      {(title || eyebrow) && (
        <div className="section__head">
          {eyebrow && <p className="eyebrow">{eyebrow}</p>}
          {title && <h2>{title}</h2>}
        </div>
      )}
      {children}
    </section>
  )
}
```

`children` is a special prop: it is whatever you put *between* the opening and closing tags
when you use the component. So `<Section title="…"><CourseGrid /></Section>` passes
`<CourseGrid />` in as `children`, and it renders where `{children}` sits. `id`, `title`,
`eyebrow` and `alt` are ordinary named props that configure the frame.

## Step 3 — Refactor `CourseCard` to one object prop

This is the important change. A tempting first design passes every field separately:

```jsx
<CourseCard emoji="🍞" title="Artisan Sourdough Bread Baking" category="Bakery"
  level="Beginner" weeks={4} fee={680} campus="Bakehouse" summary="…" />
```

Eight props to line up perfectly, per card, six times. Now the component takes one object:

```jsx
export default function CourseCard({ course }) {
  const { emoji, title, category, level, weeks, fee, summary } = course
  const isBakery = category === 'Bakery'
  // ...
}
```

and you call it with `<CourseCard course={{ id: 1, emoji: '🍞', title: '…' /* … */ }} />`.
The card is a plain `<article className="card">` for now — in Topic 6 the whole card
becomes a `<Link to={`/courses/${slug}`}>` so clicking it navigates with no page reload.

## Step 4 — Compose everything in `App.jsx`

```jsx
export default function App() {
  const scrollToCatalogue = () => {
    document.getElementById('catalogue')?.scrollIntoView({ behavior: 'smooth' })
  }

  return (
    <>
      <Navbar />
      <Hero onBrowse={scrollToCatalogue} />
      <Section id="catalogue" eyebrow="Our programmes" title="Course catalogue">
        <CourseGrid />
      </Section>
      <Footer />
    </>
  )
}
```

`App` no longer contains any markup detail. It *composes* named components and hands `Hero`
a function to run when "Browse courses" is clicked. That composition is the goal of this lab.

---

## 🎤 Vibe prompt

```text
Refactor my monolithic src/App.jsx (Cook & Bake Academy) into components. Create these
files under src/components/, each a default export, using only the existing CSS classes
(.nav .nav__inner .brand .brand__mark .brand__text .nav__links .nav__link .nav__actions
.hero .hero__content .eyebrow .hero__sub .hero__cta .hero__stats .section .section__head
.card .card__body .card__tag .card__foot .card__price .card__ask .grid .row .row--between
.footer .btn .btn--sm .btn--lg .muted):

- Navbar.jsx: a 🍞 "Cook & Bake Academy" brand on the left, Courses/About links, and a
  "Sign in" button on the right. Plain <a> links for now (no router yet).
- Hero.jsx: takes a function prop `onBrowse`. Headline "Master the art of cooking & baking",
  a sub-paragraph, and a "Browse courses" button whose onClick is onBrowse.
- Footer.jsx: a copyright line with the current year via new Date().getFullYear().
- Section.jsx: a layout component with props { id, title, eyebrow, alt, children } that
  renders an optional eyebrow + <h2> inside .section__head, then {children}.
- CourseGrid.jsx: renders six <CourseCard> inside a <div className="grid">.
- CourseCard.jsx: IMPORTANT — it must take a SINGLE prop `course` (an object) and
  destructure { emoji, title, category, level, weeks, fee, summary } from it, NOT eight
  separate props. Render a plain <article className="card"> (Topic 6 turns it into a Link).

Then rewrite src/App.jsx to import and compose Navbar, Hero (passing an onBrowse that
scrolls to the catalogue), Section (wrapping CourseGrid) and Footer. No TypeScript,
2-space indent, single quotes, no semicolons.
```

## 🔍 Read what the AI wrote

- **Did it actually collapse to one `course` prop?** Agents love to keep the eight flat
  props because that is what the old code had. Confirm the signature is
  `function CourseCard({ course })` and that `CourseGrid` passes `course={{…}}`.
- **Did it mutate a prop?** Look for anything like `course.title = …` or `props.fee += …`
  inside a component. Props are **read-only**. Mutating them is a bug even when it appears
  to work.
- **Default export vs named export.** Each component should be a single `export default`.
  If the agent wrote `export function Hero()` (named) but the import is
  `import Hero from './Hero'` (default), the import resolves to `undefined` and the app
  renders nothing. The two must match.
- **Did it invent new CSS?** The prompt says reuse the existing classes. If it produced a
  new stylesheet or Tailwind classes, that will not match the design tokens. Steer it back
  to `.card`, `.grid`, `.hero`, `.section`, etc.
- **Is `children` actually used?** A tell-tale AI mistake is to give `Section` a `content`
  prop instead of using `children`, or to forget to render `{children}` at all — in which
  case the course grid disappears.
- **Did it call `onBrowse` instead of passing it?** `onClick={onBrowse}` is right;
  `onClick={onBrowse()}` runs it during render. Same trap you'll meet again in Lab 3.4.

## 🧠 Why it works

A **component is just a function**. It takes inputs and returns a description of UI. When
you write `<Hero />`, React calls `Hero()` and splices the returned tree into the page.
Because it is a plain function, you get all the benefits of functions for free: you can
name it, reuse it, move it to its own file, and reason about it in isolation. Splitting the
monolith is not busywork — a 300-line `App.jsx` forces you to hold the whole page in your
head at once, while `Navbar`, `Hero`, `Section`, `CourseGrid`, `Footer` each fit on a
screen and can be understood alone. This is the number-one thing AI agents get *lazy*
about: they will happily generate one enormous component because it technically runs. Your
job in the read-and-correct loop is to insist on the split.

**Props are the inputs to that function, and they flow one way: parent → child.** The
parent decides what a child receives; the child reads those values but must never write
back to them. This is **one-way data flow**, and it is what makes a React app traceable:
to find out why a card shows "S$680", you look at whoever rendered `<CourseCard>` and
passed that value in — you never have to wonder whether the card changed it. Concretely,
props are **read-only**. Doing `course.fee = 0` inside `CourseCard` is a bug: you would be
mutating an object that belongs to the parent, and React does not expect the change, so the
UI and the data drift apart. If a child needs to influence the parent, the parent passes
down a *function* — which is exactly what `Hero`'s `onBrowse` prop is. The child calls it,
and the parent decides what to do. **Data down, events up.** You will lean on this again in
Lab 3.4 with `onChange` and `onSelect`.

Why refactor `CourseCard` from eight props to one `course` object? Three reasons. First,
**less to thread**: passing eight attributes through every call site is eight chances to
misspell one or swap two numbers. Second, **the shape becomes meaningful**: `course` is a
*thing* in your domain, and `{ id, code, slug, title, category, level, weeks, fee, campus,
summary, emoji, image }` is that thing's structure — the code now mirrors the concept.
Third, and most important for this course, **it matches the database**: in Topic 5 you will
fetch rows from a Neon Postgres `courses` table, and each row arrives as exactly this
object. Because `CourseCard` already speaks "course object," you will drop the live data in
without touching the component at all. Designing your prop shapes to match your data shapes
is what lets the later topics slot together.

Finally, `Section` demonstrates **composition over configuration**. A tempting alternative
design is to give `Section` a hundred props — `showGrid`, `gridColumns`, `cardStyle` — to
control everything it might contain. That path leads to an unmaintainable component with a
giant prop list. Instead, `Section` accepts `children` and simply renders whatever you nest
inside it. It stays tiny and generic; the caller composes the specific content. Most good
React APIs prefer `children` (composition) over an ever-growing bag of config props.

`children` and named props are not either/or — a well-designed component usually takes both.
`Section` itself proves it: `id`, `title`, `eyebrow` and `alt` are named props that
configure the *frame*, while `children` absorbs the *content*. A reusable `Button` is the
same shape:

```jsx
function Button({ children, onClick, variant = 'primary', disabled = false }) {
  return (
    <button className={variant} onClick={onClick} disabled={disabled}>
      {children}
    </button>
  )
}
// <Button variant="btn--ghost" onClick={enrol}>Add to shortlist</Button>
```

The `{children}` slot makes it flexible about *content*; the `onClick`, `variant` and
`disabled` props keep it configurable about *behaviour*. Notice `onClick` here is a
**function passed down as a prop** — the "events up" half of one-way data flow, exactly like
`onBrowse`.

### Props vs state (a preview)

You will meet **state** in Topic 4, but it helps to see the contrast now:

| | Props | State |
|---|---|---|
| Who owns it | The **parent** passes it in | The component **owns** it internally |
| Can the component change it | No — **read-only** | Yes — via a setter like `setCount` |
| Direction | Flows **down** (parent → child) | Lives **inside** one component |
| Changing it re-renders | The parent re-renders and passes new props | Calling the setter re-renders this component |
| Example | `course`, `title`, `onBrowse` | `query`, `category`, `isOpen` |

For now, everything on the page is driven by props. That is fine — the catalogue is still
static. Lab 3.4 adds the state that makes it interactive.

## ✅ Check your work

- [ ] `src/components/` contains `Navbar.jsx`, `Hero.jsx`, `Footer.jsx`, `Section.jsx`,
      `CourseGrid.jsx`, `CourseCard.jsx`, each a default export.
- [ ] `CourseCard`'s signature is `function CourseCard({ course })` — one prop.
- [ ] `App.jsx` imports and composes the five components and contains no course markup.
- [ ] The page renders a navbar, a hero, a titled section, six course cards, and a footer.
- [ ] The footer year is the current year (proof that `{new Date().getFullYear()}` runs).
- [ ] Clicking "Browse courses" in the hero scrolls to the catalogue (proof `onBrowse` fired).
- [ ] Nothing in any component assigns to a prop (no `course.x = …`).

## 🛠 Your turn

1. Add an `alt` block: render a second `<Section alt eyebrow="Why Cook & Bake Academy"
   title="Learn by doing">` below the catalogue and drop any content inside it. Confirm the
   `alt` prop flips the class to `section section--alt` (the default parameter path when you
   omit it renders the plain `section`).
2. Give `Hero` a `ctaLabel` prop (default `'Browse courses'`) and render it on the button.
   Now the same `Hero` could headline different pages with a different call to action.
3. Split the meta line (`{level} · {weeks} week…`) out of `CourseCard` into a small
   `CourseMeta` component that takes `{ course }`. Notice you can pass the whole object
   straight down.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `Element type is invalid: expected a string … but got: undefined` | Import/export mismatch (named vs default) | If the file has `export default function Hero`, import it as `import Hero from './Hero'` (no braces) |
| The course grid is blank inside `Section` | `Section` forgot to render `{children}`, or used a `content` prop instead | Add `{children}` to `Section`'s JSX and pass content between the tags |
| `Cannot destructure property 'emoji' of 'course' as it is undefined` | `<CourseCard />` was rendered without a `course` prop | Always pass `course={{…}}`; or add a default like `{ course = {} }` while debugging |
| Card shows eight `undefined`s | Still passing flat props (`title=…`) to the new object-based `CourseCard` | Wrap the fields in one object: `course={{ title: '…', … }}` |
| "Browse courses" does nothing | Passed `onClick={onBrowse()}` (called it) or forgot to pass `onBrowse` | Pass the function itself: `<Hero onBrowse={scrollToCatalogue} />` and `onClick={onBrowse}` |
| Console warning about a duplicate `key` (later) | Not relevant yet — appears in Lab 3.3 when you `.map()` | Handled in the next lab |

---
### ✅ Cook & Bake Academy after this lab
The app is split into reusable component files that mirror `cookbake/src/components/`, with `CourseCard` driven by a single `course` prop.
