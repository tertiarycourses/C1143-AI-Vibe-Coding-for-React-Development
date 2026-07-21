import { useState, useEffect, useCallback } from 'react'
import { api } from '../lib/api'
import { useAuth } from '../context/AuthContext'

// The data layer for course reviews.
//
// Reviews are asymmetric, and that is the lesson: ANYONE may read them (the GET
// sends no token, exactly like the catalogue), but only a signed-in student may
// write one, and only ever their own. As in useEnrollments, we never send a user
// id — the server takes it from the JWT.
export function useReviews(courseId) {
  const { user } = useAuth()
  const [reviews, setReviews] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  const load = useCallback(async () => {
    // CourseDetailPage calls useReviews(course?.id) — which is undefined on the
    // first render, before the course has loaded. Bail out until we have an id.
    if (!courseId) return
    setLoading(true)
    try {
      const data = await api.get(`/reviews?courseId=${courseId}`)
      setReviews(data)
      setError(null)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }, [courseId])

  useEffect(() => {
    load()
  }, [load])

  // The signed-in user's own review, if any — used to switch the form between
  // "write" and "edit". (This works because the API casts ids to int, so we are
  // comparing 3 === 3 and not 3 === "3". Postgres bigints arrive as strings by
  // default, and that mismatch silently breaks exactly this kind of check.)
  const myReview = reviews.find((r) => r.user_id === user?.id) ?? null

  // One POST handles both "write" and "edit". The server does an UPSERT
  // (`on conflict (user_id, course_id) do update`), so we do not have to know
  // whether a review already exists, and there is no race where two submissions
  // create two rows.
  async function submit({ rating, body }) {
    try {
      await api.post('/reviews', { courseId, rating, body })
      await load() // refetch so the list and the average stay correct
      return {}
    } catch (err) {
      return { error: { message: err.message } }
    }
  }

  async function remove(id) {
    try {
      await api.del(`/reviews/${id}`)
      setReviews((prev) => prev.filter((r) => r.id !== id))
      return {}
    } catch (err) {
      return { error: { message: err.message } }
    }
  }

  // Derived at render — never stored. The average and count fall straight out
  // of the reviews array, so they cannot drift from it.
  const count = reviews.length
  const average = count
    ? Math.round((reviews.reduce((sum, r) => sum + r.rating, 0) / count) * 10) / 10
    : null

  return { reviews, myReview, count, average, loading, error, submit, remove }
}
