"""
SINGLE SOURCE OF TRUTH for the C1143 non-WSQ courseware.

Every artifact — the slide deck (PPT), Lesson Plan (LP), Learner Guide (LG)
and the labs/ folder — is generated from (or aligned to) the data in this
module, so titles, topic numbering, activities, learning outcomes and the
schedule can never drift apart.

Edit here, then re-run build_slides.py / build_lesson_plan.py /
build_learner_guide.py  (or ./build_courseware.sh).
"""

# ------------------------------------------------------------------ metadata
TITLE        = "AI Vibe Coding for React Development"
SHORT_TITLE  = "AI Vibe Coding for React Development"
COURSE_CODE  = "C1143"
VERSION      = "v3.0"
VERSION_DATE = "21 July 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 2

# The running project every lab builds on: the Cook & Bake Academy website —
# a cooking & bakery training centre with a 20-course catalogue (10 bakery,
# 10 cooking), enrolments and reviews. Built once, progressively, across all
# six topics, and deployed live at https://cookbake-academy.vercel.app
PROJECT      = "Cook & Bake Academy"
PROJECT_URL  = "https://cookbake-academy.vercel.app"

# Learners already know modern JavaScript (arrow functions, destructuring,
# map/filter, template literals, async/await). We do NOT re-teach it. Every
# minute goes on React itself, and on driving an AI agent to write it.
ASSUMED_KNOWLEDGE = (
    "Working JavaScript: arrow functions, destructuring, spread, map/filter, "
    "template literals, promises and async/await. This course teaches React, "
    "not JavaScript."
)

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Build a React web app using vibe coding — scaffold a Vite + React project, prompt an AI coding agent, and read, understand and correct the code it generates.",
    "LO2: Deploy a React web app to the cloud — version the project with Git and GitHub, produce a production build, and publish it to Vercel or GitHub Pages.",
    "LO3: Apply core React concepts — components, JSX and how Babel compiles it, the real DOM versus the Virtual DOM, props, composition, lists and keys, conditional rendering, events and controlled forms.",
    "LO4: Apply React Hooks — useState, useEffect with cleanup, useRef for direct DOM access, useContext, useReducer, and custom hooks that share logic.",
    "LO5: Integrate a backend API and database — build serverless API routes over Neon Postgres, fetch them from React with loading and error states, and add password hashing and JWT authentication.",
    "LO6: Implement real application navigation with React Router — routes, nested layouts, dynamic parameters, URL state and protected routes — and deploy the full-stack app.",
]

