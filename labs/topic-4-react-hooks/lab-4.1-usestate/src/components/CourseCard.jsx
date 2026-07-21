import { campuses, courseImage } from '../data/courses'

// CourseCard is "dumb": it holds no shortlist state of its own. It receives the
// course, whether it is `enrolled` (on the shortlist), and two callbacks — then
// reports clicks back up. State lives in App.
//
// In Topic 6 this whole card becomes a <Link> to the course page. For now it is a
// plain card with an "Add to shortlist" button.
export default function CourseCard({ course, enrolled, onAdd, onRemove }) {
  const { title, category, level, weeks, fee, campus, image } = course
  const isBakery = category === 'Bakery'

  return (
    <article className="card">
      <div
        className="card__img"
        style={{ backgroundImage: `url('${courseImage(image)}')` }}
      >
        <span className="card__tag">{isBakery ? '🧁 Bakery' : '🍳 Cooking'}</span>
        <span className="card__lvl">{level}</span>
      </div>

      <div className="card__body">
        <h3>{title}</h3>

        <div className="card__meta">
          <span>🕒 {weeks} week{weeks > 1 ? 's' : ''}</span>
          <span>📍 {campuses[campus].area}</span>
        </div>

        <div className="card__foot">
          <span className="card__price">S${fee}</span>
          {enrolled ? (
            <button
              className="btn btn--sm btn--quiet"
              onClick={() => onRemove(course.id)}
            >
              Remove
            </button>
          ) : (
            <button className="btn btn--sm" onClick={() => onAdd(course)}>
              Add to shortlist
            </button>
          )}
        </div>
      </div>
    </article>
  )
}
