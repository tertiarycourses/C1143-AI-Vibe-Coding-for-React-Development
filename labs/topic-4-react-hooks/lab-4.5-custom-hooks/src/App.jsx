import { useEffect, useRef, useState } from 'react'
import { courses } from './data/courses'
import { useCart } from './context/CartContext'
import { useDebounce } from './hooks/useDebounce'
import Navbar from './components/Navbar'
import Hero from './components/Hero'
import Footer from './components/Footer'
import SearchBar from './components/SearchBar'
import CategoryFilter from './components/CategoryFilter'
import CourseGrid from './components/CourseGrid'
import CartSummary from './components/CartSummary'
import RenderCounter from './components/RenderCounter'

export default function App() {
  const [query, setQuery] = useState('')
  const [category, setCategory] = useState('All')

  // `query` updates on every keystroke (so the input stays responsive), but the
  // filter reads `debounced`, which only catches up 300 ms after you stop typing.
  const debounced = useDebounce(query, 300)
  const pending = query !== debounced

  const { count } = useCart()
  const searchInput = useRef(null)
  const coursesRef = useRef(null)

  useEffect(() => {
    document.title = count ? `Cook & Bake (${count})` : 'Cook & Bake Academy'
  }, [count])

  useEffect(() => {
    searchInput.current?.focus()
  }, [])

  const needle = debounced.toLowerCase()
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
    searchInput.current?.focus()
  }

  const scrollToCourses = () => {
    coursesRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }

  return (
    <>
      <Navbar />
      <Hero />

      <p className="narrow" style={{ textAlign: 'center' }}>
        <button className="btn btn--ghost btn--lg" onClick={scrollToCourses}>
          Browse courses ↓
        </button>
      </p>

      <section ref={coursesRef} className="section" id="courses">
        <div className="section__head">
          <p className="eyebrow">Our programmes</p>
          <h2>All courses</h2>
          {/* The input updates instantly; this hint shows while the filter waits. */}
          {pending ? <p className="muted">Searching…</p> : <RenderCounter />}
        </div>

        <div className="toolbar">
          <SearchBar value={query} onChange={setQuery} inputRef={searchInput} />
          <CategoryFilter value={category} onChange={selectCategory} />
        </div>

        <CartSummary />
        <CourseGrid courses={visible} />
      </section>

      <Footer />
    </>
  )
}
