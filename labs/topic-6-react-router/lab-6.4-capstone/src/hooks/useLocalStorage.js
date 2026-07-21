import { useState } from 'react'

// A useState that also writes to localStorage. The initial value is read lazily
// (the function form of useState) so we only touch localStorage once, on mount.
export function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    try {
      const stored = window.localStorage.getItem(key)
      return stored !== null ? JSON.parse(stored) : initialValue
    } catch {
      return initialValue
    }
  })

  const set = (next) => {
    setValue((prev) => {
      const resolved = typeof next === 'function' ? next(prev) : next
      try {
        window.localStorage.setItem(key, JSON.stringify(resolved))
      } catch {
        // Private-mode / quota errors: keep state in memory, just don't persist.
      }
      return resolved
    })
  }

  return [value, set]
}
