#!/usr/bin/env python3
"""Generate the C1143 Learner Guide as BOTH a Markdown mirror and a
DOCX, from one source, so they can never diverge.

House format: cover page, Document Version Control Record, auto TOC, Arial 11pt
body, one section per topic (key concepts explained, then every lab as
Objective · Goal · What you'll build · Step-by-step with code · Test it ·
Watch out for), plus environment setup, the AI React Bug Checklist,
a troubleshooting table and a glossary.

All content is driven by course_data + the domain data files, keeping the LG
100% aligned with the slide deck, the Lesson Plan and the labs/ folder.
"""
import os, sys
from docx import Document
from docx.shared import Pt, RGBColor

HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import course_data as C
from data_domain1 import DOMAIN1; from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3; from data_domain4 import DOMAIN4
from data_domain5 import DOMAIN5; from data_domain6 import DOMAIN6
from concepts import CONCEPT_SLIDES
from deep_dives import DEEP_DIVES
ACT=DOMAIN1+DOMAIN2+DOMAIN3+DOMAIN4+DOMAIN5+DOMAIN6
import prodoc
REPO=os.path.dirname(os.path.dirname(HERE)); ASSETS=os.path.join(REPO,"courseware","assets")

# ---------------- per-topic teaching prose ----------------
TOPIC_INTRO = {
1: ["Vibe coding means building software by prompting an AI agent — but the skill this course "
    "teaches is not prompting. It is reading. An agent will hand you working React in seconds, and "
    "it will just as cheerfully hand you code that is subtly, expensively wrong. Every lab in this "
    "course therefore runs the same five-step loop: Prompt, Generate, Read, Understand, Correct.",
    "In this topic you scaffold the project, generate your first component, and vibe-code a whole "
    "landing page. Then you stop and audit what the agent produced. It works — and it contains two "
    "deliberate design flaws that Topic 3 will teach you to repair. Recognising them is the point."],
2: ["Code that only runs on your laptop is not software yet. This topic puts your app on the "
    "internet, and it introduces the habit that makes fast AI editing safe: commit before you "
    "prompt. Git is what lets you read exactly what the agent changed (git diff) and throw it away "
    "when it is wrong (git restore).",
    "You will also meet the security rule that governs the rest of the course. Vite compiles every "
    "VITE_-prefixed environment variable straight into the JavaScript bundle the browser downloads. "
    "A VITE_ variable is therefore public by definition, and can never hold a secret."],
3: ["Topic 1 left you with a page that works and code that does not scale: every component crammed "
    "into one file, and six copy-pasted course cards. This topic repairs both, and in doing so "
    "teaches the ideas the whole library rests on.",
    "The central insight is that React is declarative. You never tell the browser how to change the "
    "page. You describe what the page should look like for the current state, and React compares "
    "that description against the previous one and applies the smallest possible set of real DOM "
    "edits. Everything else — JSX, props, keys, controlled inputs — follows from that one idea."],
4: ["A component that cannot remember anything can only ever render. Hooks give components memory "
    "(useState), a way to reach the outside world (useEffect), an escape hatch to the real DOM "
    "(useRef), and a way to share both state (useContext) and logic (custom hooks).",
    "Two ideas cause almost every hook bug. First, state is a snapshot: within one render, `count` "
    "never changes, which is why setCount(count + 1) twice only adds one. Second, an effect that "
    "starts something must be able to stop it: the function you return from useEffect is the "
    "cleanup, and React's StrictMode deliberately runs your effects twice in development to expose "
    "the ones that forgot it."],
5: ["Until now Cook & Bake Academy has been a pretend app: the 20-course catalogue lived in a "
    "JavaScript array and an enrolment vanished when you closed the tab. This topic gives it a real "
    "backend — a serverless API of your own over a Postgres database on Neon.",
    "The shape is three tiers: the browser calls your /api/* functions, and only those functions "
    "talk to Postgres. The connection string lives in the server's environment and never reaches "
    "the browser — which is the whole reason it must never carry a VITE_ prefix, since everything "
    "prefixed VITE_ is compiled into the bundle every visitor downloads.",
    "The network is not your computer. It is slow, it fails, and it answers out of order. Every "
    "remote read therefore has three states — loading, error and success — and AI-generated code "
    "reliably writes only two of them. And fetch does not reject on a 404 or 500; only a network "
    "failure rejects, so you must check response.ok.",
    "Finally, you will learn where security actually lives. Queries are parameterised tagged "
    "templates, so a value can never become SQL. Passwords are stored as bcrypt hashes, never in "
    "the clear. And a user's identity comes from the signed JWT the API verifies — never from the "
    "request body — with ownership of a row enforced in the SQL itself (and user_id = ${userId}). "
    "A client-side check is a convenience; the check inside the API route is the boundary."],
6: ["A real application has more than one page. React Router turns your single HTML document into "
    "a multi-page experience: the URL changes, the view swaps, and the server is never asked for a "
    "new document.",
    "Two lessons matter most here. Put filter state in the URL, not in a component, so a filtered "
    "view is shareable, bookmarkable and survives the back button. And when you guard a route "
    "behind authentication, wait for the session to finish loading before you redirect — otherwise "
    "a signed-in user is bounced to /login on every single refresh. That guard is user experience, "
    "not security; the database policies you wrote in Topic 5 are what actually protect the data."],
}

