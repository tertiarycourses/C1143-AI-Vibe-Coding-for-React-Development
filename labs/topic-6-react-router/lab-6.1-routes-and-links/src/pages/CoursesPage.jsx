import { useState } from 'react'
import SearchBar from '../components/SearchBar'
import CategoryFilter from '../components/CategoryFilter'
import CourseGrid from '../components/CourseGrid'
import { useCourses } from '../hooks/useCourses'

// The search + filter UI from Topic 4, now living on its own /courses page.
// For now the filter state is plain component state — Lab 6.2 moves it into the
// URL (?category=&q=) so a filtered view becomes shareable and bookmarkable.
export default function CoursesPage() {
  const { courses, loading, error } = useCourses()
  const [category, setCategory] = useState('All')
  const [query, setQuery] = useState('')

  const needle = query.toLowerCase()
  const visible = courses.filter((c) => {
    const matchesCat = category === 'All' || c.category === category
    const matchesQ =
      !needle ||
      c.title.toLowerCase().includes(needle) ||
      c.summary.toLowerCase().includes(needle) ||
      c.code.toLowerCase().includes(needle)
    return matchesCat && matchesQ
  })

  return (
    <section className="section" id="courses">
      <div className="section__head">
        <p className="eyebrow">Our programmes</p>
        <h2>All courses</h2>
        <p className="muted">
          {visible.length} course{visible.length === 1 ? '' : 's'} — bakery and
          cooking, beginner to advanced.
        </p>
      </div>

      <div className="toolbar">
        <SearchBar value={query} onChange={setQuery} />
        <CategoryFilter value={category} onChange={setCategory} />
      </div>

      {loading && (
        <div className="grid">
          {[1, 2, 3, 4, 5, 6].map((n) => (
            <div key={n} className="skeleton" />
          ))}
        </div>
      )}
      {error && <p className="error">{error}</p>}
      {!loading && !error && <CourseGrid courses={visible} />}
    </section>
  )
}
