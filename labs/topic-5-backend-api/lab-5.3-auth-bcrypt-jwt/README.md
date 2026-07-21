# Lab 5.3 — Accounts: Password Hashing With bcrypt, Sessions With JWT

> **Topic 5** · ~60 min · Builds on Lab 5.2 (fetching from React)

### 📖 The build so far
By the end of Lab 5.2, the app read its catalogue live from Neon through the `/api` client — but everything was **public**. There are no accounts, no sign-in, no notion of "you". **In this lab you add:** authentication built by hand, the way it actually works. Three auth routes (`signup`, `login`, `me`) that store a bcrypt **hash** of the password and issue a signed **JWT**; and the browser side — an `AuthContext` that keeps the token, restores your session on refresh, and a sign-in form. By the end, users can create an account and stay signed in.

## What you will build

Real authentication across both tiers:

- **Server:** `api/auth/signup.js` (hash the password, create the user, issue a
  token), `api/auth/login.js` (verify with `bcrypt.compare`, issue a token),
  `api/auth/me.js` (verify the token, return the current user). These use the
  JWT helpers already shipped in `api/_lib/auth.js` in Lab 5.1 — now they get used.
- **Browser:** `src/context/AuthContext.jsx` (holds `user`, stores the JWT in
  localStorage, restores the session on boot), `src/components/AuthForm.jsx` (sign
  up / sign in), plus the `Navbar` and `main.jsx` wiring.

## Concepts you will meet

| Concept | In one line |
|---|---|
| bcrypt hashing | A deliberately **slow, salted, one-way** hash — you store the hash, never the password. |
| `bcrypt.compare` | Re-hashes the submitted password with the stored salt and compares in constant time. |
| JWT (JSON Web Token) | `header.payload.signature` — the payload is **readable**, the signature (made with `JWT_SECRET`) makes it **trustworthy**. |
| The `sub` claim | The user id lives in the **verified** token — never in a request body the caller can type. |
| Token in localStorage | Survives refresh; on boot the app calls `/api/auth/me` to have the server verify it. |
| Server-side validation | The `<input required>` is a convenience; anyone can `curl` the route, so the real checks are on the server. |

## Before you start

Have Lab 5.2 working (catalogue reads from Neon; both dev servers run). Copy this
lab in — the API routes go under `api/`, the React files under `src/`:

```bash
cp -R "labs/topic-5-backend-api/lab-5.3-auth-bcrypt-jwt/api/." cookbake/api/
cp -R "labs/topic-5-backend-api/lab-5.3-auth-bcrypt-jwt/src/." cookbake/src/
```

That adds `api/auth/{signup,login,me}.js`, `src/context/AuthContext.jsx`,
`src/components/AuthForm.jsx`, and updates `Navbar.jsx` and `main.jsx`. You
already ran `npm install bcryptjs jsonwebtoken` and generated a `JWT_SECRET` in
Lab 5.1.

> `JWT_SECRET` is server-side only (**no `VITE_` prefix**). Anyone who knows it
> can mint a valid token for *any* user and sign in as them, so treat it exactly
> like a password. If it isn't set, the routes throw on startup — that's
> `api/_lib/auth.js` refusing to run without it.

---

## Step 1 — Store a HASH, never the password (`signup`)

Open `api/auth/signup.js`. The line that matters:

```js
const passwordHash = await bcrypt.hash(password, 10)

const rows = await sql`
  insert into users (email, name, password_hash)
  values (${String(email).trim().toLowerCase()}, ${name}, ${passwordHash})
  on conflict (email) do nothing
  returning id::int as id, email, name, created_at
`
```

We **never** store the password. bcrypt is a deliberately **slow, one-way** hash:
you cannot turn the hash back into the password, and the cost factor (`10`, ~100ms
per hash) makes brute-forcing a stolen table painfully expensive. bcrypt also
**salts** each hash automatically, so two users with the same password get
different hashes and cracking one doesn't unlock the other.

Look at the `RETURNING` list: `id, email, name, created_at`. **`password_hash` is
not in it.** The hash never leaves this function — not in a response, not in a log.

`on conflict (email) do nothing` returns **zero rows** when the email is taken,
which is how we detect a duplicate in one round-trip and answer **409**:

```js
if (rows.length === 0) throw new HttpError(409, 'That email is already registered. Try signing in.')
```

A brand-new account shouldn't have to log in again, so we sign them straight in —
**201** with `{ token, user }`.

## Step 2 — Validate on the SERVER, because curl exists

`AuthForm` has `<input required minLength={8}>`, but that only helps honest users
in a browser. Anyone can `POST` straight to the URL and skip the form entirely:

