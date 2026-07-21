import { useState, useEffect } from 'react'

// Returns a copy of `value` that only updates after `delay` ms of no changes.
// The cleanup cancels the pending timer on every keystroke, so a fast typist
// never fires the effect early.
//
// This is the same timer-with-cleanup shape as Lab 4.2's Countdown, now packaged
// behind a name. Because it calls hooks it IS a hook — so it must start with `use`
// and obey the Rules of Hooks. Two components calling it get two independent
// timers: a custom hook shares LOGIC, never STATE.
export function useDebounce(value, delay = 300) {
  const [debounced, setDebounced] = useState(value)

  useEffect(() => {
    const id = setTimeout(() => setDebounced(value), delay)
    return () => clearTimeout(id)
  }, [value, delay])

  return debounced
}
