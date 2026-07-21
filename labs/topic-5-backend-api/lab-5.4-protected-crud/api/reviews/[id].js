import { sql } from '../_lib/db.js'
import { requireAuth, sendError, requireMethod, HttpError } from '../_lib/auth.js'

// DELETE /api/reviews/:id -> delete MY review.
//
// Same rule as enrollments/[id].js: the id in the URL says WHICH row, the JWT
// says WHOSE. Both go into the WHERE clause. Delete somebody else's review by
// guessing its id and you get a 404, because the row never matches.
//
// ReviewList.jsx only draws a Delete button on your own reviews — but that is a
// UX nicety, not a security control. Anyone can send this request with curl, so
// the real check has to be here, in the SQL.
export default async function handler(req, res) {
  try {
    requireMethod(req, 'DELETE')

    const userId = requireAuth(req)
    const { id } = req.query ?? {}

    const rows = await sql`
      delete from reviews
      where id = ${id} and user_id = ${userId}
      returning id::int as id
    `

    if (rows.length === 0) {
      throw new HttpError(404, 'Review not found.')
    }

    return res.status(200).json({ id: rows[0].id, deleted: true })
  } catch (err) {
    return sendError(res, err)
  }
}
