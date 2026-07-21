import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import { ThemeProvider } from './context/ThemeContext'
import { CartProvider } from './context/CartContext'

// The Providers must sit ABOVE everything that reads them, so we wrap <App/>.
// Nest the more global concern (theme) on the outside. In Topic 5 an AuthProvider
// joins them, and in Topic 6 a <BrowserRouter> wraps the lot.
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <ThemeProvider>
      <CartProvider>
        <App />
      </CartProvider>
    </ThemeProvider>
  </StrictMode>,
)
