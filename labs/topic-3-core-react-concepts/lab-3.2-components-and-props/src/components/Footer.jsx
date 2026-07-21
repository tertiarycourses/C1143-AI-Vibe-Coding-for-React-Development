export default function Footer() {
  // A tiny expression in JSX: compute the year once at render time.
  const year = new Date().getFullYear()

  return (
    <footer className="footer" id="about">
      <p>© {year} Cook &amp; Bake Academy · A demo cooking &amp; bakery training centre.</p>
      <p className="muted">📞 +65 6888 1234 · ✉️ enrol@cookbakeacademy.sg</p>
    </footer>
  )
}
