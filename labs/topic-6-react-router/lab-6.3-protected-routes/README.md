# Lab 6.3 — Protected Routes

> **Topic 6** · ~55 min · Builds on Lab 6.2

### 📖 The build so far
By the end of the last lab, all of Cook & Bake Academy's routes were public. **In this lab you add:** a route guard — a private `/dashboard` that redirects signed-out visitors to the login page and returns them after they authenticate. By the end you'll have Cook & Bake Academy protecting pages behind auth.

## What you will build

An **auth-gated dashboard**. Signed-out visitors who try to reach `/dashboard`
are redirected to `/login`; after they sign in they land back exactly where they
were headed. The dashboard is itself a **nested layout** with two tabs —
`My courses` (their enrollments) and `Profile` — rendered through a second
`<Outlet/>`. You will meet the single most common bug in AI-generated auth
routing and learn to defeat it.

## Concepts you will meet

| Concept | In one line |
|---|---|
| Guard route | A wrapper route that renders `<Outlet/>` if allowed, or `<Navigate/>` if not. |
| `<Navigate to="/login" replace />` | Redirect by rendering — no click needed. |
| Waiting for `auth loading` | Don't decide "logged in?" until the session has resolved (`loading` stays true until `AuthProvider` verifies the token with `/api/auth/me`). |
| `replace` vs push | `replace` swaps the history entry so Back doesn't loop. |
| `useLocation()` + `state.from` | Remember the attempted URL and return there after login. |
| Nested routes + relative paths | `to="profile"` resolves under the current route. |
| Client guard ≠ security | The real boundary is the API — `requireAuth()` plus the `where user_id = ${userId}` ownership check; anyone can edit the JS. |

## Before you start

You need your Lab 6.2 app plus your Topic 5 auth pieces: `AuthContext`
(`useAuth()` returning `{ user, loading, signIn, signUp, signOut }`), the
`AuthForm` component, the `useEnrollments` hook and the `EnrollmentList`
component. Copy this lab's snapshot over your app:

```bash
cp -R labs/topic-6-react-router/lab-6.3-protected-routes/src/. cookbake/src/
```

This adds `components/ProtectedRoute.jsx`, `pages/LoginPage.jsx`,
`pages/DashboardPage.jsx`, `pages/dashboard/MyCoursesPage.jsx` and
`pages/dashboard/ProfilePage.jsx`; it rewrites `App.jsx` and upgrades
`Navbar.jsx` to be auth-aware (Sign in / Sign out, Dashboard link, shortlist count).

---

## Step 1 — Write the guard

`src/components/ProtectedRoute.jsx` reads `{ user, loading }` from `useAuth()`.
The whole lab hinges on the order of three returns:

```jsx
if (loading) return <p className="section muted">Checking your session…</p>
if (!user) return <Navigate to="/login" replace state={{ from: location }} />
return <Outlet />
```

## Step 2 — Nest the protected area in the route map

In `src/App.jsx` the guard is a **pathless** route wrapping the dashboard:

```jsx
<Route element={<ProtectedRoute />}>
  <Route path="dashboard" element={<DashboardPage />}>
    <Route index element={<Navigate to="my-courses" replace />} />
    <Route path="my-courses" element={<MyCoursesPage />} />
    <Route path="profile" element={<ProfilePage />} />
  </Route>
</Route>
```

Everything inside the guard is protected. `DashboardPage` is a layout of its own.

## Step 3 — Build the login page that returns you home

`src/pages/LoginPage.jsx` reads `location.state?.from?.pathname` (set by the
guard) and, on successful sign-in, calls `navigate(from, { replace: true })`.
A signed-in visitor who opens `/login` is bounced onward the same way.

## Step 4 — Build the nested dashboard

`src/pages/DashboardPage.jsx` renders two relative tabs —
`<NavLink to="my-courses">` and `<NavLink to="profile">` (no leading slash) —
styled with a `chip` render-prop, plus its own `<Outlet/>`. The child pages
render there.

## Step 5 — Prove it, then break it on purpose

