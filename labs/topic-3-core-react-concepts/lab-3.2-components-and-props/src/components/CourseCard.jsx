// One prop, one object. Before this refactor CourseCard took eight separate props
// (emoji, title, category, level, weeks, fee, campus, summary). Now it takes a single
// `course` object and destructures the fields it needs. Fewer props to thread through the
// tree, and the shape now matches a database row — in Topic 5 we fetch this exact object
// from a Neon Postgres table and pass it in unchanged.
//
// The card is a plain <article className="card"> for now. In Topic 6 (React Router) the
// whole card becomes a <Link to={`/courses/${slug}`}> so a click navigates on the client
// with no full page reload.
export default function CourseCard({ course }) {
  const { emoji, title, category, level, weeks, fee, summary } = course
  const isBakery = category === 'Bakery'

  return (
    <article className="card">
      <div className="card__body">
        <div className="row row--between">
          <span style={{ fontSize: '2rem' }} aria-hidden="true">{emoji}</span>
          <span className="card__tag">{isBakery ? '🧁 Bakery' : '🍳 Cooking'}</span>
        </div>

        <h3>{title}</h3>
        <p className="muted">{level} · {weeks} week{weeks > 1 ? 's' : ''}</p>
        <p>{summary}</p>

        <div className="card__foot">
          <span className="card__price">S${fee}</span>
          <span className="card__ask">View &amp; enrol →</span>
        </div>
      </div>
    </article>
  )
}
