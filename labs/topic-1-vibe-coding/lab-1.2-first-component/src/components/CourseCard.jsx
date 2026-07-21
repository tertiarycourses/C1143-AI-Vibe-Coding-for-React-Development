// A component is just a function that returns JSX.
// Everything this card draws arrives in ONE prop — `course` — an object shaped
// exactly like a row of the Cook & Bake catalogue:
//   { code, slug, title, category, level, weeks, fee, campus, emoji, summary }
// Destructuring it on the first line turns each field into a plain variable.
//
// The card holds no state and fetches nothing: hand it a course object and it
// renders. That is what keeps it reusable in every later topic — Topic 3 feeds
// it from data/courses.js, Topic 5 feeds it from Postgres, Topic 6 wraps it in
// a <Link> — and this markup barely changes.
export default function CourseCard({ course }) {
  const { title, category, level, weeks, fee, campus, emoji, summary } = course
  const isBakery = category === 'Bakery'

  return (
    <article className="card">
      {/* The real app puts a photo here. Until Topic 3 gives us the data file
          (and its Unsplash urls), the course emoji stands in for it. */}
      <div
        className="card__img"
        style={{
          display: 'grid',
          placeItems: 'center',
          fontSize: '3.5rem',
          background: 'var(--brand-soft)',
        }}
      >
        <span className="card__tag">{isBakery ? '🧁 Bakery' : '🍳 Cooking'}</span>
        <span className="card__lvl">{level}</span>
        {emoji}
      </div>

      <div className="card__body">
        <h3>{title}</h3>
        <p className="muted small" style={{ marginBottom: '0.9rem' }}>
          {summary}
        </p>

        <div className="card__meta">
          <span>🕒 {weeks} week{weeks > 1 ? 's' : ''}</span>
          <span>📍 {campus}</span>
        </div>

        <div className="card__foot">
          <span className="card__price">S${fee}</span>
          <span className="card__ask">View &amp; enrol →</span>
        </div>
      </div>
    </article>
  )
}