# ---------------- per-lab pitfall ----------------
PITFALL = {
"1.1": "If `npm create vite` fails, check `node --version` is 20 or newer. Vite will not run on Node 18.",
"1.2": "JSX is not HTML: it is `className`, not `class`, and a component must return a single root element (use a `<>…</>` Fragment if you need two).",
"1.3": "The AI's code works, but it is one giant file with six copy-pasted cards. Do not 'fix' it yet — Labs 3.2 and 3.3 exist precisely to repair those two smells.",
"2.1": "Never commit `.env.local`. A secret pushed to GitHub stays in the history forever — rotating the credential is the only real fix.",
"2.2": "A `VITE_`-prefixed variable is compiled into the browser bundle. It is public. Your Neon `DATABASE_URL` must never be one.",
"2.3": "GitHub Pages serves from `/<repo>/`, so a default `base` of `/` gives a blank page with 404s on every asset.",
"3.1": "`dangerouslySetInnerHTML` turns off the escaping that protects you from XSS. JSX escapes values for you — let it.",
"3.2": "Props are read-only. If a child needs to change something, the parent passes a callback down; the child never writes to a prop.",
"3.3": "`key={index}` looks fine until you delete or reorder a row, at which point React reuses the wrong DOM node and state sticks to the wrong card. And `{seats && …}` renders a literal 0, because 0 is falsy but is not `false`.",
"3.4": "Never mirror derived state into `useState` + `useEffect`. If the filtered list can be computed from `courses` and `query` during render, compute it during render.",
"4.1": "`cart.push(id)` mutates the array and does not re-render. Build a new one: `[...cart, id]`. And when the next state depends on the previous, use the updater form `setCart(prev => …)`.",
"4.2": "An effect that starts a timer, a subscription or a listener must return a cleanup function that stops it. StrictMode runs effects twice in development on purpose, to make the missing cleanup obvious.",
"4.3": "Changing `ref.current` does not re-render, and you must never read or write a ref during render. In React 19, `ref` is an ordinary prop — `forwardRef` is no longer needed, though most AI-generated code still uses it.",
"4.4": "Context is dependency injection, not a state manager. Guard the consumer hook so using it outside its provider throws a clear error rather than silently returning `undefined`.",
"4.5": "A custom hook shares logic, never state. Two components calling `useDebounce` each get their own independent state — this is the single most common misconception about hooks.",
"5.1": "The browser never talks to Postgres. `DATABASE_URL` lives only in the serverless function's environment — and it must NEVER carry a `VITE_` prefix, because every `VITE_` variable is compiled into the bundle each visitor downloads. Prove it to yourself: `grep` the built `dist/` for the value.",
"5.2": "`sql\\`... where slug = ${slug}\\`` is a tagged template, not string interpolation: the driver sends the SQL text and the value to Postgres separately, so Postgres parses the query before it ever sees the value. A value can therefore never become SQL. The moment you write `sql(\\`... '${slug}'\\`)` with parentheses, you have reopened the door — grep your `api/` folder for it.",
"5.3": "`fetch` does not reject on a 404 or a 500; only a network failure rejects. Check `response.ok`. Every remote read has three states — loading, error, success — and AI-generated code reliably writes two of them and forgets the error branch. Never make the `useEffect` callback itself `async`: it would return a Promise where React expects a cleanup function.",
"5.4": "Store a bcrypt hash, never the password, and never select `password_hash` into a response. The user id comes from the VERIFIED JWT (`sub`), never from `req.body` — if the body could name the user, anyone could enrol anyone. Enforce ownership in the SQL itself (`and user_id = ${userId}`), not in an `if`: an id in the URL is a request, not a permission.",
"6.1": "Use `<Link>`, never a plain `<a>`. An anchor triggers a full page reload, which throws away all your React state and refetches the whole bundle.",
"6.2": "Have the API return a real 404 when the slug matches nothing, and let the hook surface it — that is what lets you render a proper 'course not found' page instead of a spinner that never stops.",
"6.3": "Wait for `useAuth().loading` to become false before redirecting, or a signed-in user is bounced to `/login` on every refresh. And remember: anyone can edit your JavaScript, so this guard is UX only. The check inside the API route — user id from the token, ownership in the SQL — is the actual security boundary.",
"6.4": "Run the AI React Bug Checklist over your own code before you call the capstone done.",
"6.5": "Set `DATABASE_URL` and `JWT_SECRET` as Vercel environment variables (Production, encrypted). They are server-side only, so they never reach the browser. Confirm the SPA rewrite excludes `/api/*` — a catch-all to `index.html` will happily swallow every API route and hand your fetch an HTML page to parse.",
"6.6": "This is the mini-capstone — you drive it, mostly by prompting. The traps are the ones the course already taught: derive the average rating at render (never store it), handle the 23505 unique-violation on a second review, take the user id from the token and never from the body, gate writing behind auth, and enforce ownership in the SQL so one student cannot edit another's review. Probe your own new endpoint for injection before you call it done, then push so Vercel redeploys.",
}

