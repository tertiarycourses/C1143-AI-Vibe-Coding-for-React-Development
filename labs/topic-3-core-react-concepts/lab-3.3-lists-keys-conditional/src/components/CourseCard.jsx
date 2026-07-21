import { campuses, courseImage } from '../data/courses'

// One course, one card. Everything it draws arrives in a single `course` prop. This lab
// adds conditional rendering: a category tag and an optional "Advanced" badge chosen from
// the data, a price that can say "Free", and a pluralised "weeks".
//
// Still a plain <article className="card"> — Topic 6 turns the whole card into a
// <Link to={`/courses/${slug}`}>.
export default function CourseCard({ course }) {
  const { title, category, level, weeks, fee, campus, image } = course
  const isBakery = category === 'Bakery'
  const isAdvanced = level === 'Advanced'

  return (
    <article className="card">
      <div
        className="card__img"
        style={{ backgroundImage: `url('${courseImage(image)}')` }}
      >
        {/* Ternary: pick one of two labels to render. */}
        <span className="card__tag">{isBakery ? '🧁 Bakery' : '🍳 Cooking'}</span>
        <span className="card__lvl">{level}</span>
      </div>

      <div className="card__body">
        <h3>{title}</h3>

        {/* `&&` — render the badge only for advanced courses, otherwise nothing.
            isAdvanced is a real boolean, so there is no literal-0 footgun here. */}
        {isAdvanced && <span className="badge">🔥 Advanced · book early</span>}

        <div className="card__meta">
          <span>🕒 {weeks} week{weeks > 1 ? 's' : ''}</span>
          <span>📍 {campuses[campus].area}</span>
        </div>

        <div className="card__foot">
          {/* Ternary again: none of the seeded courses are free, but the branch is here
              so a fee of 0 would read "Free" instead of "S$0". */}
          <span className="card__price">{fee === 0 ? 'Free' : `S$${fee}`}</span>
          <span className="card__ask">View &amp; enrol →</span>
        </div>
      </div>
    </article>
  )
}
