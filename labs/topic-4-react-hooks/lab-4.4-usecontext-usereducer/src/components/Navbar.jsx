import { useTheme } from '../context/ThemeContext'
import { useCart } from '../context/CartContext'

// Navbar is far from where the theme and shortlist state live, yet it reads and
// flips the theme and shows the shortlist count with two one-line hooks — no props
// threaded down from App. That is dependency injection.
export default function Navbar() {
  const { theme, toggle } = useTheme()
  const { count } = useCart()

  return (
    <header className="nav">
      <div className="nav__inner">
        <a href="#courses" className="brand">
          <span className="brand__mark">🍞</span>
          <span className="brand__text">
            Cook&nbsp;&amp;&nbsp;Bake<small>Academy</small>
          </span>
        </a>

        <nav className="nav__links">
          <a href="#courses" className="nav__link">
            Courses
          </a>
        </nav>

        <div className="nav__actions">
          <button
            className="btn btn--sm btn--quiet"
            onClick={toggle}
            aria-label="Toggle theme"
          >
            {theme === 'dark' ? '☀️' : '🌙'}
          </button>

          <span className="badge">🧺 {count}</span>

          <button className="btn btn--sm">Sign in</button>
        </div>
      </div>
    </header>
  )
}
