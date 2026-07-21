import { Link } from 'react-router-dom'
import Section from '../components/Section'

export default function NotFoundPage() {
  return (
    <Section title="404 — Page not found">
      <p className="muted">
        That page doesn’t exist. It may have moved, or the link was mistyped.
      </p>
      <Link to="/">← Back home</Link>
    </Section>
  )
}