# ---------------- block DSL (single content stream -> MD + DOCX) ----------------
B=[]
def h1(t): B.append(("h1",t))
def h2(t): B.append(("h2",t))
def h3(t): B.append(("h3",t))
def p(t):  B.append(("p",t))
def bullets(xs): B.append(("bullets",xs))
def steps(xs): B.append(("steps",xs))
def code(t): B.append(("code",t))
def note(t): B.append(("note",t))
def rule(): B.append(("rule",))
def dl(pairs): B.append(("dl",pairs))
def table(headers,rows): B.append(("table",headers,rows))

# ---------------- content ----------------
h1("Introduction")
p(f"This Learner Guide accompanies the course {C.TITLE} ({C.COURSE_CODE}), conducted by {C.ORG}. "
  f"It provides step-by-step instructions for all {len(ACT)} hands-on labs, organised by the six course "
  f"topics, together with an explanation of the key concept behind every lab.")
p(f"Across the course you build one application: {C.PROJECT}, a full-stack React course catalogue with a "
  "Neon Postgres database, user accounts, a private dashboard and a live public URL. Each topic adds a "
  "layer to the same app, so nothing you build is thrown away.")
p("You will build it the way software is increasingly built: by prompting an AI coding agent, then "
  "reading, understanding and correcting what it produces. That second half is the whole point. An agent "
  "will hand you working React in seconds. It will also hand you a key={index} that corrupts your list on "
  "delete, an effect that leaks a timer, and a database call that leaves the UI spinning forever on a typo. "
  "If you cannot read the code, you cannot ship it.")
