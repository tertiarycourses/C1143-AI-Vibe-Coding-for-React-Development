import { createContext, useContext, useEffect, useMemo, useState } from 'react'

// createContext makes a "channel". Anything rendered inside the Provider can read
// its value with useContext — no props passed through the components in between.
const ThemeContext = createContext(null)

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState(() => localStorage.getItem('theme') || 'light')

  // The one side effect: mirror the chosen theme onto <html data-theme="…">, which
  // is what index.css keys its dark-mode variables off. Persist it for next visit.
  useEffect(() => {
    document.documentElement.dataset.theme = theme
    localStorage.setItem('theme', theme)
  }, [theme])

  const value = useMemo(
    () => ({
      theme,
      toggle: () => setTheme((t) => (t === 'dark' ? 'light' : 'dark')),
    }),
    [theme],
  )

  return <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>
}

export function useTheme() {
  const ctx = useContext(ThemeContext)
  if (!ctx) throw new Error('useTheme must be used inside <ThemeProvider>')
  return ctx
}
