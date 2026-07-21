# Lab 6.2 — Dynamic Routes

> **Topic 6** · ~50 min · Builds on Lab 6.1

### 📖 The build so far
By the end of the last lab, Cook & Bake Academy had static Home, Courses and About routes. **In this lab you add:** dynamic routing — a course detail page at `/courses/:slug`, a real 404 route, and filters that live in the URL. By the end you'll have deep-linkable Cook & Bake Academy course pages.

## What you will build

A **course detail page** at `/courses/:slug` that loads one course from your API
by its slug (`GET /api/courses/:slug`), plus a real **404 page** for any URL that
matches nothing. Each course card becomes a link into its detail page. You will
also move the Courses page's search and category filter **into the URL**
(`/courses?category=Bakery&q=sourdough`) so a filtered view is shareable,
bookmarkable, and survives a refresh.

## Concepts you will meet

| Concept | In one line |
|---|---|
| Dynamic segment `:slug` | A route path with a variable part that matches any value. |
| `useParams()` | Reads the variable part of the URL inside the page component. |
| `useNavigate()` | Navigate imperatively from code (after an action), e.g. a Back button. |
| Catch-all route `path="*"` | Matches anything no other route caught — your 404. |
| `useSearchParams()` | Read and write the `?query=string` part of the URL like state. |
| A 404 that isn't an error | The API's `404` becomes `course: null` with no error — a real "not found" screen, not a red crash. |
| URL state vs component state | Filters in the URL are shareable and back-button friendly. |

## Before you start

You need your Lab 6.1 app (multi-page, with `RootLayout` and `pages/`). Copy this
lab's snapshot over it:

```bash
cp -R labs/topic-6-react-router/lab-6.2-dynamic-routes/src/. cookbake/src/
```

This adds `pages/CourseDetailPage.jsx`, `pages/NotFoundPage.jsx` and
`hooks/useCourse.js`; it rewrites `App.jsx` (two new routes), `CourseCard.jsx`
(now a link) and `CoursesPage.jsx` (URL-driven filters).

---

## Step 1 — Add the dynamic and catch-all routes

In `src/App.jsx`, inside the layout route, add:

```jsx
<Route path="courses/:slug" element={<CourseDetailPage />} />
<Route path="*" element={<NotFoundPage />} />
```

`:slug` is a **dynamic segment** — it matches `artisan-sourdough-bread-baking`,
`knife-skills-and-kitchen-essentials`, anything. `*` is the fallback for unmatched
URLs. Add it **last**: routes are matched top-to-bottom, so a catch-all placed
first would swallow every URL. (`/login` and the protected dashboard arrive in
Lab 6.3.)

## Step 2 — Make the card a link

Open `src/components/CourseCard.jsx`. The whole card is now a
`` <Link to={`/courses/${slug}`}> ``. Clicking a card navigates to its detail
page — client-side, no reload, because React Router intercepts the click. The
card still shows its 🧁 Bakery / 🍳 Cooking tag, level, weeks, campus area and
the price as `S${fee}`.

## Step 3 — Write the one-course hook

`src/hooks/useCourse.js` fetches a single course from
`api.get(`/courses/${slug}`)` — i.e. `GET /api/courses/:slug`. The browser never
touches Postgres; it asks its own API, and the serverless function runs the SQL.

The interesting case is "no such course". The API answers **404** — the status
code *is* the answer — and the hook translates that into `course: null` with **no
error**. A `500`, by contrast, is a real error and fills `error`. Two different
failures, two different screens. That is how the detail page tells "loading"
apart from "genuinely not found" apart from "the server broke".

## Step 4 — Build the detail page

`src/pages/CourseDetailPage.jsx` reads `const { slug } = useParams()`, calls
`useCourse(slug)`, and renders four states: **loading** (a skeleton), **error**
(a red message), **not found** (`course === null` → a "Course not found" `Section`
with a link back to `/courses`) and the course itself. The loaded course shows
the image, badges (code, category, level), `🕒 weeks · 📍 campus`, the summary,
the campus address, the price as `S${course.fee}`, an `<EnrollButton course={course} />`
and an "Add to shortlist" button (`addItem` from `useCart`). The Back button uses
`useNavigate()`: `onClick={() => navigate(-1)}` goes back one entry in history.