note("Use this guide alongside the course slides and the lab folders in labs/ of the course repository. "
     "Every lab folder is a checkpoint containing a README and a drop-in src/ snapshot: if an AI edit breaks "
     "your app beyond repair, copy that lab's src/ over your own and carry on.")

h1("The Vibe Coding Loop")
p("Every lab in this course follows the same five steps. Learn the loop, not just the syntax.")
dl([("Prompt","Name the file, the exports, the props and the traps you already know about. A prompt that says "
                "'handle the error branch and clear loading in a finally' gets you code that does."),
    ("Generate","Let the agent write it. Speed is the point — this step should be seconds, not minutes."),
    ("Read","Audit the output against a checklist before you run it. Working is not the same as correct."),
    ("Understand","Learn the React concept underneath. This is the part that transfers to the next project."),
    ("Correct","Fix what the agent got wrong. Commit first, so git diff shows you exactly what changed.")])
p("The agent is a very fast junior developer with an excellent memory and no judgement. You supply the "
  "judgement.")

h1("Course Learning Outcomes")
bullets(C.LEARNING_OUTCOMES)

h1("Before You Start — Environment Setup")
h3("What you need")
bullets([
 "Node.js 20 or newer (22 recommended) — check with `node --version`.",
 "A code editor; VS Code is recommended.",
 "Git, and a GitHub account.",
 "An AI coding agent: Claude Code, Cursor or GitHub Copilot.",
 "A free Neon account (the Postgres database and authentication, from Topic 5).",
 "A free Vercel account (deployment, from Topic 2).",
])
h3("Scaffold the project")
code("npm create vite@latest cookbake -- --template react\n"
     "cd cookbake\n"
     "npm install\n"
     "npm install react-router-dom\n"
     "npm run dev")
h3("Set up the backend (needed from Topic 5 onward)")
bullets([
 "Create a free Neon project and copy its connection string (DATABASE_URL).",
 "Run neon/schema.sql once against that database. It creates the users, courses, enrolments and reviews tables and seeds the 20-course catalogue.",
 "The database is reached only from the serverless functions in api/ — never from the browser. Install the API-side packages: npm install @neondatabase/serverless bcryptjs jsonwebtoken.",
 "Copy .env.example to .env.local and set DATABASE_URL and JWT_SECRET. Neither is prefixed VITE_.",
 "For local API development, run the functions with `vercel dev` (or Vite's proxy to them); in production, set the same two variables as encrypted Vercel environment variables.",
])
h3("The one security rule")
p("The connection string (DATABASE_URL) and the signing secret (JWT_SECRET) live only on the server — inside the "
  "api/ functions — and must never appear in client code or in a VITE_-prefixed variable, because everything "
  "prefixed VITE_ is compiled into the JavaScript bundle that anyone can download and read. The browser only ever "
  "talks to your own /api/* routes. A user's identity comes from the signed JWT the API verifies, never from the "
  "request body, and ownership of a row is enforced in the SQL itself.")
h3("Conventions used in every lab")
bullets([
 "Shared files live only in the app: src/index.css (design tokens), src/data/courses.js (the 20-course catalogue used in Topics 1-4) and src/lib/api.js (the fetch wrapper that calls /api, created in Topic 5).",
 "The backend lives in api/ — serverless functions that own the database connection.",
 "Each lab folder holds a README.md and, where code changes, a drop-in src/ snapshot.",
 "Restore a checkpoint with: cp -R labs/<topic>/<lab>/src/. cookbake/src/",
 "Commit before you prompt. Inspect with `git diff`. Undo with `git restore .`",
])

# ---------------- foundations: how React really renders ----------------
h1("How React Really Renders: the DOM, the Virtual DOM and Babel")
p("This course assumes you already write modern JavaScript — arrow functions, destructuring, spread, map and "
  "filter, template literals and async/await. What makes React click is one layer down: what the DOM actually "
  "is, why updating it by hand hurts, how React's Virtual DOM avoids that, and how Babel turns the JSX you write "
  "into the plain JavaScript objects React works with.")
