import { Link } from 'react-router-dom'

// Presentational: it renders the list and calls back on actions. The data and
// the mutations live in the parent (via useEnrollments).
export default function EnrollmentList({ enrollments, onUpdateStatus, onRemove }) {
  if (!enrollments.length) {
    return (
      <p className="muted">
        You have not enrolled in any courses yet.{' '}
        <Link to="/courses">Browse the catalogue</Link>.
      </p>
    )
  }

  return (
    <ul className="stack">
      {enrollments.map((e) => (
        <li key={e.id} className="panel row row--between">
          <div>
            <h3>
              {e.courses?.emoji} {e.courses?.title ?? 'Course'}
            </h3>
            <span className="badge">{e.status}</span>
          </div>

          <div className="row">
            {e.status !== 'completed' && (
              <button
                className="btn btn--sm btn--quiet"
                onClick={() => onUpdateStatus(e.id, 'completed')}
              >
                Mark complete
              </button>
            )}
            <button
              className="btn btn--sm btn--quiet"
              onClick={() => onRemove(e.id)}
            >
              Remove
            </button>
          </div>
        </li>
      ))}
    </ul>
  )
}
