import CourseCard from './components/CourseCard'

// One course, written out by hand. In Topic 3 this object moves into
// src/data/courses.js alongside its 19 siblings — the shape stays identical, so
// CourseCard will not notice the difference.
const sourdough = {
  code: 'BAK-101',
  slug: 'artisan-sourdough-bread-baking',
  title: 'Artisan Sourdough Bread Baking',
  category: 'Bakery',
  level: 'Beginner',
  weeks: 4,
  fee: 680,
  campus: 'Bakehouse',
  emoji: '🍞',
  summary:
    'Grow your own starter, master hydration and bake a crackling open crumb loaf.',
}

export default function App() {
  return (
    <section className="section">
      <div className="section__head">
        <p className="eyebrow">Cook &amp; Bake Academy</p>
        <h2>Your very first React component</h2>
        <p className="muted">One course, one card, one prop.</p>
      </div>

      <div className="grid">
        <CourseCard course={sourdough} />
      </div>
    </section>
  )
}
