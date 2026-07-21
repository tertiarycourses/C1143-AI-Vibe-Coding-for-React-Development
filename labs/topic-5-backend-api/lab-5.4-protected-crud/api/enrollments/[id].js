import { sql } from '../_lib/db.js'
import {
  requireAuth,
  sendError,
  readBody,
  requireMethod,
  HttpError,
} from '../_lib/auth.js'

// PATCH  /api/enrollments/:id  { status }  -> update MY enrollment
// DELETE /api/enrollments/:id              -> cancel MY enrollment
//
// ===========================================================================
// THE LESSON OF THIS FILE: an id in the URL is a REQUEST, not a PERMISSION.
//
// `id` comes from the address bar. Anyone can change a 4 to a 5 and ask to
// delete enrollment #5, which may well belong to another student. So the id
// alone must never be enough. Every statement below carries TWO conditions:
//
//     where id = ${id} and user_id = ${userId}
//                        ^^^^^^^^^^^^^^^^^^^^^
//                        from the verified JWT — the caller cannot influence it
//
// The ownership check lives in the SQL, not in an `if` in JavaScript. A row you
// do not own simply does not match, so Postgres updates/deletes nothing and we
// report 404. This is called an INSECURE DIRECT OBJECT REFERENCE when you get
// it wrong, and it is one of the most common real-world API vulnerabilities.
// ===========================================================================
export default async function handler(req, res) {
  try {
    requireMethod(req, 'PATCH', 'DELETE')

    const userId = requireAuth(req)
    const { id } = req.query ?? {}

    if (req.method === 'PATCH') {
      const { status } = readBody(req)

      // Whitelist the value. Without this check a caller could set status to
      // anything; the DB's CHECK constraint would reject it, but we would be
      // answering with a 500 instead of a clear 400.
      if (!['active', 'completed', 'cancelled'].includes(status)) {
        throw new HttpError(400, 'status must be active, completed or cancelled.')
      }

      const rows = await sql`
        update enrollments
        set status = ${status}
        where id = ${id} and user_id = ${userId}
        returning id::int as id, course_id::int as course_id, status, notes, created_at
      `

      // Nothing came back: either no such enrollment, or it is not yours. We do
      // not distinguish — "404" tells a prober nothing about what exists.
      if (rows.length === 0) {
        throw new HttpError(404, 'Enrollment not found.')
      }

      return res.status(200).json(rows[0])
    }

    // ---- DELETE: cancel ----------------------------------------------------
    const rows = await sql`
      delete from enrollments
      where id = ${id} and user_id = ${userId}
      returning id::int as id
    `

    if (rows.length === 0) {
      throw new HttpError(404, 'Enrollment not found.')
    }

    return res.status(200).json({ id: rows[0].id, deleted: true })
  } catch (err) {
    return sendError(res, err)
  }
}
