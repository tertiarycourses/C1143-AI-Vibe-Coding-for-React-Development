import Section from '../components/Section'
import Chefs from '../components/Chefs'
import { campuses } from '../data/courses'

export default function AboutPage() {
  return (
    <>
      <Section
        id="about"
        eyebrow="About us"
        title="Cook & Bake Academy"
      >
        <p className="prose">
          Cook &amp; Bake Academy is a hands-on cooking and bakery training centre
          in Singapore. Every class is capped at twelve students, led by a working
          chef, and run in a real production kitchen — you cook and bake everything
          yourself, and you take it home. Twenty courses run across two campuses,
          from a one-week knife-skills workshop to an eight-week French pastry
          programme.
        </p>
      </Section>

      <Section eyebrow="Our chefs" title="Meet your instructors" alt>
        <Chefs />
      </Section>

      <Section eyebrow="Find us" title="Our campuses">
        <div className="features">
          {Object.entries(campuses).map(([key, campus]) => (
            <article key={key} className="feature">
              <div className="feature__icon">{campus.emoji}</div>
              <h3>{campus.name}</h3>
              <p className="muted">{campus.address}</p>
            </article>
          ))}
        </div>
      </Section>
    </>
  )
}
