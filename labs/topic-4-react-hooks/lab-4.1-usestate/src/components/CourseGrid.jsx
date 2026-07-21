import CourseCard from './CourseCard'

// CourseGrid forwards the shortlist data down to each card. It is a pass-through:
// notice how many props it has to carry just to reach the cards. That "prop
// drilling" is the pain Context will remove in Lab 4.4.
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
