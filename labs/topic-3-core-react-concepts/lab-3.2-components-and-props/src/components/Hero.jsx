// A pure presentational component: everything it renders comes from props, and it holds
// no state. `onBrowse` is a FUNCTION prop — the parent decides what "Browse courses"
// actually does (here: scroll to the catalogue). Passing a function down as a prop is the
// "events up" half of one-way data flow, which Lab 3.4 uses everywhere. A simplified
// ancestor of the real Hero.
export default function Hero({ onBrowse }) {
  const stats = [
    { value: '20+', label: 'Courses' },
    { value: '12', label: 'Max class size' },
    { value: '2', label: 'Campuses' },
    { value: '4.9★', label: 'Student rating' },
  ]

  return (
    <section className="hero" id="top">
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
          <button type="button" className="btn btn--lg" onClick={onBrowse}>
            Browse courses
          </button>
        </div>

        <div className="hero__stats">
          {stats.map((stat) => (
            <div key={stat.label}>
              <strong>{stat.value}</strong>
              <span>{stat.label}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
