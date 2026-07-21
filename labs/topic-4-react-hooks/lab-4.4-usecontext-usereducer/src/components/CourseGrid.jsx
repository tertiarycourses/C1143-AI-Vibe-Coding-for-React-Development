import CourseCard from './CourseCard'

// Compare this to the Lab 4.3 version: no more items / onAdd / onRemove props to
// carry. Each CourseCard now reaches into the shortlist itself via useCart(), so
// the grid only has to know about the courses it lays out. That deletion IS the
// lesson — Context removed the prop drilling.
export default function CourseGrid({ courses }) {
  if (!courses.length) {
    return <p className="muted">No courses match your search.</p>
  }

  return (
    <div className="grid">
      {courses.map((course) => (
        <CourseCard key={course.id} course={course} />
      ))}
    </div>
  )
}
