import { useEffect, useState } from 'react'
import { courses } from './data/courses'
import Navbar from './components/Navbar'
import Hero from './components/Hero'
import Footer from './components/Footer'
import SearchBar from './components/SearchBar'
import CategoryFilter from './components/CategoryFilter'
import CourseGrid from './components/CourseGrid'
import CartSummary from './components/CartSummary'

const CART_KEY = 'cart'

export default function App() {
  const [query, setQuery] = useState('')
  const [category, setCategory] = useState('All')

  // Lazy initial state: this function runs ONCE, on the first render only, to
  // restore the shortlist from localStorage. Without the arrow wrapper the
  // JSON.parse would run on every single render and be thrown away.
  const [items, setItems] = useState(() => {
    const saved = localStorage.getItem(CART_KEY)
    return saved ? JSON.parse(saved) : []
  })

  // Effect (a): keep the browser tab title in sync with the shortlist count.
  // Re-runs whenever `items` changes, because items is in the dependency array.
  useEffect(() => {
    document.title = items.length
      ? `Cook & Bake (${items.length})`
      : 'Cook & Bake Academy'
  }, [items])

  // Effect (b): persist the shortlist. This is the write side; the lazy initial
  // state above is the read side. Together they survive a page refresh.
  useEffect(() => {
    localStorage.setItem(CART_KEY, JSON.stringify(items))
  }, [items])

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
