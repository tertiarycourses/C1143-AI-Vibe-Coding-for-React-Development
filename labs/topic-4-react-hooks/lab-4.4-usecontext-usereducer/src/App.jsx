import { useEffect, useRef, useState } from 'react'
import { courses } from './data/courses'
import { useCart } from './context/CartContext'
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

  // The shortlist no longer lives in App — it lives in CartContext. App reads only
  // what it needs (the count, for the tab title) and passes NOTHING shortlist-
  // related down to CourseGrid. That is the prop drilling Context just deleted.
  const { count } = useCart()

  const searchInput = useRef(null)
  const coursesRef = useRef(null)

  useEffect(() => {
    document.title = count ? `Cook & Bake (${count})` : 'Cook & Bake Academy'
  }, [count])

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
          <RenderCounter />
        </div>

        <div className="toolbar">
          <SearchBar value={query} onChange={setQuery} inputRef={searchInput} />
          <CategoryFilter value={category} onChange={selectCategory} />
        </div>

        {/* No shortlist props threaded through — the cards read the cart directly. */}
        <CartSummary />
        <CourseGrid courses={visible} />
      </section>

      <Footer />
    </>
  )
}
