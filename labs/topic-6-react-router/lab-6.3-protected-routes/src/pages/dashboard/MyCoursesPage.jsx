import EnrollmentList from '../../components/EnrollmentList'
import { useEnrollments } from '../../hooks/useEnrollments'

export default function MyCoursesPage() {
  const { enrollments, loading, error, updateStatus, remove } = useEnrollments()

  if (loading) return <p className="muted">Loading your courses…</p>
  if (error) return <p className="error">{error}</p>

  return (
    <EnrollmentList
      enrollments={enrollments}
      onUpdateStatus={updateStatus}
      onRemove={remove}
    />
  )
}
