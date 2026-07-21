import { createContext, useContext, useEffect } from 'react'
import { useLocalStorage } from '../hooks/useLocalStorage'

const ThemeContext = createContext(null)

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useLocalStorage('theme', 'light')

  // The one side effect: mirror the chosen theme onto <html data-theme="...">,
  // which is what index.css keys its dark-mode variables off.
  useEffect(() => {
    document.documentElement.dataset.theme = theme
  }, [theme])

  const toggle = () => setTheme((t) => (t === 'dark' ? 'light' : 'dark'))

  return (
    <ThemeContext.Provider value={{ theme, toggle }}>
      {children}
    </ThemeContext.Provider>
  )
}

export function useTheme() {
  const ctx = useContext(ThemeContext)
  if (!ctx) throw new Error('useTheme must be used inside <ThemeProvider>')
  return ctx
}
