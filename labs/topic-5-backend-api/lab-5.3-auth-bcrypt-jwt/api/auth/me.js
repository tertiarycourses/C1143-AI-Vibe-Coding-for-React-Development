import { sql } from '../_lib/db.js'
import {
  requireAuth,
  toClientUser,
  sendError,
  requireMethod,
  HttpError,
} from '../_lib/auth.js'

// GET /api/auth/me   (Authorization: Bearer <token>)  -> the current user
//
// This is how the app answers "am I still signed in?" after a refresh. The
// browser keeps the JWT in localStorage, which survives a reload but which the
// SERVER has never seen before — so on boot AuthContext calls this route to have
// the token verified and to get fresh user details back.
//
// We re-read the row from Postgres rather than just trusting the name/email
// baked into the token: the token was signed days ago, and the user may have
// been deleted since. A token for a deleted user must not still work.
export default async function handler(req, res) {
  try {
    requireMethod(req, 'GET')

    // Throws 401 if the header is missing or the signature does not check out.
    const userId = requireAuth(req)

    const rows = await sql`
      select id::int as id, email, name, created_at
      from users
      where id = ${userId}
    `

    if (rows.length === 0) {
      throw new HttpError(401, 'Your account no longer exists.')
    }

    return res.status(200).json({ user: toClientUser(rows[0]) })
  } catch (err) {
    return sendError(res, err)
  }
}
