import { sql } from '../_lib/db.js'
import { sendError, requireMethod } from '../_lib/auth.js'

// GET /api/courses            -> all 20 courses
// GET /api/courses?category=Bakery
// GET /api/courses?q=sourdough
//
// Public: no token required. The catalogue is what a visitor sees before they
// have an account, so there is no requireAuth() call in this file.
export default async function handler(req, res) {
  try {
    requireMethod(req, 'GET')

    // Query-string values are attacker-controlled. They are ALSO harmless here,
    // because they only ever travel as ${} placeholders in a tagged template —
    // Postgres binds them as values, never parses them as SQL.
    const { category, q } = req.query ?? {}

    // Rather than glue a WHERE clause together with string concatenation (the
    // classic way to reintroduce SQL injection), we write one query whose
    // filters switch themselves off when the parameter is absent:
    //
    //   ${category ?? null} is null  ->  true for every row, so no filtering.
    //
    // Postgres plans this fine, and there is exactly one query to read.
    const search = q ? `%${q}%` : null

    const courses = await sql`
      select
        id::int     as id,
        code, slug, title, category, level,
        fee::float8 as fee,
        weeks, campus, summary, emoji, image, created_at
      from courses
      where (${category ?? null}::text is null or category = ${category ?? null})
        and (
          ${search}::text is null
          or title   ilike ${search}
          or summary ilike ${search}
          or code    ilike ${search}
        )
      order by id
    `

    return res.status(200).json(courses)
  } catch (err) {
    return sendError(res, err)
  }
}
