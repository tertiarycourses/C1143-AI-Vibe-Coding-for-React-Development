import { useState, useEffect, useRef } from 'react'
import { useSearchParams } from 'react-router-dom'
import SearchBar from '../components/SearchBar'
import CategoryFilter from '../components/CategoryFilter'
import CourseGrid from '../components/CourseGrid'
import CartSummary from '../components/CartSummary'
import { useCourses } from '../hooks/useCourses'
import { useDebounce } from '../hooks/useDebounce'

// The filter state lives in the URL (?category=...&q=...), not in component
// state. That makes a filtered view shareable, bookmarkable and back-button
// friendly, and it survives a refresh.
export default function CoursesPage() {
  const { courses, loading, error } = useCourses()
  const [searchParams, setSearchParams] = useSearchParams()

  const category = searchParams.get('category') ?? 'All'
  const q = searchParams.get('q') ?? ''

  // Local state for the text box so typing feels instant; the debounced value is
  // what we write to the URL, so we don't push a history entry per keystroke.
  const [query, setQuery] = useState(q)
  const debounced = useDebounce(query, 300)

  // A ref holds a mutable value that survives re-renders WITHOUT causing one.
  // Here it holds the real <input> DOM node, which is the only way to focus it:
  // "is focused" is browser state, not something JSX can describe.
  const searchInput = useRef(null)

  // Focus the search box once, when the page mounts. React has attached the DOM
  // node by the time effects run, so `.current` is safe to use here.
  useEffect(() => {
    searchInput.current?.focus()
  }, [])

  useEffect(() => {
    setSearchParams(
      (prev) => {
        const next = new URLSearchParams(prev)
        if (debounced) next.set('q', debounced)
        else next.delete('q')
        return next
      },
      { replace: true },
    )
  }, [debounced, setSearchParams])

  const setCategory = (cat) => {
    setSearchParams((prev) => {
      const next = new URLSearchParams(prev)
      if (cat && cat !== 'All') next.set('category', cat)
      else next.delete('category')
      return next
    })
    // Filtering with a chip should leave the cursor back in the search box.
    searchInput.current?.focus()
  }

  const needle = q.toLowerCase()
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
        <SearchBar value={query} onChange={setQuery} inputRef={searchInput} />
        <CategoryFilter value={category} onChange={setCategory} />
      </div>

      <CartSummary />

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
