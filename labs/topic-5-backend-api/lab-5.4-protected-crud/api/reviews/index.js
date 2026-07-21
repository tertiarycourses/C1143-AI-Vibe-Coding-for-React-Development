import { sql } from '../_lib/db.js'
import {
  requireAuth,
  sendError,
  readBody,
  requireMethod,
  HttpError,
} from '../_lib/auth.js'

// GET  /api/reviews?courseId=1                    -> PUBLIC list of reviews
// POST /api/reviews {courseId, rating, body}      -> write/update MY review
//
// Note the asymmetry, and that it is deliberate: reading is public (no token),
// writing needs a token. That is why requireAuth() is called inside the POST
// branch rather than at the top of the handler — calling it at the top would
// lock signed-out visitors out of reading reviews at all.
export default async function handler(req, res) {
  try {
    requireMethod(req, 'GET', 'POST')

    if (req.method === 'GET') {
      const { courseId } = req.query ?? {}

      if (!courseId) {
        throw new HttpError(400, 'courseId is required.')
      }

      // Join to users purely to show WHO wrote each review. Select `u.name` and
      // nothing else from that table — no email, and obviously no password_hash.
      // A join is not permission to expose every column you can now reach.
      const reviews = await sql`
        select
          r.id::int        as id,
          r.user_id::int   as user_id,
          r.course_id::int as course_id,
          r.rating,
          r.body,
          r.created_at,
          u.name           as user_name
        from reviews r
        join users u on u.id = r.user_id
        where r.course_id = ${courseId}
        order by r.created_at desc
      `

      return res.status(200).json(reviews)
    }

    // ---- POST: write or update my one review -------------------------------
    const userId = requireAuth(req)
    const { courseId, rating, body } = readBody(req)

    if (!courseId) {
      throw new HttpError(400, 'courseId is required.')
    }
    if (!Number.isInteger(rating) || rating < 1 || rating > 5) {
      throw new HttpError(400, 'rating must be a whole number from 1 to 5.')
    }
    if (typeof body !== 'string' || body.trim().length === 0 || body.length > 2000) {
      throw new HttpError(400, 'body must be between 1 and 2000 characters.')
    }

    // An UPSERT. The table has `unique (user_id, course_id)`, so if I already
    // reviewed this course the insert collides and `do update` edits MY existing
    // row instead of failing. One statement, one round-trip, and it is race-free:
    // two simultaneous submissions cannot create two reviews.
    //
    // The user_id is ${userId} from the token, so the row this touches is always
    // my own — there is no way to phrase this request so it overwrites someone
    // else's review.
    const rows = await sql`
      insert into reviews (user_id, course_id, rating, body)
      values (${userId}, ${courseId}, ${rating}, ${body.trim()})
      on conflict (user_id, course_id) do update
        set rating     = excluded.rating,
            body       = excluded.body,
            created_at = now()
      returning id::int as id, user_id::int as user_id, course_id::int as course_id,
                rating, body, created_at
    `

    return res.status(201).json(rows[0])
  } catch (err) {
    return sendError(res, err)
  }
}
