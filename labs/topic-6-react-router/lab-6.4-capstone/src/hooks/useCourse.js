import { useState, useEffect } from 'react'
import { api } from '../lib/api'

// Loads ONE course from GET /api/courses/:slug.
//
// The interesting case is "no such course". The API answers 404 — the status
// code IS the answer — and we translate that into `course: null` with NO error,
// which is what makes CourseDetailPage render its proper "Course not found"
// page. A 500, by contrast, is a real error and shows the red message.
//
// Two different failures, two different screens. Collapsing them into one
// `error` state is how you end up showing "Something went wrong" to a user who
// simply mistyped a URL.
export function useCourse(slug) {
  const [course, setCourse] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    let active = true
    setLoading(true)

    async function load() {
      try {
        const data = await api.get(`/courses/${slug}`)
        if (!active) return
        setCourse(data)
        setError(null)
      } catch (err) {
        if (!active) return
        if (err.status === 404) {
          setCourse(null) // a real 404, not a crash
          setError(null)
        } else {
          setError(err.message)
        }
      } finally {
        if (active) setLoading(false)
      }
    }

    load()
    return () => {
      active = false
    }
  }, [slug])

  return { course, loading, error }
}
