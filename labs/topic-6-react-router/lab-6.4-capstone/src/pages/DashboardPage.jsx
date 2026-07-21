import { NavLink, Outlet } from 'react-router-dom'
import Section from '../components/Section'
import { useAuth } from '../context/AuthContext'

// A nested layout: the two tabs are relative links (no leading slash), so
// "my-courses" resolves to /dashboard/my-courses. The active child renders in
// this page's own <Outlet/>.
const tabClass = ({ isActive }) => (isActive ? 'chip is-active' : 'chip')

export default function DashboardPage() {
  const { user } = useAuth()

  return (
    <Section title="Your dashboard">
      <p className="muted">Signed in as {user?.email}</p>

      <nav className="filters filters--left">
        <NavLink to="my-courses" className={tabClass}>
          My courses
        </NavLink>
        <NavLink to="profile" className={tabClass}>
          Profile
        </NavLink>
      </nav>

      <Outlet />
    </Section>
  )
}
