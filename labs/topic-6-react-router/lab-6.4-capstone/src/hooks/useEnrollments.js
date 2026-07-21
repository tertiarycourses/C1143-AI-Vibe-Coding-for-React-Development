import { useState, useEffect, useCallback } from 'react'
import { api } from '../lib/api'
import { useAuth } from '../context/AuthContext'

// The dashboard's data layer: read the signed-in student's enrolments (joined to
// their course) and create / update / delete them.
//
// LOOK AT WHAT IS MISSING FROM EVERY CALL BELOW: a user id. We never send one.
// GET /api/enrollments does not take a "whose?" parameter, and the enroll() body
// is just { courseId }. The server reads the user id out of the verified JWT and
// puts it in the SQL itself (`where user_id = ${userId}`).
//
// That is the whole security model in one sentence: the browser says WHAT it
// wants, the server decides WHO is asking. If this hook could pass a user id,
// then so could anyone with curl — and they would pass yours.
export function useEnrollments() {
  const { user } = useAuth()
  const [enrollments, setEnrollments] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  const load = useCallback(async () => {
    // A signed-out visitor has no token, so this request would come back 401.
    // Skipping it is just politeness to the network — the server would refuse
    // anyway. This check is NOT what keeps the data private.
    if (!user) {
      setEnrollments([])
      setLoading(false)
      return
    }
    setLoading(true)
    try {
      const data = await api.get('/enrollments')
      setEnrollments(data)
      setError(null)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }, [user])

  useEffect(() => {
    load()
  }, [load])

  // POST /api/enrollments { courseId } — the course is ours to choose, the user
  // is not. The API returns 409 if we are already enrolled (the DB's
  // `unique (user_id, course_id)` constraint is what guarantees that, so two
  // fast clicks still cannot create two rows).
  async function enroll(courseId, notes = '') {
    try {
      const created = await api.post('/enrollments', { courseId, notes })
      setEnrollments((prev) => [created, ...prev])
      return { data: created }
    } catch (err) {
      // The components expect { error: { message } } and never a throw.
      return { error: { message: err.message } }
    }
  }

  async function updateStatus(id, status) {
    // Optimistic update: change local state first so the click feels instant.
    const previous = enrollments
    setEnrollments((prev) => prev.map((e) => (e.id === id ? { ...e, status } : e)))

    try {
      await api.patch(`/enrollments/${id}`, { status })
      return {}
    } catch (err) {
      setEnrollments(previous) // Server disagreed — roll the UI back.
      return { error: { message: err.message } }
    }
  }

  async function remove(id) {
    const previous = enrollments
    setEnrollments((prev) => prev.filter((e) => e.id !== id))

    // DELETE /api/enrollments/:id. The id in the URL says WHICH row; the token
    // says WHOSE. The server ANDs them together in the WHERE clause, so passing
    // somebody else's id here just gets a 404 — try it in devtools.
    try {
      await api.del(`/enrollments/${id}`)
      return {}
    } catch (err) {
      setEnrollments(previous)
      return { error: { message: err.message } }
    }
  }

  return { enrollments, loading, error, enroll, updateStatus, remove, reload: load }
}