## Step 5 — Move filters into the URL

In `src/pages/CoursesPage.jsx` the category and search are now read from
`useSearchParams()` instead of `useState`:

```jsx
const category = searchParams.get('category') ?? 'All'
const q = searchParams.get('q') ?? ''
```

Changing a filter calls `setSearchParams(...)`, which updates the address bar.
The text box keeps a little local `useState` so typing feels instant, and a
`useDebounce(query, 300)` writes the settled value into the URL with
`{ replace: true }` — so a burst of keystrokes leaves **one** history entry, not
one per letter. A `useRef` pointed at the `<input>` focuses the search box on
mount (and after a chip click). Reload the page — your filter is still applied.
Copy the URL to another tab — same view.

---

## 🎤 Vibe prompt

```text
In my react-router-dom v7 Cook & Bake Academy app, add dynamic course pages.
The app already has src/lib/api.js exporting `api` (api.get/post/...) — the
browser's only door to the serverless /api/* functions. api.get throws an Error
with `err.status` set when the response is not ok (e.g. 404, 500).

1. Create src/hooks/useCourse.js exporting useCourse(slug): call
   api.get(`/courses/${slug}`) inside a useEffect keyed on [slug]; return
   { course, loading, error }. On success set course to the data. In the catch,
   if err.status === 404 set course:null and error:null (a real "not found",
   NOT an error); otherwise set error to err.message. Guard against setState
   after unmount.
2. Create src/pages/CourseDetailPage.jsx for /courses/:slug. Read slug with
   useParams(), call useCourse(slug), and render loading (skeleton), error (red
   message), not-found (course is null -> a friendly "Course not found" Section
   with a link back to /courses), and the loaded course. Add a Back button using
   useNavigate() that calls navigate(-1).
3. Create src/pages/NotFoundPage.jsx.
4. In src/App.jsx add <Route path="courses/:slug" .../> and, LAST, a catch-all
   <Route path="*" element={<NotFoundPage/>} />.
5. Make src/components/CourseCard.jsx wrap the whole card in
   <Link to={`/courses/${course.slug}`}>.
6. Change src/pages/CoursesPage.jsx so category + search live in the URL via
   useSearchParams (e.g. ?category=Bakery&q=sourdough) instead of useState.
   Debounce the query and write it with { replace: true }.

Default exports for components; named export for the hook. No new dependencies.
```

## 🔍 Read what the AI wrote

- **Does the hook treat a 404 as "not found", not an error?** The whole point is
  that a mistyped slug is a *clean* outcome, not a crash. Check the catch block:
  `if (err.status === 404) { setCourse(null); setError(null) } else setError(...)`.
  If the AI collapses every failure into one `error` state, a wrong URL shows a
  scary red box instead of a friendly 404.
- **Does the detail page distinguish "loading" from "not found"?** While the
  fetch is in flight, `course` is also null. If the code renders "404" during
  loading it will flash the 404 on every visit. Check the order:
  `loading` first, then `error`, then `!course`, then the course.
- **Is the effect keyed on `slug`?** `useCourse` must refetch when the slug
  changes. If the AI leaves the dependency array `[]`, navigating from one course
  to another shows stale data. It should be `[slug]`.
- **Back button: `navigate(-1)` vs `navigate('/courses')`.** `-1` returns the
  user to wherever they actually came from (Home, search results, a share link).
  A hardcoded path is often wrong. Prefer `-1` for a Back button.
