"""
Concept-slide DATA for the C1143 courseware (deep-teaching deck).

Pure data. No imports, no logic. One dict, CONCEPT_SLIDES, keyed by topic
number (0 = the "how React actually works" foundation mini-section, 1..6 = the
six course topics). Each value is a list of concept-slide dicts of the shape:

    dict(title, kicker, analogy, bullets=[...], code, takeaway)

Titles are <= 46 chars, bullets <= 105 chars, code lines <= 78 chars.
Every slide carries a concrete analogy and a one-line takeaway.

Learners arrive already knowing modern JavaScript (arrow functions,
destructuring, spread, map/filter, template literals, async/await). There is NO
JavaScript refresher anywhere in this deck. Topic 0 spends that time on the
three things that actually demystify React: the real DOM, the Virtual DOM, and
what Babel does to JSX before the browser ever sees it.

This course teaches React 19 (ref is a normal prop, no forwardRef) and a
THREE-TIER backend:

    React (browser) --fetch--> /api/* (Vercel functions) --sql--> Neon Postgres

The browser never talks to Postgres. There is no browser-side Data API, no
Neon Auth, no GRANTs and no Row Level Security in this app: the serverless
functions hold DATABASE_URL, run parameterised SQL, hash passwords with bcrypt,
and enforce ownership in the WHERE clause using a user id read from a verified
JWT.

Every example is from the real, deployed Cook & Bake Academy app
(https://cookbake-academy.vercel.app) — a cooking & bakery training centre with
a 20-course catalogue, enrolments and reviews.
"""

