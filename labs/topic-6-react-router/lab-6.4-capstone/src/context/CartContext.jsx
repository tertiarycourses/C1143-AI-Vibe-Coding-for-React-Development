import { createContext, useContext } from 'react'
import { useLocalStorage } from '../hooks/useLocalStorage'

const CartContext = createContext(null)

export function CartProvider({ children }) {
  // Persisted so a refresh doesn't empty the basket.
  const [items, setItems] = useLocalStorage('cart', [])

  const addItem = (course) =>
    setItems((prev) =>
      prev.some((c) => c.id === course.id) ? prev : [...prev, course],
    )
  const removeItem = (id) => setItems((prev) => prev.filter((c) => c.id !== id))
  const clear = () => setItems([])

  const total = items.reduce((sum, c) => sum + Number(c.fee), 0)

  const value = { items, addItem, removeItem, clear, total, count: items.length }

  return <CartContext.Provider value={value}>{children}</CartContext.Provider>
}

export function useCart() {
  const ctx = useContext(CartContext)
  if (!ctx) throw new Error('useCart must be used inside <CartProvider>')
  return ctx
}
