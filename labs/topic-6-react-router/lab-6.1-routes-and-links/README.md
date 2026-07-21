# Lab 6.1 — Routes and Links

> **Topic 6** · ~45 min · Builds on Lab 5.4

### 📖 The build so far

By the end of the last lab, Cook & Bake Academy was a single authenticated page. **In this lab you add:** client-side routing with React Router — `Home`, `Courses` and `About` pages sharing one layout with a persistent navbar. By the end you'll have a multi-page Cook & Bake Academy that navigates without full reloads.

## What you will build

You will turn Cook & Bake Academy from one long scrolling page into a real
**multi-page app**: a Home page, a Courses page and an About page, each at its
own URL (`/`, `/courses`, `/about`), sharing one Navbar and Footer. Nothing
reloads the browser when you move between them — React Router swaps the page in
place while your app keeps running.

## Concepts you will meet

| Concept | In one line |
|---|---|
| Single Page Application (SPA) | One HTML file; JavaScript redraws the page instead of the server sending a new one. |
| Client-side routing | The URL changes and the view changes, but the browser never makes a full-page request. |
| `<BrowserRouter>` | Wraps the app and connects it to the browser's address bar. |
| `<Routes>` / `<Route>` | A map from URL paths to the component that should render. |
| Layout (pathless) route + `<Outlet/>` | A shared shell (Navbar/Footer) whose child route renders in the hole `<Outlet/>` marks. |
| `index` route | The child that renders when the parent's path matches exactly (here, `/`). |
| `<Link>` vs `<a>` | `<Link>` navigates without a reload and keeps your React state; `<a>` throws it all away. |
| `<NavLink>` | A `<Link>` that knows if it is the active route, via an `{ isActive }` render-prop. |

## Before you start

You need your Lab 5.4 app: components in `src/components/`, the three context
providers wired in `src/main.jsx`, and the `useCourses` hook reading the
catalogue from the API. `react-router-dom` is already installed (check
`package.json`).

Copy this lab's snapshot over your app:

```bash
cp -R labs/topic-6-react-router/lab-6.1-routes-and-links/src/. cookbake/src/
```

