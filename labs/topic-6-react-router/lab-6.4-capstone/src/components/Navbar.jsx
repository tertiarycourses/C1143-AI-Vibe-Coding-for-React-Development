import { NavLink, Link } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import { useTheme } from '../context/ThemeContext'
import { useCart } from '../context/CartContext'

// NavLink hands its className a render function with an { isActive } flag, so the
// current tab can style itself without the component tracking the URL by hand.
const navClass = ({ isActive }) => (isActive ? 'nav__link is-active' : 'nav__link')

export default function Navbar() {
  const { user, signOut } = useAuth()
  const { theme, toggle } = useTheme()
  const { count } = useCart()

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
          {user && (
            <NavLink to="/dashboard" className={navClass}>
              Dashboard
            </NavLink>
          )}
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

          {user ? (
            <button className="btn btn--sm btn--quiet" onClick={signOut}>
              Sign out
            </button>
          ) : (
            <Link to="/login" className="btn btn--sm">
              Sign in
            </Link>
          )}
        </div>
      </div>
    </header>
  )
}
