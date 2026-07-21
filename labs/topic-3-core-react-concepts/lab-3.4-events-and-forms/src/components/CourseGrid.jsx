import CourseCard from './CourseCard'

// Unchanged from Lab 3.3. It renders whatever array it is handed and shows a friendly empty
// state when the array is empty — which now happens when a search or filter matches nothing.
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
