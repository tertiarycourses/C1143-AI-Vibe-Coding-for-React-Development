import { neon } from '@neondatabase/serverless'

// ===========================================================================
// The ONE place that holds a connection to Postgres.
//
//     React (browser)  --fetch-->  /api/* (this code)  --sql-->  Neon Postgres
//
// This file runs on Vercel's servers, never in the browser. DATABASE_URL is a
// plain server environment variable — it has NO `VITE_` prefix, so Vite will
// not compile it into the JS bundle. That is the whole point of the three-tier
// design: the database password never leaves the server.
// ===========================================================================
if (!process.env.DATABASE_URL) {
  throw new Error(
    'DATABASE_URL is not set. Copy .env.example to .env.local (local) or add it ' +
      'in Vercel -> Project -> Settings -> Environment Variables (deployed).',
  )
}

// `sql` is a TAGGED TEMPLATE function. You call it like sql`select ...`, not
// sql("select ..."). That distinction is the security story:
//
//     const rows = await sql`select * from courses where slug = ${slug}`
//
// looks like string interpolation but is NOT. The driver sends the query text
// and the values to Postgres SEPARATELY, as a parameterised query ($1, $2, ...).
// Postgres parses the SQL first and only then binds the value, so a slug of
// `x'; drop table users; --` is looked up as a literal (absurd) slug and finds
// nothing. It can never be executed as SQL. SQL injection is impossible here.
//
// The one thing that WOULD reintroduce it is building the string yourself:
//     await sql(`select * from courses where slug = '${slug}'`)   // NEVER DO THIS
//
// Every query in api/ is a tagged template. There is no string-built SQL and no
// sql.unsafe() anywhere in this codebase — deliberately, so there is no door to
// walk user input through.
export const sql = neon(process.env.DATABASE_URL)

// ---------------------------------------------------------------------------
// A note on Postgres types, because it bites everyone once.
//
// `bigint` (our ids) and `numeric` (our fee) arrive in JavaScript as STRINGS —
// a bigint can exceed Number.MAX_SAFE_INTEGER, so the driver refuses to guess.
// Our ids are small and our fees are dollars, so every query below casts
// explicitly — `id::int`, `fee::float8` — and the JSON the browser receives
// holds real numbers. Skip the cast and `course.id === enrollment.course_id`
// compares 1 with "1" and is silently false. That bug is very annoying to find.
// ---------------------------------------------------------------------------
