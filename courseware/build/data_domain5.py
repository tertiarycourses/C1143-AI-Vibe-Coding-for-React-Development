DOMAIN5 = [{'num': '5.1',
  'topic': 5,
  'title': 'The Three Tiers — Your First API Routes over Neon',
  'objective': 'stand up Neon Postgres, put a serverless API tier in front of it, and prove it cannot be '
               'injected',
  'desc': 'The 20 courses live in a JavaScript array. The learner creates a Neon Postgres project, runs the '
          'real schema, and writes the first serverless routes — GET /api/courses and the dynamic '
          '/api/courses/[slug] — then attacks the slug route with a real injection payload and watches the '
          'tagged template bounce it. The architectural rule is drilled here: the browser NEVER talks to '
          'Postgres.',
  'build': 'A live Neon database (20 courses seeded) behind api/_lib/db.js, api/courses/index.js and '
           'api/courses/[slug].js — tested with curl and a real injection probe',
  'services': 'Neon Postgres, @neondatabase/serverless, Vercel Functions, vercel dev, tagged templates, '
              '.env.local',
  'steps': [('Draw the three tiers before you write a line — this is the whole topic in one diagram',
             'React (browser)  --fetch-->  /api/*  (Vercel serverless)  --sql-->  Neon Postgres\n'
             '     no password              holds DATABASE_URL             the data'),
            ('Create a free Neon project, copy the connection string, and run the real schema against it',
             'psql "$DATABASE_URL" -f neon/schema.sql\n'
             '# users, courses (20 seeded: BAK-1xx bakery, CUL-2xx cooking), enrollments, reviews'),
            ('Put the connection string in .env.local with NO VITE_ prefix — and understand exactly why',
             '# ✅ server-only: Vite never touches it, only process.env in api/ can read it\n'
             'DATABASE_URL=postgresql://USER:PASSWORD@ep-xxx.aws.neon.tech/neondb?sslmode=require\n'
             '\n'
             '# ⛔ VITE_DATABASE_URL=...  would publish your database password — read AND\n'
             '#    write — to every visitor of your site. There is no exception to this.'),
            ('Install the driver and the Vercel CLI, then run the API and the front end together',
             'npm install @neondatabase/serverless\n'
             'npm i -g vercel && vercel dev   # serves /api/* AND the Vite app'),
            ('Write api/_lib/db.js — the ONE place in the codebase that holds a connection to Postgres',
             "import { neon } from '@neondatabase/serverless'\n"
             '\n'
             'if (!process.env.DATABASE_URL) {\n'
             "  throw new Error('DATABASE_URL is not set. See .env.example.')\n"
             '}\n'
             '\n'
             'export const sql = neon(process.env.DATABASE_URL)'),
            ('Prompt the agent for the first route — a Vercel function is a file that default-exports (req, '
             'res)',
             "// Vibe prompt: 'Create api/courses/index.js — a Vercel serverless function.\n"
             '// GET only. Read all courses from Neon with the tagged-template sql from\n'
             '// api/_lib/db.js and return them as JSON. Support optional ?category= and ?q=\n'
             "// filters. Cast id::int and fee::float8. Reject any other HTTP method with 405.'"),
            ('Read what it wrote: a Vercel function is just a default-exported handler, and the FILE PATH is '
             'the URL',
             'export default async function handler(req, res) {\n'
             '  const courses = await sql`select id::int as id, code, title, fee::float8 as fee ... from '
             'courses order by id`\n'
             '  return res.status(200).json(courses)\n'
             '}\n'
             '// api/courses/index.js  ->  GET /api/courses'),
            ('Cast your types. Postgres bigint and numeric arrive in JavaScript as STRINGS, and "1" !== 1 '
             'silently',
             'id::int as id,  fee::float8 as fee   -- skip these and course.id === enrollment.course_id is '
             'always false'),
            ('Hit the API directly with curl — no browser, no React. The API is a product in its own right',
             'curl http://localhost:3000/api/courses | head -c 400\n'
             "curl 'http://localhost:3000/api/courses?category=Bakery'"),
            ('Prove the boundary: build the front end and grep the bundle for the password. Nothing may come '
             'back',
             'npm run build && grep -r "postgresql://" dist/   # must return NOTHING'),
            ('Add the dynamic route. The [slug] in the FILENAME is what makes it dynamic; Vercel hands you '
             'req.query.slug',
             '// api/courses/[slug].js  ->  GET /api/courses/artisan-sourdough-bread-baking\n'
             'const { slug } = req.query ?? {}'),
            ('Query with the tagged template — note there are NO parentheses. sql`...`, not sql("...")',
             'const rows = await sql`\n'
             '  select id::int as id, code, slug, title, category, level,\n'
             '         fee::float8 as fee, weeks, campus, summary, emoji, image\n'
             '  from courses\n'
             '  where slug = ${slug}\n'
             '`'),
            ('Understand WHY that is safe. It looks like string interpolation and is not',
             '// The driver sends the query TEXT and the VALUES to Postgres separately, as a\n'
             '// parameterised query ($1). Postgres parses the SQL FIRST and only then binds\n'
             '// the value. A value can therefore never become SQL. Injection is impossible.'),
            ('PROBE IT. Attack your own API with a classic payload and watch it do nothing at all',
             'curl "http://localhost:3000/api/courses/x\'%20or%20\'1\'=\'1"\n'
             '# -> 404 {"error":"No course found at /courses/x\' or \'1\'=\'1."}\n'
             "# Postgres looked for a course whose slug is literally  x' or '1'='1  — and there isn't one."),
            ('Now write the version that is wrong, and see the difference in ONE line of code',
             '// ⛔ NEVER. This builds a STRING, so the payload becomes part of the SQL:\n'
             "// await sql(`select * from courses where slug = '${slug}'`)\n"
             '//   slug = "x\'; drop table users; --"   ->  you no longer have a users table.'),
            ('Delete the unsafe line. The rule: user input is always a ${} placeholder, never part of the '
             'query string',
             ''),
            ("Return a real 404 when no row matches — the STATUS CODE is the API's answer, not a 200 with "
             'null',
             'if (rows.length === 0) {\n'
             '  throw new HttpError(404, `No course found at /courses/${slug}.`)\n'
             '}'),
            ('Prompt the agent for the shared error plumbing so every route answers the same way',
             "// Vibe prompt: 'In api/_lib/auth.js add an HttpError class (status + message),\n"
             '// a sendError(res, err) that maps HttpError to its status and ANY other error to\n'
             '// a generic 500 (never leak a stack trace or a SQL error naming our columns),\n'
             "// and requireMethod(req, ...allowed) that throws 405.'"),
            ('Audit the whole api/ folder for the one thing that reopens the door',
             'grep -rn "sql(\\`\\|sql.unsafe" api/    # must return NOTHING — every query is a tagged '
             'template')],
  'test': 'curl /api/courses returns all 20 Cook & Bake courses as JSON with numeric ids and fees; '
          '?category=Bakery returns 10; /api/courses/not-a-course returns a real 404; the injection payload '
          "returns a harmless 404 and the users table is still there; and grepping dist/ for 'postgresql://' "
          'returns nothing.'},
 {'num': '5.2',
  'topic': 5,
  'title': 'Fetch the Catalogue From React — Loading, Error and Success',
  'objective': 'consume your own API from React with all three states handled',
  'desc': 'The API works; the app still renders a hardcoded array. The learner writes the src/lib/api.js '
          'fetch wrapper — including the check every AI forgets, response.ok, because fetch does NOT reject '
          'on a 404 — then replaces the array with the useCourses and useCourse hooks and renders loading, '
          'error and success for real.',
  'build': 'src/lib/api.js and src/hooks/useCourses.js + useCourse.js — the catalogue now comes from '
           'Postgres',
  'services': 'fetch, response.ok, HTTP status, useState + useEffect, skeleton and error UI',
  'steps': [("Write the wrapper — the browser's ONLY way to reach the server. Note what is NOT in it: no "
             'SQL, no password',
             "const BASE = '/api'\n"
             '\n'
             'async function request(method, path, body) {\n'
             '  const res = await fetch(`${BASE}${path}`, { method, ... })\n'
             '  ...\n'
             '}'),
            ('THE line AI-generated fetch code always omits: fetch does NOT reject on 404 or 500',
             'if (!res.ok) {\n'
             '  const err = new Error(data?.error ?? `Request failed (${res.status})`)\n'
             '  err.status = res.status   // carry the status so the caller can tell 404 from 500\n'
             '  throw err\n'
             '}\n'
             '// Without this, an error payload {error: "..."} sails into the UI and is rendered as a '
             'course.'),
            ('Prompt for the hook, and name all three states in the prompt so the agent cannot skip one',
             "// Vibe prompt: 'Write src/hooks/useCourses.js. Load GET /api/courses through\n"
             '// src/lib/api.js inside a useEffect. Return { courses, loading, error }. Clear\n'
             '// loading in a finally so a failed request does not leave the skeleton forever.\n'
             "// Guard against setting state after unmount with an `active` flag in the cleanup.'"),
            ('Read the result against the three states — loading, error, success. Miss one and the UI feels '
             'broken',
             'const [courses, setCourses] = useState([])\n'
             'const [loading, setLoading] = useState(true)\n'
             'const [error, setError] = useState(null)'),
            ('Check the finally and the cleanup — the two things a generated hook usually lacks',
             '} finally {\n'
             '  if (active) setLoading(false)   // no finally = a stuck skeleton forever\n'
             '}\n'
             'return () => { active = false }    // no guard = setState on an unmounted component'),
            ('Render all three in CoursesPage and HomePage — skeletons, a red error line, then the grid',
             '{loading && <div className="grid">{[1,2,3,4,5,6].map(n => <div key={n} className="skeleton" '
             '/>)}</div>}\n'
             '{error && <p className="error">{error}</p>}\n'
             '{!loading && !error && <CourseGrid courses={visible} />}'),
            ('Write useCourse(slug) and make it distinguish the two failures — a 404 is NOT a crash',
             'if (err.status === 404) {\n'
             "  setCourse(null)   // -> the 'Course not found' page\n"
             '  setError(null)\n'
             '} else {\n'
             "  setError(err.message)   // -> the red 'Something went wrong'\n"
             '}'),
            ('Delete the import of src/data/courses.js from the pages. The catalogue is now Postgres', ''),
            ('Prove it end to end: change a fee in the Neon table editor and refresh the browser',
             "update courses set fee = 720 where code = 'BAK-101';"),
            ('Test the error branch on purpose — throttle the network, then point BASE at a bad path',
             '// DevTools -> Network -> Slow 3G  (see the skeletons)\n'
             "// const BASE = '/apix'                (see the error line, not a blank page)")],
  'test': 'The catalogue renders from Postgres after a skeleton; editing a fee in Neon changes the page on '
          "refresh; /courses/not-a-course shows 'Course not found' (not a red error); and breaking the API "
          'base URL shows the error message instead of an endless skeleton.'},
 {'num': '5.3',
  'topic': 5,
  'title': 'Accounts — Password Hashing with bcrypt, Sessions with JWT',
  'objective': 'hash passwords with bcrypt, issue and verify JWTs, and restore the session on refresh',
  'desc': 'Students must be able to sign up and sign in. The learner builds api/auth/signup, login and me '
          'with bcrypt hashing and JWT signing, writes requireAuth — the single source of identity for the '
          'whole API — and adds the AuthContext that stores the token, sends it on every request and '
          'restores the session on boot.',
  'build': 'api/auth/signup.js, login.js, me.js, api/_lib/auth.js and src/context/AuthContext.jsx',
  'services': 'bcryptjs, jsonwebtoken, JWT_SECRET, Authorization: Bearer',
  'steps': [('Add the second server-side secret — again, NO VITE_ prefix. Anyone holding it can mint a token '
             'for any user',
             'JWT_SECRET=$(node -e "console.log(require(\'crypto\').randomBytes(32).toString(\'hex\'))")\n'
             'npm install bcryptjs jsonwebtoken'),
            ('NEVER store the password. bcrypt is a deliberately slow, salted, one-way hash',
             'const passwordHash = await bcrypt.hash(password, 10)   // ~100ms by design: brute force is '
             'expensive\n'
             '// bcrypt salts every hash, so two users with the same password get different hashes.'),
            ('Insert the user and look hard at the RETURNING list — password_hash is NOT in it, and never '
             'will be',
             'const rows = await sql`\n'
             '  insert into users (email, name, password_hash)\n'
             '  values (${email.trim().toLowerCase()}, ${name}, ${passwordHash})\n'
             '  on conflict (email) do nothing\n'
             '  returning id::int as id, email, name, created_at\n'
             '`\n'
             '// zero rows = the email is taken -> 409. The hash never leaves this function.'),
            ('Log in with bcrypt.compare — never re-hash and compare with ===, and give ONE message for both '
             'failures',
             'const ok = user ? await bcrypt.compare(password, user.password_hash) : false\n'
             "if (!ok) throw new HttpError(401, 'Invalid email or password.')\n"
             "// Separate messages for 'no such email' and 'wrong password' hand an attacker a\n"
             '// free tool for discovering which emails have accounts.'),
            ('Sign a JWT. The payload is base64, NOT encrypted — anyone can read it, so put no secret in it',
             'export function signToken(user) {\n'
             '  return jwt.sign({ sub: String(user.id), email: user.email, name: user.name },\n'
             "                  JWT_SECRET, { expiresIn: '7d' })\n"
             '}\n'
             '// What makes it trustworthy is the SIGNATURE. Edit one byte of the payload and\n'
             '// verify() throws — which is why we may trust `sub` and must not trust req.body.'),
            ('Write requireAuth — the single source of identity for the whole API',
             'export function requireAuth(req) {\n'
             "  const header = req.headers?.authorization ?? ''\n"
             "  if (!header.startsWith('Bearer ')) throw new HttpError(401, 'Missing Authorization "
             "header.')\n"
             '  const payload = jwt.verify(header.slice(7).trim(), JWT_SECRET)   // throws if tampered or '
             'expired\n'
             "  return Number(payload.sub)   // the user's id — VERIFIED, not claimed\n"
             '}'),
            ('Build AuthContext on top of it: store the token, send it on every request, verify it on boot '
             'with /api/auth/me',
             '// src/lib/api.js\n'
             '...(token ? { Authorization: `Bearer ${token}` } : {}),\n'
             '\n'
             '// src/context/AuthContext.jsx — on boot, ask the SERVER who we are\n'
             "const { user } = await api.get('/auth/me')   // 401 -> clearToken()"),
            ('Tamper with the token in devtools (change one character) and refresh. The signature no longer '
             'matches',
             "# localStorage['cookbake.token'] -> edit a char -> refresh -> 401 -> signed out.\n"
             '# The browser cannot lie about who it is.')],
  'test': 'You can sign up, sign in, refresh and stay signed in; password_hash appears in NO API response; '
          'and editing the JWT in localStorage signs you straight out.'},
 {'num': '5.4',
  'topic': 5,
  'title': 'Protected CRUD — Enrolments Scoped to the Signed-in User',
  'objective': 'let only the owner create, read and delete their own rows',
  'desc': 'With accounts in place, students can finally enrol. The learner builds the enrolments API — where '
          'the security rule of the whole course lands: the user id comes from the VERIFIED TOKEN, never '
          'from the request body, and ownership is enforced in the WHERE clause, not in an if statement — '
          "then attacks the API by deleting another student's enrolment and watches it return 404.",
  'build': "api/enrollments/index.js and api/enrollments/[id].js, the enrol button, the 'My learning' list "
           'and the route guard',
  'services': 'Authorization: Bearer, insecure direct object references, ownership in SQL',
  'steps': [('THE RULE. In POST /api/enrollments the caller chooses the COURSE. The caller does NOT choose '
             'the USER',
             'const userId = requireAuth(req)          // from the token\n'
             'const { courseId } = readBody(req)       // from the caller\n'
             '\n'
             'await sql`insert into enrollments (user_id, course_id, status)\n'
             "          values (${userId}, ${courseId}, 'active')\n"
             '          on conflict (user_id, course_id) do nothing\n'
             '          returning id::int as id`\n'
             '// If this trusted req.body.userId, anyone could enrol anyone. And they would.'),
            ('Enforce OWNERSHIP in the SQL, not in an if. The id in the URL is a REQUEST, not a PERMISSION',
             '// api/enrollments/[id].js\n'
             'await sql`delete from enrollments\n'
             '          where id = ${id} and user_id = ${userId}\n'
             '          returning id::int as id`\n'
             '//                    ^^^^^^^^^^^^^^^^^^^^ from the verified JWT\n'
             '// A row you do not own simply does not match -> 0 rows -> 404. Get this wrong and\n'
             '// you have shipped an Insecure Direct Object Reference, the classic API hole.'),
            ('Scope every read the same way — this WHERE clause IS the access control. There is no RLS '
             'behind it',
             'select ... from enrollments e join courses c on c.id = e.course_id\n'
             'where e.user_id = ${userId}\n'
             'order by e.created_at desc'),
            ("Wire the front end: the enrol button posts to /api/enrollments and 'My learning' lists only "
             'your rows',
             "await api.post('/enrollments', { courseId: course.id })"),
            ("ATTACK YOUR OWN API. Sign in as student A, then try to delete student B's enrolment by "
             'guessing the id',
             'curl -X DELETE http://localhost:3000/api/enrollments/1 \\\n'
             '  -H "Authorization: Bearer <STUDENT-A-TOKEN>"\n'
             '# -> 404 Enrollment not found.  The row exists — it is just not yours.')],
  'test': "Enrolling writes a row you can see in Neon; 'My learning' shows only your enrolments; and "
          "deleting another student's enrolment by id returns 404 — the row exists, it is just not yours."}]
