import CourseCard from './CourseCard'

// Unchanged from Lab 4.1/4.2 — it still forwards the shortlist data to each card.
// (The scroll ref lives on the <section> in App, not here, so the grid stays a
// plain pass-through.) Context will delete these props in Lab 4.4.
export default function CourseGrid({ courses, items, onAdd, onRemove }) {
  if (!courses.length) {
    return <p className="muted">No courses match your search.</p>
  }

  return (
    <div className="grid">
      {courses.map((course) => (
        <CourseCard
          key={course.id}
          course={course}
          enrolled={items.some((c) => c.id === course.id)}
          onAdd={onAdd}
          onRemove={onRemove}
        />
      ))}
    </div>
  )
}
