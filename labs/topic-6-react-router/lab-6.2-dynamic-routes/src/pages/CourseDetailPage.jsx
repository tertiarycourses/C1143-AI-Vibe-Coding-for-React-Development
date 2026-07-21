import { useParams, useNavigate, Link } from 'react-router-dom'
import Section from '../components/Section'
import EnrollButton from '../components/EnrollButton'
import { useCourse } from '../hooks/useCourse'
import { useCart } from '../context/CartContext'
import { campuses, courseImage } from '../data/courses'

export default function CourseDetailPage() {
  // :slug in the route path arrives here. The URL is the input to this page.
  const { slug } = useParams()
  const navigate = useNavigate()
  const { course, loading, error } = useCourse(slug)
  const { addItem } = useCart()

  if (loading) {
    return (
      <Section>
        <div className="skeleton skeleton--tall" />
      </Section>
    )
  }

  if (error) {
    return (
      <Section title="Something went wrong">
        <p className="error">{error}</p>
      </Section>
    )
  }

  // The API answered 404, so useCourse handed back course: null (not an error).
  // Render a real "not found" instead of crashing on course.title.
  if (!course) {
    return (
      <Section title="Course not found">
        <p className="muted">
          We couldn’t find a course at <code>/courses/{slug}</code>.
        </p>
        <Link to="/courses">← Back to all courses</Link>
      </Section>
    )
  }

  const campus = campuses[course.campus]

  return (
    <Section>
      {/* -1 goes back to wherever the visitor came from — no hardcoded path. */}
      <button className="btn btn--sm btn--quiet" onClick={() => navigate(-1)}>
        ← Back
      </button>

      <article className="detail">
        <div
          className="detail__img"
          style={{ backgroundImage: `url('${courseImage(course.image)}')` }}
        />

        <div className="detail__body">
          <div className="row">
            <span className="badge">{course.code}</span>
            <span className="badge">
              {course.category === 'Bakery' ? '🧁 Bakery' : '🍳 Cooking'}
            </span>
            <span className="badge">{course.level}</span>
          </div>

          <h1>
            {course.emoji} {course.title}
          </h1>

          <p className="muted">
            🕒 {course.weeks} week{course.weeks > 1 ? 's' : ''} · 📍 {campus.name}
          </p>

          <p>{course.summary}</p>
          <p className="muted small">{campus.address}</p>

          <div className="detail__foot">
            <span className="card__price">S${course.fee}</span>
            <div className="row">
              <EnrollButton course={course} />
              <button className="btn btn--quiet" onClick={() => addItem(course)}>
                Add to shortlist
              </button>
            </div>
          </div>
        </div>
      </article>
    </Section>
  )
}