for cs in CONCEPT_SLIDES[0]:
    h2(cs["title"])
    p(f"Think of it like… {cs['analogy']}")
    bullets(cs["bullets"])
    if cs["code"]: code(cs["code"])
    note(cs["takeaway"])

# ---------------- per-topic, per-lab ----------------
for t in C.TOPICS:
    h1(f"Topic {t['code']} — {t['title']}")
    p(t["subtitle"])
    for para in TOPIC_INTRO[t["num"]]:
        p(para)
    h2(f"Key Concepts — Topic {t['code']}")
    dl([(c[0], c[1]) for c in t["concepts"]])

    # Every concept, explained: analogy, bullets, a worked snippet, and the takeaway.
    h2(f"Concepts Explained — Topic {t['code']}")
    for cs in CONCEPT_SLIDES.get(t["num"], []):
        h3(cs["title"])
        p(f"Think of it like… {cs['analogy']}")
        bullets(cs["bullets"])
        if cs["code"]: code(cs["code"])
        note(cs["takeaway"])

    # The long-form teaching payload for this topic.
    for dd in DEEP_DIVES.get(t["num"], []):
        h2(f"Deep Dive — {dd['heading']}")
        for para in dd["paras"]:
            p(para)
        if dd.get("bullets"): bullets(dd["bullets"])
        if dd.get("code"): code(dd["code"])

    for a in [x for x in ACT if x["topic"]==t["num"]]:
        h2(f"Lab {a['num']} — {a['title']}")
        p(f"Objective: {a['objective']}.")
        p(f"Goal: {a['desc']}")
        h3("What you'll build")
        p(a["build"] + f"   (Tech & files: {a['services']}.)")
        h3("Step-by-step")
        steps([(instr,cmd) for instr,cmd in a["steps"]])
        h3("Test it")
        p(a["test"])
        h3("Watch out for")
        p(PITFALL[a["num"]])
        rule()

# ---------------- appendices ----------------
h1("Appendix A — The AI React Bug Checklist")
p("This is the course in one page. Every item is a mistake AI coding agents reliably make, and every one of "
  "them appears in a lab. Run this list against generated code before you run the app.")
h3("Rendering")
bullets([
 "key={index} on a list — breaks on reorder, insert and delete. Use a stable id. (Lab 3.3)",
 "{count && <Badge/>} renders a literal 0, because 0 is falsy but not false. Use count > 0 && … (Lab 3.3)",
 "Mutating props or state — cart.push(x) does not re-render. Build a new array. (Labs 3.2, 4.1)",
 "dangerouslySetInnerHTML offered casually — it turns off the escaping that prevents XSS. (Lab 3.1)",
])
h3("State and effects")
bullets([
 "Derived state stored in useState + useEffect — compute it during render instead. The most common AI React mistake. (Labs 3.4, 4.2)",
 "setCount(count + 1) called twice only increments once. State is a snapshot; use setCount(c => c + 1). (Lab 4.1)",
 "useEffect with no cleanup — timers, subscriptions and listeners leak. StrictMode double-invokes effects to expose this. (Lab 4.2)",
 "Missing or wrong dependency array — useEffect(fn) with no array runs after every render. (Lab 4.2)",
 "forwardRef in React 19 — no longer needed; ref is an ordinary prop. (Lab 4.3)",
 "Reading or writing ref.current during render. (Lab 4.3)",
 "Assuming a custom hook shares state between components. It shares logic only. (Lab 4.5)",
 "Calling a data hook in two components — you get two divergent copies. Call it once, pass the pieces down. (Lab 5.3)",
])
h3("Data and the backend")
bullets([
 "No error state — every remote read has three states; agents write two. (Lab 5.1)",
 "response.ok unchecked — fetch does not reject on a 404 or a 500. (Lab 5.1)",
 "An async useEffect callback — it returns a Promise where React expects a cleanup function. (Lab 5.1)",
 "No AbortController — a stale response overwrites a fresh one. (Lab 5.1)",
 "String-concatenating a value into SQL — sql(`... '${x}'`) invites injection. Always use the sql`` tagged template so the value travels separately from the query. (Lab 5.2)",
 "The browser talking to Postgres directly — only the /api functions hold the connection; the browser calls /api. (Lab 5.1)",
 "DATABASE_URL or JWT_SECRET in client code, or any secret in a VITE_ variable — VITE_ values are compiled into the public bundle. (Labs 2.2, 5.1)",
 "Storing a password instead of a bcrypt hash, or selecting password_hash into a response. (Lab 5.3)",
 "Trusting req.body for the user id — it comes from the verified JWT, never the request body. (Lab 5.4)",
 "Ownership checked in an if instead of the SQL — enforce `and user_id = ${userId}` in the WHERE clause. (Lab 5.4)",
 "No loading gate on the session — the first paint shows 'signed out' to a signed-in user. (Labs 5.3, 6.3)",
])
h3("Routing")
bullets([
 "<a href> instead of <Link> — a full page reload throws away all your React state. (Lab 6.1)",
 "A client-side guard mistaken for security — the API's token + ownership check is the real boundary. (Lab 6.3)",
 "Redirecting before auth resolves. (Lab 6.3)",
 "Deep links 404 on a static host — you need an SPA rewrite or a 404.html fallback. (Labs 2.2, 2.3, 6.5)",
 "Changing a VITE_ env var and expecting a live change — they are baked in at build time. (Labs 2.2, 6.5)",
])

