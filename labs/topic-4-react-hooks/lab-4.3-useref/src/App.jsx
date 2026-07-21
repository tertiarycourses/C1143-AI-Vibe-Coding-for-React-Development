import { useEffect, useRef, useState } from 'react'
import { courses } from './data/courses'
import Navbar from './components/Navbar'
import Hero from './components/Hero'
import Footer from './components/Footer'
import SearchBar from './components/SearchBar'
import CategoryFilter from './components/CategoryFilter'
import CourseGrid from './components/CourseGrid'
import CartSummary from './components/CartSummary'
import RenderCounter from './components/RenderCounter'

const CART_KEY = 'cart'

export default function App() {
  const [query, setQuery] = useState('')
  const [category, setCategory] = useState('All')
  const [items, setItems] = useState(() => {
    const saved = localStorage.getItem(CART_KEY)
    return saved ? JSON.parse(saved) : []
  })

  // A ref holds the real <input> DOM node so we can focus it — "is focused" is
  // browser state, not something JSX can describe. useRef(null) is a stable box;
  // React sets .current to the element after it mounts (it is null during render).
  const searchInput = useRef(null)

  // A second ref points at the courses <section> so we can scroll to it.
  const coursesRef = useRef(null)

  useEffect(() => {
    document.title = items.length
      ? `Cook & Bake (${items.length})`
      : 'Cook & Bake Academy'
  }, [items])

  useEffect(() => {
    localStorage.setItem(CART_KEY, JSON.stringify(items))
  }, [items])

  // Focus the search box once, when the page mounts. Effects run AFTER the DOM is
  // committed, so searchInput.current is the real <input> here — never null.
  useEffect(() => {
    searchInput.current?.focus()
  }, [])

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

  const selectCategory = (cat) => {
    setCategory(cat)
    // Filtering with a chip should leave the caret back in the search box.
    searchInput.current?.focus()
  }

  const addItem = (course) =>
    setItems((prev) =>
      prev.some((c) => c.id === course.id) ? prev : [...prev, course],
    )
  const removeItem = (id) => setItems((prev) => prev.filter((c) => c.id !== id))
  const clear = () => setItems([])

  const scrollToCourses = () => {
    // Imperative DOM: reach past React to call a browser method directly.
    coursesRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }

  return (
    <>
      <Navbar />
      <Hero />

      {/* In the finished app this button IS the hero's "Browse courses" button,
          wired via <Hero onBrowse={scrollToCourses} />. There is no router yet,
          so we render it here. */}
      <p className="narrow" style={{ textAlign: 'center' }}>
        <button className="btn btn--ghost btn--lg" onClick={scrollToCourses}>
          Browse courses ↓
        </button>
      </p>

      <section ref={coursesRef} className="section" id="courses">
        <div className="section__head">
          <p className="eyebrow">Our programmes</p>
          <h2>All courses</h2>
          <RenderCounter />
        </div>

        <div className="toolbar">
          <SearchBar
            value={query}
            onChange={setQuery}
            inputRef={searchInput}
          />
          <CategoryFilter value={category} onChange={selectCategory} />
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
