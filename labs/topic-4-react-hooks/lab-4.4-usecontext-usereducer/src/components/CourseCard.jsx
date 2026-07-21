import { campuses, courseImage } from '../data/courses'
import { useCart } from '../context/CartContext'

// The card now consumes the shortlist directly via useCart() instead of receiving
// props for it. A leaf component reaching into shared state is exactly what
// Context is for — no cart props threaded down from App through CourseGrid.
export default function CourseCard({ course }) {
  const { items, addItem, removeItem } = useCart()
  const { title, category, level, weeks, fee, campus, image } = course
  const isBakery = category === 'Bakery'
  const enrolled = items.some((c) => c.id === course.id)

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
              onClick={() => removeItem(course.id)}
            >
              Remove
            </button>
          ) : (
            <button className="btn btn--sm" onClick={() => addItem(course)}>
              Add to shortlist
            </button>
          )}
        </div>
      </div>
    </article>
  )
}