h1("Appendix B — Troubleshooting")
table(["Symptom","Likely cause","Fix"],[
 ("A fetch to /api returns HTML, not JSON","The SPA rewrite is swallowing /api","Exclude /api from the rewrite: \"/((?!api/).*)\" (Labs 2.2, 6.5)"),
 ("Env var changes have no effect","VITE_ vars are baked in at build time","Restart the dev server locally; redeploy on Vercel"),
 ("500 from an /api route, logs say 'DATABASE_URL undefined'","The function has no env var","Set DATABASE_URL (and JWT_SECRET) in .env.local locally and in Vercel for production"),
 ("Loading skeleton never stops","A rejected fetch with no catch/finally, or response.ok unchecked","Check response.ok; handle the error branch; clear loading in a finally (Lab 5.2)"),
 ("'Objects are not valid as a React child'","Rendering an error object","Render error.message"),
 ("401 from a protected route while signed in","The Bearer token is missing or stale","api.js must attach the JWT from localStorage; sign in again if it was tampered with (Lab 5.4)"),
 ("A delete/patch returns 404 for a row you can see","Ownership check: it is not yours","The WHERE clause is `and user_id = ${userId}` — this is the guard working (Lab 5.4)"),
 ("Insert fails with code 23505","The unique (user_id, course_id) constraint","Already enrolled/reviewed — handle it gracefully (Labs 5.4, 6.6)"),
 ("Sign-up returns 409","The email is already registered","Log in instead, or use another email (Lab 5.3)"),
 ("Signed-in user bounced to /login on refresh","Guard redirects before loading is false","Wait for loading (Lab 6.3)"),
 ("Deep link 404s in production","No SPA fallback on the static host","Add the vercel.json rewrite (Labs 2.2, 6.5)"),
 ("Effect runs twice in development","StrictMode, on purpose","Add the missing cleanup"),
])

