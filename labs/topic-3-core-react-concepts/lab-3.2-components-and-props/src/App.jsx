import Navbar from './components/Navbar'
import Hero from './components/Hero'
import Section from './components/Section'
import CourseGrid from './components/CourseGrid'
import Footer from './components/Footer'

// App is now a composition of small components instead of one long file.
// It reads like a table of contents for the page.
export default function App() {
  // A function prop for Hero. It scrolls to the catalogue section by its id. In the real
  // app Topic 4 replaces this getElementById call with a useRef; here it just shows that a
  // parent can hand behaviour DOWN to a child as a prop.
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
        title="Course catalogue"
      >
        <CourseGrid />
      </Section>
      <Footer />
    </>
  )
}