This adds `src/pages/` and `src/layouts/`, and rewrites `src/App.jsx`,
`src/main.jsx`, `src/components/Navbar.jsx` and `src/components/Hero.jsx` (the
hero's "See all courses" button becomes a `<Link>`). Your existing `Section`,
`SearchBar`, `CategoryFilter`, `CourseGrid`, `Chefs` and `useCourses` are reused
unchanged.

---

## Step 1 — Wrap the app in `<BrowserRouter>`

Routing only works if something is listening to the address bar. Open
`src/main.jsx` and wrap everything in `<BrowserRouter>` — **outside** your theme,
auth and cart providers, so every component (including the ones inside those
providers) can use routing:

```jsx
<BrowserRouter>
  <ThemeProvider>
    <AuthProvider>
      <CartProvider>
        <App />
      </CartProvider>
    </AuthProvider>
  </ThemeProvider>
</BrowserRouter>
```

## Step 2 — Turn `App.jsx` into a route map

`App` no longer renders a page directly. It declares which component belongs at
which URL. See this lab's `src/App.jsx`: one layout `<Route path="/">` wrapping
three children — an `index` route for Home, `courses`, and `about`. The course
**detail** page, `/login` and the private **dashboard** arrive in the next labs;
for now these three routes are enough to turn one long page into a real
multi-page app.

## Step 3 — Build the shared layout

`src/layouts/RootLayout.jsx` renders `<Navbar/>`, then `<Outlet/>`, then
`<Footer/>`. `<Outlet/>` is the hole where the matched child route appears. The
Navbar and Footer render once and stay put while the middle changes.

## Step 4 — Split the page into pages

The three files in `src/pages/` are just the sections you already had, each
now a page component:

- `HomePage` — the `Hero`, a "Popular courses" grid of the first 6 courses, the
  "Why Cook & Bake Academy" features block, the campuses section and the CTA —
  all the sections from Topics 1–4, now living on the `/` route. The hero's
  "Browse courses" button scrolls down to the grid: `HomePage` holds a `useRef`
  (known from Topic 4) on the grid `<section>` and passes a scroll function to
  the hero's `onBrowse` prop.
- `CoursesPage` — `SearchBar` + `CategoryFilter` + `CourseGrid`, with the filter
  state kept in plain `useState` for now.
- `AboutPage` — an intro paragraph, `<Chefs/>` (the chef instructor cards) and
  the two campuses.

## Step 5 — Replace `<a>` with `<Link>` / `<NavLink>`

In `src/components/Navbar.jsx` the nav items are now `<NavLink>`s and the brand
is a `<Link>`. For this lab the navbar is deliberately small — the 🍞 brand, two
tabs (Courses, About) and the theme toggle. (The shortlist badge, the Dashboard
link and Sign in / Sign out arrive in Lab 6.3.) Click around: the page changes
with no white flash, and the active tab is highlighted.

---

## 🎤 Vibe prompt

```text
In my Vite + React app (react-router-dom v7 is installed) convert the
single-page Cook & Bake Academy app into a multi-page SPA.

1. In src/main.jsx wrap the existing provider tree in <BrowserRouter> from
   react-router-dom, OUTSIDE ThemeProvider/AuthProvider/CartProvider.
2. Create src/layouts/RootLayout.jsx that renders <Navbar/>, then <Outlet/>,
   then <Footer/>.
3. Create src/pages/HomePage.jsx (the Hero plus a "Popular courses" grid of the
   first 6 courses from useCourses; the Hero's onBrowse prop scrolls to that
   grid via a useRef), src/pages/CoursesPage.jsx (move the SearchBar +
   CategoryFilter + CourseGrid here, keep filter state in useState for now), and
   src/pages/AboutPage.jsx (an intro paragraph plus the existing Chefs
   component).
4. Rewrite src/App.jsx to render <Routes> with one layout <Route path="/">
   wrapping: index -> HomePage, "courses" -> CoursesPage, "about" -> AboutPage.
5. Update src/components/Navbar.jsx to use <Link> for the 🍞 brand and <NavLink>
   for Courses/About, with an isActive-based className that returns
   'nav__link is-active' when active and 'nav__link' otherwise.

Use default exports for components. Do not add any new dependencies.
```

## 🔍 Read what the AI wrote

- **Is `<BrowserRouter>` outside the providers?** If it wraps only `<App/>` but
  the providers wrap `<BrowserRouter>`, routing hooks used inside a provider
  will crash. Router outermost is safest.
- **Did it use `<Link to="...">` or leave `<a href="...">`?** An `<a>` triggers a
  full-page reload — the entire React app restarts and all state is lost. AI
  often leaves stray `<a>` tags. Every internal link must be `<Link>`/`<NavLink>`.
- **Is there exactly one `index` route?** The child with no `path`, marked
  `index`, is what renders at `/`. AI sometimes writes `path=""` or `path="/"` on
  a child, which is not the same thing.
- **Does `RootLayout` actually render `<Outlet/>`?** Forgetting it is the classic
  "my Navbar shows but the page is blank" bug — the child route has nowhere to go.
- **Are the NavLink paths absolute (`/courses`) not relative (`courses`)?** In the
  Navbar both work, but AI mixing the two under nested routes causes surprises.
- **Did it invent a fourth page?** The app has exactly three routes for now.
  A generated `AboutPage` that renders an "Instructors" component is wrong — the
  real component is `Chefs`. Match the components the app actually ships.

## 🧠 Why it works

A **Single Page Application** ships exactly one HTML file — the `index.html` with
`<div id="root">`. When you first load `/`, the server sends that file, the
browser downloads your JavaScript bundle, and React fills the div. From then on,
**the server never sees the URL change again.** When you click "Courses", you are
not asking the server for a `/courses` page; there is no such file. React Router
intercepts the click, updates the address bar with the browser's History API, and
re-renders your components to match. That is **client-side routing**: same
document, new view, no round-trip.

This is why `<Link>` matters. A normal `<a href="/courses">` does what anchors
have always done — it tells the browser to throw the current document away and
fetch a new one from the server. In an SPA that means your whole React tree is
destroyed and rebuilt from scratch: every `useState`, your loaded courses, your
scroll position, the theme you just toggled — all gone, and the user watches a
white flash while the bundle reboots. `<Link to="/courses">` renders an `<a>` for
accessibility but hijacks the click, so navigation is instant and your state
survives. **Inside a React app, internal navigation is always `<Link>`, never
`<a>`.**

`<Routes>` is a matcher: it looks at the current URL and renders the first
`<Route>` whose `path` fits. Routes nest to mirror layout. Here the outer
`<Route path="/">` renders `RootLayout` (your Navbar + Footer shell), and its
children render **inside** that shell wherever you put `<Outlet/>`. The child
marked `index` is the one for the parent's own path — so `/` shows the Home page
*within* the layout. This is the pattern the whole topic builds on: one shell,
many pages, and later a nested shell (the dashboard) inside it.

`<NavLink>` is `<Link>` plus awareness. It hands your `className` a function with
an object `{ isActive }` that is `true` when the current URL matches the link's
`to`. This lab's Navbar returns a class name from it:

```jsx
const navClass = ({ isActive }) => (isActive ? 'nav__link is-active' : 'nav__link')
```

(You could return a `style` object instead.) Either way, the current page's tab
highlights itself with zero manual bookkeeping.

**One more route earns its place: the catch-all.** `<Routes>` renders the *first* `<Route>` whose
`path` matches, so a route with `path="*"` — the wildcard that matches anything — placed **last**
becomes your in-app 404 page:

```jsx
<Route path="/" element={<RootLayout />}>
  <Route index element={<HomePage />} />
  <Route path="courses" element={<CoursesPage />} />
  <Route path="about" element={<AboutPage />} />
  <Route path="*" element={<NotFound />} />   {/* matches every unmatched path */}
</Route>
```

Order matters precisely because matching stops at the first hit: put `path="*"` at the top and it
would swallow `/courses` and `/about` too, so it has to sit at the bottom. This is a *client-side*
404 — React Router showing a friendly "page not found" for a URL your app simply doesn't define. Do
not confuse it with the *server-side* deep-link 404 in the next paragraph: that one is the static
host refusing to serve `/courses` as a file at all, and it is fixed by the host rewrite, not by this
route. You will add a real `NotFoundPage` in Lab 6.2.

**Callback to Labs 2.2 / 2.3:** remember the `vercel.json` rewrite (and the
404-fallback for GitHub Pages) you configured back then? This is *why*. On a
static host, requesting `/courses` directly asks the server for a file that does
not exist — a 404 — because the only real file is `index.html`. The rewrite tells
the host "for any path, serve `index.html`", so your SPA boots and React Router
takes over and shows the right page. Without it, links work but **refreshing on a
deep link 404s.** You will confirm this on the deployed app in Lab 6.4.

## ✅ Check your work

- [ ] `npm run dev` runs; `/`, `/courses`, `/about` each show a different page.
- [ ] The Navbar and Footer stay on screen on all three pages (they don't reload).
- [ ] Clicking a nav link changes the page with **no white flash / full reload**.
- [ ] The active tab is visually highlighted (it uses the `isActive` render-prop).
- [ ] Toggling the theme, then navigating, keeps the theme — state survived.
- [ ] The hero's "Browse courses" button scrolls down to the Popular courses grid.
- [ ] Typing a search on `/courses`, navigating away and back re-runs the page
      (filter state resets — that is the problem Lab 6.2 fixes).

## 🛠 Your turn

1. The Home page already links to `/courses` in two places (the hero's "See all
   20 courses" and the "See all 20 courses →" under the grid). Add one more
   `<Link>` — say, from the campuses section to `/about`. Confirm it navigates
   without a reload.
2. Open the Network tab, tick "Disable cache", and click between pages. Watch
   that **no document request** fires on a `<Link>` click — only on a manual
   refresh. Now temporarily change one `<NavLink>` to a plain `<a>` and watch the
   full document reload return.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `useRoutes() may be used only in the context of a <Router>` | A routing hook/component is rendered outside `<BrowserRouter>`. | Make sure `<BrowserRouter>` wraps `<App/>` (and the providers) in `main.jsx`. |
| Navbar shows but the page area is blank | The layout route forgot `<Outlet/>`. | Render `<Outlet/>` inside `RootLayout` where the page should appear. |
| Full-page reload / white flash on link click | An internal link is still an `<a href>`. | Replace it with `<Link to>` / `<NavLink to>`. |
| Home page doesn't render at `/` | Missing `index` on the child route. | Use `<Route index element={<HomePage/>} />`, not `path="/"`. |
| Active styling never turns on | Passed a plain object/string to `className`/`style` instead of a function. | Use the render-prop form: `className={({ isActive }) => ...}`. |
| A custom 404 page never shows, or it hides real pages | `<Route path="*">` is missing, or placed above the other routes so it matches first. | Add it **last** inside `<Routes>` so it only matches unmatched paths. |

---
### ✅ Cook & Bake Academy after this lab
Cook & Bake Academy is a multi-page app — Home, Courses and About routes share a layout and navigate instantly.
