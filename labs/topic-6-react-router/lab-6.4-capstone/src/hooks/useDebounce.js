import { useState, useEffect } from 'react'

// Returns a copy of `value` that only updates after `delay` ms of no changes.
// The cleanup cancels the pending timer on every keystroke, so a fast typist
// never fires the effect early.
export function useDebounce(value, delay = 300) {
  const [debounced, setDebounced] = useState(value)

  useEffect(() => {
    const id = setTimeout(() => setDebounced(value), delay)
    return () => clearTimeout(id)
  }, [value, delay])

  return debounced
}