Sign in, open `/dashboard/my-courses`, and **refresh**. You stay. Now (see "Your
turn") remove the `loading` check and refresh again — you get bounced to
`/login`. Put it back. That is the bug this lab exists to teach.

---

## 🎤 Vibe prompt

```text
In my react-router-dom v7 Cook & Bake Academy app, add a protected dashboard.
Auth already exists: a useAuth() hook returns { user, loading, signIn, signUp,
signOut }. `user` is null when signed out; `loading` stays true on boot until
AuthProvider has verified the stored JWT against GET /api/auth/me.

1. src/components/ProtectedRoute.jsx: a layout route. Read { user, loading }
   from useAuth() and useLocation(). If loading, render a "Checking your
   session…" placeholder. If not loading and no user, return
   <Navigate to="/login" replace state={{ from: location }} />. Otherwise
   render <Outlet/>. The loading check MUST come first.
2. src/pages/LoginPage.jsx: render <AuthForm/>. Compute
   from = location.state?.from?.pathname ?? '/dashboard'. On success call
   navigate(from, { replace: true }). Also redirect there if a signed-in user
   opens /login.
3. src/pages/DashboardPage.jsx: a nested layout with two <NavLink> tabs
   (relative: "my-courses" and "profile") and its own <Outlet/>.
4. src/pages/dashboard/MyCoursesPage.jsx (uses useEnrollments + EnrollmentList)
   and src/pages/dashboard/ProfilePage.jsx (shows user name/email/id + Sign out).
5. In src/App.jsx wrap the dashboard routes in <Route element={<ProtectedRoute/>}>.
   Add an index redirect from /dashboard to my-courses.
6. Update Navbar to show Sign in when logged out and Sign out + a Dashboard
   link when logged in.

Default exports for components. No new dependencies.
```

## 🔍 Read what the AI wrote

- **THE BIG ONE — does the guard wait for `loading`?** This is the most common
  bug in AI-generated auth routing. On a hard refresh, `AuthProvider` holds a
  token from a previous visit but has not checked it yet; it calls
  `GET /api/auth/me` to verify the signature, and until that answer arrives `user`
  is `null`. A guard written as `if (!user) return <Navigate to="/login" />` fires
  *during* that moment and **kicks a signed-in user to the login screen on every
  refresh.** The fix is one line: check `if (loading) return <spinner/>` **before**
  you check `!user`. If the AI's guard has no `loading` branch, it is broken —
  fix it.
- **Is the redirect `replace`?** Without `replace`, `/login` gets pushed onto
  history; after logging in and going back, the user hits `/login` again, which
  redirects forward — a confusing loop. `replace` swaps the entry so Back skips it.
- **Does login send the user back where they were headed?** Look for
  `location.state.from` on the redirect and `navigate(from, { replace: true })`
  after sign-in. AI often hardcodes `navigate('/dashboard')`, losing the deep link.
- **Are the dashboard tab links relative?** `to="profile"` (no leading slash)
  resolves to `/dashboard/profile`. `to="/profile"` would jump to a top-level
  route that doesn't exist. Relative links are what make nested routes portable.
- **Does the code treat this guard as security?** It must not. It is UX only —
  see Why it works. The real protection is the API: `requireAuth()` plus the
  `where user_id = ${userId}` ownership check you built in `topic-5-backend-api`.

## 🧠 Why it works

A **protected route** is just a component that decides between two renders:
`<Outlet/>` (show the nested pages) or `<Navigate/>` (redirect). `<Navigate>` is
the declarative twin of `useNavigate()` — rendering it *is* the redirect, no
event required. Because the guard is a pathless `<Route element={<ProtectedRoute/>}>`
wrapping the dashboard routes, every child inherits the gate automatically; you
never repeat the check per page.

Now the bug the whole lab is built around. Authentication state is not known
instantly. When the page first loads or is refreshed, your `AuthProvider` still
holds a token from a previous visit, but *this* page load has never had it
checked — so it calls `GET /api/auth/me` to verify the signature and hand back
the current user, and that answer arrives a tick later. While the request is in
flight (your `loading`), the honest value of `user` is "we don't know yet" — but
in code it reads as `null`, which looks identical to "signed out". If your guard
decides on `user` alone, it will, on **every refresh**, briefly believe a
logged-in user is logged out and redirect them to `/login`. Users experience this
as "the app logs me out whenever I reload." The cure is to make the third state
explicit: `loading`. While `loading` is true you render nothing decisive (a
placeholder); only once it is false do you trust `user`. **Order matters:**
`loading` check first, `!user` second, `<Outlet/>` last. This is the single most
valuable thing to verify in any AI-generated auth routing — agents omit it
constantly because the happy path (navigating in from a click, where the session
is already known) works fine and hides the bug until you refresh.

`replace` versus push is about the history stack. Normal navigation *pushes*: it
adds an entry, so Back returns to the previous one. A redirect should *replace*
instead — you don't want the page you were bounced away from (or the interstitial
`/login`) sitting in history, because Back would just re-trigger the redirect and
trap the user. Both the guard's `<Navigate replace>` and the post-login
`navigate(from, { replace: true })` use replace for exactly this reason.

