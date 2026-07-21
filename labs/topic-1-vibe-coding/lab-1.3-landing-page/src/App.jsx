import CourseCard from './components/CourseCard'

// Everything lives in this one file on purpose. It works, but it is deliberately
// monolithic and repetitive — Topic 3 is where you learn to break it apart
// (3.2 moves Navbar, Hero and CourseCard into their own files, exactly like the
// real cookbake/src/components/) and kill the repetition below with .map() over
// data/courses.js (3.3). For now, notice the smell; don't fix it yet.

function Navbar() {
  return (
    <header className="nav">
      <div className="nav__inner">
        <span className="brand">
          <span className="brand__mark">🍞</span>
          <span className="brand__text">
            Cook &amp; Bake<small>Academy</small>
          </span>
        </span>

        <nav className="nav__links">
          <a href="#courses" className="nav__link">Courses</a>
          <a href="#about" className="nav__link">About</a>
        </nav>

        <div className="nav__actions">
          <button className="btn btn--sm">Sign in</button>
        </div>
      </div>
    </header>
  )
}

function Hero() {
  return (
    <section className="hero">
      <div className="hero__bg" />
      <div className="hero__overlay" />
      <div className="hero__content">
        <p className="eyebrow">Singapore&apos;s hands-on culinary studio</p>
        <h1>
          Master the art of <span>cooking</span> &amp; <span>baking</span>
        </h1>
        <p className="hero__sub">
          From artisan sourdough to French pastry, sushi to street food — learn
          practical, job-ready skills from professional chefs in small classes.
        </p>

        <div className="hero__cta">
          <a href="#courses" className="btn btn--lg">Browse courses</a>
        </div>
      </div>
    </section>
  )
}

function CourseGrid() {
  return (
    <section id="courses" className="section">
      <div className="section__head">
        <p className="eyebrow">Our catalogue</p>
        <h2>Popular courses</h2>
        <p className="muted">Six of our twenty hands-on programmes.</p>
      </div>

      <div className="grid">
        <CourseCard
          course={{
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
          }}
        />
        <CourseCard
          course={{
            code: 'BAK-102',
            slug: 'french-pastry-and-viennoiserie',
            title: 'French Pastry & Viennoiserie',
            category: 'Bakery',
            level: 'Intermediate',
            weeks: 8,
            fee: 1480,
            campus: 'Bakehouse',
            emoji: '🥐',
            summary:
              'Laminated dough, croissants, pain au chocolat and the classic French pastry canon.',
          }}
        />
        <CourseCard
          course={{
            code: 'BAK-104',
            slug: 'macaron-masterclass',
            title: 'Macaron Masterclass',
            category: 'Bakery',
            level: 'Intermediate',
            weeks: 2,
            fee: 420,
            campus: 'Bakehouse',
            emoji: '🍬',
            summary:
              'Perfect feet, smooth shells and ganache fillings — the meringue method demystified.',
          }}
        />
        <CourseCard
          course={{
            code: 'CUL-201',
            slug: 'italian-cuisine-mastery',
            title: 'Italian Cuisine Mastery',
            category: 'Cooking',
            level: 'Intermediate',
            weeks: 6,
            fee: 1180,
            campus: 'Culinary',
            emoji: '🍝',
            summary:
              'Fresh pasta by hand, risotto, ragù and regional classics from Naples to Milan.',
          }}
        />
        <CourseCard
          course={{
            code: 'CUL-203',
            slug: 'japanese-sushi-and-sashimi',
            title: 'Japanese Sushi & Sashimi',
            category: 'Cooking',
            level: 'Intermediate',
            weeks: 4,
            fee: 980,
            campus: 'Culinary',
            emoji: '🍣',
            summary:
              'Shari rice, fish selection, filleting and nigiri technique from a sushi chef.',
          }}
        />
        <CourseCard
          course={{
            code: 'CUL-210',
            slug: 'knife-skills-and-kitchen-essentials',
            title: 'Knife Skills & Kitchen Essentials',
            category: 'Cooking',
            level: 'Beginner',
            weeks: 1,
            fee: 160,
            campus: 'Culinary',
            emoji: '🔪',
            summary:
              'Grip, julienne, brunoise and honing — one week that speeds up every dish after it.',
          }}
        />
      </div>
    </section>
  )
}

function Footer() {
  return (
    <footer className="footer">
      <p>© 2026 Cook &amp; Bake Academy · A demo cooking &amp; bakery training centre.</p>
      <p className="muted">📞 +65 6888 1234 · ✉️ enrol@cookbakeacademy.sg</p>
    </footer>
  )
}

export default function App() {
  return (
    <>
      <Navbar />
      <Hero />
      <CourseGrid />
      <Footer />
    </>
  )
}