```bash
curl -s -X POST http://localhost:3000/api/auth/signup \
  -H 'Content-Type: application/json' \
  -d '{"email":"","name":"","password":"123"}'
# {"error":"Email, name and password are all required."}
```

That is why the route re-checks everything server-side:

```js
if (!email || !name || !password) throw new HttpError(400, 'Email, name and password are all required.')
if (typeof password !== 'string' || password.length < 8) throw new HttpError(400, 'Password must be at least 8 characters.')
```

**HTML validation is UX; server validation is security.** The server check is the
real one.

## Step 3 — Verify with `bcrypt.compare`, one error for both failures (`login`)

Open `api/auth/login.js`. `password_hash` is selected **here and only here**,
because we need to compare against it — into a local variable, never into `res`:

```js
const rows = await sql`select id::int as id, email, name, password_hash, created_at from users where email = ${…}`
const user = rows[0]
const ok = user ? await bcrypt.compare(password, user.password_hash) : false

if (!ok) throw new HttpError(401, 'Invalid email or password.')
```

Two details do real security work:

- **`bcrypt.compare`** re-hashes the submitted password with the salt baked into
  the stored hash and compares in constant time. Never write
  `hash(password) === stored` yourself — bcrypt salts every hash so that is always
  false, and a plain `===` on secrets leaks information through *how long* it takes
  to fail.
- **One message for both failures.** "No such email" and "wrong password" return
  the *same* `401`. Split them and you hand an attacker a free tool to discover
  which emails have accounts.

## Step 4 — What a JWT is, and why it can't be forged

When login succeeds, `signToken(user)` (in `api/_lib/auth.js`) issues a **JWT**:

```js
jwt.sign({ sub: String(user.id), email: user.email, name: user.name }, JWT_SECRET, { expiresIn: '7d' })
```

A JWT is three base64 chunks: `header.payload.signature`. Paste one into
<https://jwt.io> and read it — the payload is only **encoded, not encrypted**, so
*anyone* can read it. Never put a secret in it. What makes it *trustworthy* is the
**signature**, computed with `JWT_SECRET`, which only the server knows. Change one
byte of the payload — say `sub` from your id to someone else's — and the signature
no longer matches, so verification throws. That is why the server can **trust
`sub`** and must **never trust `req.body.userId`**.

`requireAuth(req)` reads `Authorization: Bearer <token>`, verifies the signature,
and returns the user id as a number — throwing **401** for a missing header, a bad
signature, or an expired token:

```js
const payload = jwt.verify(token, JWT_SECRET)
return Number(payload.sub)   // the user's id — VERIFIED, not claimed
```

There is no hand-written "is it expired?" check — `jwt.verify()` does that and
throws `TokenExpiredError`. Hand-rolling expiry is how people ship tokens that
never die.

## Step 5 — `/api/auth/me`: verifying the token on every boot

Open `api/auth/me.js`. This answers "am I still signed in?" after a refresh:

```js
const userId = requireAuth(req)               // 401 if the token is bad/missing/expired
const rows = await sql`select id::int as id, email, name, created_at from users where id = ${userId}`
if (rows.length === 0) throw new HttpError(401, 'Your account no longer exists.')
```

The browser keeps the JWT in localStorage, which survives a reload — but *this*
page load has never had it checked. So on boot the app sends the token here to be
verified. Note it **re-reads the row from Postgres** rather than trusting the
name/email baked into the token days ago: a token for a since-deleted user must
not still work.

## Step 6 — The browser side: `AuthContext` + the token

Open `src/context/AuthContext.jsx` and `src/lib/api.js`. The token lives in
localStorage, and `api.js` attaches it to every request:

```js
...(token ? { Authorization: `Bearer ${token}` } : {})
```

On boot, `AuthContext` restores the session by asking the server to verify the
stored token:

```js
if (!getToken()) { setLoading(false); return }
try { const { user } = await api.get('/auth/me'); setUser(user) }
catch { clearToken(); setUser(null) }        // expired/tampered/deleted -> bin it
finally { setLoading(false) }
```

`loading` is **not optional**: without it the UI flashes "signed out" for a moment
on every refresh even for a logged-in user (and, in Lab 5.4, bounces them to
`/login`). `signIn` / `signUp` call the API and translate the result into
`{ data, error }` so `AuthForm` never has to wrap a call in `try/catch` just to
show a red message. **Signing out is purely client-side** — drop the token, forget
the user; there is no server session to destroy (that's what "stateless JWT"
means, and why the token has a short expiry).

## Step 7 — Wire the providers and the form

`main.jsx` wraps the app in `<AuthProvider>` (inside `ThemeProvider`, outside
`CartProvider`), so every component can read who's signed in. `AuthForm` is one
form with two modes; the **Name** field shows only in sign-up mode (the signup
route requires it). `Navbar` now shows **Sign out** when `user` is set and a
**Sign in** link when it isn't.

