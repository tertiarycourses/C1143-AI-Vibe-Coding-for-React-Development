"""
Diagram-slide DATA for the C1143 courseware.

Pure data. One list, DIAGRAM_SLIDES. Each entry pairs a real image file from
<REPO>/reference/images/ with a topic number, a title, a kicker, teaching
bullets and a caption. Only images that actually exist on disk are referenced.

Each entry:
    dict(topic, title, image, kicker, bullets=[...], caption="...")
"""

DIAGRAM_SLIDES = [

    dict(
        topic=1,
        title="A component is a function that returns JSX",
        image="simple-component-1.png",
        kicker="TOPIC 01 · COMPONENTS",
        bullets=[
            "This is the whole shape of a React component: a capitalised function that returns JSX.",
            "It destructures its props ({ name }) straight out of the parameter list, like function arguments.",
            "The {name} in the markup is a curly-brace window where a live JavaScript value flows in.",
            "export default makes the component importable and usable elsewhere as <WelcomeMessage />.",
        ],
        caption="A minimal React component: props in through destructuring, JSX out, exported for reuse.",
    ),

    dict(
        topic=3,
        title="An app is a tree of nested components",
        image="timer-components.png",
        kicker="TOPIC 03 · COMPOSITION",
        bullets=[
            "A React app is a tree: App contains Timer, which contains TimerDisplay and TimerControls.",
            "Each box is one component with one job, composed together to build the whole interface.",
            "Data flows down this tree as props; a parent passes values to the children it renders.",
            "Breaking UI into small nested components is what makes it readable, reusable and testable.",
        ],
        caption="Composition in practice: a parent component nests smaller, single-purpose children.",
    ),

    dict(
        topic=4,
        title="Every component has a lifecycle",
        image="react-lifecycle-1.png",
        kicker="TOPIC 04 · LIFECYCLE",
        bullets=[
            "Every component passes through three phases: it mounts, it updates, and it unmounts.",
            "Mount is the first render; update happens whenever state or props change; unmount is removal.",
            "With function components you tap into all three phases through the useEffect hook.",
            "This cycle is why effects need cleanup — the unmount phase is where you tear things down.",
        ],
        caption="Mount, update, unmount — the three phases useEffect lets you hook into.",
    ),

    dict(
        topic=5,
        title="The structure of a JSON Web Token",
        image="jwt-structure.png",
        kicker="TOPIC 05 · AUTH",
        bullets=[
            "A JWT has three parts: a header, a payload of claims, and a cryptographic signature.",
            "The payload is only base64-encoded, not encrypted — anyone can read it, so never put a secret in it.",
            "The signature is computed with JWT_SECRET, known only to the server, so the token cannot be forged.",
            "Our API's requireAuth() verifies that signature and reads the user id from the 'sub' claim.",
            "That verified id — never a value from the request body — is what every protected route trusts.",
        ],
        caption="A signed JWT carries the user's id in its payload; requireAuth() verifies the signature and reads 'sub'.",
    ),

    dict(
        topic=6,
        title="How a single-page application loads",
        image="SPA.png",
        kicker="TOPIC 06 · SPA",
        bullets=[
            "The browser loads the page and its static assets from the server just once.",
            "The React framework then renders the layout and runs entirely in the browser.",
            "JavaScript fetches data as JSON and drops it into the already-rendered page.",
            "From there the user interacts and the view updates in place, with no full reload.",
        ],
        caption="An SPA loads once, then updates the view in the browser without fresh page loads.",
    ),

    dict(
        topic=6,
        title="Client-side routing maps URLs to components",
        image="client-side-routing.png",
        kicker="TOPIC 06 · ROUTING",
        bullets=[
            "The server sends one index.html that contains the whole React app.",
            "React Router inspects the current URL and decides which component to render.",
            "Each path — /, /about, /posts, /posts/1 — is mapped to its own component.",
            "Components may still call the server for data, but navigation stays in the browser.",
        ],
        caption="React Router matches each URL path to a component, all without leaving the page.",
    ),

    dict(
        topic=6,
        title="Traditional server-side routing, for contrast",
        image="server-side-routing.png",
        kicker="TOPIC 06 · SERVER ROUTING",
        bullets=[
            "In the traditional model, navigating to /about sends a fresh request to the server.",
            "The server renders the HTML for that page and sends the whole document back.",
            "Every navigation is a full round-trip, so any in-page state is lost on the way.",
            "From there the client-side JavaScript takes over and the page becomes interactive.",
            "Contrast this with the SPA model, where the client handles navigation after the first load.",
        ],
        caption="Server-side routing round-trips for every page — the opposite of the SPA model.",
    ),
]

# Additional diagrams selected from reference/images/ for topics that had none.
DIAGRAM_SLIDES += [
    dict(
        topic=1,
        title="Everything on screen is a component",
        image="notion-components.png",
        kicker="TOPIC 01 · COMPONENT THINKING",
        bullets=[
            "Before you write a line of code, look at a real interface and draw boxes around its parts.",
            "Each box is a component: a sidebar, a page header, a row, a button, a comment.",
            "Boxes nest. A page contains a header; the header contains a title and an avatar.",
            "That nesting is exactly the component tree React renders, parent passing props to child.",
            "Naming the boxes first is how you decide what components to build.",
        ],
        caption="A familiar app decomposed into boxes — this is the component tree, before any code exists.",
    ),
    dict(
        topic=2,
        title="Deploying from Git to the cloud",
        image="vercel-1.png",
        kicker="TOPIC 02 · DEPLOYMENT",
        bullets=[
            "You connect the host to your GitHub repository once; after that, a push is a deploy.",
            "The host clones your repo, runs npm run build, and serves the static dist/ folder.",
            "Every branch gets its own preview URL, so you can review a change before it reaches users.",
            "Environment variables are set in the dashboard, not committed — and VITE_ ones are public.",
            "Because they are baked in at build time, changing one requires a redeploy, not a restart.",
        ],
        caption="Git-connected deployment: push to main, the host rebuilds and publishes automatically.",
    ),
    dict(
        topic=4,
        title="The class lifecycle useEffect replaced",
        image="react-lifecycle-2.png",
        kicker="TOPIC 04 · WHY HOOKS EXIST",
        bullets=[
            "This is the OLD class-component API. You will not write any of these methods in this course.",
            "Logic for one feature was scattered across componentDidMount, componentDidUpdate and componentWillUnmount.",
            "Subscribe in one method, update in a second, unsubscribe in a third — easy to forget the third.",
            "One useEffect replaces all three: the body handles mount and update, the returned function handles unmount.",
            "You will still meet this diagram in older codebases and in AI-generated code trained on them.",
        ],
        caption="The class-era lifecycle methods. A single useEffect now covers all three columns.",
    ),
]