- **Did filters end up in the URL or back in `useState`?** AI defaults to
  `useState`. Verify `CoursesPage` reads `searchParams.get('category')` and calls
  `setSearchParams`, that the debounced write uses `{ replace: true }` (so typing
  doesn't bury the Back button under a history entry per keystroke), and that
  reloading the page keeps the filter.

## 🧠 Why it works

A **dynamic segment** is a slot. `path="courses/:slug"` matches `/courses/`
followed by anything, and captures that anything under the name `slug`. Inside
the matched component, `useParams()` returns an object of those captures:
`const { slug } = useParams()`. One route definition serves all twenty courses
(and any you add later) because the component reads the slug at runtime and asks
the API for the matching row. That is the whole point of dynamic routing: you
describe the *shape* of the URL once, not one route per record.

There are two ways to change the URL, and choosing correctly is a real skill.
`<Link>` is for **navigation the user initiates** — they see a thing and click
it, which is why the whole `CourseCard` is a `<Link>`. `useNavigate()` returns a
`navigate` function for **navigation your code initiates in response to something
else**: an action finished, a guard failed, a form submitted. The Back button is
imperative because "go back" is a behaviour, not a destination you can hardcode —
so `navigate(-1)` walks the history stack. Later, `EnrollButton` uses the same
hook to send a signed-out visitor to `/login` (that route is wired up in Lab 6.3).
Rule of thumb: if it renders as a clickable thing, use `<Link>`; if it happens
as a *consequence*, use `navigate()`.

The 404 is the database half of a good "not found", and it lives in the API, not
the browser. `GET /api/courses/:slug` runs one parameterised query; if no row
matches it returns **status 404**, and `api.get` turns any non-ok response into a
thrown `Error` carrying `err.status`. `useCourse` reads that status: `404` means
"this slug simply doesn't exist" → `course: null`, no error; anything else is a
real failure → `error`. That single distinction is what lets the detail page tell
three situations apart — still loading, the server broke, and "no such course" —
and render a genuine 404 for the last one instead of a spinner that never stops
or a red error box. The catch-all `<Route path="*">` handles the *other* kind of
not-found: a URL that matched no route at all, like `/pricing`. Because it's the
last route, it only fires when nothing above it matched.

Finally, **why put filters in the URL instead of `useState`?** Because the URL is
shared state that outlives the component. When the category lives in `useState`,
it exists only in memory: reload and it resets, copy the link and your friend
sees the unfiltered page, hit Back and nothing happens. When it lives in the URL
via `useSearchParams`, the filtered view becomes a *place* — bookmarkable,
shareable, and the browser's Back button steps through your filter changes for
free. `useSearchParams` feels like `useState` (a value and a setter) but the
"state" is the query string. The one subtlety is history: the debounced query is
written with `{ replace: true }` so typing "sourdough" edits the current entry
instead of stacking eight of them, keeping the Back button useful. Component state
is for things nobody else needs to know (a dropdown's open/closed); URL state is
for anything worth sharing or restoring.

## ✅ Check your work

- [ ] Clicking a course card opens `/courses/<slug>` with that course's details.
- [ ] Visiting `/courses/does-not-exist` shows your "Course not found" screen, not
      a crash, a red error box, or an endless spinner.
- [ ] Visiting `/totally/made/up` shows the catch-all `NotFoundPage`.
- [ ] The Back button returns you to the exact page you came from.
- [ ] Filtering on `/courses` updates the URL to `?category=...&q=...`.
- [ ] Reloading a filtered `/courses` URL keeps the filter; the link works in a
      fresh tab, and typing a query doesn't flood the browser's Back button.

## 🛠 Your turn

1. Add "Prev / Next course" links on the detail page that navigate to the
   neighbouring course by slug. (Hint: you'll need the full list; `useCourses`
   plus the current index.)
2. Add a `?sort=fee` search param to `CoursesPage` and a little sort control
   that writes it. Confirm sorting is now shareable via the URL too.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| Red error box on a bad slug instead of a 404 | The hook lumped the 404 in with real errors. | Special-case `err.status === 404` → `course: null`, `error: null`. |
| 404 flashes on every valid course for a moment | Rendered "not found" while still loading. | Check `loading` before `!course`. |
| Detail page shows the previous course after navigating | Effect dependency array is `[]`. | Depend on `[slug]` so it refetches. |
| `Cannot read properties of null (reading 'title')` | Rendered the course before the null/loading guards. | Return early for loading / error / not-found first. |
| Every URL renders the 404 page | Catch-all `path="*"` placed above the real routes. | Put `*` last so it only matches unmatched URLs. |
| Filter resets on refresh | Filters kept in `useState`. | Read/write them with `useSearchParams`. |

---
### ✅ Cook & Bake Academy after this lab
Every course has its own `/courses/:slug` page served by the API, filters live in the URL, and unknown paths hit a real 404.