h1("Appendix C — Glossary")
dl([
 ("API route (serverless function)","A file in api/ that runs on the server, holds the database connection and answers a browser fetch. The backend tier."),
 ("Babel","The compiler that turns the JSX you write into plain JavaScript (React.createElement / jsx calls) the browser can run. Vite runs it for you."),
 ("bcrypt","A deliberately slow, salted, one-way password hash. You store the hash; you never store or return the password itself."),
 ("Cleanup function","The function returned from useEffect. React runs it before the next effect and on unmount."),
 ("Component","A JavaScript function that returns JSX. The unit of reuse in React."),
 ("Connection string (DATABASE_URL)","The credential that opens the database. It lives only on the server, never in client code, and never in a VITE_ variable."),
 ("Controlled input","An input whose value comes from state and whose onChange updates that state."),
 ("Custom hook","A function whose name begins with 'use' and which calls other hooks. Shares logic; each caller gets its own state."),
 ("Declarative","Describing what the UI should be for the current state, and letting React work out how to change the DOM."),
 ("Dependency array","The second argument to useEffect. None = every render; [] = once; [deps] = when deps change."),
 ("Derived state","A value computable from existing state. Compute it during render; do not store it."),
 ("DOM","The browser's live object tree of the page. The page you see IS the DOM; changing it is what makes the screen update."),
 ("JSX","The HTML-like syntax in .jsx files. Babel compiles it to function calls returning plain JavaScript objects."),
 ("JWT","A signed token proving who a user is. The browser sends it as a Bearer header; the API verifies the signature and reads the user id from it. Trust the token, not the request body."),
 ("key","The prop that gives React a stable identity for a list row across renders. Not merely 'an id React needs'."),
 ("Lifting state up","Moving state to the closest common ancestor of the components that need it."),
 ("Parameterised query","sql`... where slug = ${slug}` — the value is sent to Postgres separately from the SQL, so it can never become SQL. The defence against injection."),
 ("Props","The arguments to a component. Read-only, and they flow one way: parent to child."),
 ("Reconciliation","React diffing the new Virtual DOM tree against the previous one and patching only the difference."),
 ("Ref","A mutable { current } box that survives re-renders and does not cause one when changed."),
 ("SPA","Single Page Application — one HTML document; JavaScript swaps the view and rewrites the URL."),
 ("Three-tier architecture","Browser → your /api functions → the database. The browser never talks to Postgres directly."),
 ("State","Data a component remembers between renders, and which triggers a re-render when it changes."),
 ("StrictMode","A development-only wrapper that double-invokes components and effects to surface missing cleanup."),
 ("Updater form","setCount(c => c + 1). Reads the latest value rather than the render's snapshot."),
 ("Virtual DOM","React's in-memory object tree describing the UI. Cheap to build and diff; the real DOM is what is expensive."),
])

# ---------------- render Markdown ----------------
def _anchor(txt):
    return "".join(ch.lower() if ch.isalnum() else ("-" if ch in " -" else "") for ch in txt)

def render_md():
    out=[f"# {C.TITLE} — Learner Guide",""]
    out.append(f"**Course Code:** {C.COURSE_CODE}  |  **Conducted by:** {C.ORG} ({C.UEN.replace('UEN: ','UEN ')})  |  **Version {C.VERSION} · {C.VERSION_DATE}**")
    out.append("")
    out.append("## Contents"); out.append("")
    for kind,*rest in B:
        if kind=="h1": out.append(f"- [{rest[0]}](#{_anchor(rest[0])})")
        elif kind=="h2": out.append(f"  - [{rest[0]}](#{_anchor(rest[0])})")
    out.append("")
    for kind,*rest in B:
        if kind=="h1": out+=["",f"## {rest[0]}",""]
        elif kind=="h2": out+=["",f"### {rest[0]}",""]
        elif kind=="h3": out+=[f"**{rest[0]}**",""]
        elif kind=="p": out+=[rest[0],""]
        elif kind=="bullets": out+=[f"- {x}" for x in rest[0]]+[""]
        elif kind=="steps":
            for i,(instr,cmd) in enumerate(rest[0],1):
                out.append(f"{i}. {instr}")
                if cmd: out+=["","   ```bash","   "+cmd,"   ```",""]
            out.append("")
        elif kind=="code": out+=["```bash",rest[0],"```",""]
        elif kind=="note": out+=[f"> **Note:** {rest[0]}",""]
        elif kind=="rule": out+=["---",""]
        elif kind=="dl":
            for term,defn in rest[0]: out.append(f"- **{term}** — {defn}")
            out.append("")
        elif kind=="table":
            headers,rows=rest
            out.append("| "+" | ".join(headers)+" |")
            out.append("|"+"---|"*len(headers))
            for r in rows: out.append("| "+" | ".join(r)+" |")
            out.append("")
    return "\n".join(out)