# ------------------------------------------------------------------ topics
# num, code, title, subtitle, weighting (= scope label), concept bullets
TOPICS = [
    dict(num=1, code="01",
         title="Build a React Web App Using Vibe Coding",
         short="Vibe Coding",
         subtitle="Vite · JSX · Components · Props · The Prompt → Read → Correct loop",
         weighting="3 labs · Day 1",
         concepts=[
            ("Vibe coding is a loop, not a shortcut", "Prompt → Generate → Read → Understand → Correct. The agent writes; you supply the judgement."),
            ("A component is just a function", "It takes props (its arguments) and returns JSX describing what the UI should look like."),
            ("JSX is not HTML", "It compiles to function calls returning plain JavaScript objects. Hence className, camelCase, one root element, and {} for expressions."),
            ("Props flow one way", "Parent to child, and they are read-only. A child never writes to a prop."),
            ("The entry point", "index.html holds <div id=\"root\">; main.jsx calls createRoot(...).render(<App/>) to mount React into it."),
            ("Never ship code you cannot read", "AI output that works is not the same as AI output that is correct. Audit it before you run it."),
         ]),
    dict(num=2, code="02",
         title="Deploy Your React Web App to the Cloud",
         short="Cloud Deployment",
         subtitle="Git & GitHub · Production builds · Vercel · GitHub Actions · Env vars",
         weighting="3 labs · Day 1",
         concepts=[
            ("Git is the vibe coder's safety net", "Commit before you prompt. git diff shows what the agent changed; git restore undoes it."),
            ("React compiles to static files", "npm run build produces dist/ — plain HTML, CSS and JS that any static host can serve."),
            ("Never commit secrets", "node_modules, dist and .env.local stay out of Git. A leaked credential in history is permanent."),
            ("VITE_ variables are public", "Anything prefixed VITE_ is baked into the browser bundle at build time. Change one and you must rebuild."),
            ("Deploy on every push", "Vercel rebuilds from GitHub automatically and gives every branch its own preview URL."),
            ("SPA deep links need a rewrite", "A static host looks for /courses on disk. Rewrite every path to /index.html or refreshing a route 404s."),
         ]),
    dict(num=3, code="03",
         title="Improving Your App by Learning Core React Concepts",
         short="Core React Concepts",
         subtitle="DOM vs Virtual DOM · Babel & JSX · Components & props · Lists and keys · Events & forms",
         weighting="4 labs · Day 1",
         concepts=[
            ("The DOM is the browser's object tree", "The page you see IS the DOM. Touching it directly is slow and easy to get wrong — document.getElementById, innerHTML, manual patching."),
            ("The Virtual DOM is React's plan", "React builds a lightweight JS object tree, diffs it against the previous one, and patches ONLY the real DOM nodes that actually changed."),
            ("Babel compiles JSX away", "The browser has never seen JSX. Babel rewrites <CourseCard fee={680}/> into React.createElement(...) — a plain function call returning a plain object. Vite runs Babel for you."),
            ("Declarative beats imperative", "You describe what the UI should be for the current state; React works out which DOM operations get there."),
            ("Composition over configuration", "The children prop lets a component wrap arbitrary content instead of growing endless options."),
            ("key is identity, not decoration", "It tells React which course card is which across renders. key={index} corrupts state on reorder or delete."),
            ("The 0 && footgun", "0 is falsy but not false, so {seats && <Badge/>} renders a literal 0. Write seats > 0 && ..."),
            ("Derived state must not be stored", "If a value can be computed from existing state during render, compute it. Do not mirror it into useState."),
         ]),
    dict(num=4, code="04",
         title="React Hooks (The Vibe Way)",
         short="React Hooks",
         subtitle="useState · useEffect · useRef · useContext · useReducer · Custom hooks",
         weighting="5 labs · Day 2",
         concepts=[
            ("The Rules of Hooks", "Call them at the top level of a component or another hook. React tracks hooks by call order."),
            ("State is a snapshot", "count does not change mid-render. Use the updater form setCount(c => c + 1) when the next state depends on the previous."),
            ("Immutable updates", "cart.push(x) does not re-render. Build a new array: [...cart, x]."),
            ("Every effect cleans up after itself", "Timers, subscriptions and listeners are torn down in the function useEffect returns. StrictMode double-invokes effects to expose the ones that don't."),
            ("useRef is an escape hatch to the real DOM", "Changing .current does NOT re-render. It is how you focus the search box, scroll to the course grid, or hold a timer id — the one sanctioned way to touch a DOM node directly."),
            ("ref vs state — the dividing line", "If changing it should redraw the screen, it is state. If it should not, it is a ref. Putting a timer id in state re-renders on every tick."),
            ("Context is dependency injection", "It removes prop drilling. useReducer names the actions that change state. Custom hooks share logic, never state."),
         ]),
    dict(num=5, code="05",
         title="Giving Your App a Backend API and a Database",
         short="Backend API & Neon",
         subtitle="Three tiers · Serverless API routes · Neon Postgres · SQL injection · Password hashing · JWT",
         weighting="4 labs · Day 2",
         concepts=[
            ("Three tiers, one rule", "Browser → your API → the database. The browser NEVER talks to Postgres. The connection string lives only on the server."),
            ("A VITE_ variable is public", "Anything prefixed VITE_ is compiled into the bundle every visitor downloads. DATABASE_URL must never carry that prefix — it holds the password."),
            ("Every remote read has three states", "Loading, error, success. AI-generated code writes two of them and forgets the error branch."),
            ("fetch does not reject on 404", "Only a network failure rejects. Check response.ok, or you will parse an error page and render nonsense."),
            ("Parameterised queries, always", "sql`... where slug = ${slug}` sends the value separately from the SQL. String-concatenating user input is how you get dropped tables."),
            ("Never store a password", "Store a bcrypt hash. If the table leaks, the hashes are useless. Never select the hash into a response."),
            ("Trust the token, not the body", "The user id comes from the verified JWT — never from the request body. Enforce ownership in the SQL: `and user_id = ${userId}`."),
         ]),
    dict(num=6, code="06",
         title="React Router for Real App Navigation",
         short="React Router & Deploy",
         subtitle="Routes · Layouts · Dynamic params · Protected routes · Deploy full stack",
         weighting="6 labs · Day 2",
         concepts=[
            ("A Single Page Application", "One HTML document. JavaScript swaps the view and rewrites the URL with no server round-trip."),
            ("<Link> not <a>", "A plain anchor reloads the page and throws away every piece of React state you were holding."),
            ("Layout routes and <Outlet/>", "A pathless parent route renders the shared chrome; <Outlet/> is where the matched child appears."),
            ("URL state beats component state", "Filters in ?category=Frontend are shareable, bookmarkable, and survive the back button and a refresh."),
            ("Wait for auth before you redirect", "The session resolves asynchronously. Guard on loading first, or a signed-in user is bounced to /login on every refresh."),
            ("A client guard is UX, not security", "Anyone can edit the JavaScript. The check inside the API route — user id from the verified token, ownership in the SQL — is what actually protects the data."),
         ]),
]