## Step 8 — Try it end to end

With both servers running, open the app, go to `/login`, and **Sign up** with a
name, email, and an 8+ char password. You're signed in immediately — the navbar
shows **Sign out**. Refresh the page: you **stay** signed in (that's `/auth/me`
verifying the stored token), with no flash. Now prove the security by hand:

```bash
# duplicate email -> 409
curl -s -X POST http://localhost:3000/api/auth/login -H 'Content-Type: application/json' \
  -d '{"email":"you@example.com","password":"wrong-password"}'
# {"error":"Invalid email or password."}   <- same message whether email exists or not

# tampered token -> 401 (change one character of a real token)
curl -s http://localhost:3000/api/auth/me -H 'Authorization: Bearer not.a.realtoken'
# {"error":"Invalid or expired session. Please sign in again."}
```

---

## 🎤 Vibe prompt

```text
In my three-tier app (React -> /api/* serverless -> Neon), add hand-rolled auth.
I have api/_lib/db.js (`sql` tagged template) and api/_lib/auth.js exporting
signToken(user), requireAuth(req) (returns the user id from a VERIFIED JWT `sub`),
toClientUser(user), sendError, readBody, requireMethod, HttpError. Use bcryptjs
and jsonwebtoken. Create three routes, each `export default async function
handler(req,res)` wrapped in try/catch ending in sendError:

1. api/auth/signup.js — POST {email,name,password}. Validate server-side (all
   required; password is a string >= 8 chars). Hash with bcrypt.hash(password, 10).
   Insert into users (email lowercased/trimmed, name, password_hash) with
   `on conflict (email) do nothing returning id::int as id, email, name, created_at`
   — NEVER return password_hash. Zero rows -> 409 "already registered". Else 201
   with { token: signToken(user), user: toClientUser(user) }.

2. api/auth/login.js — POST {email,password}. Select id,email,name,password_hash by
   lowercased email. ok = user ? await bcrypt.compare(password, user.password_hash)
   : false. If !ok -> 401 with ONE message for both no-such-email and wrong-password.
   Else 200 { token, user }.

3. api/auth/me.js — GET. userId = requireAuth(req). Re-read the user row from the DB
   by id (do NOT trust the token payload). No row -> 401. Return { user:
   toClientUser(row) }.

Then a browser AuthContext (src/context/AuthContext.jsx): keep the JWT in
localStorage, on boot call GET /api/auth/me to restore the session (with a
`loading` flag so the UI doesn't flash signed-out), expose { user, loading,
signIn, signUp, signOut } where signIn/signUp POST and translate to { data, error }
and never throw, and signOut just clears the token. Never put JWT_SECRET or
DATABASE_URL in any src/ file.
```

## 🔍 Read what the AI wrote

- **Is the password ever stored in plain text?** Grep for the `insert into users`.
  It must store `password_hash` from `bcrypt.hash(password, 10)` — never `password`.
- **Does any response return `password_hash`?** Check every `RETURNING` and every
  `res.json`. Login selects the hash to compare, but it must never send it.
- **One login error, or two?** Separate "no such user" and "wrong password"
  messages are an account-enumeration leak. There must be one message for both.
- **Is the user id read from the token, not the body?** The dangerous pattern is a
  protected route trusting `req.body.userId` / a query param. Identity must come
  from `requireAuth(req)` (the verified `sub`).
- **Does `me` re-read the DB, or trust the token payload?** A token signed days ago
  may name a deleted user. It must re-query by id.
- **Is `loading` gating the UI in `AuthContext`?** Missing it is the classic
  "flash to signed-out on every refresh" bug.
- **Any secret in `src/`?** `JWT_SECRET` or `DATABASE_URL` in a browser file is a
  breach — reject it.

## 🧠 Why it works

**Hashing, not encryption.** Encryption is reversible — if you can decrypt it, so
can an attacker who steals the key. Passwords must **never** be reversible, so we
*hash*: a one-way function you cannot run backwards. bcrypt adds two things a plain
SHA-256 lacks. It is **slow by design** (the cost factor), so an attacker who
steals the table can only try a few thousand guesses a second instead of billions.
And it **salts** every hash with random bytes stored alongside it, so identical
passwords produce different hashes — a precomputed "rainbow table" is useless, and
cracking one account tells you nothing about another. You store the hash; the
plaintext password exists for a few milliseconds inside the request and is then
gone.

