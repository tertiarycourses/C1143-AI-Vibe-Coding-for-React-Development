import { sql } from '../_lib/db.js'
import {
  requireAuth,
  sendError,
  readBody,
  requireMethod,
  HttpError,
} from '../_lib/auth.js'

// GET  /api/enrollments            -> MY enrollments, joined to their course
// POST /api/enrollments {courseId} -> enrol ME in a course
//
// Both require a valid token. Both derive the user id from that token.
export default async function handler(req, res) {
  try {
    requireMethod(req, 'GET', 'POST')

    // THE important line in this file. `userId` is the verified `sub` claim of
    // a signed JWT. It is not req.body.userId, and it is not a query param —
    // those are just things the caller typed. This is the only identity we trust.
    const userId = requireAuth(req)

    if (req.method === 'GET') {
      // `where user_id = ${userId}` is what scopes the result to you. There is
      // no hidden per-row database policy behind this API doing it for us: this
      // WHERE clause IS the access control. Forget it and every user sees
      // everyone's data.
      //
      // json_build_object nests the course under a `courses` key, which is the
      // shape EnrollmentList already renders (e.courses.title).
      const enrollments = await sql`
        select
          e.id::int        as id,
          e.course_id::int as course_id,
          e.status,
          e.notes,
          e.created_at,
          json_build_object(
            'id',       c.id::int,
            'code',     c.code,
            'slug',     c.slug,
            'title',    c.title,
            'category', c.category,
            'level',    c.level,
            'fee',      c.fee::float8,
            'weeks',    c.weeks,
            'campus',   c.campus,
            'summary',  c.summary,
            'emoji',    c.emoji,
            'image',    c.image
          ) as courses
        from enrollments e
        join courses c on c.id = e.course_id
        where e.user_id = ${userId}
        order by e.created_at desc
      `
      return res.status(200).json(enrollments)
    }

    // ---- POST: enrol -------------------------------------------------------
    const { courseId, notes = '' } = readBody(req)

    if (!courseId) {
      throw new HttpError(400, 'courseId is required.')
    }

    // The caller chooses the COURSE. The caller does not choose the USER — we
    // supply ${userId} from the token. This is the difference between "enrol me
    // in course 7" and "enrol anyone I like in course 7".
    const rows = await sql`
      insert into enrollments (user_id, course_id, status, notes)
      values (${userId}, ${courseId}, 'active', ${notes})
      on conflict (user_id, course_id) do nothing
      returning id::int as id, course_id::int as course_id, status, notes, created_at
    `

    // Zero rows means the `unique (user_id, course_id)` constraint fired: they
    // are already enrolled. That is a 409, not a crash — and the DB, not the UI,
    // is what guarantees it (two fast clicks cannot create two rows).
    if (rows.length === 0) {
      throw new HttpError(409, 'You are already enrolled in this course.')
    }

    // Send back the same joined shape as GET, so the UI can push it straight
    // into its list without a refetch.
    const [enrollment] = await sql`
      select
        e.id::int        as id,
        e.course_id::int as course_id,
        e.status,
        e.notes,
        e.created_at,
        json_build_object(
          'id',       c.id::int,
          'code',     c.code,
          'slug',     c.slug,
          'title',    c.title,
          'category', c.category,
          'level',    c.level,
          'fee',      c.fee::float8,
          'weeks',    c.weeks,
          'campus',   c.campus,
          'summary',  c.summary,
          'emoji',    c.emoji,
          'image',    c.image
        ) as courses
      from enrollments e
      join courses c on c.id = e.course_id
      where e.id = ${rows[0].id} and e.user_id = ${userId}
    `

    return res.status(201).json(enrollment)
  } catch (err) {
    return sendError(res, err)
  }
}