CONCEPT_SLIDES = {

    # ============================== TOPIC 0 — how React actually works
    0: [
        dict(
            title="The DOM is the browser's object tree",
            kicker="FOUNDATIONS · THE REAL DOM",
            analogy="The DOM is not a picture of the page — it IS the page, a live model you can reach in and edit.",
            bullets=[
                "When the browser parses HTML it builds the DOM: a live tree of objects, one per element.",
                "The page you see on screen is a picture of that tree. Change the tree and the screen changes.",
                "JavaScript can reach into it: document.getElementById returns the real object for one node.",
                "Every element node has properties you can write — textContent, className, style, value.",
                "React does not replace the DOM. It manages it for you, so you stop writing the code below.",
            ],
            code="""
// The DOM is a real, live object you can hold:
const el = document.getElementById('count')

el.textContent = '19'         // the screen updates
el.className = 'badge is-on'  // so does this
""",
            takeaway="The DOM is the browser's live object tree — the page itself, not a copy.",
        ),
        dict(
            title="Updating the page without React",
            kicker="FOUNDATIONS · BY HAND",
            analogy="Manual DOM work is giving turn-by-turn directions from memory — miss one turn and nobody notices until you are lost.",
            bullets=[
                "Without React you must say HOW to update: find the node, then overwrite each property by hand.",
                "You write the change twice — once in the markup, once in the patch code — and they drift apart.",
                "The data now lives in a DOM string. Reading '19' back out and adding to it is your problem.",
                "Add a filter, a search box and a shortlist and every one of them must patch every affected node.",
                "Twenty course cards, four fields each: eighty little patches you have to remember to keep in step.",
            ],
            code="""
// Vanilla JS: filter the catalogue by hand.
function showBakery() {
  const cards = document.querySelectorAll('.card')
  cards.forEach((card) => {
    const isBakery = card.dataset.category === 'Bakery'
    card.style.display = isBakery ? 'block' : 'none'
  })
  document.getElementById('count').textContent = '10 courses'
  // ...and now update the chip, the heading, the empty
  // state, the URL... every one, every time, by hand.
}
""",
            takeaway="Hand-patching the DOM means saying HOW, everywhere, forever — and it does not scale.",
        ),
        dict(
            title="The Virtual DOM is React's plan",
            kicker="FOUNDATIONS · VIRTUAL DOM",
            analogy="The Virtual DOM is an architect's drawing — React compares the new plan to the old before knocking down a single real wall.",
            bullets=[
                "The Virtual DOM is a lightweight tree of plain JavaScript objects describing what the UI should be.",
                "It is cheap: making one is just allocating objects. Touching the REAL DOM is what costs.",
                "On every render React builds a fresh virtual tree for the current state.",
                "Reconciliation is the diff: it compares the new tree with the previous one, node by node.",
                "It then patches ONLY the real DOM nodes that actually changed, and leaves the rest alone.",
            ],
            code="""
// State changes: 20 courses -> 10 (Bakery only).
// React builds a NEW virtual tree, diffs it, and
// concludes: remove 10 <article> nodes, and set one
// text node from '20 courses' to '10 courses'.
//
// It does NOT rebuild the navbar, the hero, the
// footer or the surviving cards. They did not change.
""",
            takeaway="React diffs a cheap JS tree, then patches only the real nodes that changed.",
        ),
        dict(
            title="Real DOM vs Virtual DOM, side by side",
            kicker="FOUNDATIONS · THE CONTRAST",
            analogy="Imperative is reciting the recipe step by step; declarative is ordering the dish and letting the kitchen work out the steps.",
            bullets=[
                "Imperative (no React): you locate nodes and mutate them. You own every step of HOW.",
                "Declarative (React): you describe WHAT the UI is for the current state. React works out the steps.",
                "The React version has no getElementById, no textContent and no className assignment anywhere.",
                "Because the UI is recomputed from state every time, it can never silently drift out of sync.",
                "Your job shrinks to one thing: keep the state correct, and describe the UI as a function of it.",
            ],
            code="""
// WITHOUT React — you patch the real DOM yourself:
const el = document.getElementById('seats')
el.textContent = String(seats)
el.className = seats > 0 ? 'badge' : 'badge is-full'

// WITH React — you describe the result, once:
<span className={seats > 0 ? 'badge' : 'badge is-full'}>
  {seats}
</span>
""",
            takeaway="Stop describing HOW to change the page; describe WHAT it should be.",
        ),
        dict(
            title="Babel: the browser never sees JSX",
            kicker="FOUNDATIONS · BABEL",
            analogy="Babel is the translator in the booth — you speak JSX, the browser only ever hears JavaScript.",
            bullets=[
                "JSX is not valid JavaScript. Paste it into a browser console and you get a syntax error.",
                "Babel is a compiler that rewrites your JSX into ordinary function calls before it ships.",
                "Vite runs Babel for you through @vitejs/plugin-react — it is why the plugin is in vite.config.js.",
                "<CourseCard fee={680}/> becomes React.createElement(CourseCard, { fee: 680 }).",
                "That call is not markup and it is not a DOM node. It returns a plain JavaScript OBJECT.",
            ],
            code="""
// YOU WRITE (JSX):
<CourseCard course={course} fee={680} />

// BABEL COMPILES IT TO (plain JavaScript):
React.createElement(CourseCard, { course: course, fee: 680 })

// WHICH RETURNS (a plain object — this is a React element):
{ type: CourseCard, props: { course: {...}, fee: 680 } }
""",
            takeaway="JSX is sugar. Babel turns every tag into a call that returns a plain object.",
        ),
        dict(
            title="Why that one fact explains everything",
            kicker="FOUNDATIONS · JSX RULES",
            analogy="Once you know JSX is JavaScript in a costume, its 'weird' rules stop being rules and become consequences.",
            bullets=[
                "You write className, not class, because class is a reserved word in JavaScript.",
                "Attributes are camelCase (onClick, htmlFor) because they are really keys in a props object.",
                "{} is a window for an EXPRESSION — a value. An if or a for produces no value, so it cannot fit.",
                "One root element per return, because a JavaScript function returns exactly one value.",
                "Capitalised names, because createElement('div') means a tag but createElement(CourseCard) means YOUR function.",
            ],
            code="""
<h3 className="card__title">{course.title}</h3>
// -> createElement('h3', {className:'card__title'}, ...)
//    lowercase string 'h3'  = a real HTML tag

<CourseCard course={course} />
// -> createElement(CourseCard, {course})
//    capitalised IDENTIFIER = your function
""",
            takeaway="Every JSX rule falls out of one fact: it compiles to createElement calls.",
        ),
    ],

    # ===================================================== TOPIC 1 — Vibe coding
    1: [
        dict(
            title="Vibe coding is a loop, not magic",
            kicker="TOPIC 01 · THE LOOP",
            analogy="Vibe coding is flying with autopilot on — you still watch the instruments and take the controls the moment something drifts.",
            bullets=[
                "The loop is Prompt, Generate, Read, Understand, Correct — the agent writes, you supply the judgement.",
                "An AI agent produces working React in seconds, but 'working' and 'correct' are not the same thing.",
                "The value you add is reading the output against a checklist and knowing the concept underneath it.",
                "Every lab in this course repeats the same five steps so the habit becomes automatic.",
                "By the end you should build fast and be able to say exactly why every line is there.",
            ],
            code="""
// The five-step loop, every lab:
//   1 Prompt   2 Generate   3 Read
//   4 Understand            5 Correct
//
// The agent writes. You supply the judgement.
""",
            takeaway="Speed comes from the agent; correctness comes from you reading it.",
        ),
        dict(
            title="A component is just a function",
            kicker="TOPIC 01 · COMPONENTS",
            analogy="A component is a cookie cutter: define the shape once, stamp out as many cookies as you like.",
            bullets=[
                "A React component is a JavaScript function that returns JSX describing a piece of the UI.",
                "Its name must start with a capital letter, or Babel compiles it to a literal HTML tag instead.",
                "You use it by writing it like a tag: <CourseCard /> calls the function and renders what it returns.",
                "Because it is a function, you reuse it by calling it many times, each with different props.",
                "This course uses function components and hooks only — never class components.",
            ],
            code="""
function CourseCard() {
  return <h3>Artisan Sourdough Bread Baking</h3>
}

<CourseCard />
""",
            takeaway="Capitalised function in, JSX out — that is the whole idea.",
        ),
        dict(
            title="What a component really is",
            kicker="TOPIC 01 · COMPONENTS",
            analogy="A component is a vending machine: press the same buttons (props) and the same snack (UI) always drops out.",
            bullets=[
                "A component is a plain function: it takes props in and returns one JSX tree describing the UI.",
                "It must return a single root — one tree — because a JavaScript function returns exactly one value.",
                "A component should be pure: given the same props, it must always return the same output.",
                "Purity means no surprises in render — no fetching, timers or mutation; those belong in effects.",
                "Purity is what lets React render it as often as it likes, and trust the result every time.",
            ],
            code="""
function CourseCard({ title }) {
  return <h3>{title}</h3>   // one tree, no side effects
}

// same title in -> same markup out, every time
""",
            takeaway="Same props in, same tree out — a capitalised, pure function.",
        ),
        dict(
            title="JSX is a blueprint, not HTML",
            kicker="TOPIC 01 · JSX",
            analogy="JSX is a blueprint, not the building — React reads it and constructs the real DOM from the instructions.",
            bullets=[
                "JSX looks like HTML but is not — Babel compiles it to createElement calls that return objects.",
                "Those objects describe what the UI should look like; React turns them into real DOM nodes for you.",
                "Because it is really JavaScript, HTML's class becomes className and attributes become camelCase.",
                "Understanding that JSX is code, not markup, explains every rule that follows in this topic.",
                "You never call createElement by hand — Vite runs Babel — but knowing it is there demystifies JSX.",
            ],
            code="""
const el = <h1 className="brand">Cook &amp; Bake</h1>

// Babel compiles it to:
React.createElement('h1', { className: 'brand' },
                    'Cook & Bake')
""",
            takeaway="JSX compiles to createElement calls returning plain JS objects, not HTML.",
        ),
        dict(
            title="One root element and Fragments",
            kicker="TOPIC 01 · RETURN SHAPE",
            analogy="One root is a single moving box React hands back — not an armful of loose items; a Fragment is a box with no cardboard.",
            bullets=[
                "A component must return a single root element, because a function returns exactly one value.",
                "Wrapping siblings in an extra <div> works but litters the page with meaningless containers.",
                "A Fragment (<>...</>) groups siblings under one root while adding no node to the real DOM.",
                "Reach for a Fragment whenever a wrapper div would only exist to satisfy this one-root rule.",
                "Returning two adjacent tags with no wrapper is a syntax error the agent will sometimes produce.",
            ],
            code="""
// RootLayout.jsx — the real app shell
return (
  <>
    <Navbar />
    <main><Outlet /></main>
    <Footer />
  </>
)   // one root; <> adds no extra div
""",
            takeaway="Return one root; use a Fragment to group without an extra div.",
        ),
        dict(
            title="Curly braces embed expressions",
            kicker="TOPIC 01 · EXPRESSIONS",
            analogy="Curly braces are a window cut into your markup — JavaScript shows through, but only values, never statements.",
            bullets=[
                "Inside JSX, {} drops the result of a JavaScript expression into the output.",
                "An expression produces a value: a variable, a call, a ternary, a template literal all qualify.",
                "A statement such as if, for or a variable declaration does not — it produces no value and errors.",
                "This is why you use a ternary or && inside JSX rather than an if statement.",
                "The braces run the code every render, so what you see always reflects the current data.",
            ],
            code="""
<h1>Welcome to {academy}</h1>            // expression: ok
<span>S${course.fee}</span>              // expression: ok
<span>{isBakery ? '🧁 Bakery' : '🍳 Cooking'}</span>  // ok

<h1>{if (x) {}}</h1>                     // statement: error
""",
            takeaway="{} takes expressions (values), never statements like if or for.",
        ),
        dict(
            title="Props are a component's arguments",
            kicker="TOPIC 01 · PROPS",
            analogy="Props are a recipe card handed to a component: it reads the ingredients and cooks, but never edits the card.",
            bullets=[
                "A prop is a value passed into a component, exactly as you pass an argument to a function.",
                "You read props by destructuring them in the parameter list: function CourseCard({ course }).",
                "Give a default with = so a missing prop has a sensible value: ({ fee = 0 }).",
                "Props flow one way, parent to child, and they are read-only — a child must never reassign a prop.",
                "String props use quotes; any other type uses braces: title=\"Macaron Masterclass\" fee={420}.",
            ],
            code="""
function CourseCard({ title, fee = 0 }) {
  return <h3>{title} — S${fee}</h3>
}

<CourseCard title="Macaron Masterclass" fee={420} />
""",
            takeaway="Props are read-only arguments that flow down from parent to child.",
        ),
        dict(
            title="One object prop beats nine loose ones",
            kicker="TOPIC 01 · PROPS",
            analogy="Passing one course object is handing over the whole recipe card, not reading out nine ingredients down the phone.",
            bullets=[
                "The real CourseCard takes ONE prop — course — and destructures the fields it needs inside.",
                "That object's shape is the database row you will fetch in Topic 5, so nothing downstream changes.",
                "Nine separate props means nine things to keep in step at every call site. One object means one.",
                "Destructure inside the body when the object is the prop: const { slug, title, fee } = course.",
                "Collect leftover props with ...rest and spread them onward: <article {...rest}>.",
            ],
            code="""
// src/components/CourseCard.jsx (real code)
export default function CourseCard({ course }) {
  const { slug, title, category, level, fee } = course
  return <Link to={`/courses/${slug}`}>{title}</Link>
}

<CourseCard course={course} />
""",
            takeaway="Pass the whole object; its shape is the DB row, so the card never changes.",
        ),
        dict(
            title="The entry point: #root and main.jsx",
            kicker="TOPIC 01 · MOUNTING",
            analogy="index.html is an empty stage with one marked spot; main.jsx is the stagehand who mounts the whole React play onto it.",
            bullets=[
                "index.html is almost empty — its job is to provide one <div id=\"root\"></div>.",
                "main.jsx is the entry file: it imports App and mounts it into that root div.",
                "createRoot(...).render(<App/>) is the single call that hands the whole app over to React.",
                "This is the ONE place React touches the real DOM by hand. Everything below it is declarative.",
                "Knowing this chain explains where the app 'starts' when you read AI-scaffolded code.",
            ],
            code="""
// index.html
<div id="root"></div>

// src/main.jsx (real code)
createRoot(document.getElementById('root')).render(
  <StrictMode><App /></StrictMode>,
)
""",
            takeaway="main.jsx mounts <App/> into the single #root div in index.html.",
        ),
        dict(
            title="Never ship code you cannot read",
            kicker="TOPIC 01 · JUDGEMENT",
            analogy="AI code that runs is a contract you have not read — it may work today and cost you everything on the clause you skipped.",
            bullets=[
                "Code that compiles and renders can still hide bugs the agent has no way to notice.",
                "Run every generated file past a short checklist before you trust it in your project.",
                "Common landmines: key={index}, a useEffect with no cleanup, a fetch with no error branch.",
                "Also check that no secret has been placed in a VITE_ variable, where it becomes public.",
                "If you cannot explain why a line is there, you are not ready to ship it — that is the whole skill.",
            ],
            code="""
// Audit checklist before you run AI code:
//   - key={index} on a list?
//   - useEffect missing a cleanup return?
//   - fetch with no error state?
//   - a secret sitting in a VITE_ variable?
//   - SQL built by string concatenation?
""",
            takeaway="Audit generated code against a checklist before you trust it.",
        ),
    ],

    # ===================================================== TOPIC 2 — Deploy
    2: [
        dict(
            title="Git is the vibe coder's safety net",
            kicker="TOPIC 02 · GIT",
            analogy="Git is a video-game save point: commit before you prompt, and any bad edit is one 'load' away from undone.",
            bullets=[
                "Commit before you ask the agent to change anything, so you always have a clean point to return to.",
                "git diff shows exactly which lines the agent touched, line by line, before you accept them.",
                "git restore . throws away the working changes and puts you back at your last commit.",
                "Small, frequent commits make it obvious which prompt introduced which change.",
                "Without this habit, one confident-but-wrong AI edit can quietly break code you cannot recover.",
            ],
            code="""
git add -A && git commit -m 'before AI edit'

# prompt the agent, then review:
git diff              # what did it change?
git restore .         # undo if it went wrong
""",
            takeaway="Commit before you prompt; diff to review; restore to undo.",
        ),
        dict(
            title="React compiles to static files",
            kicker="TOPIC 02 · THE BUILD",
            analogy="npm run build is packing for a trip — your sprawling workshop becomes one sealed suitcase of plain files any host can carry.",
            bullets=[
                "npm run build bundles your source into a dist/ folder of plain HTML, CSS and JavaScript.",
                "Babel has already compiled every piece of JSX away — the shipped bundle contains no JSX at all.",
                "Those files are static: no Node server runs them, so any file host on earth can serve them.",
                "npm run preview serves the built dist/ locally so you can test the real production output.",
                "The API routes in api/ are NOT part of this bundle — Vercel deploys them as separate functions.",
            ],
            code="""
npm run build     # -> dist/ (html, css, js — no JSX)
npm run preview   # serve dist/ locally to test

# dist/assets/index-*.js is what every visitor
# downloads. Open it. Anything in there is public.
""",
            takeaway="A React build is a folder of static files any host can serve.",
        ),
        dict(
            title="Never commit secrets",
            kicker="TOPIC 02 · GITIGNORE",
            analogy="A secret in Git history is a postcard, not a letter — once written on the back, everyone down the line can read it forever.",
            bullets=[
                "A .gitignore lists paths Git must never track, keeping junk and secrets out of your history.",
                "Always ignore node_modules (huge, reinstallable), dist (rebuildable), and .env.local (secret).",
                "A credential committed even once lives in the history forever, even after you delete the line.",
                "If a secret is ever pushed, treat it as leaked: rotate it immediately, do not just remove it.",
                "Commit .env.example instead — the variable NAMES, with placeholder values and no real secrets.",
            ],
            code="""
# .gitignore
node_modules
dist
.env.local        # holds DATABASE_URL and JWT_SECRET

# .env.example    <- this one IS committed
DATABASE_URL=postgresql://USER:PASSWORD@...
JWT_SECRET=dev-secret-change-me
""",
            takeaway="node_modules, dist and .env.local never belong in Git history.",
        ),
        dict(
            title="VITE_ variables are public. Always.",
            kicker="TOPIC 02 · ENV VARS",
            analogy="A VITE_ variable is printed on the flyer, not whispered — baked into the bundle for anyone to read.",
            bullets=[
                "Vite exposes only variables prefixed VITE_ to browser code, via import.meta.env.VITE_SOMETHING.",
                "It SUBSTITUTES the value straight into the .js file it ships. It is not looked up at runtime.",
                "So a VITE_ variable is visible to every visitor: open devtools, or just read dist/assets/index-*.js.",
                "A VITE_ variable may hold a public URL. It may never hold a password, a key or a token.",
                "A variable with no VITE_ prefix is never touched by Vite and never reaches the browser at all.",
            ],
            code="""
# .env.local
VITE_SITE_NAME=Cook & Bake Academy   # public. fine.
DATABASE_URL=postgresql://user:PASSWORD@...  # SERVER ONLY

// Browser code can only ever see the first one:
const name = import.meta.env.VITE_SITE_NAME
""",
            takeaway="VITE_ vars are compiled into the public bundle — no secrets, ever.",
        ),
        dict(
            title="Deploy on every push",
            kicker="TOPIC 02 · CI/CD",
            analogy="Connecting Vercel to GitHub is a standing order to a baker — every push, a fresh loaf is baked and set out, no phone call needed.",
            bullets=[
                "Connect your GitHub repo to Vercel once, and every push to main triggers a fresh build and deploy.",
                "This is continuous deployment: your live site always reflects the latest committed code.",
                "Every branch and pull request gets its own preview URL, so you can test before merging.",
                "Vercel also builds everything in api/ into serverless functions, on the same domain as the site.",
                "Secrets like DATABASE_URL are set in the Vercel dashboard, encrypted — never in the repo.",
            ],
            code="""
git push origin main
# Vercel rebuilds and deploys automatically:
#   dist/   -> the static site
#   api/    -> serverless functions
# Same domain, so the browser calls /api/courses
# with no CORS and no separate backend URL.
""",
            takeaway="Push to GitHub; Vercel rebuilds the site AND the API functions.",
        ),
        dict(
            title="SPA deep links need a rewrite",
            kicker="TOPIC 02 · SPA HOSTING",
            analogy="A static host is a receptionist with a filing cabinet — ask for /courses, find no such file, and you must be told to always hand back index.html.",
            bullets=[
                "A single-page app has only one real file, index.html; the router fakes the other paths in the browser.",
                "Type /courses directly or refresh, and the static host looks for that file on disk and 404s.",
                "The fix is a rewrite rule: send every path to /index.html and let React Router match it.",
                "But you must EXCLUDE /api/*, or your API calls get rewritten to index.html and return a web page.",
                "That is what \"Unexpected token '<'\" means: you fetched a URL and res.json() got HTML back.",
            ],
            code="""
// vercel.json (real) — note the negative lookahead
{
  "rewrites": [
    { "source": "/((?!api/).*)", "destination": "/index.html" }
  ]
}
// Everything EXCEPT /api/* falls back to index.html.
""",
            takeaway="Rewrite every path to /index.html — except /api/*, or the API breaks.",
        ),
    ],

    # ===================================================== TOPIC 3 — Core React
    3: [
        dict(
            title="The real DOM, and life without React",
            kicker="TOPIC 03 · THE REAL DOM",
            analogy="The DOM is the page itself — a live object tree. Editing it by hand is rewiring a running machine.",
            bullets=[
                "The DOM is the browser's live object tree. Change a node's property and the screen changes.",
                "Without React you say HOW: getElementById, then overwrite textContent, className, style, value.",
                "The truth now lives in a DOM string, so you read '10 courses' back out and parse it to add to it.",
                "Every new feature multiplies the patches: filter the grid and you must also fix the count and the chip.",
                "One missed patch and the screen quietly disagrees with your data. Nothing throws. Nobody notices.",
            ],
            code="""
// Vanilla: filtering the Cook & Bake catalogue.
document.querySelectorAll('.card').forEach((card) => {
  const show = card.dataset.category === 'Bakery'
  card.style.display = show ? 'block' : 'none'
})
document.getElementById('count').textContent = '10 courses'
// ...plus the chip, the heading, the empty state...
""",
            takeaway="Hand-patching the DOM means saying HOW, in every place, every time.",
        ),
        dict(
            title="The Virtual DOM and reconciliation",
            kicker="TOPIC 03 · VIRTUAL DOM",
            analogy="The Virtual DOM is an architect's blueprint — React compares the new drawing to the old before knocking down a single real wall.",
            bullets=[
                "React keeps a lightweight JavaScript tree — the Virtual DOM — describing what the UI should be.",
                "Building it is cheap: it is just plain objects. Touching the real DOM is the expensive part.",
                "On each render React builds a NEW virtual tree for the current state.",
                "Reconciliation is the diff: it compares the new tree to the previous one to find what changed.",
                "It patches only those differences into the real DOM. Unchanged nodes are never touched.",
            ],
            code="""
// You describe the UI for this state:
<p>{visible.length} courses</p>

// Filter to Bakery: React builds a new virtual tree,
// diffs it, and patches ONE text node ('20' -> '10')
// plus removing 10 cards. The navbar, hero and footer
// were identical in both trees, so they are untouched.
""",
            takeaway="React diffs a virtual tree and patches only what actually changed.",
        ),
        dict(
            title="Babel compiles JSX into function calls",
            kicker="TOPIC 03 · BABEL",
            analogy="Babel is a translator in a booth — you speak JSX, and the browser only ever hears plain JavaScript.",
            bullets=[
                "The browser has NEVER seen JSX. It is not JavaScript and no browser can parse it.",
                "Babel compiles it away at build time. Vite wires Babel in through @vitejs/plugin-react.",
                "<CourseCard fee={680}/> becomes React.createElement(CourseCard, { fee: 680 }).",
                "That call returns a plain JavaScript object — { type, props } — not HTML and not a DOM node.",
                "A tree of those objects IS the Virtual DOM. This is the join between the last slide and this one.",
            ],
            code="""
// YOU WRITE (JSX):
<CourseCard course={course} fee={680} />

// BABEL COMPILES IT TO (plain JavaScript):
React.createElement(CourseCard, { course: course, fee: 680 })

// WHICH RETURNS (a plain object — a React element):
{ type: CourseCard, props: { course: {...}, fee: 680 } }
""",
            takeaway="Babel rewrites every JSX tag into a call that returns a plain object.",
        ),
        dict(
            title="Declarative beats imperative",
            kicker="TOPIC 03 · DECLARATIVE UI",
            analogy="Declarative code is ordering a dish, not reciting the recipe — you state the result you want and let React cook.",
            bullets=[
                "Imperative code lists the steps: find the element, set its text, toggle a class, and so on.",
                "Declarative code describes the end result for the current state and lets React reach it.",
                "In React you never write 'update this node' — you write what the UI is, as a function of state.",
                "This means the UI can never drift out of sync with your data the way manual DOM edits do.",
                "Change the state, and the correct UI follows automatically; that is React's core promise.",
            ],
            code="""
// Imperative (vanilla): you do each step
el.textContent = String(visible.length)

// Declarative (React): you state the result
<p>{visible.length} courses</p>
""",
            takeaway="Describe the UI for the current state; React figures out the how.",
        ),
        dict(
            title="State vs props",
            kicker="TOPIC 03 · STATE vs PROPS",
            analogy="Props are the mail a component receives; state is the note it keeps on its own desk — one comes from outside, one it writes itself.",
            bullets=[
                "Props are passed in from the parent and are read-only — the component cannot change them.",
                "State is owned by the component itself and can change over time in response to events.",
                "Changing state triggers a re-render; receiving new props from a parent also triggers a re-render.",
                "Ask 'does this component own this value, or is it given?' to decide between state and props.",
                "CourseCard is all props and no state. CoursesPage owns the query state and passes it down.",
            ],
            code="""
// SearchBar owns nothing — pure props.
function SearchBar({ value, onChange }) {
  return <input value={value}
    onChange={(e) => onChange(e.target.value)} />
}

// CoursesPage owns the state:
const [query, setQuery] = useState('')
<SearchBar value={query} onChange={setQuery} />
""",
            takeaway="Props come from outside and are read-only; state is owned and changeable.",
        ),
        dict(
            title="State: a component's memory",
            kicker="TOPIC 03 · STATE",
            analogy="State is a component's memory — a notepad it keeps between renders, not scratch paper binned each time.",
            bullets=[
                "State is data a component owns and remembers across renders, unlike a variable reset every render.",
                "A plain let is recomputed and lost each render, so changing it can never update what is on screen.",
                "useState gives a remembered value plus a setter: const [query, setQuery] = useState('').",
                "Calling the setter does two things: it stores the new value and schedules a re-render to show it.",
                "That re-render is the point — the UI redraws from the new state, so screen and data stay in step.",
            ],
            code="""
let q = ''       // reset every render — useless
q = 'sushi'      // nothing on screen changes

const [q, setQ] = useState('')
setQ('sushi')    // stored, AND schedules a re-render
""",
            takeaway="State is remembered data; its setter stores the value and re-renders.",
        ),
        dict(
            title="Composition and the children prop",
            kicker="TOPIC 03 · COMPOSITION",
            analogy="The children prop is a picture frame — it does not care what photo you slide in, it just wraps whatever you hand it.",
            bullets=[
                "Composition means building complex UI by nesting simple components inside one another.",
                "The special children prop holds whatever JSX sits between a component's opening and closing tags.",
                "This lets Section, a Card or a Layout wrap arbitrary content without knowing what that content is.",
                "Favour composition over configuration — do not pile endless boolean props onto one component.",
                "The real Section takes id, title, eyebrow, alt and children — and renders anything you nest in it.",
            ],
            code="""
// src/components/Section.jsx (real code)
export default function Section({ title, children }) {
  return (
    <section className="section">
      {title && <h2>{title}</h2>}
      {children}
    </section>
  )
}

<Section title="Popular courses"><CourseGrid /></Section>
""",
            takeaway="children lets a component wrap any content instead of endless props.",
        ),
        dict(
            title="Rendering lists with map()",
            kicker="TOPIC 03 · LISTS",
            analogy="map is a name-tag printer: feed it a list of students and it hands back one printed tag per person, in order.",
            bullets=[
                "You render a list by calling map() to turn an array of data into an array of JSX elements.",
                "React accepts an array of elements directly inside JSX and renders them in order.",
                "This is what kills the hand-typed cards from Topic 1: 20 courses, one CourseGrid, one map().",
                "Adding a course is now a data edit, not a markup edit — and the grid updates itself.",
                "Every element in the returned list needs a key, which the next slide explains.",
            ],
            code="""
// src/components/CourseGrid.jsx (real code)
<div className="grid">
  {courses.map((course) => (
    <CourseCard key={course.id} course={course} />
  ))}
</div>
""",
            takeaway="map() turns a data array into an array of elements React renders.",
        ),
        dict(
            title="key is identity, not decoration",
            kicker="TOPIC 03 · KEYS",
            analogy="A key is a student's name tag, not their seat number — reshuffle the room and React still knows exactly who is who.",
            bullets=[
                "A key is a stable id React uses to track which item is which across renders.",
                "It lets React move, keep or remove the right cards instead of rebuilding the whole grid.",
                "Use a stable id from your data (course.id), never the array index, as the key.",
                "key={index} looks fine until you filter, reorder or delete — then state attaches to the wrong card.",
                "This is one of the single most common bugs in AI-generated list code, so always check it.",
            ],
            code="""
{courses.map((course) => (
  <CourseCard key={course.id} course={course} />
))}

// key={index} corrupts state when you filter to Bakery:
// the card at index 0 is now a different course, but
// React thinks it is the same one and keeps its state.
""",
            takeaway="Key each card by a stable id; key={index} corrupts state on change.",
        ),
        dict(
            title="Conditional rendering and the 0 && trap",
            kicker="TOPIC 03 · CONDITIONALS",
            analogy="0 && is a trapdoor — zero is falsy but not nothing, so React renders a bare 0 unless you gate on seats > 0.",
            bullets=[
                "Use a ternary in JSX to choose between two elements based on a condition.",
                "Use && to render an element only when a condition is true, and nothing otherwise.",
                "The footgun: {seats && <Badge/>} renders a literal 0 on screen when seats is 0, because 0 is falsy.",
                "Fix it by making the left side a real boolean: {seats > 0 && <Badge/>}.",
                "This is subtle and the agent produces it often, so scan every && for a number on its left.",
            ],
            code="""
// From CourseCard: a ternary picks one of two.
<span>{isBakery ? '🧁 Bakery' : '🍳 Cooking'}</span>

// && renders one thing or nothing:
{seats > 0 && <span>{seats} places left</span>}

// {seats && ...} prints a literal 0 when seats is 0.
""",
            takeaway="Gate && on a real boolean (seats > 0), never a bare number.",
        ),
        dict(
            title="Derived state must not be stored",
            kicker="TOPIC 03 · DERIVED STATE",
            analogy="Storing a derived value is photocopying a number already on the page — keep the copy and it soon disagrees with the original.",
            bullets=[
                "If a value can be computed from existing state during render, compute it. Do not store it.",
                "The filtered course list is derived from courses + category + query. It is not its own state.",
                "Mirroring it into useState creates two sources of truth, and they will drift apart.",
                "Computing on render is cheap and always correct; a stored copy needs syncing you will forget.",
                "The agent loves to add a useState for filtered lists and totals. Delete it and compute inline.",
            ],
            code="""
// src/pages/CoursesPage.jsx (real code) — DERIVED.
const visible = courses.filter((c) => {
  const matchesCat = category === 'All'
    || c.category === category
  const matchesQ = !needle
    || c.title.toLowerCase().includes(needle)
  return matchesCat && matchesQ
})
""",
            takeaway="Compute derived values on render; never mirror them into useState.",
        ),
        dict(
            title="Synthetic events",
            kicker="TOPIC 03 · EVENTS",
            analogy="A synthetic event is a universal remote — React wraps every browser's quirks in one consistent set of buttons.",
            bullets=[
                "You attach handlers with camelCase props like onClick and onChange, passing a function.",
                "Pass the function, do not call it: onClick={handleEnroll}, not onClick={handleEnroll()}.",
                "To pass an argument, wrap it in an arrow: onClick={() => onChange(cat.value)}.",
                "React hands your handler a synthetic event, a cross-browser wrapper over the native event.",
                "Read the input's value from e.target.value; call e.preventDefault() to stop a form reloading.",
            ],
            code="""
// src/components/CategoryFilter.jsx (real code)
{categories.map((cat) => (
  <button key={cat.value}
    onClick={() => onChange(cat.value)}>
    {cat.label}
  </button>
))}
// onClick={onChange(cat.value)} would CALL it on render.
""",
            takeaway="Pass a function to onClick; wrap in an arrow to pass an argument.",
        ),
        dict(
            title="Controlled inputs",
            kicker="TOPIC 03 · FORMS",
            analogy="A controlled input is a puppet on React's strings — state moves the field, and every keystroke reports back to pull the string.",
            bullets=[
                "In a controlled input, React state is the single source of truth for the field's value.",
                "You bind value={state} and update it in onChange, so state and the input never disagree.",
                "This unlocks live search, validation, formatting and disabling a submit button as the user types.",
                "A value with no onChange makes the field read-only — React warns you in the console.",
                "SearchBar is controlled and owns nothing: the value comes down, every keystroke goes back up.",
            ],
            code="""
// src/components/SearchBar.jsx (real code)
<input
  type="search"
  placeholder="Search sourdough, sushi, macaron…"
  value={value}
  onChange={(e) => onChange(e.target.value)}
/>
""",
            takeaway="Bind value to state and update it in onChange — React owns the field.",
        ),
    ],

    # ===================================================== TOPIC 4 — Hooks
    4: [
        dict(
            title="The Rules of Hooks",
            kicker="TOPIC 04 · RULES",
            analogy="Hooks are called in roll-call order — React counts 'hook one, hook two' every render, so you must never skip or reorder a name.",
            bullets=[
                "Call hooks only at the top level of a component or hook — never in a loop, condition or nested function.",
                "React identifies each hook purely by its call order, which must be identical on every render.",
                "A hook inside an if runs some renders and not others, and the whole list of hooks shifts and breaks.",
                "Only call hooks from React function components or from your own custom hooks.",
                "The lint rules for hooks catch most violations — do not disable them to silence a warning.",
            ],
            code="""
function CoursesPage({ open }) {
  const [q, setQ] = useState('')  // ok: top level
  if (open) {
    const [x] = useState(1)       // never: in an if
  }
}
""",
            takeaway="Call hooks at the top level, in the same order, every render.",
        ),
        dict(
            title="What a hook actually is",
            kicker="TOPIC 04 · HOOKS",
            analogy="A hook is a power outlet on the render: plug in with use…() and your function taps React's memory and lifecycle.",
            bullets=[
                "A hook is a function whose name starts with 'use' that lets a function component use React features.",
                "Hooks let a stateless function remember values (useState) and sync with the outside (useEffect).",
                "React identifies each hook by call order, matching it to a memory slot by position, not by name.",
                "That is why hooks live at the top level — never inside an if, a loop, or after an early return.",
                "Only components and other hooks may call hooks; a plain helper function cannot.",
            ],
            code="""
function CoursesPage() {
  const { courses } = useCourses()   // custom hook
  const [q, setQ] = useState('')     // slot 2
  const searchInput = useRef(null)   // slot 3
  useEffect(() => {                  // slot 4
    searchInput.current?.focus()
  }, [])
}
""",
            takeaway="A hook is a use…() function; React tracks it by call order.",
        ),
        dict(
            title="State is a snapshot",
            kicker="TOPIC 04 · useState",
            analogy="State is a photograph, not a live feed — count is frozen at the value it had when this render's photo was taken.",
            bullets=[
                "useState returns the current value and a setter: const [count, setCount] = useState(0).",
                "Within one render the state value never changes — it is a snapshot captured at render time.",
                "Calling setCount(count + 1) twice in a row adds only one, because both read the same stale count.",
                "When the next value depends on the previous, use the updater form: setCount(c => c + 1).",
                "Setting state schedules a re-render; it does not change the current variable mid-function.",
            ],
            code="""
setCount(count + 1)     // stale: +1 total
setCount(count + 1)

setCount((c) => c + 1)  // updater: +1
setCount((c) => c + 1)  // updater: +2
""",
            takeaway="State is fixed per render; use setX(prev => ...) for dependent updates.",
        ),
        dict(
            title="Immutable updates",
            kicker="TOPIC 04 · IMMUTABILITY",
            analogy="Mutating state is editing the original photo — React only re-renders when you hand it a brand-new print.",
            bullets=[
                "React decides to re-render by checking whether the state value is a NEW reference.",
                "items.push(course) mutates the same array, so the reference is unchanged and nothing re-renders.",
                "Build a new value with spread instead: setItems([...items, course]) creates a fresh array.",
                "Update an object the same way: setCourse({ ...course, fee: 720 }).",
                "The real CartContext never mutates: every add, remove and clear returns a brand-new array.",
            ],
            code="""
// src/context/CartContext.jsx (real code)
const addItem = (course) =>
  setItems((prev) =>
    prev.some((c) => c.id === course.id)
      ? prev
      : [...prev, course])   // NEW array -> re-renders

const removeItem = (id) =>
  setItems((prev) => prev.filter((c) => c.id !== id))
""",
            takeaway="Never mutate state — build a new array or object with spread.",
        ),
        dict(
            title="useEffect and the dependency array",
            kicker="TOPIC 04 · useEffect",
            analogy="The dependency array is a guest list — the effect only re-runs when a name on the list actually changes.",
            bullets=[
                "useEffect runs code after render for side effects: fetching, subscriptions, timers, the DOM.",
                "Its second argument, the dependency array, decides when it re-runs.",
                "An empty array [] runs the effect once after the first render, and never again.",
                "Listing [slug] re-runs the effect whenever slug changes — that is how a new course gets fetched.",
                "Omit the array entirely and it runs after every render — the classic infinite-fetch loop.",
            ],
            code="""
// src/context/ThemeContext.jsx (real code)
useEffect(() => {
  document.documentElement.dataset.theme = theme
}, [theme])   // re-runs only when the theme changes
""",
            takeaway="[] runs once; [dep] re-runs when dep changes; no array runs always.",
        ),
        dict(
            title="Every effect cleans up after itself",
            kicker="TOPIC 04 · CLEANUP",
            analogy="useEffect cleanup is turning the tap off as you leave the room — StrictMode runs in and out twice to catch a tap left running.",
            bullets=[
                "An effect that starts something ongoing must stop it, or you leak timers, listeners and requests.",
                "Return a cleanup function from the effect; React runs it before the next effect and on unmount.",
                "clearTimeout, clearInterval, removeEventListener and unsubscribe all belong in that function.",
                "In development, StrictMode mounts, unmounts and remounts once to expose effects with no cleanup.",
                "So a double log in dev is not a bug — it is React helping you find a missing cleanup.",
            ],
            code="""
// src/hooks/useDebounce.js (real code)
useEffect(() => {
  const id = setTimeout(() => setDebounced(value), delay)
  return () => clearTimeout(id)   // cleanup
}, [value, delay])
// Every keystroke cancels the previous pending timer,
// so only the last one ever fires.
""",
            takeaway="Return a cleanup for anything ongoing; StrictMode double-runs to test it.",
        ),
        dict(
            title="useRef: the escape hatch to the DOM",
            kicker="TOPIC 04 · useRef",
            analogy="A ref is a sticky note the renderer never reads — write to .current all you like and React will not repaint the screen.",
            bullets=[
                "useRef returns a mutable object, { current }, whose value persists across renders like state does.",
                "But unlike state, writing to .current never triggers a re-render — that is its defining difference.",
                "Job one: a live handle on a real DOM node, for the things JSX cannot describe.",
                "Job two: a mutable box for a value that must survive renders but must not drive the UI.",
                "In React 19 ref is a normal prop, so you pass it straight to your own components — no forwardRef.",
            ],
            code="""
const searchInput = useRef(null)  // job one: a DOM handle
const timer = useRef(null)        // job two: a mutable box

// .current is null on the first render — React has not
// created the node yet. It is set right after paint.
useEffect(() => {
  searchInput.current?.focus()
}, [])

<input ref={searchInput} />   // React 19: ref is a prop
""",
            takeaway="Two jobs — a DOM handle and a mutable box; neither triggers a re-render.",
        ),
        dict(
            title="ref vs state — the dividing line",
            kicker="TOPIC 04 · REF vs STATE",
            analogy="State is what the audience sees; a ref is the stagehand's clipboard — necessary, remembered, and never on stage.",
            bullets=[
                "The whole decision is one question: should changing this value REDRAW the screen?",
                "If yes, it is STATE. The search text is state — every keystroke must repaint the results.",
                "If no, it is a REF. Focus, scroll position and a timer id change nothing that is rendered.",
                "Put a timer id in state and you re-render the entire component on every single tick. For nothing.",
                "'Is focused' is browser state, not React state. There is no JSX you can write to express it.",
            ],
            code="""
// STATE — the screen must change:
const [query, setQuery] = useState('')

// REF — the screen must NOT change:
const searchInput = useRef(null)   // which DOM node
const timer = useRef(null)         // the interval id

// timer in useState => a re-render every tick, forever.
""",
            takeaway="Redraw the screen? State. Must not redraw? Ref. That is the whole rule.",
        ),
        dict(
            title="Three real refs in Cook & Bake",
            kicker="TOPIC 04 · useRef IN THE APP",
            analogy="Refs are the three things the declarative world cannot say: put the cursor here, scroll there, hold this receipt.",
            bullets=[
                "CoursesPage focuses the search box on mount, and again after every category chip click.",
                "The ref is created in the PARENT and handed down to SearchBar as an ordinary prop.",
                "HomePage points a ref at the course grid, so the hero's 'Browse courses' button can scroll to it.",
                "Hero receives onBrowse as a function prop — it never knows a ref or a DOM node exists.",
                "A timer id lives in a ref because clearing it later must not cost the user a re-render.",
            ],
            code="""
// CoursesPage.jsx — focus the search input
const searchInput = useRef(null)
useEffect(() => { searchInput.current?.focus() }, [])
<SearchBar inputRef={searchInput} ... />

// HomePage.jsx — scroll the grid into view
const popularRef = useRef(null)
const scrollToCourses = () =>
  popularRef.current?.scrollIntoView({ behavior: 'smooth' })
<Hero onBrowse={scrollToCourses} />
<section ref={popularRef}>...</section>
""",
            takeaway="Focus, scroll and timer ids: the sanctioned reasons to hold a DOM node.",
        ),
        dict(
            title="useContext ends prop drilling",
            kicker="TOPIC 04 · CONTEXT",
            analogy="Context is a building's PA system — announce once and any floor hears it, instead of passing a note desk to desk down every level.",
            bullets=[
                "Prop drilling is threading a value through components that do not use it, just to reach a deep child.",
                "Context provides a value once high in the tree and lets any component below read it directly.",
                "Create a context, wrap a subtree in its Provider, and read it with useContext — or a custom hook.",
                "Cook & Bake has three: ThemeContext (dark mode), AuthContext (the user), CartContext (shortlist).",
                "Do not use context for fast-changing values like keystrokes — every consumer re-renders on change.",
            ],
            code="""
// src/context/CartContext.jsx (real code)
export function useCart() {
  const ctx = useContext(CartContext)
  if (!ctx) throw new Error('useCart needs <CartProvider>')
  return ctx
}

// Anywhere, at any depth, with no prop drilling:
const { count } = useCart()
""",
            takeaway="Provide once, read anywhere with useContext — no more prop drilling.",
        ),
        dict(
            title="useReducer and custom hooks",
            kicker="TOPIC 04 · REDUCER & HOOKS",
            analogy="A reducer is a vending machine — press a labelled button (an action) and get a predictable new state, every time.",
            bullets=[
                "useReducer suits state with several related actions, like a shortlist's add, remove and clear.",
                "A reducer is a pure function (state, action) => newState — same inputs always give the same output.",
                "It must build and return new state, never mutate the state it was handed.",
                "A custom hook is a function starting with 'use' that bundles hook logic for reuse.",
                "Custom hooks share LOGIC, not state — each caller of useLocalStorage gets its own key and value.",
            ],
            code="""
function cartReducer(state, action) {
  switch (action.type) {
    case 'ADD':
      return state.some((c) => c.id === action.course.id)
        ? state
        : [...state, action.course]
    case 'REMOVE':
      return state.filter((c) => c.id !== action.id)
    default: return state
  }
}
""",
            takeaway="Reducers are pure (state, action) => newState; custom hooks share logic, not state.",
        ),
    ],

    # ================================== TOPIC 5 — Backend API, Neon, auth
    5: [
        dict(
            title="Three tiers, and one hard rule",
            kicker="TOPIC 05 · ARCHITECTURE",
            analogy="The API is the counter in a bank — customers state what they want; only staff go into the vault.",
            bullets=[
                "React (browser) --fetch--> /api/* (Vercel functions) --sql--> Neon Postgres. Three tiers.",
                "The BROWSER NEVER TALKS TO POSTGRES. It has no driver, no connection string and no SQL.",
                "It knows one thing: how to call our own /api/* URLs. The functions decide what is allowed.",
                "Every security rule lives in the middle tier, on a server, where the user cannot edit it.",
                "Anything you enforce in the browser is a suggestion. Anything you enforce in /api/ is a rule.",
            ],
            code="""
  React (browser)          src/lib/api.js
        |  fetch('/api/courses')
        v
  /api/* (Vercel function) api/courses/index.js
        |  sql`select ... from courses`
        v
  Neon Postgres            DATABASE_URL lives ONLY here
""",
            takeaway="The browser asks the API. Only the API touches the database.",
        ),
        dict(
            title="Why the browser cannot hold the password",
            kicker="TOPIC 05 · VITE_ AND SECRETS",
            analogy="Putting DATABASE_URL in a VITE_ variable is printing your house key on the flyer and posting it to every visitor.",
            bullets=[
                "Vite compiles any VITE_-prefixed variable straight into the JavaScript bundle it ships.",
                "Every visitor downloads that bundle. They can read it. There is no exception and no hiding it.",
                "DATABASE_URL contains the database password and grants full READ AND WRITE to your data.",
                "So DATABASE_URL must NEVER carry the VITE_ prefix. It is read only in api/, via process.env.",
                "If you ever 'fix' a connection error by renaming it VITE_DATABASE_URL, you have published the vault key.",
            ],
            code="""
# .env.local — the prefix is the whole security boundary
DATABASE_URL=postgresql://user:PASSWORD@ep-...neon.tech/db
JWT_SECRET=<32 random bytes>
# NO VITE_ prefix on either. Both are server-only.

// api/_lib/db.js — the ONLY place it is ever read:
export const sql = neon(process.env.DATABASE_URL)
""",
            takeaway="A VITE_ variable is public. DATABASE_URL must never have that prefix.",
        ),
        dict(
            title="A serverless API route is a function",
            kicker="TOPIC 05 · API ROUTES",
            analogy="Each file in api/ is a shopfront window: one URL, one handler, opened only when someone knocks.",
            bullets=[
                "A file in api/ becomes a URL: api/courses/index.js serves GET /api/courses.",
                "It exports one default async handler(req, res) — no Express app, no server to keep running.",
                "Square brackets make it dynamic: api/courses/[slug].js matches /api/courses/macaron-masterclass.",
                "Vercel hands you the matched segment as req.query.slug, and the query string as req.query too.",
                "The status code IS the answer: 200 for a course, 404 for no such slug, 401 for no valid token.",
            ],
            code="""
// api/courses/[slug].js (real code)
import { sql } from '../_lib/db.js'

export default async function handler(req, res) {
  const { slug } = req.query ?? {}
  const rows = await sql`
    select id::int as id, code, slug, title, fee::float8 as fee
    from courses where slug = ${slug}
  `
  if (rows.length === 0) throw new HttpError(404, 'No course.')
  return res.status(200).json(rows[0])
}
""",
            takeaway="One file, one URL, one async handler — and it holds the only DB connection.",
        ),
        dict(
            title="Tagged templates defeat SQL injection",
            kicker="TOPIC 05 · PARAMETERISED SQL",
            analogy="A parameterised query is a form with boxes — Postgres reads the form first, then fills the boxes. Text in a box can never become an instruction.",
            bullets=[
                "sql`...` is a TAGGED TEMPLATE. You call it with backticks, not brackets — and that is the whole story.",
                "It LOOKS like string interpolation but is not: the SQL text and the values travel SEPARATELY.",
                "The driver sends `where slug = $1` plus the value. Postgres parses the SQL, THEN binds the value.",
                "So a slug of `x'; drop table users; --` is looked up as an absurd literal slug and finds nothing.",
                "The one thing that reintroduces the hole is building the string yourself. Never do sql(`...${x}...`).",
            ],
            code="""
// SAFE — a tagged template. Value travels separately.
await sql`select * from courses where slug = ${slug}`
//         Postgres receives:  where slug = $1
//         and, separately:    ["macaron-masterclass"]

// CATASTROPHIC — never build SQL by concatenation:
await sql(`select * from courses where slug = '${slug}'`)
// slug = "x'; drop table users; --"  now EXECUTES.
""",
            takeaway="The value travels separately from the SQL, so it can never be parsed as SQL.",
        ),
        dict(
            title="Never store a password",
            kicker="TOPIC 05 · bcrypt",
            analogy="A hash is a fingerprint, not a photograph — you can check a match, but you can never reconstruct the face.",
            bullets=[
                "Store a bcrypt HASH, never the password. Hashing is one-way: the hash cannot be turned back.",
                "bcrypt is deliberately SLOW (cost 10, ~100ms), which makes brute-forcing a stolen table painful.",
                "It salts every hash automatically, so two users with the same password get different hashes.",
                "Verify with bcrypt.compare(), which re-hashes with the stored salt and compares in constant time.",
                "NEVER select password_hash into a response. Whitelist the fields you send; do not blacklist.",
            ],
            code="""
// api/auth/signup.js (real code)
const passwordHash = await bcrypt.hash(password, 10)
await sql`
  insert into users (email, name, password_hash)
  values (${email}, ${name}, ${passwordHash})
  returning id::int as id, email, name, created_at
`   // note what is NOT in RETURNING: password_hash.

// api/auth/login.js
const ok = await bcrypt.compare(password, user.password_hash)
""",
            takeaway="Hash with bcrypt, compare with bcrypt, and never let the hash leave the server.",
        ),
        dict(
            title="Trust the token, never the body",
            kicker="TOPIC 05 · JWT",
            analogy="A JWT is a tamper-proof wristband — the payload is readable by anyone, but only the door staff can make a real one.",
            bullets=[
                "A JWT is header.payload.signature. The payload is ENCODED, not encrypted — never put a secret in it.",
                "The signature is what makes it trustworthy: it is computed with JWT_SECRET, which only the server has.",
                "Edit one byte of the payload and the signature no longer matches, so jwt.verify() throws.",
                "So the user id comes from the VERIFIED token's `sub` claim — NEVER from req.body.userId.",
                "If POST /api/enrollments trusted req.body.userId, anyone with curl could enrol anyone.",
            ],
            code="""
// api/_lib/auth.js (real code)
export function requireAuth(req) {
  const header = req.headers?.authorization ?? ''
  if (!header.startsWith('Bearer ')) throw new HttpError(401, '...')
  const token = header.slice('Bearer '.length).trim()
  const payload = jwt.verify(token, JWT_SECRET)  // throws if forged
  return Number(payload.sub)   // verified, not claimed
}
""",
            takeaway="The id comes from a verified signature, not from something the caller typed.",
        ),
        dict(
            title="Ownership is enforced in the SQL",
            kicker="TOPIC 05 · AUTHORISATION",
            analogy="An id in the URL is a request, not a permission — asking for locker 5 does not make locker 5 yours.",
            bullets=[
                "An id in the URL comes from the address bar. Anyone can change a 4 to a 5 and ask to delete it.",
                "So the id alone is never enough. Every statement carries TWO conditions, and the second is ownership.",
                "`where id = ${id} and user_id = ${userId}` — the userId comes from the verified JWT, not the caller.",
                "A row you do not own simply does not match, so Postgres changes nothing and we answer 404.",
                "Get this wrong and you have an Insecure Direct Object Reference — one of the commonest real bugs.",
            ],
            code="""
// api/enrollments/[id].js (real code)
const userId = requireAuth(req)         // from the JWT
const { id } = req.query ?? {}          // from the URL

const rows = await sql`
  delete from enrollments
  where id = ${id} and user_id = ${userId}
  returning id::int as id
`                    // ^^^^^^^^^^^^^^^^^^^ the real check
if (rows.length === 0) throw new HttpError(404, 'Not found.')
""",
            takeaway="The URL says WHICH row; the token says WHOSE. Both go in the WHERE clause.",
        ),
        dict(
            title="Every remote read has three states",
            kicker="TOPIC 05 · THREE STATES",
            analogy="Every fetch is a package delivery — it is either in transit, lost, or on your doorstep, and the UI must show all three.",
            bullets=[
                "A remote read is never instant, so you must model loading, error and success as distinct states.",
                "Hold three pieces of state: the data, a loading flag, and an error value.",
                "Show a skeleton while loading, a message on error, and the data on success — never assume success.",
                "AI-generated code reliably writes the loading and success branches and forgets the error one.",
                "Always clear the flag in a finally, or one failed request leaves the UI spinning forever.",
            ],
            code="""
// src/hooks/useCourses.js (real code)
try {
  const data = await api.get('/courses')
  setCourses(data); setError(null)
} catch (err) {
  setError(err.message)          // the branch AI forgets
} finally {
  setLoading(false)              // or it spins forever
}
""",
            takeaway="Model loading, error and success — the error branch is the one AI skips.",
        ),
        dict(
            title="fetch does not reject on 404",
            kicker="TOPIC 05 · response.ok",
            analogy="fetch only cries if the road is out — a 404 is a signed 'not found' slip delivered successfully, so you must read the slip.",
            bullets=[
                "fetch rejects its Promise only on a network failure, not on a 404 or a 500 HTTP response.",
                "A 404 is a successful delivery of a failure message, so the await resolves perfectly normally.",
                "Always check response.ok (true only for 200-299) before you read the body.",
                "Skip it and an error payload like {error: '...'} sails into your UI and renders as if it were a course.",
                "Carry the status on the thrown error so a 404 (no such course) is distinguishable from a 500.",
            ],
            code="""
// src/lib/api.js (real code)
const res = await fetch(`${BASE}${path}`, { ... })
const data = res.status === 204 ? null : await res.json()

if (!res.ok) {
  const err = new Error(data?.error ?? `Failed (${res.status})`)
  err.status = res.status   // 404 -> not found page
  throw err                 // 500 -> error message
}
""",
            takeaway="Check response.ok before reading the body — fetch won't reject on 404.",
        ),
    ],

    # ===================================================== TOPIC 6 — Routing
    6: [
        dict(
            title="A Single Page Application",
            kicker="TOPIC 06 · SPA",
            analogy="A single-page app is a theatre with one stage — JavaScript changes the scenery and the marquee while the audience never leaves their seats.",
            bullets=[
                "A traditional site fetches a fresh HTML page from the server on every navigation.",
                "A single-page app loads one HTML document, then JavaScript swaps the view in place.",
                "The router also rewrites the URL bar so back, forward and bookmarks still work.",
                "No server round-trip means navigation is instant and React state is preserved across views.",
                "React Router maps each URL path to the component that should render for it.",
            ],
            code="""
// src/App.jsx (real code)
<Routes>
  <Route path="/" element={<RootLayout />}>
    <Route index element={<HomePage />} />
    <Route path="courses" element={<CoursesPage />} />
    <Route path="courses/:slug" element={<CourseDetailPage />} />
    <Route path="*" element={<NotFoundPage />} />
  </Route>
</Routes>
""",
            takeaway="One document; JS swaps views and rewrites the URL, no server reload.",
        ),
        dict(
            title="Use <Link>, not <a>",
            kicker="TOPIC 06 · NAVIGATION",
            analogy="An <a> tag rebuilds the whole theatre between scenes; <Link> just swaps the set, keeping every actor in place.",
            bullets=[
                "A plain <a href> triggers a full-page reload, refetching the whole app from scratch.",
                "That reload throws away every piece of React state — the shortlist, the search box, the scroll.",
                "<Link to> navigates within the SPA, swapping the view without any reload.",
                "The whole CourseCard is a <Link>, so clicking anywhere on a card routes to its detail page.",
                "Use <a> only for links that truly leave your app; use <Link> for every internal route.",
            ],
            code="""
// src/components/CourseCard.jsx (real code)
<Link to={`/courses/${slug}`} className="card">
  ...the entire card...
</Link>

<a href="/courses">Browse</a>   // full reload: state gone
""",
            takeaway="<Link> navigates in-app and keeps state; <a> reloads and loses it.",
        ),
        dict(
            title="Layout routes and <Outlet/>",
            kicker="TOPIC 06 · LAYOUTS",
            analogy="A layout route is a picture frame with a window — <Outlet/> is the window where each page's picture slots into the same frame.",
            bullets=[
                "A layout route is a parent route that renders shared chrome like the navbar and footer.",
                "Its child routes render inside it, so the shared frame is written once, not per page.",
                "The layout component renders <Outlet/> to mark where the matched child should appear.",
                "Layouts nest: DashboardPage is itself a layout, with My Courses and Profile inside its own Outlet.",
                "A PATHLESS parent route adds no URL segment — which is exactly how ProtectedRoute gates a subtree.",
            ],
            code="""
// src/layouts/RootLayout.jsx (real code)
export default function RootLayout() {
  return (
    <>
      <Navbar />
      <main><Outlet /></main>   {/* the matched child */}
      <Footer />
    </>
  )
}
""",
            takeaway="A layout route holds shared chrome; <Outlet/> is where children render.",
        ),
        dict(
            title="Dynamic params and useParams",
            kicker="TOPIC 06 · DYNAMIC ROUTES",
            analogy="A dynamic segment is a mail slot labelled :slug — useParams reaches in and reads whichever course the URL dropped through.",
            bullets=[
                "A path segment starting with a colon, like :slug, is a placeholder that matches any value.",
                "One route definition serves all 20 courses: /courses/macaron-masterclass, /courses/knife-skills…",
                "Inside the component, useParams() returns an object of the matched segment values.",
                "Read it with const { slug } = useParams(), then fetch that one course from /api/courses/:slug.",
                "useNavigate() moves programmatically: navigate(-1) goes back with no hardcoded path.",
            ],
            code="""
<Route path="courses/:slug" element={<CourseDetailPage />} />

// src/pages/CourseDetailPage.jsx (real code)
const { slug } = useParams()
const { course, loading, error } = useCourse(slug)
// null course = no such slug -> render a real 404 page
""",
            takeaway="A :param matches any value; useParams() reads it inside the component.",
        ),
        dict(
            title="URL state beats component state",
            kicker="TOPIC 06 · URL STATE",
            analogy="Putting filters in the URL is writing them on a shareable ticket — bookmark it, send it, hit back, and the same view returns.",
            bullets=[
                "Filters, search terms and pagination are state, but they belong in the URL, not just useState.",
                "/courses?category=Bakery&q=sourdough is shareable, bookmarkable and survives a refresh.",
                "It also makes the browser back button restore the previous filter instead of leaving the app.",
                "useSearchParams reads and writes the query string exactly like a piece of state.",
                "Debounce before you write: one history entry per keystroke would wreck the back button.",
            ],
            code="""
// src/pages/CoursesPage.jsx (real code)
const [searchParams, setSearchParams] = useSearchParams()
const category = searchParams.get('category') ?? 'All'
const q = searchParams.get('q') ?? ''

// { replace: true } updates the URL without a new
// history entry — the debounced value is what we write.
""",
            takeaway="Put shareable view state in the URL with useSearchParams, not useState.",
        ),
        dict(
            title="Protected routes wait for auth",
            kicker="TOPIC 06 · PROTECTED ROUTES",
            analogy="Guarding before auth loads is checking a wristband in the dark — wait for the lights (loading) or you eject your own paying guest.",
            bullets=[
                "A protected route should render only for a signed-in user and redirect everyone else.",
                "The catch is that the session resolves asynchronously: on boot we ask /api/auth/me to verify the token.",
                "During that moment `user` is null but nobody is actually signed out. You know nothing yet.",
                "Guard on loading FIRST: while loading, show a message and redirect nobody.",
                "Skip that check and a signed-in student is bounced to /login on every single refresh.",
            ],
            code="""
// src/components/ProtectedRoute.jsx (real code)
const { user, loading } = useAuth()

if (loading) return <p>Checking your session…</p>  // FIRST
if (!user) {
  return <Navigate to="/login" replace
    state={{ from: location }} />   // remember where
}
return <Outlet />
""",
            takeaway="Wait for loading before redirecting, or you eject real users on refresh.",
        ),
        dict(
            title="A client guard is UX, not security",
            kicker="TOPIC 06 · REAL SECURITY",
            analogy="A client-side guard is a velvet rope, not a vault — anyone can step over it in devtools; only the API can lock the door.",
            bullets=[
                "Hiding a link or redirecting from a route improves the experience for honest users.",
                "It is not security: anyone can edit the JavaScript, or skip the app entirely and call /api/ with curl.",
                "The client cannot be trusted, because it runs entirely on the user's own machine.",
                "Real protection is in the API: requireAuth(req) for identity, and `and user_id = ${userId}` for ownership.",
                "Design so that a completely bypassed client guard exposes nothing the server would not already allow.",
            ],
            code="""
// Hiding the link is NOT security:
{user && <NavLink to="/dashboard">Dashboard</NavLink>}

// THIS is security — and it runs on the server:
const userId = requireAuth(req)        // 401 if forged
await sql`select * from enrollments
          where user_id = ${userId}`   // your rows only
""",
            takeaway="Client guards are UX only; the API's auth checks are what protect the data.",
        ),
    ],
}
