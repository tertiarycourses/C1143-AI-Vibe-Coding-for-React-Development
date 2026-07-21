"""
Concept DEEP-DIVE data for the C1143 courseware.

Pure data. One dict, DEEP_DIVES, keyed by topic number (1..6). Each value is
a list of deep-dive dicts:

    dict(heading, paras=[...], code="", bullets=[...])

These become the "Concept deep dive" sections of the Learner Guide DOCX.
Unlike the slide bullets, paras carry no length cap — they are full teaching
prose that explains a concept from first principles, with the analogy woven
through. code may be "" and bullets may be [].

Learners already know modern JavaScript (arrow functions, destructuring,
spread, map/filter, template literals, async/await), so nothing here re-teaches
the language. Every deep dive is about React, the backend, or driving an AI
coding agent.

Written for React 19 (ref is a normal prop, no forwardRef) and a THREE-TIER
backend:

    React (browser) --fetch--> /api/* (Vercel functions) --sql--> Neon Postgres

The browser never talks to Postgres. There is no browser-side Data API, no
Neon Auth, no GRANTs and no Row Level Security: the serverless functions hold
DATABASE_URL, run parameterised (tagged-template) SQL, hash passwords with
bcrypt, and read the user id from a verified JWT. Every example is real code
from the deployed Cook & Bake Academy app (https://cookbake-academy.vercel.app).
"""

