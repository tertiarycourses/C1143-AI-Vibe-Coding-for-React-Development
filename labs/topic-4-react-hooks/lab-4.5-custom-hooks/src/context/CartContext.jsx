import { createContext, useContext } from 'react'
import { useLocalStorage } from '../hooks/useLocalStorage'

const CartContext = createContext(null)

// This is the finished-app CartContext. Lab 4.4 drove the shortlist through a
// reducer to NAME the actions; here we keep it simpler — plain immutable setters
// over useLocalStorage. The persistence that took a bespoke effect in Lab 4.2 is
// now one hook, and a refresh no longer empties the basket. Both forms are fine;
// the reducer earns its keep only once the actions multiply.
export function CartProvider({ children }) {
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
