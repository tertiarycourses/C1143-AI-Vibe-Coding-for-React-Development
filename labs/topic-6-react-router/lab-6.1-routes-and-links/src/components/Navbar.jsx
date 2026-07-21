import { NavLink, Link } from 'react-router-dom'
import { useTheme } from '../context/ThemeContext'

// NavLink hands its className a render function with an { isActive } flag, so the
// current tab can style itself without the component tracking the URL by hand.
// The shortlist badge, the Dashboard link and Sign in / Sign out arrive in
// Lab 6.3 — for now the navbar is just the brand, two tabs and the theme toggle.
const navClass = ({ isActive }) => (isActive ? 'nav__link is-active' : 'nav__link')

export default function Navbar() {
  const { theme, toggle } = useTheme()

  return (
    <header className="nav">
      <div className="nav__inner">
        <Link to="/" className="brand">
          <span className="brand__mark">🍞</span>
          <span className="brand__text">
            Cook&nbsp;&amp;&nbsp;Bake<small>Academy</small>
          </span>
        </Link>

        <nav className="nav__links">
          <NavLink to="/courses" className={navClass}>
            Courses
          </NavLink>
          <NavLink to="/about" className={navClass}>
            About
          </NavLink>
        </nav>

        <div className="nav__actions">
          <button
            className="btn btn--sm btn--quiet"
            onClick={toggle}
            aria-label="Toggle theme"
          >
            {theme === 'dark' ? '☀️' : '🌙'}
          </button>
        </div>
      </div>
    </header>
  )
}
