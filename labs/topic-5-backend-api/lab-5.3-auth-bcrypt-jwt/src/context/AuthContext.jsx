import { createContext, useContext, useState, useEffect, useCallback } from 'react'
import { api, getToken, setToken, clearToken } from '../lib/api'

// One place that knows "who is signed in". Any component can read it with
// useAuth().
//
// The token is a JWT issued by /api/auth/login. We keep it in localStorage and
// send it on every request; the SERVER verifies its signature and reads the user
// id out of it. That means the browser cannot lie about who it is — edit the
// token in devtools and the signature no longer matches, so the API answers 401.
const AuthContext = createContext(null)

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)

  // On boot we may hold a token from a previous visit, but THIS page load has
  // never had it checked. So before trusting it we ask /api/auth/me to verify
  // the signature and hand back the current user.
  //
  // `loading` is not optional. Without it the UI flashes "signed out" for a
  // moment even for a logged-in user, and — far worse — ProtectedRoute bounces
  // them to /login on every refresh.
  useEffect(() => {
    let active = true

    async function restore() {
      if (!getToken()) {
        setLoading(false)
        return
      }
      try {
        const { user } = await api.get('/auth/me')
        if (active) setUser(user)
      } catch {
        // Expired, tampered with, or the account is gone. Bin the token rather
        // than send it again on every request for the rest of time.
        clearToken()
        if (active) setUser(null)
      } finally {
        if (active) setLoading(false)
      }
    }

    restore()
    return () => {
      active = false
    }
  }, [])

  // api.post THROWS on a failed request, but AuthForm expects `{ data, error }`
  // back. Translate once, here, so no component has to wrap a call in try/catch
  // just to show a red message.
  const run = useCallback(async (path, body) => {
    try {
      const { token, user } = await api.post(path, body)
      setToken(token)
      setUser(user)
      return { data: user }
    } catch (err) {
      return { error: { message: err.message } }
    }
  }, [])

  const value = {
    // Components only check this for truthiness; keeping it means Navbar,
    // ProtectedRoute and friends did not have to change at all.
    session: user ? { token: getToken() } : null,
    user,
    loading,
    signUp: (email, password, name) => run('/auth/signup', { email, password, name }),
    signIn: (email, password) => run('/auth/login', { email, password }),
    // Signing out is purely a client-side act: drop the token and forget the
    // user. There is no server-side session to destroy — that is what "stateless
    // JWT" means, and it is also why we give the token a short expiry.
    signOut: () => {
      clearToken()
      setUser(null)
    },
  }

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
}

export function useAuth() {
  const context = useContext(AuthContext)
  if (context === null) {
    throw new Error('useAuth must be used inside an <AuthProvider>')
  }
  return context
}
