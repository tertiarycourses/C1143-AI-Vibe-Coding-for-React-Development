import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import './index.css'
import App from './App.jsx'
import { ThemeProvider } from './context/ThemeContext'
import { AuthProvider } from './context/AuthContext'
import { CartProvider } from './context/CartContext'

// This is the ONE place React touches the real DOM. createRoot takes over the
// empty <div id="root"> in index.html; from here down, everything you write is
// JSX describing what the UI should look like, and React diffs that description
// against its Virtual DOM to work out the smallest set of real DOM edits.
//
// Provider order matters. BrowserRouter is outermost so every component below
// it can use routing hooks. The three app providers sit inside it and outside
// <App/>, so the whole route tree can read theme, auth and basket.
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <ThemeProvider>
        <AuthProvider>
          <CartProvider>
            <App />
          </CartProvider>
        </AuthProvider>
      </ThemeProvider>
    </BrowserRouter>
  </StrictMode>,
)
