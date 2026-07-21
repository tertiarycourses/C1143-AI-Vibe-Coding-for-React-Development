// The top bar. For now every link is a plain <a> and "Sign in" is a plain button — there
// is no router or auth yet. Topic 6 swaps the <a>s for React Router <NavLink>s, and Topic 4
// wires the theme toggle and cart badge. A simplified ancestor of the real Navbar.
export default function Navbar() {
  return (
    <header className="nav">
      <div className="nav__inner">
        <a href="#top" className="brand">
          <span className="brand__mark">🍞</span>
          <span className="brand__text">
            Cook&nbsp;&amp;&nbsp;Bake<small>Academy</small>
          </span>
        </a>

        <nav className="nav__links">
          <a href="#catalogue" className="nav__link">Courses</a>
          <a href="#about" className="nav__link">About</a>
        </nav>

        <div className="nav__actions">
          <button type="button" className="btn btn--sm">Sign in</button>
        </div>
      </div>
    </header>
  )
}
