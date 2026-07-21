import { Link } from 'react-router-dom'
import { campuses, courseImage } from '../data/courses'

// One course, one card. Everything it draws arrives in a single `course` prop —
// the component never fetches, never stores state, and is therefore reusable
// anywhere a course object exists.
//
// The whole card is a <Link>: clicking it navigates on the client, with no full
// page reload, because React Router intercepts the click.
export default function CourseCard({ course }) {
  const { slug, title, category, level, weeks, fee, campus, image } = course
  const isBakery = category === 'Bakery'

  return (
    <Link to={`/courses/${slug}`} className="card">
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
          <span className="card__ask">View &amp; enrol →</span>
        </div>
      </div>
    </Link>
  )
}