MD_OUT=os.path.join(REPO,"courseware",f"LG-{C.SHORT_TITLE}.md")
with open(MD_OUT,"w") as f: f.write(render_md())
print("Saved",MD_OUT)

# ---------------- render DOCX ----------------
BRAND=RGBColor(0x1F,0x6F,0xEB); GREY=RGBColor(0x55,0x5B,0x66)
INKCODE=RGBColor(0x0B,0x30,0x60)
doc=Document()
normal=doc.styles["Normal"]; normal.font.name="Arial"; normal.font.size=Pt(11)
prodoc.style_headings(doc)
prodoc.add_cover_page(doc,"LEARNER GUIDE",C.TITLE,C.VERSION.lstrip("v"),
                      org_logo=os.path.join(ASSETS,"tertiary-infotech-logo.png"),
                      course_logo=None, course_code=C.COURSE_CODE)
prodoc.add_version_control(doc,[
    ("2.0","12 July 2026","C1143 20-lab agentic-loop edition.",C.TRAINER),
    ("2.1","21 July 2026","Title, contents and schedule corrections.",C.TRAINER),
    (C.VERSION.lstrip("v"),C.VERSION_DATE,
     "Rebuilt on the flagship 2-day Full Stack React with Vibe Coding courseware: 25 hands-on labs across six topics "
     "building the Cook & Bake Academy app end to end, with key-concept explanations, deep dives, the AI React Bug "
     "Checklist, troubleshooting and a glossary. Non-assessed delivery.",C.TRAINER)])
prodoc.add_toc(doc)

def code_para(text):
    for line in text.split("\n"):
        para=doc.add_paragraph()
        r=para.add_run(line); r.font.name="Consolas"; r.font.size=Pt(9.5); r.font.color.rgb=INKCODE

for kind,*rest in B:
    if kind=="h1": doc.add_heading(rest[0],level=1)
    elif kind=="h2": doc.add_heading(rest[0],level=2)
    elif kind=="h3":
        para=doc.add_paragraph(); r=para.add_run(rest[0]); r.bold=True; r.font.size=Pt(11); r.font.color.rgb=BRAND
    elif kind=="p": doc.add_paragraph(rest[0])
    elif kind=="bullets":
        for x in rest[0]: doc.add_paragraph(x,style="List Bullet")
    elif kind=="steps":
        for i,(instr,cmd) in enumerate(rest[0],1):
            para=doc.add_paragraph(style="List Number"); para.add_run(instr)
            if cmd: code_para(cmd)
    elif kind=="code": code_para(rest[0])
    elif kind=="note":
        para=doc.add_paragraph(); r=para.add_run("Note: "); r.bold=True; r.font.color.rgb=BRAND
        para.add_run(rest[0]).font.size=Pt(10)
    elif kind=="rule": doc.add_paragraph("")
    elif kind=="dl":
        for term,defn in rest[0]:
            para=doc.add_paragraph(style="List Bullet")
            r=para.add_run(term+" — "); r.bold=True; para.add_run(defn)
    elif kind=="table":
        headers,rows=rest
        tb=doc.add_table(rows=0,cols=len(headers)); tb.style="Table Grid"
        hr=tb.add_row().cells
        for i,htext in enumerate(headers):
            hr[i].text=""; rr=hr[i].paragraphs[0].add_run(htext)
            rr.bold=True; rr.font.size=Pt(9.5); rr.font.color.rgb=RGBColor(0xFF,0xFF,0xFF)
            prodoc._shade_cell(hr[i],"1F6FEB")
        for row in rows:
            cells=tb.add_row().cells
            for i,val in enumerate(row):
                cells[i].text=""; cells[i].paragraphs[0].add_run(str(val)).font.size=Pt(9)

prodoc.add_page_numbers(doc)
prodoc.enable_update_fields(doc)
DOCX_OUT=os.path.join(REPO,"courseware",f"LG-{C.SHORT_TITLE}.docx")
doc.save(DOCX_OUT)
print("Saved",DOCX_OUT)
