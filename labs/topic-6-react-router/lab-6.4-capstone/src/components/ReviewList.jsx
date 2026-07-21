import StarRating from './StarRating'

// Presentational: renders the reviews and calls back when the owner deletes one.
//
// `currentUserId` decides whose review shows a Delete button — but that is a UX
// nicety, NOT a security control. Hiding a button stops nobody: anyone can call
// DELETE /api/reviews/:id with curl. What actually stops them is the ownership
// check in the SQL (`where id = ${id} and user_id = ${userId}`), where the user
// id comes from their verified token. Never let a hidden button be your defence.
export default function ReviewList({ reviews, currentUserId, onDelete }) {
  if (!reviews.length) {
    return <p className="muted">No reviews yet. Be the first to review this course.</p>
  }

  return (
    <ul className="stack">
      {reviews.map((r) => (
        <li key={r.id} className="panel">
          <div className="row row--between">
            <StarRating value={r.rating} />
            {r.user_id === currentUserId && (
              <button className="btn btn--sm btn--quiet" onClick={() => onDelete(r.id)}>
                Delete
              </button>
            )}
          </div>

          <p>{r.body}</p>

          <p className="muted small">
            {/* user_name comes from the join to users in GET /api/reviews. The
                API selects only the name from that table — never the email, and
                obviously never the password hash. */}
            {r.user_name ?? 'Student'} · {new Date(r.created_at).toLocaleDateString()}
            {r.user_id === currentUserId && ' · your review'}
          </p>
        </li>
      ))}
    </ul>
  )
}
