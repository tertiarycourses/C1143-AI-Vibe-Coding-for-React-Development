import CourseCard from './CourseCard'

// The six hand-written cards are gone. We render one <CourseCard> per course object by
// mapping the array to an array of elements. `key` gives each element a stable identity so
// React can match old elements to new ones between renders (reconciliation). Use the data's
// own id — never the array index (see the README, and KeyBugDemo, for why).
export default function CourseGrid({ courses }) {
  // Early return: handle the empty case first, then the JSX below can assume a list.
  if (courses.length === 0) {
    return (
      <div className="card">
        <p className="muted" style={{ padding: '1.4rem', margin: 0 }}>
          No courses to show yet.
        </p>
      </div>
    )
  }

  return (
    <div className="grid">
      {courses.map((course) => (
        <CourseCard key={course.id} course={course} />
      ))}
    </div>
  )
}
