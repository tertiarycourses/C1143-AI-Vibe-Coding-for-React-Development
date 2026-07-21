import { sql } from '../_lib/db.js'
import { sendError, requireMethod, HttpError } from '../_lib/auth.js'

// GET /api/courses/artisan-sourdough-bread-baking -> one course, or 404.
//
// The [slug] in the FILENAME is what makes this a dynamic route: Vercel matches
// /api/courses/anything and hands us the matched segment as req.query.slug.
export default async function handler(req, res) {
  try {
    requireMethod(req, 'GET')

    const { slug } = req.query ?? {}

    // `slug` came from the URL, so a caller can put anything in it — including
    // `x' or '1'='1`. It does not matter: ${slug} is bound as a parameter, so
    // Postgres compares the column against that literal string and finds no row.
    const rows = await sql`
      select
        id::int     as id,
        code, slug, title, category, level,
        fee::float8 as fee,
        weeks, campus, summary, emoji, image, created_at
      from courses
      where slug = ${slug}
    `

    // No row -> a real 404, not a 200 with `null`. The status code IS the API's
    // answer; the frontend renders its "Course not found" page from it.
    if (rows.length === 0) {
      throw new HttpError(404, `No course found at /courses/${slug}.`)
    }

    return res.status(200).json(rows[0])
  } catch (err) {
    return sendError(res, err)
  }
}