DEEP_DIVES = {

    # ============================================================ TOPIC 1
    1: [
        dict(
            heading="What vibe coding actually is",
            paras=[
                "Vibe coding is a way of building software where you describe what you want in plain "
                "language and an AI coding agent writes the code. It is genuinely fast, and it is genuinely "
                "the direction the industry is moving. But the word 'vibe' hides a trap: it makes the process "
                "sound like you can switch your brain off and let the machine drive. You cannot. The right "
                "mental model is an aircraft on autopilot. The autopilot flies the plane and does the tedious "
                "work, but the pilot never stops watching the instruments, and the instant the aircraft drifts, "
                "the pilot takes the controls. In vibe coding you are the pilot, and the code is the aircraft.",
                "That is why this course frames every task as a five-step loop: Prompt, Generate, Read, "
                "Understand, Correct. You write a clear prompt. The agent generates code. Then comes the half "
                "the course actually teaches: you read the output line by line, you understand the React "
                "concept underneath each line, and you correct whatever is wrong before it ever runs in your "
                "project. The agent supplies speed; you supply judgement. Remove your judgement from the loop "
                "and you are not a fast developer, you are a fast producer of bugs you cannot explain.",
                "This matters because an AI agent will hand you code that runs but is subtly wrong far more "
                "often than code that obviously breaks. It will give you a list keyed by array index that "
                "corrupts on delete, an effect with no cleanup that leaks a timer, a fetch with no error "
                "branch that spins forever on a typo, or an /api/ route that trusts a user id out of the "
                "request body. None of these throw an error at you. Every one of them is a bug you can only "
                "catch by reading. The goal of Topic 1 is to make you someone who can build the Cook & Bake "
                "Academy site in minutes and say exactly why every single line of it is there.",
            ],
            code="",
            bullets=[
                "Prompt: describe the outcome you want, with enough context to be unambiguous.",
                "Generate: let the agent produce the code.",
                "Read: go through it line by line, not just glance at the result in the browser.",
                "Understand: name the React concept behind each part.",
                "Correct: fix the subtle bugs before the code enters your project.",
            ],
        ),
        dict(
            heading="Why JSX is not HTML — and what Babel does to it",
            paras=[
                "The single most useful thing you can internalise in Topic 1 is that JSX is not HTML — it is "
                "JavaScript wearing an HTML-shaped costume. The browser has never seen JSX and cannot parse "
                "it; paste <CourseCard fee={680}/> into a console and you get a syntax error. Something has to "
                "translate it into real JavaScript before it ships, and that something is Babel, a compiler. "
                "Vite wires Babel in for you through the @vitejs/plugin-react plugin listed in vite.config.js. "
                "When Babel meets <CourseCard fee={680}/>, it rewrites it into a plain function call, "
                "React.createElement(CourseCard, { fee: 680 }), and that call returns an ordinary JavaScript "
                "object — roughly { type: CourseCard, props: { fee: 680 } }. That object is not markup and it "
                "is not a DOM node; it is a lightweight description React can hold in memory. A whole tree of "
                "those objects is what we later call the Virtual DOM. You are not writing markup the browser "
                "parses; you are writing a blueprint that Babel turns into function calls and React reads to "
                "construct the building.",
                "Once you see JSX as code that compiles to createElement calls, every rule that trips people "
                "up stops being arbitrary. You write className instead of class because class is a reserved "
                "word in JavaScript. Attributes are camelCase (onClick, htmlFor) because they are really keys "
                "in the props object of that createElement call. You wrap expressions in curly braces because "
                "{} is the window through which live JavaScript values flow into the output — and only "
                "expressions, things that produce a value, fit through that window; an if statement or a for "
                "loop produces no value and so is a syntax error inside JSX. And a component must return a "
                "single root element because a function returns exactly one thing; when you do not want an "
                "extra wrapper div, a Fragment (<>...</>) groups the siblings under one root while adding "
                "nothing to the real DOM.",
                "This is also why component names must be capitalised. Babel compiles a lowercase tag like "
                "<div> to createElement('div', ...) — a string, meaning a built-in HTML element — but a "
                "capitalised tag like <CourseCard> to createElement(CourseCard, ...) — an identifier, meaning "
                "your function. The capital letter is the single signal the compiler uses to tell your "
                "components apart from the browser's own elements. None of this is memorisation for its own "
                "sake; every rule falls straight out of the one fact that JSX compiles to createElement calls.",
            ],
            code="// YOU WRITE (JSX):\n<CourseCard course={course} fee={680} />\n\n// BABEL COMPILES IT TO (plain JavaScript):\nReact.createElement(CourseCard, { course: course, fee: 680 })\n\n// WHICH RETURNS (a plain object — a React element):\n{ type: CourseCard, props: { course: {...}, fee: 680 } }",
            bullets=[
                "The browser never sees JSX; Babel (run by Vite via @vitejs/plugin-react) compiles it away.",
                "<CourseCard fee={680}/> becomes React.createElement(CourseCard, {fee:680}), which returns a plain object.",
                "class becomes className, attributes are camelCase, because they are keys in a props object.",
                "{} embeds expressions (values) only; one root per return; capitalised names mean YOUR function.",
            ],
        ),
        dict(
            heading="Components and props: functions and their arguments",
            paras=[
                "A React component is nothing more exotic than a JavaScript function that returns JSX. That is "
                "the entire definition. If you can write a function, you can write a component. The power comes "
                "from the fact that, like any function, a component can take inputs — and in React those inputs "
                "are called props. Think of a component as a cookie cutter: you define the shape once, then "
                "stamp out as many cookies as you like, and props are what let each cookie come out different. "
                "One CourseCard definition renders all twenty Cook & Bake courses, each fed a different course "
                "object.",
                "Props are best understood as a recipe card handed to a chef. The chef reads the card, cooks "
                "exactly what it says, and hands back the dish — but the chef never scribbles on the card. That "
                "is the one rule that matters most: props flow one way, from parent down to child, and they are "
                "read-only. A child component must never reassign a prop it was given. Data flows down. If a "
                "child needs to change something, the parent passes down a function for the child to call — the "
                "way HomePage passes Hero an onBrowse function so the hero's button can trigger a scroll it "
                "knows nothing about — but the value itself stays owned by whoever passed it. This one-way flow "
                "is what makes a React app predictable: you can always trace where a value came from by walking "
                "up the tree.",
                "In practice you read props by destructuring them straight out of the parameter list. The real "
                "CourseCard takes a single course prop — function CourseCard({ course }) — and then pulls the "
                "fields it needs out of that object with const { slug, title, category, fee } = course. One "
                "object prop beats nine loose ones, and there is a deeper payoff: the shape of that object is "
                "exactly the database row you will fetch in Topic 5, so when the data stops being a hard-coded "
                "array and starts arriving over the network, not a single line of CourseCard has to change. "
                "You give a prop a default with an equals sign, ({ fee = 0 }), so a missing prop degrades "
                "gracefully instead of rendering undefined, and you pass props at the call site like "
                "attributes: strings in quotes, everything else in braces, so title=\"Macaron Masterclass\" "
                "fee={420}. When you read AI-generated components, the first thing to check is that the props "
                "flowing in match the props being read out.",
            ],
            code="// src/components/CourseCard.jsx (real code)\nexport default function CourseCard({ course }) {\n  const { slug, title, category, fee } = course\n  return <Link to={`/courses/${slug}`}>{title} — S${fee}</Link>\n}\n\n<CourseCard course={course} />",
            bullets=[
                "A component is a capitalised function that returns JSX.",
                "Props are its arguments, read by destructuring: function CourseCard({ course }).",
                "Props are read-only and flow one way, parent to child.",
                "Pass one object prop whose shape is the DB row, so nothing downstream changes in Topic 5.",
            ],
        ),
        dict(
            heading="A component is a pure function",
            paras=[
                "You already know a component is a JavaScript function that returns JSX, but there is a deeper "
                "property that makes React work at all, and it is worth stating plainly: a component should be a "
                "pure function of its props. Purity has a precise meaning here. Given the same props, a component "
                "must always return the same tree, and while it renders it must not change anything outside "
                "itself — no writing to variables declared elsewhere, no fetching, no timers, no direct DOM edits. "
                "It simply takes props in and returns a description of UI out, like a vending machine that drops "
                "the same snack every time the same button is pressed. The name is capitalised so React can tell "
                "your component apart from a built-in HTML tag, and it returns a single root element because a "
                "function returns exactly one value.",
                "Why does React demand this? Because purity is what lets React call your component whenever it "
                "likes, as often as it likes, and trust the result. React may render a component to build the "
                "Virtual DOM and then throw that render away; it may re-render it many times as state changes; in "
                "development StrictMode deliberately renders it twice to flush out impurity. If rendering had side "
                "effects — incrementing a counter, firing off a request — those would happen unpredictably and "
                "multiply. So React draws a hard line: rendering is for computing UI, and everything else, the "
                "side effects, happens elsewhere. Work triggered by the user goes in event handlers; work that "
                "must synchronise with an external system goes in useEffect (Topic 4). Keep render pure and your "
                "component becomes something React — and you — can reason about; break purity and you get the "
                "class of bugs that appear only sometimes, which are the hardest of all to find.",
                "Purity is also what makes composition safe. React builds complex interfaces by nesting small, "
                "pure components, and the mechanism that keeps this flexible is the children prop: whatever JSX "
                "you place between a component's opening and closing tags arrives inside it as props.children. The "
                "real Section component is exactly this — a picture frame that renders {children} inside a "
                "centred container and does not care whether you slid a CourseGrid, a form, or a paragraph into "
                "it. The design rule that follows is to favour composition over configuration: rather than piling "
                "boolean props onto one component to cover every possible variation, let it accept children and "
                "stay generic. A handful of small pure components you can slot together will take you much "
                "further than one enormous component with thirty configuration props.",
            ],
            code="// src/components/Section.jsx (real code)\nfunction Section({ title, children }) {\n  return (\n    <section className='section'>\n      {title && <h2>{title}</h2>}\n      {children}\n    </section>\n  )\n}\n\n<Section title='Popular courses'><CourseGrid courses={popular} /></Section>",
            bullets=[
                "A component should be pure: same props in, same tree out, with no side effects during render.",
                "Purity lets React render freely — repeatedly, speculatively, twice in StrictMode — and trust the output.",
                "Side effects belong in event handlers and useEffect, never in the body of a render.",
                "Compose small pure components; the children prop lets a wrapper like Section hold any content.",
            ],
        ),
    ],

    # ============================================================ TOPIC 2
    2: [
        dict(
            heading="Git is the vibe coder's safety net",
            paras=[
                "Version control matters for every developer, but for a vibe coder it is not optional — it is "
                "the safety net without which the whole approach is reckless. When you let an AI agent edit your "
                "code, you are handing the keys to something confident, fast, and occasionally very wrong. Git "
                "is the save point that lets you undo any move it makes. The discipline is simple: commit your "
                "working code before you prompt the agent to change anything. That commit is a clean state you "
                "can always return to, no matter how tangled the next few minutes get.",
                "After the agent has worked, git diff is your review tool. It shows you, line by line, exactly "
                "what changed — which is precisely the 'Read' step of the loop made concrete. You are not "
                "trusting the agent's summary of what it did; you are looking at the actual edits. If you like "
                "them, you commit. If the agent has gone off the rails, git restore . throws the changes away "
                "and drops you back at your last commit as if the detour never happened. Small, frequent commits "
                "make this even more powerful, because each one isolates the effect of a single prompt, so when "
                "something breaks you know exactly which instruction caused it.",
            ],
            code="git add -A && git commit -m 'before AI edit'\n\n# prompt the agent, then review:\ngit diff              # what changed?\ngit restore .         # undo if wrong",
            bullets=[
                "Commit before every prompt so you always have a clean point to return to.",
                "git diff is the 'Read' step made concrete — the actual line-by-line changes.",
                "git restore . discards the working changes and returns you to the last commit.",
                "Small, frequent commits isolate which prompt caused which change.",
            ],
        ),
        dict(
            heading="From build to deployment, and the secrets rule",
            paras=[
                "A React app in development runs through Vite's dev server, but that is not what you ship. When "
                "you run npm run build, Vite bundles and minifies everything into a dist/ folder containing "
                "nothing but plain HTML, CSS and JavaScript — Babel has already compiled every piece of JSX "
                "away, so the shipped bundle contains no JSX at all. Those files are static — no Node process "
                "runs them — which is why deploying the front end is really just uploading a folder of files "
                "that any host on earth can serve. The api/ folder is different: Vercel builds each file there "
                "into a serverless function and serves it from the same domain, so the browser can call "
                "/api/courses with no CORS and no separate backend URL. Connect your GitHub repository to Vercel "
                "and all of this becomes automatic: every push to your main branch triggers a fresh build and "
                "deploy of both the static site and the functions, and every branch gets its own preview URL. "
                "This is continuous deployment, and it means your live site always reflects your latest "
                "committed code.",
                "Two rules keep this safe, and both are about secrets. First, some things must never enter Git "
                "at all: node_modules (enormous and reinstallable), dist (rebuildable), and above all .env.local "
                "(your DATABASE_URL and JWT_SECRET). A .gitignore file lists these so Git never tracks them; you "
                "commit .env.example instead, which carries the variable names and placeholder values but no "
                "real secrets. A credential committed even once lives in the history permanently, so a leak "
                "means rotating the key, not just deleting the line. Second, understand exactly what 'public' "
                "means for environment variables, because this is the rule that returns with force in Topic 5. "
                "Vite exposes only variables prefixed VITE_ to your browser code, and it does not look them up "
                "at runtime — it substitutes their values straight into the JavaScript bundle at build time. "
                "That means a VITE_ variable is completely visible to anyone who opens dev tools or simply reads "
                "dist/assets/index-*.js. It is printed on the flyer, not whispered. So a VITE_ variable may hold "
                "a public site name or a public URL, but it may never hold a password, a key or a token — and "
                "DATABASE_URL, which carries the database password, must therefore never carry the VITE_ prefix. "
                "If you ever 'fix' a connection error by renaming DATABASE_URL to VITE_DATABASE_URL, you have "
                "just published full read-and-write access to your database to every visitor of your site.",
            ],
            code="# .gitignore\nnode_modules\ndist\n.env.local          # DATABASE_URL, JWT_SECRET\n\n# .env.example  <- committed; names only, no secrets\nDATABASE_URL=postgresql://USER:PASSWORD@ep-...neon.tech/db\nJWT_SECRET=dev-secret-change-me",
            bullets=[
                "npm run build produces a static dist/ folder; api/ becomes serverless functions on the same domain.",
                "Vercel rebuilds and redeploys both on every push; each branch gets a preview URL.",
                "Never commit node_modules, dist or .env.local — a leaked secret is permanent; commit .env.example.",
                "VITE_ variables are compiled into the browser bundle, so DATABASE_URL must never carry that prefix.",
            ],
        ),
        dict(
            heading="Why refreshing a route can 404",
            paras=[
                "This is the single most common deployment surprise, and it catches almost everyone once. Your "
                "single-page app has exactly one real HTML file: index.html. When a user clicks a <Link> to "
                "/courses, no new file is fetched — React Router simply swaps the view in the browser and "
                "rewrites the URL. It all works beautifully. Then the user bookmarks /courses, or just presses "
                "refresh, and the app 404s. Why? Because a refresh asks the server directly for /courses, and a "
                "static host is a receptionist with a filing cabinet: it looks for a file literally named "
                "courses, finds nothing, and returns 'not found'.",
                "The fix is a rewrite rule that tells the host to hand back /index.html for every path it does "
                "not recognise as a real file. Once index.html loads, React Router reads the URL and renders "
                "the right component, exactly as if you had navigated there in-app. On Vercel this is a couple "
                "of lines in vercel.json, but with one crucial subtlety: the rule must EXCLUDE /api/*. If you "
                "rewrite everything to index.html, your API calls get sent the HTML of your home page instead of "
                "JSON, and res.json() throws the tell-tale \"Unexpected token '<'\" — you asked for data and got "
                "a web page. The real vercel.json uses a negative lookahead, \"/((?!api/).*)\", so every path "
                "except /api/* falls back to index.html. The symptom to watch for is an app that works "
                "perfectly while you click around but breaks the instant anyone refreshes on a deep link — so "
                "test a refresh on /courses before you call a deployment done.",
            ],
            code='// vercel.json (real)\n{\n  "rewrites": [\n    { "source": "/((?!api/).*)", "destination": "/index.html" }\n  ]\n}\n// Everything EXCEPT /api/* falls back to index.html.',
            bullets=[
                "An SPA has one real file; the router fakes the other paths in the browser.",
                "A refresh asks the server for the real path, which does not exist on disk.",
                "Rewrite every unmatched path to /index.html — but EXCLUDE /api/*, or the API returns HTML.",
                "Always test a refresh on a deep link before declaring a deploy finished.",
            ],
        ),
    ],

    # ============================================================ TOPIC 3
    3: [
        dict(
            heading="The real DOM, and updating a page without React",
            paras=[
                "Before you can appreciate what React does, you have to see what it saves you from. When the "
                "browser loads a page it parses the HTML into the DOM — the Document Object Model — which is a "
                "live tree of objects, one for each element. This is the crucial point that beginners miss: the "
                "DOM is not a picture of the page or a copy of it. The DOM IS the page. The pixels on screen are "
                "a rendering of that object tree, so when you change an object in the tree, the screen changes "
                "with it. JavaScript can reach straight into this tree: document.getElementById('count') hands "
                "you the real object for one node, and you can write to its properties — textContent, className, "
                "style, value — and watch the display update.",
                "The problem is not that this is impossible; it is that YOU have to describe every step of HOW. "
                "Suppose the Cook & Bake catalogue has twenty course cards and you add a Bakery/Cooking filter. "
                "In vanilla JavaScript you select every card, loop over them, and toggle each one's display by "
                "hand. But that is only the beginning, because the number of visible courses is shown in a "
                "heading, so you must also find that node and overwrite its text; the active filter chip needs a "
                "class toggled; the empty-state message must appear when nothing matches; the URL might need "
                "updating so the filter is shareable. Every one of these is a separate manual patch, and every "
                "new feature multiplies them. Worse, the truth now lives inside a DOM string: to increment a "
                "count you read '10 courses' back out of a text node, parse the number, add one, and write it "
                "back. Miss a single one of these patches and the screen quietly disagrees with your data — the "
                "heading says twenty while ten cards show. Nothing throws an error. Nobody notices until a user "
                "does. This is exactly the tangle React was built to eliminate, and seeing it first is what "
                "makes the next two ideas land.",
            ],
            code="// Vanilla JS: filter the catalogue BY HAND.\ndocument.querySelectorAll('.card').forEach((card) => {\n  const show = card.dataset.category === 'Bakery'\n  card.style.display = show ? 'block' : 'none'\n})\n// ...now keep the count in step, by hand:\nconst el = document.getElementById('count')\nel.textContent = '10 courses'\n// ...plus the chip, the empty state, the URL...",
            bullets=[
                "The DOM is the browser's live object tree — the page itself, not a copy of it.",
                "Without React you say HOW: getElementById, then overwrite textContent, className, style by hand.",
                "The truth ends up living in DOM strings, which you must read back out and parse to update.",
                "Every feature multiplies the manual patches, and one missed patch silently desyncs the screen.",
            ],
        ),
        dict(
            heading="The Virtual DOM, and declarative UI",
            paras=[
                "React's answer to all that manual patching is the Virtual DOM. Instead of mutating the real DOM "
                "directly, React keeps a lightweight copy of the UI tree made of plain JavaScript objects — "
                "exactly the objects that Babel's createElement calls return, from Topic 1. Building this "
                "virtual tree is cheap, because it is just allocating objects in memory; it is touching the real "
                "DOM that is comparatively slow. Every time your state changes, React builds a brand-new virtual "
                "tree describing what the UI should be right now. Then it does something clever called "
                "reconciliation: it compares that new tree against the previous one, works out the minimal set "
                "of differences, and patches only those into the real DOM. Picture an architect comparing a new "
                "blueprint against the old one before knocking down a single real wall — nothing physical "
                "changes until the cheap paper comparison has found exactly what needs to move. When the Cook & "
                "Bake filter narrows twenty courses to ten, React does not rebuild the navbar, the hero or the "
                "footer; the diff shows they are identical in both trees, so it leaves them completely alone and "
                "only removes ten cards and updates one number.",
                "This is what makes React declarative, and the distinction is the heart of the whole library. "
                "Imperative code is a list of steps to mutate the page — the vanilla filter from the previous "
                "dive. Declarative code describes the end result for the current state and lets React figure "
                "out how to get there. You never write 'update this text node' or 'toggle that display'; you "
                "write 'the visible courses are these, given this filter', and when the filter changes the "
                "correct UI simply follows. It is the difference between reciting a recipe and ordering the "
                "finished dish. And because the UI is always computed fresh from state, it can never silently "
                "fall out of step with your data the way hand-written DOM manipulation does — the desync bug "
                "from the previous dive becomes impossible by construction. Your whole job shrinks to two "
                "things: keep the state correct, and describe the UI as a function of it.",
            ],
            code="// WITHOUT React — you patch the real DOM yourself:\nel.textContent = String(visible.length)\nel.className = visible.length ? 'grid' : 'grid is-empty'\n\n// WITH React — you describe the result, once:\n<p>{visible.length} courses</p>\n<CourseGrid courses={visible} />",
            bullets=[
                "The Virtual DOM is a cheap JavaScript tree (the objects createElement returns) React diffs first.",
                "Reconciliation finds the minimal changes and patches only those real nodes; the rest are untouched.",
                "Declarative means you describe the UI for the current state, not the steps to mutate the page.",
                "Because the UI is recomputed from state, it can never silently drift out of sync with your data.",
            ],
        ),
        dict(
            heading="Keys are identity, and why key={index} bites",
            paras=[
                "When you render a list, you map an array of data into an array of JSX elements, and React asks "
                "you to give each element a key. It is tempting to treat the key as a formality and reach for "
                "the array index, and the agent will often do exactly that. This works right up until the list "
                "changes order, and then it produces one of the most confusing bugs in React. The reason is "
                "what a key actually means. A key is not a position — it is an identity. It is the name tag a "
                "student wears, not the seat they happen to be sitting in. Across renders, React uses keys to "
                "answer the question 'is this the same item as before, or a different one?' so it can move, "
                "keep, or remove the right rows rather than rebuilding the whole list.",
                "Now picture the Cook & Bake grid keyed by index 0, 1, 2, and imagine each card holds some "
                "internal state — a hover flourish, or an input. Filter the catalogue to Bakery only, and the "
                "course that used to sit at index 3 is now at index 0. React sees 'key 0 still exists' and keeps "
                "the state that belonged to the old index-0 card, attaching it to a completely different course. "
                "The visible symptom is state jumping to the wrong cards on filter, reorder or delete. The fix "
                "is to key by something stable and unique from your data — course.id, which the real CourseGrid "
                "uses — so the name tag travels with the item no matter where it moves in the list. Whenever you "
                "review AI-generated list code, checking the key is one of the highest-value things you can do, "
                "because this bug renders perfectly and only surfaces on interaction.",
            ],
            code="// src/components/CourseGrid.jsx (real code)\n{courses.map((course) => (\n  <CourseCard key={course.id} course={course} />\n))}\n\n// key={index} corrupts state when you filter to Bakery",
            bullets=[
                "A key is a stable identity, not a position — a name tag, not a seat number.",
                "React uses keys to move, keep or remove the right cards across renders.",
                "key={index} attaches state to the wrong course when the grid filters, reorders or shrinks.",
                "Key by a stable id (course.id) from your data; auditing keys is high-value on AI code.",
            ],
        ),
        dict(
            heading="Composition, events and controlled inputs",
            paras=[
                "React builds complex interfaces by composing simple components, and the mechanism that makes "
                "this elegant is the children prop. Whatever JSX you place between a component's opening and "
                "closing tags arrives inside that component as props.children. The real Section component uses "
                "exactly this: it renders {children} inside a centred container, so it can wrap a CourseGrid on "
                "the home page and a form somewhere else without knowing or caring what it holds. The lesson is "
                "to favour composition over configuration: rather than growing a component endless boolean props "
                "to cover every case, let it wrap arbitrary children and stay generic. A Section that renders "
                "{children} is reusable everywhere; a Section with twenty props for every possible layout is "
                "reusable nowhere.",
                "Interactivity comes from events. You attach handlers with camelCase props like onClick and "
                "onChange, and the critical detail is that you pass the function rather than call it: "
                "onClick={handleEnroll}, never onClick={handleEnroll()}, because the second runs it immediately "
                "during render. When you need to pass an argument you wrap the call in an arrow, exactly as "
                "CategoryFilter does — onClick={() => onChange(cat.value)} — so the function runs on click, not "
                "on render. React hands your handler a synthetic event, a cross-browser wrapper that smooths "
                "over the differences between browsers, a universal remote over everyone's slightly different "
                "hardware. From it you read e.target.value to see what the user typed, and you call "
                "e.preventDefault() to stop a form doing its default full-page reload.",
                "Those two ideas combine in the controlled input, the standard way React handles forms. In a "
                "controlled input, React state is the single source of truth for the field: you bind "
                "value={state} and update that state in onChange. The real SearchBar is precisely this — it "
                "owns no state of its own, takes the value down as a prop and reports every keystroke back up "
                "through onChange. The input becomes a puppet on React's strings: state moves the field, and "
                "every keystroke reports back to pull the string. This is more setup than an uncontrolled field, "
                "but it is what unlocks the live-as-you-type search filter, validation, and disabling a submit "
                "button until a form is valid. If you set value without an onChange, React warns you that you "
                "have made a read-only field, because you have given it a source of truth but no way to update "
                "it.",
            ],
            code="// src/components/SearchBar.jsx (real code)\nexport default function SearchBar({ value, onChange }) {\n  return (\n    <input\n      type='search'\n      value={value}\n      onChange={(e) => onChange(e.target.value)}\n    />\n  )\n}",
            bullets=[
                "children lets a component like Section wrap arbitrary content — favour composition over configuration.",
                "Pass a function to onClick/onChange; wrap it in an arrow to pass an argument (() => onChange(x)).",
                "Synthetic events give one consistent, cross-browser event object; read e.target.value from it.",
                "A controlled input binds value to state and updates it in onChange — SearchBar owns nothing.",
            ],
        ),
        dict(
            heading="State: a component's memory",
            paras=[
                "Topic 3 introduces the single idea that turns a static page into an application: state. State is a "
                "component's memory — the data it owns and remembers from one render to the next. The reason a "
                "component needs a special mechanism for this, rather than an ordinary variable, is that a "
                "component function runs again from scratch on every render. Any plain variable you declare "
                "inside it is created fresh and thrown away each time, so changing it does nothing lasting "
                "and, crucially, cannot change what is on screen. Write let query = '' and then query = 'sushi' "
                "inside a component and the screen never moves, because the next render simply starts over at "
                "the empty string. State is the notepad React keeps for the component between renders; a local "
                "variable is scratch paper torn off and binned each time.",
                "You create state with useState, which hands back the current value and a setter: "
                "const [query, setQuery] = useState(''). The setter is the important half, because calling it "
                "does two things at once. It stores the new value so the component will remember it on the next "
                "render, and it schedules a re-render so the screen catches up. That second step is precisely "
                "what a plain variable can never do. This is the loop at the heart of React: an event calls the "
                "setter, the setter records the new state and asks React to re-render, the component runs again, "
                "and it returns fresh JSX computed from the new state. You never touch the DOM yourself — you "
                "change state, and the declarative render you met earlier redraws the UI to match. State and "
                "screen stay in step by construction, which is the exact opposite of the manual-DOM desync from "
                "the first dive in this topic.",
                "Deciding whether a value should be state or a prop comes down to one question: does this "
                "component own the value, or was it given the value? Props come from the parent and are "
                "read-only; state is owned locally and can change over time. SearchBar owns nothing and is all "
                "props; CoursesPage owns the search query in state and passes it down. When several components "
                "need the same changing value, the answer is not to copy state into each of them — it is to lift "
                "the state up to their nearest common parent and pass it back down as props, so there is a "
                "single source of truth. Two rules from Topic 4 then govern how you change state safely, and "
                "they are worth previewing: within a render the state value is a fixed snapshot, and you replace "
                "it with a brand-new value rather than mutating it in place. But the foundational idea comes "
                "first and is simpler — state is the memory that lets a component change, and the setter is what "
                "makes the screen follow.",
            ],
            code="let query = ''       // reset every render — useless\nquery = 'sushi'      // the screen never moves\n\nconst [query, setQuery] = useState('')\nsetQuery('sushi')    // stored, and re-renders the UI",
            bullets=[
                "State is data a component owns and remembers across renders; a local variable resets every render.",
                "A plain variable cannot update the screen — only a setter both stores a value and re-renders.",
                "The loop: event → setter → re-render → UI recomputed from the new state.",
                "Ask 'owned or given?' — owned is state, given is a prop; lift shared state to a common parent.",
            ],
        ),
    ],

    # ============================================================ TOPIC 4
    4: [
        dict(
            heading="State is a snapshot, and updates are immutable",
            paras=[
                "The deepest source of confusion with useState is expecting the state variable to change the "
                "moment you set it. It does not. Within a single render, a state value is a snapshot — a "
                "photograph taken when that render began — and it stays frozen at that value for the whole "
                "render, no matter how many times you call the setter. This is why setCount(count + 1) called "
                "twice in a row only increments once: both calls read the same frozen count and both schedule "
                "it to become that same value plus one. When the next value depends on the previous, you must "
                "use the updater form, setCount(c => c + 1), which hands React a function that receives the "
                "latest pending value rather than the stale snapshot. Two updater calls correctly increment by "
                "two, because each builds on the result of the last.",
                "The second half of using state correctly is immutability. React decides whether to re-render "
                "by checking whether the new state is a different reference from the old one — not whether its "
                "contents differ. So items.push(course) is invisible to React: it mutates the same array, the "
                "reference is unchanged, and nothing re-renders. Mutating state is like editing the original "
                "photograph; React only reacts when you hand it a brand-new print. You create that new "
                "reference with the spread operator: the real CartContext adds to the shortlist with "
                "setItems(prev => [...prev, course]) — a fresh array — and updates an object the same way with "
                "{ ...course, fee: 720 }. This is why immutable updates underpin every single state update you "
                "will write; a stray .push() is one of the quiet bugs to watch for in generated code, because "
                "the array really does change but the screen never does.",
            ],
            code="// src/context/CartContext.jsx (real code)\nsetItems((prev) =>\n  prev.some((c) => c.id === course.id)\n    ? prev\n    : [...prev, course])   // NEW array -> re-renders\n\n// items.push(course)      // same array -> nothing renders",
            bullets=[
                "A state value is a snapshot, frozen for the whole render.",
                "Use setX(prev => ...) whenever the next value depends on the previous one.",
                "React re-renders on a new reference, not on changed contents.",
                "Build new arrays/objects with spread; never push or mutate state in place.",
            ],
        ),
        dict(
            heading="useEffect: dependencies, cleanup and StrictMode",
            paras=[
                "useEffect exists for side effects — the things that reach outside React's render, such as "
                "fetching data, setting up a subscription, starting a timer, or touching the DOM directly. Its "
                "behaviour is governed entirely by its second argument, the dependency array, which acts like a "
                "guest list: the effect re-runs only when a value on the list actually changes. An empty array "
                "means it runs once after the first render and never again — how ThemeContext applies the saved "
                "theme on boot. Listing [theme] means it re-runs whenever the theme changes, which is how the "
                "toggle updates <html data-theme>. Listing [slug] is how a detail page refetches when the user "
                "navigates to a different course. Omitting the array entirely means it runs after every render, "
                "which is almost always a mistake and a common cause of infinite fetch loops in generated code.",
                "The other half of useEffect is cleanup, and it is the part AI code forgets most often. Any "
                "effect that starts something ongoing must also stop it, or you leak. A timer keeps ticking "
                "after the component is gone; an event listener keeps firing; a subscription keeps receiving. "
                "You prevent this by returning a cleanup function from the effect — React runs it before the "
                "next effect and when the component unmounts. The real useDebounce hook shows the pattern in "
                "miniature: it sets a timeout and returns () => clearTimeout(id), so every keystroke cancels the "
                "previous pending timer and only the last one ever fires. The mental image is turning the tap "
                "off as you leave the room: whatever you turned on, turn off in the returned function.",
                "This is where StrictMode enters, and why it confuses people. In development, React's "
                "StrictMode deliberately mounts each component, immediately unmounts it, and mounts it again. "
                "It does this to expose effects with no cleanup: if your effect sets a timer and never clears "
                "it, StrictMode's double-invoke leaves two timers running and you notice. So a console message "
                "that logs twice in development is not a bug — it is React holding up a mirror to a missing "
                "cleanup. Write the cleanup, and the double-invoke becomes harmless. In production StrictMode "
                "does not double-invoke, but by then your effects are already correct.",
            ],
            code="// src/hooks/useDebounce.js (real code)\nuseEffect(() => {\n  const id = setTimeout(() => setDebounced(value), delay)\n  return () => clearTimeout(id)   // cleanup\n}, [value, delay])",
            bullets=[
                "The dependency array controls when the effect re-runs: [] once, [dep] on change, none every render.",
                "Return a cleanup function to tear down timers, listeners and subscriptions.",
                "StrictMode double-invokes effects in development to expose missing cleanups.",
                "A double log in dev usually means an effect you forgot to clean up.",
            ],
        ),
        dict(
            heading="useRef: two jobs, and the dividing line against state",
            paras=[
                "useRef returns a small object with a single property, current, and it has two defining "
                "characteristics. Like state, the value survives across renders — React hands you back the same "
                "ref object every render, so whatever you stored in .current is still there. Unlike state, "
                "changing .current does not trigger a re-render. That combination is the whole point: a ref is a "
                "sticky note the renderer never reads. It gives you exactly one clean decision to make, and "
                "learning to make it is a real mark of understanding React: should changing this value redraw "
                "the screen? If yes, it is state. If no, it is a ref. The search text in CoursesPage is state, "
                "because every keystroke must repaint the filtered results. Which DOM node the search box is, "
                "and whether it is focused, is a ref, because focusing it changes nothing that is rendered.",
                "That dividing line has a sharp, practical edge, and it is worth stating as a warning: a value "
                "that changes often but should not repaint the screen is a ref, and putting it in state instead "
                "is a real performance bug. The classic example is the id returned by setInterval or setTimeout. "
                "You need to keep it so you can clear the timer later, but it should never cause a render — and "
                "if you stored it in state, the component would re-render every time the timer id changed, which "
                "for a per-second tick means re-rendering the whole component every second for nothing. A plain "
                "variable cannot do the job either, because it is reset on every render. A ref threads the "
                "needle: it remembers the value across renders, and touching it costs nothing.",
                "The ref's second job is to be the sanctioned escape hatch to the real DOM. Most of the time you "
                "never touch the DOM in React; you describe UI as a function of state and let React do the rest. "
                "But a few things genuinely require a live DOM node, and 'is focused' or 'scroll to here' are "
                "browser state that no JSX can express. The Cook & Bake app uses this in three real places. "
                "CoursesPage creates a ref, hands it to SearchBar as an ordinary prop, and calls "
                "searchInput.current?.focus() in a mount effect so the cursor lands in the search box — and "
                "again after every category chip, so the user can keep typing. HomePage points a ref at the "
                "course grid and gives the hero an onBrowse function that calls "
                "popularRef.current?.scrollIntoView, so 'Browse courses' smoothly scrolls down; note that Hero "
                "receives only a function and never knows a DOM node exists. And a timer id, as above, lives in "
                "a ref. Two details matter: .current is null on the first render because React has not created "
                "the node yet, and is filled right after paint, which is why you read it inside an effect; and "
                "in React 19 ref is now an ordinary prop, so you pass it straight through to your own "
                "components with no forwardRef wrapper. The discipline to keep is that refs are the escape "
                "hatch, not the main road: reach for a DOM ref only for the handful of things state genuinely "
                "cannot express.",
            ],
            code="// src/pages/CoursesPage.jsx  (focus)  ·  HomePage.jsx  (scroll)\nconst searchInput = useRef(null)          // a DOM handle\nuseEffect(() => { searchInput.current?.focus() }, [])\n<SearchBar inputRef={searchInput} ... />   // ref as a prop\n\nconst popularRef = useRef(null)\nconst scrollToCourses = () =>\n  popularRef.current?.scrollIntoView({ behavior: 'smooth' })\n<Hero onBrowse={scrollToCourses} />\n<section ref={popularRef}>...</section>",
            bullets=[
                "A ref persists across renders like state, but changing it never triggers a re-render.",
                "The rule: should changing it redraw the screen? Yes = state; no = ref.",
                "Job one: a mutable box for values you must remember but must not repaint on — like a timer id.",
                "Job two: a live DOM handle for focus, scroll or measurement, read inside an effect after mount.",
                "A timer id in state re-renders on every tick; React 19 makes ref a normal prop — no forwardRef.",
            ],
        ),
        dict(
            heading="Context, reducers and custom hooks",
            paras=[
                "Context solves prop drilling: the tedious threading of a value through layers of components "
                "that do not use it, purely to reach a deep child. Context is the building's PA system compared "
                "to passing a note desk to desk down every floor — you provide a value once, high in the tree, "
                "and any component below reads it directly with useContext, skipping every layer in between. It "
                "is dependency injection for React. Cook & Bake has three contexts, each wrapped around App in "
                "main.jsx: ThemeContext holds the light/dark choice, AuthContext holds the signed-in user, and "
                "CartContext holds the shortlist. Each exposes a custom hook — useTheme, useAuth, useCart — that "
                "wraps useContext and throws a clear error if used outside its provider, so Navbar can read the "
                "shortlist count with a single line and no prop drilling. The one caution is that every consumer "
                "re-renders when the context value changes, so context is wrong for high-frequency updates like "
                "keystrokes; it shines for relatively stable shared state like the current user, theme, or "
                "shortlist.",
                "For state with several related operations, useReducer is often clearer than juggling many "
                "useState calls. A reducer is a pure function of the form (state, action) => newState — a "
                "vending machine where each labelled button (an action like { type: 'ADD', course }) yields a "
                "predictable new state, and, being pure, it must return new state rather than mutating what it "
                "was given. The shortlist's add, remove and clear map naturally onto a reducer's cases, each "
                "returning a fresh array with the spread operator.",
                "Finally, a custom hook is any function named with a leading 'use' that packages hook logic for "
                "reuse. The Cook & Bake app is full of them: useLocalStorage (a useState that persists), "
                "useDebounce (a value that lags behind by a delay), useCourses and useCourse and useReviews "
                "(each wrapping a fetch with loading and error state). The vital thing to grasp is that custom "
                "hooks share logic, not state: ThemeContext and CartContext both call useLocalStorage, but each "
                "gets its own independent key and value. You are reusing the behaviour, not sharing a single "
                "value between them — which is exactly why a custom hook is safe to call from as many "
                "components as you like.",
            ],
            code="// src/context/CartContext.jsx (real code)\nexport function useCart() {\n  const ctx = useContext(CartContext)\n  if (!ctx) throw new Error('useCart must be used inside <CartProvider>')\n  return ctx\n}\n\nconst { count } = useCart()   // any depth, no prop drilling",
            bullets=[
                "Context provides a value once and reads it anywhere below, ending prop drilling.",
                "Cook & Bake has three: ThemeContext, AuthContext, CartContext — each with its own custom hook.",
                "Reducers are pure (state, action) => newState and must return new state, never mutate.",
                "Custom hooks share logic, not state — two callers of useLocalStorage get independent values.",
            ],
        ),
        dict(
            heading="What a hook is, and why the rules exist",
            paras=[
                "Before you can use hooks well, it helps to know what a hook actually is. A hook is simply a "
                "function whose name begins with 'use' and that lets a plain function component tap into React's "
                "built-in features: useState gives it memory, useEffect lets it synchronise with the outside "
                "world, useContext reads shared values, useRef holds a mutable box. Before hooks existed, only "
                "class components could do these things; hooks brought state and lifecycle to ordinary functions, "
                "which is why modern React — and every line of the Cook & Bake app — is written with them and "
                "never with class components. A hook is a power outlet on the render: call use…() at the top of "
                "your function and it plugs into machinery React maintains on the component's behalf.",
                "Now the part that explains every rule you have been told to follow. React does not identify your "
                "hooks by name — it identifies them by the order in which they are called. Picture React keeping, "
                "for each component instance, an ordered list of memory slots. The first time the component "
                "renders, the first useState call claims slot one, the second useState claims slot two, the "
                "useRef claims slot three, the useEffect claims slot four, and so on down the list. On every "
                "subsequent render React walks that same list in the same order, handing slot one back to the "
                "first hook it meets, slot two to the second, and so on. It has no names to match on, only "
                "position. This is elegant and fast, but it has an ironclad requirement: the sequence of hook "
                "calls must be exactly the same on every single render.",
                "That single fact is the origin of the Rules of Hooks. If you call a hook inside an if, a loop, "
                "or after an early return, then on some renders that call happens and on others it does not — the "
                "slots shift, and slot two's state suddenly gets handed to what used to be slot three. The result "
                "is state attaching to the wrong hook, corrupt values, and crashes. So the rules are not "
                "arbitrary ceremony: call hooks only at the top level of a component or another hook, never "
                "conditionally, so the call order can never change; and call them only from React function "
                "components or your own custom hooks, because only those run inside React's render machinery. The "
                "eslint-plugin-react-hooks lint rules catch almost every violation automatically — treat a "
                "warning from them as a real bug, never as noise to silence. And note the consequence for custom "
                "hooks: because each component that calls a custom hook runs its hook calls in its own slot list, "
                "custom hooks share logic, not state — every caller gets its own independent copy.",
            ],
            code="function CoursesPage() {\n  const { courses } = useCourses()   // slot 1\n  const [query, setQuery] = useState('')  // slot 2\n  const searchInput = useRef(null)   // slot 3\n  useEffect(() => { /* ... */ }, [])  // slot 4\n  // order is identical every render, so slots line up\n}",
            bullets=[
                "A hook is a use…() function that lets a function component tap React's memory and lifecycle.",
                "React tracks hooks by call order, matching each to a memory slot by position, not by name.",
                "So the call order must be identical every render — no hooks in ifs, loops or after an early return.",
                "Call hooks only from components or custom hooks; custom hooks share logic, not state.",
            ],
        ),
    ],

    # ============================================================ TOPIC 5
    5: [
        dict(
            heading="Three tiers: why the browser never touches Postgres",
            paras=[
                "Everything in Topic 5 rests on one diagram: React (in the browser) calls /api/* (serverless "
                "functions on Vercel), and only those functions run SQL against Neon Postgres. Three tiers, and "
                "the rule that gives them meaning is that the browser NEVER talks to Postgres. It has no "
                "database driver, no connection string, and no SQL anywhere in it. Look at src/lib/api.js and "
                "you will find no password and no query — only fetch calls to our own /api/* URLs. Think of the "
                "API as the counter in a bank: customers state what they want, but only staff go into the "
                "vault, and the customer never sees the combination. This is not architectural fashion; it is "
                "the only place security can actually live. Anything you check in the browser, a determined user "
                "can bypass by editing the JavaScript or calling the API directly with curl. Anything you "
                "enforce inside an /api/ function runs on a server the user cannot touch. So the browser decides "
                "WHAT it wants; the server decides WHO is allowed and WHAT is true.",
                "The concrete reason the browser cannot be trusted with a connection is the environment-variable "
                "rule from Topic 2, now with teeth. Vite compiles any variable prefixed VITE_ straight into the "
                "JavaScript bundle every visitor downloads — it is public, always, with no exception. "
                "DATABASE_URL contains the database password and grants full read AND write access to all your "
                "data, so it must never carry the VITE_ prefix. It is read in exactly one place, api/_lib/db.js, "
                "as process.env.DATABASE_URL, which only Node code running on Vercel's servers can see. The "
                "single most dangerous 'fix' a beginner or an over-eager agent can make is to rename it "
                "VITE_DATABASE_URL to make a connection error go away — that one edit publishes full control of "
                "your database to every visitor of the site. The same rule protects JWT_SECRET: anyone who "
                "learns it can mint a valid login token for any user, so it too is server-only.",
            ],
            code="// api/_lib/db.js (real code)\nimport { neon } from '@neondatabase/serverless'\n\n// No VITE_ prefix, so Vite never bundles it. Server-only.\nexport const sql = neon(process.env.DATABASE_URL)\n\n// src/lib/api.js (the browser) holds NO url, NO sql:\nawait fetch('/api/courses')   // that is all the browser knows",
            bullets=[
                "React → /api/* → Neon. The browser never talks to Postgres; it only calls our own /api/* URLs.",
                "Security can only live on the server: a client check is bypassable with devtools or curl.",
                "A VITE_ variable is compiled into the public bundle, so DATABASE_URL must never carry that prefix.",
                "DATABASE_URL and JWT_SECRET are read only in api/ via process.env — never in React code.",
            ],
        ),
        dict(
            heading="Serverless API routes and parameterised SQL",
            paras=[
                "A serverless API route is far simpler than a traditional backend: a file in the api/ folder "
                "becomes a URL, and it exports one default async handler(req, res). There is no Express app to "
                "configure and no server process to keep alive — Vercel runs the function on demand when a "
                "request arrives. api/courses/index.js serves GET /api/courses; putting the filename in square "
                "brackets makes the route dynamic, so api/courses/[slug].js matches "
                "/api/courses/macaron-masterclass and hands you the matched segment as req.query.slug. The "
                "handler's job is to read the request, run a query, and answer with a status code and JSON — and "
                "the status code IS the answer: 200 with a course, 404 when no slug matches, 401 when the token "
                "is missing or forged. The front-end hooks translate those codes into screens, which is why "
                "useCourse renders a real 'Course not found' page from a 404 rather than a red error.",
                "The security heart of every route is how it puts values into SQL, and it rests on a JavaScript "
                "feature that is easy to miss: the tagged template. When you write sql`select ... where slug = "
                "${slug}`, you are not calling sql with an interpolated string; you are calling it as a tagged "
                "template, and that distinction is the whole defence against SQL injection. The driver does not "
                "paste the value into the query text. It sends Postgres the query with a numbered placeholder "
                "— where slug = $1 — and sends the value separately, as data. Postgres parses the SQL first, "
                "decides what is a keyword and what is a table, and only THEN binds the value into the "
                "placeholder. Because the value arrives after parsing is finished, it can never be interpreted "
                "as SQL. A slug of x'; drop table users; -- is simply looked up as an absurd literal string "
                "that matches no course; it cannot execute. The one thing that would reintroduce the "
                "vulnerability is building the query string yourself with ordinary interpolation — "
                "sql(`... where slug = '${slug}'`) — which pastes the attacker's text straight into the SQL. "
                "The Cook & Bake codebase never does this: every query is a tagged template, there is no "
                "string-built SQL and no sql.unsafe anywhere, deliberately, so there is no door to walk user "
                "input through. One more practical note that bites everyone once: Postgres returns bigint and "
                "numeric columns as strings, so the queries cast explicitly — id::int, fee::float8 — and the "
                "browser receives real numbers, which keeps course.id === enrollment.course_id from silently "
                "comparing 1 with '1'.",
            ],
            code="// api/courses/[slug].js (real code)\nexport default async function handler(req, res) {\n  const { slug } = req.query ?? {}\n  const rows = await sql`\n    select id::int as id, code, slug, title, fee::float8 as fee\n    from courses where slug = ${slug}\n  `\n  if (rows.length === 0) throw new HttpError(404, 'No course.')\n  return res.status(200).json(rows[0])\n}\n// Postgres receives:  where slug = $1   +   [\"...\"]",
            bullets=[
                "A file in api/ is a URL exporting one async handler; [slug] makes it a dynamic route.",
                "The status code is the answer: 200 a course, 404 no such slug, 401 no valid token.",
                "sql`... ${slug}` is a tagged template — the value travels separately and is never parsed as SQL.",
                "Never build SQL by string concatenation; cast ids with ::int so numbers compare correctly.",
            ],
        ),
        dict(
            heading="Passwords, tokens, and enforcing ownership in SQL",
            paras=[
                "Authentication and authorisation are where a hobby app becomes a real one, and the Cook & Bake "
                "backend does both in a handful of small, careful functions. Start with passwords, and the "
                "iron rule: never store one. When a user signs up, api/auth/signup.js runs bcrypt.hash(password, "
                "10) and stores only the resulting hash. Hashing is one-way — you cannot turn a hash back into "
                "the password — and bcrypt is deliberately slow, so brute-forcing a stolen table is painfully "
                "expensive; it also salts every hash automatically, so two users who happen to pick the same "
                "password still get different hashes. Just as important is what leaves the function: the INSERT's "
                "RETURNING list is id, email, name, created_at, and password_hash is deliberately not in it. The "
                "hash never appears in a response body or a log line. Login mirrors this: api/auth/login.js "
                "selects password_hash into a local variable — the only place it is ever read — and verifies the "
                "attempt with bcrypt.compare(), which re-hashes with the stored salt and compares in constant "
                "time. It returns one identical error for both 'no such email' and 'wrong password', so an "
                "attacker cannot use the response to discover which emails have accounts.",
                "On success, login and signup issue a JSON Web Token. A JWT is three base64 chunks — "
                "header.payload.signature — and the crucial thing to understand is that the payload is only "
                "ENCODED, not encrypted; anyone can read it, so it must never contain a secret. What makes it "
                "trustworthy is the signature, computed with JWT_SECRET, which only the server knows. Change a "
                "single byte of the payload — say, the sub claim, which holds the user's id, from your id to "
                "someone else's — and the signature no longer matches, so jwt.verify throws. This is the entire "
                "basis of the most important rule in the backend: the user id ALWAYS comes from the verified "
                "token, and NEVER from the request body. requireAuth(req) in api/_lib/auth.js reads the "
                "Authorization: Bearer header, verifies the signature, and returns Number(payload.sub) — an id "
                "the caller cannot forge. If POST /api/enrollments trusted req.body.userId instead, anyone with "
                "curl could enrol anyone; because it reads the id from the token, a request can only ever act as "
                "the person who holds that token.",
                "Verifying WHO is calling is only half of authorisation; the other half is making sure they can "
                "only touch their OWN rows, and in this app that check lives in the SQL itself. Consider "
                "DELETE /api/enrollments/:id. The id comes from the address bar, so a caller can change a 4 to a "
                "5 and ask to delete enrollment 5 — which may belong to another student. The id alone must "
                "therefore never be enough. Every statement carries two conditions: where id = ${id} and "
                "user_id = ${userId}, where userId is the verified value from the token. A row the caller does "
                "not own simply does not match, so Postgres deletes nothing and the route answers 404. There is "
                "no Row Level Security behind this doing the work invisibly — this WHERE clause IS the access "
                "control, and forgetting the second condition is the classic Insecure Direct Object Reference, "
                "one of the most common real-world API vulnerabilities. The same pattern secures enrolling "
                "(the row is inserted with user_id = ${userId}, never a client-supplied id) and reviews (the "
                "UPSERT can only ever touch the caller's own review). Read as one sentence: the URL says WHICH "
                "row, the token says WHOSE, and both go into the WHERE clause.",
            ],
            code="// api/enrollments/[id].js (real code)\nconst userId = requireAuth(req)   // verified JWT 'sub'\nconst { id } = req.query ?? {}     // from the URL\n\nconst rows = await sql`\n  delete from enrollments\n  where id = ${id} and user_id = ${userId}\n  returning id::int as id\n`\nif (rows.length === 0) throw new HttpError(404, 'Not found.')",
            bullets=[
                "Never store a password: bcrypt.hash on signup, bcrypt.compare on login; the hash never leaves the server.",
                "Whitelist response fields (RETURNING id, email, name…) so password_hash cannot leak.",
                "A JWT's payload is only encoded — the signature (JWT_SECRET) is what makes it trustworthy.",
                "The user id comes from the verified token, never req.body; requireAuth returns an id you cannot forge.",
                "Enforce ownership in SQL: `where id = ${id} and user_id = ${userId}` — the WHERE clause IS the access control.",
            ],
        ),
        dict(
            heading="The three states of a fetch, and response.ok",
            paras=[
                "Once the data lives behind a network call, the front end has to cope with the fact that a read "
                "is never instant and can fail. Any remote read is in one of three states — loading, error, or "
                "success — and you must model all three explicitly, usually as the data itself, a loading flag "
                "and an error value. While loading, show a skeleton; on error, show a message; on success, "
                "render the data. This is precisely where AI-generated code fails in a recognisable way: it "
                "reliably writes the loading and success branches and forgets the error branch entirely, which "
                "is exactly why a real app spins forever on a failed request instead of telling the user "
                "something went wrong. The real useCourses hook models all three, and — just as important — "
                "clears the loading flag in a finally block, so a failure stops the spinner instead of leaving "
                "it turning forever. Treat a fetch as a package delivery that is either in transit, lost, or on "
                "your doorstep, and make sure the UI can render all three.",
                "There is a specific browser trap that magnifies this, and the Cook & Bake api wrapper exists to "
                "handle it once for everyone. fetch only rejects its Promise on a genuine network failure — the "
                "road being out. A 404 or a 500 is a response that arrived successfully; it is a signed "
                "'not found' slip, delivered to your door. So the await resolves normally, and if you go "
                "straight to response.json() you will happily parse an error page and render nonsense. The guard "
                "is to check response.ok, which is true only for status codes in the 200s, before reading the "
                "body — and to throw if it is false, so the catch block runs and the error state is set. "
                "src/lib/api.js does this in one place and, cleverly, carries the status code onto the thrown "
                "error (err.status = res.status). That lets each hook tell the difference between failures that "
                "look the same to fetch but mean different things: useCourse turns a 404 into 'course not "
                "found' with no error screen, but shows the red error for a 500. Two different failures, two "
                "different screens — collapsing them is how you end up showing 'Something went wrong' to a user "
                "who simply mistyped a URL.",
            ],
            code="// src/lib/api.js (real code)\nconst data = res.status === 204 ? null : await res.json()\n\nif (!res.ok) {                       // fetch won't do this\n  const err = new Error(data?.error ?? `Failed (${res.status})`)\n  err.status = res.status            // 404 vs 500\n  throw err\n}\nreturn data",
            bullets=[
                "Model loading, error and success as three explicit states, and clear the flag in a finally.",
                "AI code reliably writes loading and success and forgets error — the branch that stops the spinner.",
                "fetch rejects only on network failure — a 404 resolves normally, so check response.ok yourself.",
                "Carry the status on the thrown error so a 404 (not found) is distinguishable from a 500 (broke).",
            ],
        ),
    ],

    # ============================================================ TOPIC 6
    6: [
        dict(
            heading="Single-page apps and client-side routing",
            paras=[
                "A traditional website fetches a fresh HTML page from the server every time you navigate — you "
                "physically move to a new document. A single-page application works differently: it loads one "
                "HTML document once, and from then on JavaScript swaps the visible view in place and rewrites "
                "the URL bar, with no server round-trip. It is a theatre with a single stage where the scenery "
                "and the marquee change while the audience never leaves their seats. The benefit is that "
                "navigation is instant and, crucially, your React state survives it — the shortlist, the search "
                "box, the scroll position are all still there because the page never actually reloaded.",
                "React itself has no router; routing is a separate concern solved by a library, and this course "
                "uses React Router in its declarative mode. You declare a set of routes that map URL paths to "
                "the components that should render for them, and the router watches the URL and renders the "
                "match. This is why the choice between <Link> and a plain <a> tag is not cosmetic. An <a href> "
                "triggers a full-page reload: it rebuilds the entire theatre between scenes and throws away "
                "every piece of React state you were holding. <Link to> navigates within the SPA — it swaps the "
                "set and updates the URL while keeping every actor in place. In Cook & Bake the whole CourseCard "
                "is a <Link>, so clicking anywhere on a card routes to its detail page with no reload. Use <a> "
                "only for links that truly leave your app, and <Link> for every internal route.",
            ],
            code="// src/components/CourseCard.jsx (real code)\n<Link to={`/courses/${slug}`} className='card'>\n  ...the entire card...\n</Link>\n\n<a href='/courses'>Browse</a>   // full reload: state gone",
            bullets=[
                "An SPA loads one document; JavaScript swaps views and rewrites the URL.",
                "Navigation is instant and React state survives because nothing reloads.",
                "React has no built-in router; React Router maps paths to components.",
                "<Link> navigates in-app and preserves state; <a> reloads and discards it.",
            ],
        ),
        dict(
            heading="Layouts, dynamic params and URL state",
            paras=[
                "Real apps share chrome — a navbar, a footer, a sidebar — across many pages, and you do not "
                "want to repeat it in every component. A layout route solves this: it is a parent route that "
                "renders the shared structure once, and its child routes render inside it. The layout marks "
                "where children go by rendering <Outlet/> — a picture frame with a window, where each page's "
                "picture slots into the same surrounding frame. RootLayout is exactly this: it renders the "
                "Navbar and Footer once and an <Outlet/> in between for the matched page. Layouts nest, too: "
                "DashboardPage is itself a layout with its own <Outlet/>, inside which My Courses and Profile "
                "render. And a PATHLESS parent route — one with an element but no path — adds no URL segment at "
                "all, which is precisely how ProtectedRoute wraps and gates a whole subtree without changing "
                "any address.",
                "Most real routes are not fixed strings but patterns. A path segment written with a leading "
                "colon, like /courses/:slug, is a placeholder that matches any value, so one route definition "
                "serves all twenty courses, from /courses/macaron-masterclass to /courses/knife-skills-and-"
                "kitchen-essentials. Inside the component, useParams() reads the matched value out — const "
                "{ slug } = useParams() — like reaching into a labelled mail slot and pulling out whichever "
                "course the URL dropped through; CourseDetailPage then feeds that slug to useCourse to fetch "
                "the one course. When you need to navigate in code rather than from a click — after saving a "
                "form, or a back button — useNavigate() does it, and navigate(-1) simply returns to wherever "
                "the user came from with no hardcoded path.",
                "Finally, an important habit: some state belongs in the URL, not in useState. Filters, search "
                "terms and pagination are the classic cases. CoursesPage keeps its category and search query "
                "in the URL with useSearchParams, so /courses?category=Bakery&q=sourdough is a shareable "
                "ticket — bookmark it, send it to a colleague, press the back button, refresh the page, and the "
                "exact same filtered view returns every time. If that state lived only in component state it "
                "would vanish on refresh and could not be shared. One subtlety the real page handles: it writes "
                "the debounced query to the URL with { replace: true }, so a burst of keystrokes does not stuff "
                "the history with an entry per character and wreck the back button. The rule of thumb is: if a "
                "view should be reproducible from its link alone, its state belongs in the URL.",
            ],
            code="<Route path='courses/:slug' element={<CourseDetailPage />} />\n\n// src/pages/CourseDetailPage.jsx (real code)\nconst { slug } = useParams()\nconst { course, loading, error } = useCourse(slug)",
            bullets=[
                "A layout route renders shared chrome once; <Outlet/> is where children appear, and layouts nest.",
                "A :param matches any value; useParams() reads it, and a pathless route gates a subtree.",
                "useNavigate() moves programmatically; navigate(-1) goes back with no hardcoded path.",
                "Put shareable view state (filters, search) in the URL with useSearchParams, debounced with replace.",
            ],
        ),
        dict(
            heading="Protected routes, and why a client guard is not security",
            paras=[
                "Some pages should only render for a signed-in user — the private dashboard, the profile page. A "
                "protected route wraps such a page and redirects everyone else to the login screen. The subtle "
                "part is timing. When your app first loads, the authentication session resolves asynchronously: "
                "AuthContext holds a JWT from a previous visit in localStorage, but this page load has never had "
                "it checked, so on boot it calls /api/auth/me to have the server verify the signature and hand "
                "back the current user. For that brief moment you do not yet know whether anyone is signed in. "
                "If your guard treats that unknown moment as 'not signed in' and redirects, then a genuinely "
                "signed-in user gets bounced to /login on every single refresh, because the redirect fires "
                "before the verification returns. It is checking a wristband in the dark and ejecting your own "
                "paying guest. The fix, which ProtectedRoute implements, is to guard on the loading state "
                "first: while loading, render a 'Checking your session…' message and redirect nobody; only once "
                "loading is false do you decide between rendering the page and navigating to login.",
                "The most important idea in the whole topic, though, is that a client-side guard is user "
                "experience, not security. Hiding the Dashboard link from signed-out users and redirecting them "
                "away from the route makes the app pleasant and coherent — but it protects nothing, because all "
                "of that code runs on the user's own machine. Anyone can open dev tools, edit the JavaScript, "
                "or ignore the app entirely and call your API directly with curl, stepping straight over the "
                "velvet rope. Real protection lives on the server, in the /api/ functions from Topic 5: "
                "requireAuth(req) rejects any request without a validly signed token, and every query that "
                "reads or writes a user's data carries `and user_id = ${userId}` with the id taken from that "
                "verified token. So even if someone completely bypasses ProtectedRoute and hits "
                "GET /api/enrollments by hand, the server still only ever returns their own rows, and a request "
                "with no valid token gets a 401. Design so that a bypassed client guard exposes nothing the "
                "server would not already allow: the client makes the app nice to use; the API is what makes "
                "it safe.",
            ],
            code="// src/components/ProtectedRoute.jsx (real code)\nconst { user, loading } = useAuth()\nif (loading) return <p>Checking your session…</p>   // FIRST\nif (!user) return <Navigate to='/login' replace\n  state={{ from: location }} />\nreturn <Outlet />\n\n// The REAL guard, server-side: requireAuth(req) + user_id = ${userId}",
            bullets=[
                "A protected route renders only for signed-in users and redirects the rest.",
                "The session loads asynchronously (a /api/auth/me check) — guard on loading before you redirect.",
                "Skip that check and real users get bounced to login on every refresh.",
                "A client guard is UX only; the API's requireAuth plus `user_id = ${userId}` is what protects data.",
            ],
        ),
    ],
}
