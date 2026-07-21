import CourseCard from './CourseCard'

// Maps an array of courses to cards. `key={course.id}` gives React a stable
// identity per card, so when the list is filtered it can move the surviving
// cards instead of rebuilding them. Never use the array index as the key.
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
