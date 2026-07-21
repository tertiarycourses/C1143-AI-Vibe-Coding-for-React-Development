import { useState } from 'react'
import { useAuth } from '../context/AuthContext'

// One form, two modes. Every field is a *controlled input*: its value comes from
// state, and onChange writes the next value back. React is the single source of
// truth for what the box contains.
//
// Our /api/auth/signup route requires a display `name`, so that field appears
// only in sign-up mode. signIn / signUp from AuthContext resolve to { data, error }
// — they do not throw. Check `error` or a wrong password silently does nothing.
export default function AuthForm({ onSuccess }) {
  const { signIn, signUp } = useAuth()
  const [mode, setMode] = useState('signin')
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState(null)

  const isSignUp = mode === 'signup'

  const handleSubmit = async (e) => {
    e.preventDefault() // Without this the browser reloads the page on submit.
    setBusy(true)
    setError(null)

    const { error } = isSignUp
      ? await signUp(email, password, name)
      : await signIn(email, password)

    setBusy(false)
    if (error) {
      setError(error.message)
      return
    }
    onSuccess?.()
  }

  return (
    <form className="panel" onSubmit={handleSubmit}>
      <h2>{isSignUp ? 'Create your account' : 'Sign in'}</h2>

      {isSignUp && (
        <label>
          Name
          <input
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
            autoComplete="name"
          />
        </label>
      )}

      <label>
        Email
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
          autoComplete="email"
        />
      </label>

      <label>
        Password
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          minLength={8}
          autoComplete={isSignUp ? 'new-password' : 'current-password'}
        />
      </label>

      {error && <p className="error">{error}</p>}

      <button type="submit" className="btn" disabled={busy}>
        {busy ? 'Working…' : isSignUp ? 'Sign up' : 'Sign in'}
      </button>

      <p className="muted">
        {isSignUp ? 'Already have an account?' : 'New here?'}{' '}
        <button
          type="button"
          className="linkbtn"
          onClick={() => {
            setMode(isSignUp ? 'signin' : 'signup')
            setError(null)
          }}
        >
          {isSignUp ? 'Sign in' : 'Create one'}
        </button>
      </p>
    </form>
  )
}
