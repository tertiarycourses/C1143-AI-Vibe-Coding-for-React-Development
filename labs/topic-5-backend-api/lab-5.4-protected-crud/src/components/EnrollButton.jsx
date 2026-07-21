import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import { useEnrollments } from '../hooks/useEnrollments'

// Enrolling is an *action*, so it navigates imperatively with useNavigate:
// a signed-out visitor is sent to /login; a signed-in student's click writes a row.
export default function EnrollButton({ course }) {
  const { user } = useAuth()
  const navigate = useNavigate()
  const { enrollments, enroll } = useEnrollments()
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState(null)

  const already = enrollments.some((e) => e.course_id === course.id)

  const handleEnroll = async () => {
    if (!user) {
      navigate('/login')
      return
    }
    setBusy(true)
    setError(null)
    // enroll() returns { data } or { error } — it never throws, so there is
    // nothing for a try/catch to catch here.
    const { error } = await enroll(course.id)
    setBusy(false)
    if (error) setError(error.message)
  }

  if (already) {
    return (
      <button className="btn" disabled>
        ✓ Enrolled
      </button>
    )
  }

  return (
    <>
      <button className="btn" onClick={handleEnroll} disabled={busy}>
        {busy ? 'Enrolling…' : user ? 'Enrol now' : 'Sign in to enrol'}
      </button>
      {error && <p className="error">{error}</p>}
    </>
  )
}