# ------------------------------------------------------------------ 2-day schedule
DAY_THEMES = {
    1: "Vibe Coding, Cloud Deployment & Core React",
    2: "Hooks, Data, Routing & Capstone",
}

# ------------------------------------------------------------------ the build story
# The deck is ONE continuous build of the Cook & Bake Academy website — from an empty
# folder to a deployed full-stack app with a real database. Each topic is a PHASE of
# that build. These strings frame every phase so the slides read as a story, not a
# taxonomy. The finished app the learners are building towards is live at PROJECT_URL.
#   phase   — the build milestone (what we make the app do in this phase)
#   so_far  — where the app is when this phase starts
#   now     — what we add in this phase
#   payoff  — what SkillForge can do once the phase is done
#   needs   — the React ideas this phase forces us to learn
BUILD = {
    1: dict(phase="Make the First Screen",
            so_far="You have an empty folder and a client brief: a website for a cooking & bakery school.",
            now="a vibe-coded landing page — the Cook & Bake navbar, hero and a grid of course cards",
            payoff="show a real bakery site in the browser, built from your own components",
            needs="components, JSX and props"),
    2: dict(phase="Put It on the Internet",
            so_far="The bakery site runs only on your laptop.",
            now="the exact same app live on a public URL, redeployed automatically on every git push",
            payoff="send the client a link to their running website",
            needs="Git, the production build and environment variables"),
    3: dict(phase="Make It Real, Not Hardcoded",
            so_far="The page is copy-pasted markup — six course cards typed by hand.",
            now="real components driven by data, all 20 courses rendered with map(), and a working Bakery/Cooking filter and search",
            payoff="add a course by editing data, not markup — and filter the catalogue as you type",
            needs="the real DOM vs the Virtual DOM, how Babel compiles JSX, composition, lists and keys, and events"),
    4: dict(phase="Make It Remember and React",
            so_far="A catalogue you can only look at — it forgets everything on refresh.",
            now="a shortlist of courses, a dark-mode theme, a search box that focuses itself, and reusable logic — all powered by hooks",
            payoff="shortlist courses, keep them across refreshes, toggle the theme, and jump to the grid",
            needs="the hooks: useState, useEffect, useRef (the DOM escape hatch), useContext, useReducer and custom hooks"),
    5: dict(phase="Give It a Real Backend",
            so_far="The 20 courses live in a JavaScript array and every enrolment vanishes when the tab closes.",
            now="a serverless API over a live Neon Postgres database, with real accounts, hashed passwords and JWTs",
            payoff="read the catalogue from Postgres, sign up, enrol, review — and have it all still be there tomorrow",
            needs="the three-tier split, API routes, parameterised SQL, bcrypt and JWT auth"),
    6: dict(phase="Ship a Real Product",
            so_far="A powerful single page over a real database.",
            now="a multi-page app with course detail pages and a private student dashboard, deployed to Vercel — then you add a whole feature yourself",
            payoff="navigate real routes, guard the dashboard, deploy the lot, and extend it on your own",
            needs="routing, dynamic params, protected routes — and everything you have learned"),
}

# ------------------------------------------------------------------ tooling
STACK = [
    ("Vite + React 19", "Function components and hooks only — no class components. Vite runs Babel to compile your JSX."),
    ("React Router 7", "Routes, nested layouts, dynamic params, protected routes."),
    ("Vercel Functions", "The backend tier: /api/* serverless routes. The only thing that holds the database password."),
    ("Neon Postgres", "Serverless Postgres. Reached over SQL from the API, never from the browser."),
    ("Plain CSS", "Design tokens in index.css — no CSS framework to learn."),
    ("Vercel", "Git-connected deployments, preview URLs and encrypted environment variables."),
    ("An AI coding agent", "Claude Code, Cursor or GitHub Copilot — the 'vibe' in vibe coding."),
]
