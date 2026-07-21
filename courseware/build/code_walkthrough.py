"""Code-walkthrough DATA for the C1143 courseware — real code from each lab,
keyed by lab number. Rendered as code-forward slides in the deck."""

CODE_WALKTHROUGH = {'1.2': [{'title': 'CourseCard.jsx — your first component',
          'file': 'src/components/CourseCard.jsx',
          'code': 'export default function CourseCard({\n'
                  '  title, category, level, fee,\n'
                  '}) {\n'
                  '  return (\n'
                  '    <article className="card">\n'
                  '      <span className="card__tag">{category}</span>\n'
                  '      <h3>{title}</h3>\n'
                  '      <span className="card__lvl">{level}</span>\n'
                  '      <strong>S${fee}</strong>\n'
                  '    </article>\n'
                  '  )\n'
                  '}',
          'points': ['A component is a function whose name is Capitalised and returns JSX markup.',
                     'It destructures its props — title, category, level, fee — from the single argument '
                     'object.',
                     '{title} is a curly-brace window where a live JavaScript value flows into the markup.']},
         {'title': 'App.jsx — passing props in',
          'file': 'src/App.jsx',
          'code': "import CourseCard from './components/CourseCard'\n"
                  '\n'
                  'export default function App() {\n'
                  '  return (\n'
                  '    <div className="container">\n'
                  '      <h1>Cook &amp; Bake Academy</h1>\n'
                  '      <CourseCard\n'
                  '        title="Artisan Sourdough Bread Baking"\n'
                  '        category="Bakery"\n'
                  '        level="Beginner"\n'
                  '        fee={680}\n'
                  '      />\n'
                  '    </div>\n'
                  '  )\n'
                  '}',
          'points': ['Props are passed like HTML attributes: strings in quotes, numbers in braces '
                     '(fee={680}).',
                     'Each <CourseCard .../> renders one card from the exact values you hand it.']}],
 '1.3': [{'title': 'One file, six hand-typed cards',
          'file': 'src/App.jsx',
          'code': 'function CourseGrid() {\n'
                  '  return (\n'
                  '    <section id="courses" className="container">\n'
                  '      <h2>Popular courses</h2>\n'
                  '      <div className="grid">\n'
                  '        <CourseCard title="Artisan Sourdough Bread Baking"\n'
                  '          category="Bakery" level="Beginner" fee={680} />\n'
                  '        <CourseCard title="Macaron Masterclass"\n'
                  '          category="Bakery" level="Intermediate" fee={420} />\n'
                  '        {/* ...four more, all hand-typed... */}\n'
                  '      </div>\n'
                  '    </section>\n'
                  '  )\n'
                  '}',
          'points': ['Every card is the same component pasted again with different literal values.',
                     'Notice the repetition — it is the smell Topic 3 removes with data plus .map().']},
         {'title': 'App composes small components',
          'file': 'src/App.jsx',
          'code': 'export default function App() {\n'
                  '  return (\n'
                  '    <>\n'
                  '      <Navbar />\n'
                  '      <Hero />\n'
                  '      <CourseGrid />\n'
                  '      <Footer />\n'
                  '    </>\n'
                  '  )\n'
                  '}',
          'points': ['A component can render other components, nesting them like HTML tags.',
                     'App reads like a table of contents: Navbar, Hero, CourseGrid, Footer.']}],
 '3.1': [{'title': 'Without React: you patch the DOM by hand',
          'file': '(vanilla JS, for contrast)',
          'code': 'function filterBakery() {\n'
                  '  // Find every card and toggle it, one by one.\n'
                  "  document.querySelectorAll('.card').forEach((card) => {\n"
                  "    const show = card.dataset.category === 'Bakery'\n"
                  "    card.style.display = show ? 'block' : 'none'\n"
                  '  })\n'
                  '  // ...and now keep the count in step, by hand:\n'
                  "  const el = document.getElementById('count')\n"
                  "  el.textContent = '10 courses'\n"
                  '}',
          'points': ['The vanilla-JS way: find nodes and mutate them — you own every step of HOW.',
                     "The truth now lives in a DOM string; reading '10' back out to add to it is your "
                     'problem.',
                     'Every extra feature is another patch you must remember to keep in sync.']},
         {'title': 'With React: you describe the result',
          'file': 'src/pages/CoursesPage.jsx',
          'code': "const [category, setCategory] = useState('All')\n"
                  '\n'
                  'const visible = courses.filter(\n'
                  "  (c) => category === 'All' || c.category === category\n"
                  ')\n'
                  '\n'
                  'return (\n'
                  '  <>\n'
                  '    <p>{visible.length} courses</p>\n'
                  '    <CourseGrid courses={visible} />\n'
                  '  </>\n'
                  ')',
          'points': ['State holds the filter; you only declare WHAT the UI is for the current value.',
                     'setCategory re-renders — React builds a new virtual tree, diffs it, and patches only '
                     'what changed.',
                     'No getElementById, no textContent, no style: the count and the grid can never drift '
                     'apart.']}],
 '3.2': [{'title': 'CourseCard takes one course object',
          'file': 'src/components/CourseCard.jsx',
          'code': '// One prop, one object — the shape of a DB row.\n'
                  'export default function CourseCard({ course }) {\n'
                  '  const { slug, title, category, level, fee } = course\n'
                  "  const isBakery = category === 'Bakery'\n"
                  '  return (\n'
                  '    <Link to={`/courses/${slug}`} className="card">\n'
                  '      <span className="card__tag">\n'
                  "        {isBakery ? '🧁 Bakery' : '🍳 Cooking'}\n"
                  '      </span>\n'
                  '      <h3>{title}</h3>\n'
                  '      <span className="card__price">S${fee}</span>\n'
                  '    </Link>\n'
                  '  )\n'
                  '}',
          'points': ['One `course` prop replaces five — its shape matches the DB row you fetch in Topic 5.',
                     'Destructuring pulls the fields you need out of the object in a single line.',
                     'The whole card is a <Link>, so a click routes to the detail page with no reload.']},
         {'title': 'Section composes with children',
          'file': 'src/components/Section.jsx',
          'code': 'export default function Section({ title, children }) {\n'
                  '  return (\n'
                  '    <section className="section">\n'
                  '      {title && <h2>{title}</h2>}\n'
                  '      {children}\n'
                  '    </section>\n'
                  '  )\n'
                  '}\n'
                  '\n'
                  '// Used as a wrapper around anything:\n'
                  '<Section title="Popular courses">\n'
                  '  <CourseGrid courses={popular} />\n'
                  '</Section>',
          'points': ['Whatever you nest between the tags arrives as the children prop.',
                     'Section wraps CourseGrid without knowing what it is — composition over '
                     'configuration.']}],
 '3.3': [{'title': 'Render a list with .map() and key',
          'file': 'src/components/CourseGrid.jsx',
          'code': 'export default function CourseGrid({ courses }) {\n'
                  '  if (!courses.length) {\n'
                  '    return <p className="muted">No courses match your search.</p>\n'
                  '  }\n'
                  '  return (\n'
                  '    <div className="grid">\n'
                  '      {courses.map((course) => (\n'
                  '        <CourseCard\n'
                  '          key={course.id}\n'
                  '          course={course}\n'
                  '        />\n'
                  '      ))}\n'
                  '    </div>\n'
                  '  )\n'
                  '}',
          'points': ['courses.map() turns an array of data into an array of <CourseCard> elements.',
                     'key={course.id} gives each card a stable identity so React reconciles efficiently.',
                     "Use the data's own id as the key — never the array index.",
                     'An early return handles the empty list first, so the JSX below can assume data.']},
         {'title': 'Conditional rendering & the 0 trap',
          'file': 'src/components/CourseCard.jsx',
          'code': '// Ternary: choose one of two things to render.\n'
                  '<span className="card__tag">\n'
                  "  {isBakery ? '🧁 Bakery' : '🍳 Cooking'}\n"
                  '</span>\n'
                  '\n'
                  "<span>🕒 {weeks} week{weeks > 1 ? 's' : ''}</span>\n"
                  '\n'
                  '{/* Footgun: `seats > 0 &&`, never `seats &&`.\n'
                  '    A bare 0 renders a literal "0" on the card. */}\n'
                  '{seats > 0 && <p>{seats} places left</p>}',
          'points': ['A ternary picks one of two elements: the Bakery tag vs the Cooking tag.',
                     '`{cond && <x/>}` renders x only when cond is true.',
                     "Trap: write `seats > 0 &&`, not `seats &&` — a bare 0 renders a literal '0' on "
                     'screen.']}],
 '3.4': [{'title': 'A controlled input',
          'file': 'src/components/SearchBar.jsx',
          'code': 'export default function SearchBar({ value, onChange }) {\n'
                  '  return (\n'
                  '    <input\n'
                  '      type="search"\n'
                  '      value={value}\n'
                  '      onChange={(e) => onChange(e.target.value)}\n'
                  '      placeholder="Search sourdough, sushi, macaron…"\n'
                  '    />\n'
                  '  )\n'
                  '}',
          'points': ['value comes from state and onChange reports every keystroke up to the parent.',
                     'React state is the single source of truth — the DOM input only displays it.']},
         {'title': 'Derived data, not extra state',
          'file': 'src/pages/CoursesPage.jsx',
          'code': "const category = searchParams.get('category') ?? 'All'\n"
                  'const needle = q.toLowerCase()\n'
                  '\n'
                  '// Derived data — NOT state. Recomputed each render.\n'
                  'const visible = courses.filter((c) => {\n'
                  '  const matchesCat =\n'
                  "    category === 'All' || c.category === category\n"
                  '  const matchesQ =\n'
                  '    !needle ||\n'
                  '    c.title.toLowerCase().includes(needle) ||\n'
                  '    c.code.toLowerCase().includes(needle)\n'
                  '  return matchesCat && matchesQ\n'
                  '})',
          'points': ['`visible` is recomputed from courses, category and the query on every render.',
                     "If you can calculate it, don't store it — duplicating it in state causes stale "
                     'lists.']},
         {'title': 'Passing an argument to a handler',
          'file': 'src/components/CategoryFilter.jsx',
          'code': '{categories.map((cat) => (\n'
                  '  <button\n'
                  '    key={cat.value}\n'
                  '    className={\n'
                  "      cat.value === value ? 'chip is-active' : 'chip'\n"
                  '    }\n'
                  '    onClick={() => onChange(cat.value)}\n'
                  '  >\n'
                  '    {cat.label}\n'
                  '  </button>\n'
                  '))}',
          'points': ['Wrap the call in an arrow: onClick={() => onChange(cat.value)}.',
                     'onClick={onChange(cat.value)} would CALL it during every render — a bug.']}],
 '4.1': [{'title': 'useState & immutable updates',
          'file': 'src/context/CartContext.jsx',
          'code': '// The shortlist lives in context, persisted to storage.\n'
                  "const [items, setItems] = useLocalStorage('cart', [])\n"
                  '\n'
                  'const addItem = (course) =>\n'
                  '  setItems((prev) =>\n'
                  '    // Immutable: build a NEW array, never push().\n'
                  '    prev.some((c) => c.id === course.id)\n'
                  '      ? prev\n'
                  '      : [...prev, course])\n'
                  '\n'
                  'const removeItem = (id) =>\n'
                  '  setItems((prev) => prev.filter((c) => c.id !== id))',
          'points': ['The shortlist lives once, in CartContext — the single owner of that state.',
                     'Build a NEW array with the spread ...prev; never mutate with items.push().',
                     'The updater form (prev => ...) always reads the latest state, so it is safe.']},
         {'title': "A 'dumb' presentational component",
          'file': 'src/components/CourseCard.jsx',
          'code': '// CourseCard holds no cart state. It just renders a\n'
                  '// course and links to it. The Add-to-shortlist button\n'
                  '// lives on the detail page and calls addItem(course)\n'
                  '// from context — the card stays pure.\n'
                  'export default function CourseCard({ course }) {\n'
                  '  const { slug, title, fee } = course\n'
                  '  return (\n'
                  '    <Link to={`/courses/${slug}`} className="card">\n'
                  '      <h3>{title}</h3>\n'
                  '      <span className="card__price">S${fee}</span>\n'
                  '    </Link>\n'
                  '  )\n'
                  '}',
          'points': ['CourseCard holds no state; everything it draws arrives in the single `course` prop.',
                     'State lives in context, read where it is needed — the card is reusable anywhere.']}],
 '4.2': [{'title': 'useEffect with a cleanup',
          'file': 'src/hooks/useDebounce.js',
          'code': 'export function useDebounce(value, delay = 300) {\n'
                  '  const [debounced, setDebounced] = useState(value)\n'
                  '\n'
                  '  useEffect(() => {\n'
                  '    const id = setTimeout(\n'
                  '      () => setDebounced(value), delay)\n'
                  '    // Cleanup cancels the pending timer on every\n'
                  '    // keystroke — without it, a fast typist fires\n'
                  '    // the effect early and the search feels janky.\n'
                  '    return () => clearTimeout(id)\n'
                  '  }, [value, delay])\n'
                  '\n'
                  '  return debounced\n'
                  '}',
          'points': ['setTimeout schedules the update; the returned function is the cleanup.',
                     "Each keystroke's cleanup clears the previous timer, so only the last one fires.",
                     'StrictMode double-invokes this in dev to prove the cleanup is really there.']},
         {'title': 'An effect that syncs with state',
          'file': 'src/context/ThemeContext.jsx',
          'code': "const [theme, setTheme] = useLocalStorage('theme', 'light')\n"
                  '\n'
                  '// The one side effect: mirror the chosen theme onto\n'
                  '// <html data-theme="...">, which index.css keys its\n'
                  '// dark-mode variables off. Re-runs only when theme changes.\n'
                  'useEffect(() => {\n'
                  '  document.documentElement.dataset.theme = theme\n'
                  '}, [theme])\n'
                  '\n'
                  'const toggle = () =>\n'
                  "  setTheme((t) => (t === 'dark' ? 'light' : 'dark'))",
          'points': ['The effect re-runs only when `theme` changes — that is what [theme] declares.',
                     'Touching document is a side effect, so it belongs in an effect, never in render.',
                     'useLocalStorage persists the choice, so the theme survives a refresh.']}],
 '4.3': [{'title': 'ref vs state — the dividing line',
          'file': 'src/pages/CoursesPage.jsx',
          'code': '// STATE: the search text. Changing it MUST redraw the\n'
                  '// results, so it is state.\n'
                  "const [query, setQuery] = useState('')\n"
                  '\n'
                  '// REF: the real <input> DOM node. Focusing it changes\n'
                  '// nothing that is rendered, so it is a ref — bumping\n'
                  '// .current never triggers a re-render.\n'
                  'const searchInput = useRef(null)\n'
                  '\n'
                  '// A timer id would be a ref too: clearing it later\n'
                  '// must not cost the user a re-render.',
          'points': ['The whole decision: should changing it redraw the screen? Yes = state, no = ref.',
                     "'Is focused' is browser state — there is no JSX that can express it, so you need a "
                     'ref.',
                     'A timer id in useState would re-render the component on every tick, for nothing.']},
         {'title': 'useRef for focus & scroll',
          'file': 'src/pages/CoursesPage.jsx  ·  HomePage.jsx',
          'code': '// CoursesPage: focus the search box on mount, and\n'
                  '// again after every category chip click.\n'
                  'const searchInput = useRef(null)\n'
                  'useEffect(() => { searchInput.current?.focus() }, [])\n'
                  '<SearchBar value={query} onChange={setQuery}\n'
                  '           inputRef={searchInput} />\n'
                  '\n'
                  '// HomePage: the hero button scrolls to the grid.\n'
                  'const popularRef = useRef(null)\n'
                  'const scrollToCourses = () =>\n'
                  "  popularRef.current?.scrollIntoView({ behavior: 'smooth' })\n"
                  '<Hero onBrowse={scrollToCourses} />\n'
                  '<section ref={popularRef}>...</section>',
          'points': ['useRef(null) gives a stable box; React fills .current with the DOM node after mount.',
                     'The ref is created in the PARENT and passed down — in React 19 ref is a normal prop.',
                     'Focus and scroll are the classic jobs state cannot do: reach for a ref, sparingly.']}],
 '4.4': [{'title': 'A pure reducer',
          'file': 'src/context/CartContext.jsx',
          'code': '// A reducer is PURE: (state, action) => nextState.\n'
                  'function cartReducer(state, action) {\n'
                  '  switch (action.type) {\n'
                  "    case 'ADD':\n"
                  '      return state.some((c) => c.id === action.course.id)\n'
                  '        ? state\n'
                  '        : [...state, action.course]\n'
                  "    case 'REMOVE':\n"
                  '      return state.filter((c) => c.id !== action.id)\n'
                  "    case 'CLEAR':\n"
                  '      return []\n'
                  '    default:\n'
                  '      return state\n'
                  '  }\n'
                  '}',
          'points': ['A reducer is a pure function: (state, action) => nextState, with no mutation.',
                     'Each case returns a brand-new array, making it trivial to reason about and test.']},
         {'title': 'A context provider',
          'file': 'src/context/CartContext.jsx',
          'code': 'export function CartProvider({ children }) {\n'
                  "  const [items, setItems] = useLocalStorage('cart', [])\n"
                  '\n'
                  '  const value = {\n'
                  '    items,\n'
                  '    addItem: (course) => setItems((p) =>\n'
                  '      p.some((c) => c.id === course.id) ? p : [...p, course]),\n'
                  '    removeItem: (id) => setItems((p) =>\n'
                  '      p.filter((c) => c.id !== id)),\n'
                  '    count: items.length,\n'
                  '  }\n'
                  '\n'
                  '  return (\n'
                  '    <CartContext.Provider value={value}>\n'
                  '      {children}\n'
                  '    </CartContext.Provider>\n'
                  '  )\n'
                  '}',
          'points': ['The provider owns the shortlist and exposes it plus the functions that change it.',
                     'count is DERIVED (items.length) — never stored, so it cannot drift from the array.']},
         {'title': 'Consuming context with a custom hook',
          'file': 'src/context/CartContext.jsx',
          'code': 'export function useCart() {\n'
                  '  const ctx = useContext(CartContext)\n'
                  '  if (!ctx) {\n'
                  "    throw new Error('useCart must be used inside <CartProvider>')\n"
                  '  }\n'
                  '  return ctx\n'
                  '}\n'
                  '\n'
                  '// In Navbar, at any depth, no prop drilling:\n'
                  'const { count } = useCart()\n'
                  '<span className="badge">🧺 {count}</span>',
          'points': ['useCart wraps useContext and throws if used outside a provider — a clear early error.',
                     'Any component reads the shared shortlist with one line, no prop drilling.']}],
 '4.5': [{'title': 'useLocalStorage custom hook',
          'file': 'src/hooks/useLocalStorage.js',
          'code': '// A use* function that calls other hooks.\n'
                  'export function useLocalStorage(key, initialValue) {\n'
                  '  const [value, setValue] = useState(() => {\n'
                  '    try {\n'
                  '      const stored = window.localStorage.getItem(key)\n'
                  '      return stored !== null ? JSON.parse(stored) : initialValue\n'
                  '    } catch {\n'
                  '      return initialValue\n'
                  '    }\n'
                  '  })\n'
                  '  const set = (next) => {\n'
                  '    setValue((prev) => {\n'
                  '      const resolved =\n'
                  "        typeof next === 'function' ? next(prev) : next\n"
                  '      window.localStorage.setItem(key, JSON.stringify(resolved))\n'
                  '      return resolved\n'
                  '    })\n'
                  '  }\n'
                  '  return [value, set]\n'
                  '}',
          'points': ['A custom hook is just a function named use* that calls other hooks.',
                     'It returns [value, set] like useState, but mirrors the value into localStorage.',
                     'Lazy initial state (() => ...) reads storage once, on mount — not every render.']},
         {'title': 'Custom hooks share logic, not state',
          'file': 'src/context/ThemeContext.jsx  ·  CartContext.jsx',
          'code': '// Two callers of the SAME hook, each with its own\n'
                  '// independent key and value — logic is reused, state is not.\n'
                  "const [theme, setTheme] = useLocalStorage('theme', 'light')\n"
                  "const [items, setItems] = useLocalStorage('cart', [])\n"
                  '\n'
                  '// useDebounce is reused the same way, per-component:\n'
                  'const debounced = useDebounce(query, 300)',
          'points': ['Each call to useLocalStorage gets its own state — the hook shares behaviour, not data.',
                     'That is the whole point of a custom hook: package logic once, reuse it everywhere.']}],
 '5.1': [{'title': 'The API route that reads the catalogue',
          'file': 'api/courses/index.js',
          'code': "import { sql } from '../_lib/db.js'\n"
                  '\n'
                  '// GET /api/courses  ·  public, no token required.\n'
                  'export default async function handler(req, res) {\n'
                  '  const { category, q } = req.query ?? {}\n'
                  '  const search = q ? `%${q}%` : null\n'
                  '\n'
                  '  const courses = await sql`\n'
                  '    select id::int as id, code, slug, title, category,\n'
                  '           level, fee::float8 as fee, weeks, campus,\n'
                  '           summary, emoji, image\n'
                  '    from courses\n'
                  '    where (${category ?? null}::text is null\n'
                  '           or category = ${category ?? null})\n'
                  '      and (${search}::text is null\n'
                  '           or title ilike ${search})\n'
                  '    order by id\n'
                  '  `\n'
                  '  return res.status(200).json(courses)\n'
                  '}',
          'points': ["A file in api/ IS a URL: this one serves GET /api/courses, running on Vercel's "
                     'servers.',
                     'Query-string values are attacker-controlled — but they only travel as ${} '
                     'placeholders.',
                     'id::int and fee::float8 cast Postgres strings to real numbers, so === comparisons '
                     'work.']},
         {'title': 'Tagged templates defeat SQL injection',
          'file': 'api/_lib/db.js',
          'code': "import { neon } from '@neondatabase/serverless'\n"
                  '\n'
                  '// DATABASE_URL is read ONLY here — no VITE_ prefix, so\n'
                  '// Vite never bundles it into the browser. The password\n'
                  '// never leaves the server.\n'
                  'export const sql = neon(process.env.DATABASE_URL)\n'
                  '\n'
                  '// sql`...` is a TAGGED TEMPLATE: the query text and the\n'
                  '// value are sent to Postgres SEPARATELY as $1, $2...\n'
                  '//   await sql`... where slug = ${slug}`   // SAFE\n'
                  '// Building the string yourself is the door to injection:\n'
                  "//   await sql(`... where slug = '${slug}'`)  // NEVER",
          'points': ['DATABASE_URL has NO VITE_ prefix, so it stays on the server and never reaches the '
                     'bundle.',
                     "The tagged template sends the SQL and the value separately — the value can't become "
                     'SQL.',
                     "A slug of `x'; drop table users; --` is looked up as an absurd literal and matches "
                     'nothing.']}],
 '5.2': [{'title': "Three tiers: the browser's only door",
          'file': 'src/lib/api.js',
          'code': "// The browser's ONLY way to reach the server.\n"
                  '//   React (this file) --fetch--> /api/* --sql--> Neon\n'
                  '// No connection string, no password, no SQL in here.\n'
                  "const BASE = '/api'\n"
                  '\n'
                  'async function request(method, path, body) {\n'
                  '  const token = getToken()\n'
                  '  const res = await fetch(`${BASE}${path}`, {\n'
                  '    method,\n'
                  '    headers: {\n'
                  "      ...(body ? { 'Content-Type': 'application/json' } : {}),\n"
                  '      ...(token ? { Authorization: `Bearer ${token}` } : {}),\n'
                  '    },\n'
                  '    body: body ? JSON.stringify(body) : undefined,\n'
                  '  })\n'
                  '  // ...check res.ok, parse JSON...\n'
                  '}',
          'points': ['The browser knows one thing: how to call our own /api/* URLs. It never touches '
                     'Postgres.',
                     'The JWT rides along in the Authorization header; the server verifies it before '
                     'trusting it.',
                     'Every rule of security lives on the other side of this fetch, where the user cannot '
                     'edit it.']},
         {'title': 'fetch does not reject on 404',
          'file': 'src/lib/api.js',
          'code': 'const data = res.status === 204\n'
                  '  ? null\n'
                  '  : await res.json().catch(() => null)\n'
                  '\n'
                  '// fetch() does NOT throw on 404 or 500 — only a\n'
                  '// network failure rejects. Without this check, an\n'
                  '// error payload would sail into the UI as if it were\n'
                  '// data and be rendered as a course.\n'
                  'if (!res.ok) {\n'
                  '  const err = new Error(data?.error ?? `Failed (${res.status})`)\n'
                  '  err.status = res.status   // carry it: 404 vs 500\n'
                  '  throw err\n'
                  '}\n'
                  'return data',
          'points': ['fetch resolves a 404 normally — you must check res.ok yourself before reading the '
                     'body.',
                     "Carrying err.status lets a caller tell 'no such course' (404) from 'server broke' "
                     '(500).',
                     'This one wrapper gives every hook the same three-state behaviour for free.']}],
 '5.3': [{'title': 'Signup: hash the password, never store it',
          'file': 'api/auth/signup.js',
          'code': "import bcrypt from 'bcryptjs'\n"
                  '\n'
                  '// NEVER store the password. bcrypt is a slow, salted,\n'
                  '// one-way hash — a stolen table is useless to an attacker.\n'
                  'const passwordHash = await bcrypt.hash(password, 10)\n'
                  '\n'
                  'const rows = await sql`\n'
                  '  insert into users (email, name, password_hash)\n'
                  '  values (${email}, ${name}, ${passwordHash})\n'
                  '  on conflict (email) do nothing\n'
                  '  returning id::int as id, email, name, created_at\n'
                  '`   // ^ password_hash is NOT in RETURNING. It never\n'
                  '    //   leaves this function.\n'
                  'return res.status(201).json({\n'
                  '  token: signToken(rows[0]), user: toClientUser(rows[0]),\n'
                  '})',
          'points': ['bcrypt.hash is one-way and salts each hash, so identical passwords get different '
                     'hashes.',
                     'The RETURNING list omits password_hash — the hash is never sent in any response.',
                     'toClientUser() whitelists the fields the browser may see, so nothing private leaks by '
                     'accident.']},
         {'title': 'requireAuth: trust the signature, not the caller',
          'file': 'api/_lib/auth.js',
          'code': 'export function requireAuth(req) {\n'
                  "  const header = req.headers?.authorization ?? ''\n"
                  "  if (!header.startsWith('Bearer '))\n"
                  "    throw new HttpError(401, 'Missing token.')\n"
                  '\n'
                  "  const token = header.slice('Bearer '.length).trim()\n"
                  '  try {\n'
                  '    // Verifies the signature with JWT_SECRET (server-only).\n'
                  '    // Edit the payload and this throws.\n'
                  '    const payload = jwt.verify(token, JWT_SECRET)\n'
                  '    return Number(payload.sub)   // the user id — verified\n'
                  '  } catch {\n'
                  "    throw new HttpError(401, 'Invalid or expired session.')\n"
                  '  }\n'
                  '}',
          'points': ['The payload is only base64-encoded — the SIGNATURE is what makes the token '
                     'trustworthy.',
                     'jwt.verify throws on a bad signature or an expired token, so `sub` can be trusted.',
                     'This returns an id the caller cannot forge, which every protected route builds its SQL '
                     'on.']},
         {'title': 'AuthContext restores the session on boot',
          'file': 'src/context/AuthContext.jsx',
          'code': 'const [user, setUser] = useState(null)\n'
                  'const [loading, setLoading] = useState(true)\n'
                  '\n'
                  '// We may hold a token from a previous visit, but THIS\n'
                  '// page load has never had it checked. Ask the server.\n'
                  'useEffect(() => {\n'
                  '  async function restore() {\n'
                  '    if (!getToken()) { setLoading(false); return }\n'
                  '    try {\n'
                  "      const { user } = await api.get('/auth/me')\n"
                  '      setUser(user)\n'
                  '    } catch {\n'
                  '      clearToken()          // expired or tampered with\n'
                  '    } finally {\n'
                  '      setLoading(false)     // NOT optional — see below\n'
                  '    }\n'
                  '  }\n'
                  '  restore()\n'
                  '}, [])',
          'points': ['The JWT lives in localStorage, so it survives a refresh — but the server must '
                     're-verify it.',
                     '/api/auth/me verifies the signature and returns fresh user details, or 401s.',
                     '`loading` is not optional: without it ProtectedRoute bounces a signed-in user on every '
                     'refresh.']}],
 '5.4': [{'title': 'Enrol: the id comes from the token',
          'file': 'api/enrollments/index.js',
          'code': '// THE important line. userId is the verified `sub` of\n'
                  '// the JWT — not req.body.userId, not a query param.\n'
                  'const userId = requireAuth(req)\n'
                  '\n'
                  'const { courseId } = readBody(req)\n'
                  '\n'
                  '// The caller chooses the COURSE. The caller does NOT\n'
                  '// choose the USER — we supply ${userId} from the token.\n'
                  'const rows = await sql`\n'
                  '  insert into enrollments (user_id, course_id, status)\n'
                  "  values (${userId}, ${courseId}, 'active')\n"
                  '  on conflict (user_id, course_id) do nothing\n'
                  '  returning id::int as id, course_id::int as course_id\n'
                  '`\n'
                  'if (rows.length === 0)\n'
                  "  throw new HttpError(409, 'Already enrolled.')",
          'points': ['userId comes from requireAuth — a cryptographically verified value, not the request '
                     'body.',
                     "'Enrol me in course 7' is safe; 'enrol anyone I like' is impossible because you can't "
                     'set user_id.',
                     'The unique (user_id, course_id) constraint means two fast clicks still create one row: '
                     'a 409.']},
         {'title': 'Ownership lives in the WHERE clause',
          'file': 'api/enrollments/[id].js',
          'code': '// An id in the URL is a REQUEST, not a PERMISSION.\n'
                  'const userId = requireAuth(req)   // from the JWT\n'
                  'const { id } = req.query ?? {}    // from the address bar\n'
                  '\n'
                  '// Every statement carries BOTH conditions. A row you do\n'
                  '// not own simply does not match, so nothing is deleted.\n'
                  'const rows = await sql`\n'
                  '  delete from enrollments\n'
                  '  where id = ${id} and user_id = ${userId}\n'
                  '  returning id::int as id\n'
                  '`\n'
                  'if (rows.length === 0)\n'
                  "  throw new HttpError(404, 'Enrollment not found.')",
          'points': ['The id says WHICH row; the token says WHOSE. Both go into the WHERE clause.',
                     'Forget `and user_id = ${userId}` and you have an Insecure Direct Object Reference.',
                     'There is no RLS behind this — this WHERE clause IS the access control.']}],
 '6.1': [{'title': 'Declaring a route map',
          'file': 'src/App.jsx',
          'code': "import { Routes, Route, Navigate } from 'react-router-dom'\n"
                  '// App declares a route MAP. The layout route wraps its\n'
                  "// children; the matching URL renders into RootLayout's\n"
                  '// <Outlet/>. `index` is "/" itself.\n'
                  'export default function App() {\n'
                  '  return (\n'
                  '    <Routes>\n'
                  '      <Route path="/" element={<RootLayout />}>\n'
                  '        <Route index element={<HomePage />} />\n'
                  '        <Route path="courses" element={<CoursesPage />} />\n'
                  '        <Route path="courses/:slug"\n'
                  '          element={<CourseDetailPage />} />\n'
                  '        <Route path="about" element={<AboutPage />} />\n'
                  '      </Route>\n'
                  '    </Routes>\n'
                  '  )\n'
                  '}',
          'points': ["App declares routes, not a page; the matching URL renders into the layout's <Outlet/>.",
                     "The layout <Route> wraps children; `index` is the route for '/' itself."]},
         {'title': 'A layout route with <Outlet/>',
          'file': 'src/layouts/RootLayout.jsx',
          'code': "import { Outlet } from 'react-router-dom'\n"
                  "import Navbar from '../components/Navbar'\n"
                  "import Footer from '../components/Footer'\n"
                  '// The app shell. Navbar and Footer render on every\n'
                  '// page; the active route renders at Outlet.\n'
                  'export default function RootLayout() {\n'
                  '  return (\n'
                  '    <>\n'
                  '      <Navbar />\n'
                  "      <main style={{ minHeight: '70vh' }}>\n"
                  '        <Outlet />\n'
                  '      </main>\n'
                  '      <Footer />\n'
                  '    </>\n'
                  '  )\n'
                  '}',
          'points': ['Navbar and Footer render on every page — the shared app shell.',
                     'The active child route renders wherever <Outlet/> sits.']}],
 '6.2': [{'title': 'Fetch one course by its slug',
          'file': 'src/hooks/useCourse.js',
          'code': 'export function useCourse(slug) {\n'
                  '  const [course, setCourse] = useState(null)\n'
                  '  const [loading, setLoading] = useState(true)\n'
                  '  const [error, setError] = useState(null)\n'
                  '\n'
                  '  useEffect(() => {\n'
                  '    async function load() {\n'
                  '      try {\n'
                  '        const data = await api.get(`/courses/${slug}`)\n'
                  '        setCourse(data)\n'
                  '      } catch (err) {\n'
                  "        // A 404 is 'no such course', not a crash:\n"
                  '        if (err.status === 404) setCourse(null)\n'
                  '        else setError(err.message)\n'
                  '      } finally { setLoading(false) }\n'
                  '    }\n'
                  '    load()\n'
                  '  }, [slug])\n'
                  '  return { course, loading, error }\n'
                  '}',
          'points': ['The [slug] dependency refetches whenever the URL segment changes.',
                     "A 404 becomes course:null with NO error — which powers a real 'Course not found' page.",
                     'A 500 sets error — two different failures, two different screens.']},
         {'title': 'useParams reads the URL segment',
          'file': 'src/pages/CourseDetailPage.jsx',
          'code': 'export default function CourseDetailPage() {\n'
                  '  // useParams reads :slug from the URL.\n'
                  '  const { slug } = useParams()\n'
                  '  const navigate = useNavigate()\n'
                  '  const { course, loading, error } = useCourse(slug)\n'
                  '\n'
                  '  if (loading) return <Skeleton />\n'
                  '  if (error) return <p className="error">{error}</p>\n'
                  '  // null course -> no such slug -> render a 404.\n'
                  '  if (!course) return <NotFound slug={slug} />\n'
                  '\n'
                  '  return (\n'
                  '    <article className="detail">\n'
                  '      <h1>{course.emoji} {course.title}</h1>\n'
                  '      <button onClick={() => navigate(-1)}>← Back</button>\n'
                  '    </article>\n'
                  '  )\n'
                  '}',
          'points': ['useParams() reads the :slug segment declared in the route path.',
                     'A null course means the slug matched nothing — render a 404 instead of crashing.',
                     'navigate(-1) goes back to wherever the user came from, with no hardcoded path.']}],
 '6.3': [{'title': 'A route guard that waits for auth',
          'file': 'src/components/ProtectedRoute.jsx',
          'code': 'import { Navigate, useLocation, Outlet }\n'
                  "  from 'react-router-dom'\n"
                  "import { useAuth } from '../context/AuthContext'\n"
                  'export default function ProtectedRoute() {\n'
                  '  const { user, loading } = useAuth()\n'
                  '  const location = useLocation()\n'
                  '  // MOST IMPORTANT LINE: wait for loading. Skip it and\n'
                  '  // a refresh bounces a signed-in user to /login.\n'
                  '  if (loading) return <p>Checking your session…</p>\n'
                  '  if (!user) {\n'
                  '    return <Navigate to="/login" replace\n'
                  '      state={{ from: location }} />\n'
                  '  }\n'
                  '  return <Outlet />\n'
                  '}',
          'points': ['The most important line waits for `loading` — skip it and a refresh bounces a user.',
                     'With no user, <Navigate> redirects to /login, remembering where they wanted to go.',
                     'This is UX, not security — the real check is requireAuth() in every /api/ route.']},
         {'title': 'Nested & auth-gated routes',
          'file': 'src/App.jsx',
          'code': '<Routes>\n'
                  '  <Route path="/" element={<RootLayout />}>\n'
                  '    <Route index element={<HomePage />} />\n'
                  '    <Route path="courses/:slug"\n'
                  '      element={<CourseDetailPage />} />\n'
                  '    <Route path="login" element={<LoginPage />} />\n'
                  '    {/* Pathless route: everything inside is auth-gated. */}\n'
                  '    <Route element={<ProtectedRoute />}>\n'
                  '      <Route path="dashboard" element={<DashboardPage />}>\n'
                  '        <Route index element={\n'
                  '          <Navigate to="my-courses" replace />} />\n'
                  '        <Route path="my-courses" element={<MyCoursesPage />} />\n'
                  '        <Route path="profile" element={<ProfilePage />} />\n'
                  '      </Route>\n'
                  '    </Route>\n'
                  '    <Route path="*" element={<NotFoundPage />} />\n'
                  '  </Route>\n'
                  '</Routes>',
          'points': ["Nesting mirrors the URL; children render into their parent's <Outlet/>.",
                     'A pathless <Route element={<ProtectedRoute/>}> gates everything inside it.',
                     'DashboardPage is itself a layout, with My Courses and Profile in its own Outlet.']}],
 '6.6': [{'title': 'Derived average, never stored',
          'file': 'src/hooks/useReviews.js',
          'code': 'export function useReviews(courseId) {\n'
                  '  const [reviews, setReviews] = useState([])\n'
                  '  // ... load() fetches /api/reviews?courseId=... ...\n'
                  '\n'
                  '  // My own review, if any — switches the form between\n'
                  '  // "write" and "edit".\n'
                  '  const myReview =\n'
                  '    reviews.find((r) => r.user_id === user?.id) ?? null\n'
                  '\n'
                  '  // DERIVED at render — never stored, so it can never\n'
                  '  // drift from the reviews array.\n'
                  '  const count = reviews.length\n'
                  '  const average = count\n'
                  '    ? Math.round(\n'
                  '        reviews.reduce((s, r) => s + r.rating, 0)\n'
                  '        / count * 10) / 10\n'
                  '    : null\n'
                  '  return { reviews, myReview, count, average, submit, remove }\n'
                  '}',
          'points': ['count and average fall straight out of the reviews array at render time.',
                     "Because they're derived, they can never drift from the underlying list.",
                     'myReview compares r.user_id === user.id — the API casts ids to int so 3 === 3, not 3 '
                     "=== '3'."]},
         {'title': 'An UPSERT: write or edit one review',
          'file': 'api/reviews/index.js',
          'code': '// POST /api/reviews — reading is public, writing needs\n'
                  '// a token, so requireAuth() is inside the POST branch.\n'
                  'const userId = requireAuth(req)\n'
                  'const { courseId, rating, body } = readBody(req)\n'
                  '\n'
                  '// One statement handles write AND edit. The table has\n'
                  '// unique (user_id, course_id), so a second review from\n'
                  '// the same user UPDATES their existing row.\n'
                  'const rows = await sql`\n'
                  '  insert into reviews (user_id, course_id, rating, body)\n'
                  '  values (${userId}, ${courseId}, ${rating}, ${body.trim()})\n'
                  '  on conflict (user_id, course_id) do update\n'
                  '    set rating = excluded.rating, body = excluded.body\n'
                  '  returning id::int as id, rating, body, created_at\n'
                  '`',
          'points': ['user_id is ${userId} from the token, so a request can only ever touch your OWN review.',
                     "The UPSERT means the client need not know whether a review already exists — and it's "
                     'race-free.',
                     "rating and body are validated on the server before the query — the form's checks are "
                     'UX only.']},
         {'title': 'StarRating: read-only or interactive',
          'file': 'src/components/StarRating.jsx',
          'code': '// Read-only when given just `value`; interactive when\n'
                  '// also given `onChange`. Interactive stars are real\n'
                  '// <button>s — never divs with onClick.\n'
                  'export default function StarRating({ value, onChange }) {\n'
                  '  const stars = [1, 2, 3, 4, 5]\n'
                  '  if (!onChange) {\n'
                  '    return stars.map((n) => (\n'
                  '      <span key={n}\n'
                  "        className={n <= value ? 'star is-on' : 'star'}>★</span>\n"
                  '    ))\n'
                  '  }\n'
                  '  return stars.map((n) => (\n'
                  '    <button key={n} type="button"\n'
                  '      onClick={() => onChange(n)}>★</button>\n'
                  '  ))\n'
                  '}',
          'points': ['Pass just `value` for a display; add `onChange` to make the stars clickable.',
                     'Interactive stars are real <button>s so they stay keyboard-accessible.']}]}