**`bcrypt.compare`, and why not `===`.** At login you can't "un-hash" the stored
value to check it. Instead `bcrypt.compare(submitted, stored)` reads the salt out
of the stored hash, re-hashes the submitted password with that same salt, and
compares the results — in **constant time**, so an attacker can't learn anything
from timing. Writing `hash(password) === stored` yourself fails twice over: it
re-salts randomly (so it's always false), and `===` on secret material short-
circuits at the first differing byte, leaking how much of a guess was right.

**A JWT trades server memory for a signature.** The old way to track "who's signed
in" was a session table the server looks up on every request. A JWT flips that: the
server signs a small token that *states* who you are and hands it to the client,
which sends it back on every request. The server keeps **no** session state — it
just re-verifies the signature. The payload (`sub`, `email`, `name`, `exp`) is
plain base64, readable by anyone, which is why it holds only an identity claim and
never a secret. The **signature** is an HMAC over the payload using `JWT_SECRET`.
Verifying it proves two things at once: the payload wasn't altered, and it was
issued by someone who holds the secret — i.e. us. Change the `sub` to another
user's id and the signature no longer matches, so `jwt.verify` throws and the
request is refused. This is the whole reason the server can trust `sub` and must
never trust a user id that arrives in the request body.

**Identity comes from the token, full stop.** Every protected route derives the
user id from `requireAuth(req)`, which returns the **verified** `sub`. It is not
`req.body.userId` and not a query param — those are just things the caller typed.
If `signup` or a future enrol route trusted a body field for identity, anyone with
curl could act as anyone. Centralising this in one helper means no route can get it
wrong by accident.

**Why `me` exists and re-reads the DB.** localStorage survives a refresh, but the
*server* has never seen this page load's token before, so the app can't assume it's
valid — it asks `/auth/me` to verify it and hand back fresh user details. And it
re-queries Postgres rather than trusting the token's baked-in name/email, because
the token was signed days ago: the user may have changed their name, or been
deleted. A token for a deleted user must stop working, and re-reading the row is
what guarantees that.

**Why `loading` is mandatory in the client.** Auth state isn't known
synchronously — on boot the app has to round-trip to `/auth/me` before it knows
whether you're signed in. Treat "not resolved yet" as "signed out" and every
refresh flashes the logged-out UI at logged-in users. Modelling it as a third
state — *don't know yet* — and holding the UI until it resolves is what separates
correct auth from the demo that "works on my machine". It's the same three-states
discipline from Lab 5.2, now applied to identity.

## ✅ Check your work

- [ ] Signing up creates a user whose `password_hash` is a bcrypt string, and the
      response contains **no** `password_hash` (check the Network tab).
- [ ] Signing up with an existing email returns **409**; a wrong password returns
      **401** with the *same* message as an unknown email.
- [ ] After signing in, refreshing the page keeps you signed in with **no** flash
      to "Sign in".
- [ ] A tampered `Authorization` token gets **401** from `/api/auth/me`.
- [ ] No file under `src/` references `JWT_SECRET` or `DATABASE_URL`.
- [ ] You can explain why the JWT payload is safe to read but the signature can't
      be forged.

## 🛠 Your turn

1. Add a `PATCH /api/auth/me` (or `api/auth/profile.js`) that lets a signed-in user
   change their `name`. Derive the id from `requireAuth(req)` — never from the body —
   and return `toClientUser` of the updated row.
2. Shorten the token to `expiresIn: '30s'`, sign in, wait, then trigger a request:
   watch `/auth/me` return 401 and the app sign you out. Confirm `jwt.verify` — not
   any code you wrote — is what enforced the expiry. Then set it back to `7d`.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `JWT_SECRET is not set` thrown at startup | Missing from `.env.local`, or `vercel dev` wasn't restarted. | Add `JWT_SECRET` (no `VITE_`) and restart `npx vercel dev`. |
| Login always fails even with the right password | You hashed at login and compared strings, or stored the password unhashed. | Store `bcrypt.hash` at signup; verify with `bcrypt.compare` at login. |
| `password_hash` shows up in a response | It's in a `RETURNING`/`res.json`. | Return only `toClientUser(...)` fields; select the hash into a local var only. |
| UI flashes "Sign in" on every refresh | Rendered before `loading` (the `/auth/me` round-trip) resolved. | Gate the account UI on `loading`. |
| `401` on every protected call after signing in | The token isn't attached, or `AuthProvider` is mis-placed. | Ensure `api.js` sends `Authorization: Bearer` and `<AuthProvider>` wraps `<App/>`. |
| Signing up twice with one email 500s instead of 409 | Missing `on conflict (email) do nothing` / zero-rows check. | Use the conflict clause and throw 409 when no row returns. |

---
### ✅ Cook & Bake Academy after this lab
Visitors can create an account and sign in; passwords are stored as bcrypt hashes and sessions are carried by a signed JWT the server verifies on every request.