Capturing the attempted URL is what makes the flow feel intelligent. When the
guard redirects, it stashes the current location in the navigation `state`:
`<Navigate to="/login" replace state={{ from: location }} />`. The login page
reads `location.state?.from?.pathname` and, after a successful sign-in, sends the
user *there* instead of to a generic home. Click a protected deep link while
signed out, sign in, and you arrive exactly where you meant to go.

Finally, the disclaimer that matters most: **this guard is UX, not security.**
Everything here runs in the browser, and the browser is the user's machine — they
can open dev tools, edit your JavaScript, and delete the guard. A client-side
route guard only decides what the UI *shows*; it cannot stop a determined request
to your database. The actual security boundary is the **API** you built in
`topic-5-backend-api`. Every protected serverless function calls `requireAuth(req)`,
which verifies the JWT's signature with the server's secret and returns the user
id from the token's verified `sub` claim — a value the browser cannot forge,
because editing the token breaks the signature and `requireAuth` answers 401.
Then every protected query carries `where user_id = ${userId}`, so ownership is
enforced in SQL: `GET /api/enrollments` takes no "whose?" parameter, and
`DELETE /api/enrollments/:id` ANDs the id from the URL with the id from the token,
so asking for someone else's row simply matches nothing and returns 404. The
browser says *what* it wants; the server decides *who* is asking. The guard makes
the app pleasant; the API makes it safe. You need both, and you must never
mistake the first for the second.

## ✅ Check your work

- [ ] Signed out, visiting `/dashboard` redirects to `/login`.
- [ ] After signing in from that redirect, you land on `/dashboard` (or the deep
      link you originally tried), not a generic page.
- [ ] Signed in, open `/dashboard/my-courses` and **refresh** — you stay signed
      in and on the page (no bounce to `/login`).
- [ ] `/dashboard` alone redirects to `/dashboard/my-courses`.
- [ ] The dashboard tabs switch the inner content without leaving the dashboard.
- [ ] `Profile` shows your name, email and User ID (that id is the JWT's verified
      `sub` — the same value the API puts in every `where user_id = ${...}`).
- [ ] Signing out from Profile returns you to a signed-out state; `/dashboard`
      now redirects again.

## 🛠 Your turn

1. **See the bug.** Temporarily delete the `if (loading) …` line in
   `ProtectedRoute`, refresh on `/dashboard/my-courses`, and watch yourself get
   logged out. Restore the line. You now recognise this bug on sight.
2. **Prove the guard is only cosmetic.** Sign in, open the Network tab, and
   confirm `GET /api/enrollments` sends no user id — just your `Authorization`
   header. Then try `DELETE`ing another id in devtools: you get 404, because the
   server's `where user_id = ${userId}` never matched. The UI hid the button; the
   API is what actually refused.
3. Add a third dashboard tab, `Settings`, at `/dashboard/settings` with a
   relative `<NavLink>`. Notice you didn't touch the guard — nesting inherits it.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| Refresh on a dashboard URL logs the user out | Guard checks `!user` before `loading` resolves. | Return a placeholder while `loading`, then check `user`. |
| Back button loops back to `/login` | Redirect pushed instead of replaced. | Use `<Navigate ... replace />` and `navigate(from, { replace: true })`. |
| Login always lands on `/dashboard`, ignoring the deep link | `from` not captured or not used. | Pass `state={{ from: location }}`, read `location.state.from` on login. |
| Dashboard tab link jumps to a 404 | Used an absolute `to="/profile"`. | Use relative `to="profile"` under the dashboard route. |
| Blank dashboard body | `DashboardPage` missing its own `<Outlet/>`. | Render `<Outlet/>` inside `DashboardPage`. |
| Treating the hidden button as protection | Trusting the client guard to keep data private. | The API enforces it: `requireAuth()` + `where user_id = ${userId}`, not the UI. |

---
### ✅ Cook & Bake Academy after this lab
A `/dashboard` route is gated behind auth — signed-out visitors are redirected to log in.
