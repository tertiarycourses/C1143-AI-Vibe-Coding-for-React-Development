import { useState } from 'react'
import { courses } from './data/courses'
import Navbar from './components/Navbar'
import Hero from './components/Hero'
import Footer from './components/Footer'
import SearchBar from './components/SearchBar'
import CategoryFilter from './components/CategoryFilter'
import CourseGrid from './components/CourseGrid'
import CartSummary from './components/CartSummary'

export default function App() {
  // Two independent pieces of UI state, each its own useState call.
  const [query, setQuery] = useState('')
  const [category, setCategory] = useState('All')

  // The shortlist: an array of the course OBJECTS a visitor has picked. It lives
  // HERE, in App — the closest common parent of the cards (which add / remove) and
  // the CartSummary (which displays). That is "lifting state up".
  const [items, setItems] = useState([])

  // Derived data, not state: `visible` is recomputed on every render from
  // `courses`, `query` and `category`. It is always in sync because it is never
  // stored. If you can calculate it, don't put it in useState.
  const needle = query.toLowerCase()
  const visible = courses.filter((c) => {
    const matchesCategory = category === 'All' || c.category === category
    const matchesQuery =
      !needle ||
      c.title.toLowerCase().includes(needle) ||
      c.summary.toLowerCase().includes(needle) ||
      c.code.toLowerCase().includes(needle)
    return matchesCategory && matchesQuery
  })

  function addItem(course) {
    // Immutable update: build a NEW array. items.push(course) would mutate the
    // SAME array (same reference), so React would see no change and skip the
    // re-render. The updater form (prev => …) reads the latest state, so it is
    // safe even if the setter runs twice in a row.
    setItems((prev) =>
      prev.some((c) => c.id === course.id) ? prev : [...prev, course],
    )
  }

  function removeItem(id) {
    setItems((prev) => prev.filter((c) => c.id !== id))
  }

  function clear() {
    setItems([])
  }

  return (
    <>
      <Navbar />
      <Hero />

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

        <CartSummary items={items} onRemove={removeItem} onClear={clear} />

        <CourseGrid
          courses={visible}
          items={items}
          onAdd={addItem}
          onRemove={removeItem}
        />
      </section>

      <Footer />
    </>
  )
}
