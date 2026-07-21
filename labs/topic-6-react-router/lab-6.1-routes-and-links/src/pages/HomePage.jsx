import { useRef } from 'react'
import { Link } from 'react-router-dom'
import Hero from '../components/Hero'
import Section from '../components/Section'
import CourseGrid from '../components/CourseGrid'
import { useCourses } from '../hooks/useCourses'
import { campuses } from '../data/courses'

const features = [
  {
    icon: '👨‍🍳',
    title: 'Pro chef instructors',
    text: 'Every class is led by working chefs and pastry experts with industry experience.',
  },
  {
    icon: '🙌',
    title: '100% hands-on',
    text: 'No watching from the back. You cook and bake everything yourself, and take it home.',
  },
  {
    icon: '📜',
    title: 'Recognised certificate',
    text: 'Earn a certificate on completion to kick-start a cafe, home business or new career.',
  },
  {
    icon: '🧑‍🤝‍🧑',
    title: 'Small classes',
    text: 'Capped at 12 students so you get personal guidance and plenty of practice time.',
  },
]

export default function HomePage() {
  const { courses, loading, error } = useCourses()

  // A ref is a box React hands you that survives re-renders and — unlike state —
  // changing it never re-renders anything. Point one at a DOM node and you can
  // do the things JSX cannot describe: scroll it, focus it, measure it.
  //
  // `popularRef.current` is null on the very first render (React has not created
  // the <section> yet) and is set to the real element right after it is painted.
  const popularRef = useRef(null)

  const scrollToCourses = () => {
    popularRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }

  const popular = courses.slice(0, 6)

  return (
    <>
      <Hero onBrowse={scrollToCourses} />

      <section ref={popularRef} className="section" id="courses">
        <div className="section__head">
          <p className="eyebrow">Our programmes</p>
          <h2>Popular courses</h2>
          <p className="muted">
            Bakery &amp; cooking courses for every level, from a one-week workshop
            to an eight-week programme.
          </p>
        </div>

        {loading && (
          <div className="grid">
            {[1, 2, 3, 4, 5, 6].map((n) => (
              <div key={n} className="skeleton" />
            ))}
          </div>
        )}
        {error && <p className="error">{error}</p>}
        {!loading && !error && <CourseGrid courses={popular} />}

        <p className="section__more">
          <Link to="/courses">See all 20 courses →</Link>
        </p>
      </section>

      <Section
        eyebrow="Why Cook & Bake Academy"
        title="Learn by doing, every session"
        alt
      >
        <div className="features">
          {features.map((f) => (
            <article key={f.title} className="feature">
              <div className="feature__icon">{f.icon}</div>
              <h3>{f.title}</h3>
              <p className="muted">{f.text}</p>
            </article>
          ))}
        </div>
      </Section>

      <section className="section" id="campus">
        <div className="campus">
          <div className="campus__media" />
          <div className="campus__text">
            <p className="eyebrow">Our campuses</p>
            <h2>Two studio kitchens in the heart of the city</h2>
            <ul className="campus__list">
              {Object.entries(campuses).map(([key, campus]) => (
                <li key={key}>
                  <strong>
                    {campus.emoji} {campus.name}
                  </strong>
                  <br />
                  {campus.address}
                </li>
              ))}
            </ul>
            <Link to="/about" className="btn">
              About the academy
            </Link>
          </div>
        </div>
      </section>

      <section className="cta" id="contact">
        <h2>Ready to roll up your sleeves?</h2>
        <p>
          Pick a course, reserve your bench, and cook your first dish in week one.
        </p>
        <Link to="/courses" className="btn btn--lg">
          Browse all courses
        </Link>
        <p className="cta__contact">📞 +65 6888 1234 · ✉️ enrol@cookbakeacademy.sg</p>
      </section>
    </>
  )
}
