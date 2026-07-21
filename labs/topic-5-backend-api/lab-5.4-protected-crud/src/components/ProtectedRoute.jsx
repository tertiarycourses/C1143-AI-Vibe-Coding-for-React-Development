import { Navigate, useLocation, Outlet } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'

// A layout route that guards everything nested inside it.
//
// The single most important line here is the `loading` check. On a hard refresh
// the auth provider needs a tick to rehydrate the session; during that tick
// `user` is null. If you redirect on `!user` WITHOUT waiting for `loading` to
// finish, a signed-in user gets bounced to /login on every refresh. Wait first.
export default function ProtectedRoute() {
  const { user, loading } = useAuth()
  const location = useLocation()

  if (loading) {
    return <p className="section muted">Checking your session…</p>
  }

  if (!user) {
    // `replace` so /login doesn't land in history (Back shouldn't return here).
    // `state.from` remembers where they wanted to go, so we can send them back.
    return <Navigate to="/login" replace state={{ from: location }} />
  }

  return <Outlet />
}
