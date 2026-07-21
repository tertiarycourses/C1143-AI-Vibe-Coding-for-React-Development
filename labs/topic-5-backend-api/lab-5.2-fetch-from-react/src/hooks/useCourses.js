import { useState, useEffect } from 'react'
import { api } from '../lib/api'

// Loads the public catalogue from GET /api/courses.
//
// No token is attached and none is needed: the catalogue is what a visitor sees
// before they have an account, and the function behind this URL calls no
// requireAuth(). Reads are public; writes are not.
//
// Compare this with src/data/courses.js, which Topics 1-4 rendered from. The
// components downstream cannot tell the difference — same array, same fields.
// The only new thing is that the data now ARRIVES OVER A NETWORK, and a network
// can be slow (hence `loading`) or fail (hence `error`). Every remote read in a
// real app needs all three states, and forgetting one is what makes UIs feel broken.
export function useCourses() {
  const [courses, setCourses] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    let active = true

    async function load() {
      try {
        // api.get() throws on a network failure AND on any non-2xx response, so
        // a single catch covers both. Raw fetch() does NOT do the second part:
        // it happily resolves a 500, which is how an error payload ends up being
        // rendered as though it were data. Our wrapper checks res.ok for us.
        const data = await api.get('/courses')
        if (!active) return
        setCourses(data)
        setError(null)
      } catch (err) {
        if (active) setError(err.message)
      } finally {
        // Without a `finally`, one failed request leaves the UI stuck on its
        // loading skeleton forever.
        if (active) setLoading(false)
      }
    }

    load()
    // `active` guards against setting state after the component unmounted.
    return () => {
      active = false
    }
  }, [])

  return { courses, loading, error }
}
