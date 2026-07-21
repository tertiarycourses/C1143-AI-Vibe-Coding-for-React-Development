import { useEffect } from 'react'
import { useNavigate, useLocation } from 'react-router-dom'
import Section from '../components/Section'
import AuthForm from '../components/AuthForm'
import { useAuth } from '../context/AuthContext'

export default function LoginPage() {
  const { user } = useAuth()
  const navigate = useNavigate()
  const location = useLocation()

  // Where the guard wanted to send us (set by ProtectedRoute), or the dashboard.
  const from = location.state?.from?.pathname ?? '/dashboard'

  // If someone visits /login while already signed in, bounce them onward.
  useEffect(() => {
    if (user) navigate(from, { replace: true })
  }, [user, from, navigate])

  return (
    <Section title="Sign in to Cook & Bake Academy">
      <div className="narrow">
        <AuthForm onSuccess={() => navigate(from, { replace: true })} />
      </div>
    </Section>
  )
}
