import { useEffect, useState } from 'react'

// A countdown to the next class intake. This is the classic effect that MUST
// clean up after itself: it starts a repeating timer.
export default function Countdown({ hours = 72 }) {
  // Lazy initial state again: fix the deadline once, on mount.
  const [deadline] = useState(() => Date.now() + hours * 60 * 60 * 1000)
  const [remaining, setRemaining] = useState(() => deadline - Date.now())

  useEffect(() => {
    const id = setInterval(() => {
      setRemaining(deadline - Date.now())
    }, 1000)

    // The cleanup function. React runs it before the next effect and when the
    // component unmounts. Without it, every re-run would start ANOTHER interval
    // and the old ones would keep firing forever — a leak.
    return () => clearInterval(id)
  }, [deadline])

  if (remaining <= 0) {
    return <p className="muted">Enrolment is now open!</p>
  }

  const totalSeconds = Math.floor(remaining / 1000)
  const hh = Math.floor(totalSeconds / 3600)
  const mm = Math.floor((totalSeconds % 3600) / 60)
  const ss = totalSeconds % 60
  const pad = (n) => String(n).padStart(2, '0')

  return (
    <p className="muted">
      ⏳ Next sourdough intake starts in{' '}
      <strong>
        {pad(hh)}:{pad(mm)}:{pad(ss)}
      </strong>
    </p>
  )
}
