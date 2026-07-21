import { useState } from 'react'
import { courses } from './data/courses'
import Navbar from './components/Navbar'
import Hero from './components/Hero'
import Section from './components/Section'
import SearchBar from './components/SearchBar'
import CategoryFilter from './components/CategoryFilter'
import CourseGrid from './components/CourseGrid'
import Footer from './components/Footer'

// App holds the interactive state for the catalogue: the search text and the chosen
// category. Two small pieces of state; everything the user sees is computed from them.
export default function App() {
  const [query, setQuery] = useState('')
  const [category, setCategory] = useState('All')

  const scrollToCatalogue = () => {
    document.getElementById('catalogue')?.scrollIntoView({ behavior: 'smooth' })
  }

  // DERIVED DATA — not state. `visible` is recomputed from scratch on every render,
  // directly from `courses`, `query` and `category`. It is always in sync because it is
  // never stored. Do NOT copy this into its own useState and sync it with useEffect — that
  // duplicate-source-of-truth pattern is the single most common mistake AI agents make, and
  // it produces stale, flickering lists. If you can calculate it, don't store it.
  const visible = courses.filter((course) => {
    const matchesCategory = category === 'All' || course.category === category
    const matchesQuery = course.title.toLowerCase().includes(query.trim().toLowerCase())
    return matchesCategory && matchesQuery
  })

  return (
    <>
      <Navbar />
      <Hero onBrowse={scrollToCatalogue} />
      <Section id="catalogue" eyebrow="Our programmes" title="Find your course">
        <div className="toolbar">
          <SearchBar value={query} onChange={setQuery} />
          <CategoryFilter value={category} onChange={setCategory} />
        </div>
        <CourseGrid courses={visible} />
      </Section>
      <Footer />
    </>
  )
}
