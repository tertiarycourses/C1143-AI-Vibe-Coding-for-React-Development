import { useAuth } from '../../context/AuthContext'

export default function ProfilePage() {
  const { user, signOut } = useAuth()

  return (
    <div className="panel">
      <h3>Profile</h3>
      <p>
        <strong>Name:</strong> {user?.name}
      </p>
      <p>
        <strong>Email:</strong> {user?.email}
      </p>
      <p>
        {/* This id is the JWT's verified `sub` claim — the value the server read
            out of your signed token, not something the browser can set. The same
            id goes into every protected query's `where user_id = ${...}`, which
            is what scopes your data to you. */}
        <strong>User ID:</strong> <code>{user?.id}</code>
      </p>
      <p className="muted">
        Joined {user?.createdAt ? new Date(user.createdAt).toLocaleDateString() : '—'}
      </p>
      <button className="btn btn--quiet" onClick={signOut}>
        Sign out
      </button>
    </div>
  )
}
