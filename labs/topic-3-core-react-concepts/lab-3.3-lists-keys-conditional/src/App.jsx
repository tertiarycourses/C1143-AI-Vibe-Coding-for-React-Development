import { courses } from './data/courses'
import Navbar from './components/Navbar'
import Hero from './components/Hero'
import Section from './components/Section'
import CourseGrid from './components/CourseGrid'
import Footer from './components/Footer'

// App owns the data now and passes it down as a prop (one-way data flow, parent → child).
// CourseGrid no longer hardcodes anything — hand it any array of courses and it renders it.
// This is why designing CourseCard around a single `course` object (Lab 3.2) paid off: the
// map body is a clean one-liner.
export default function App() {
  const scrollToCatalogue = () => {
    document.getElementById('catalogue')?.scrollIntoView({ behavior: 'smooth' })
  }

  return (
    <>
      <Navbar />
      <Hero onBrowse={scrollToCatalogue} />
      <Section
        id="catalogue"
        eyebrow="Our programmes"
        title="All 20 courses"
      >
        <CourseGrid courses={courses} />
      </Section>
      <Footer />
    </>
  )
}
