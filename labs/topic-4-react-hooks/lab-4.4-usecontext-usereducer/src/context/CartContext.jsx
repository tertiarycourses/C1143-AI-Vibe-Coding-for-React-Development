import { createContext, useContext, useMemo, useReducer } from 'react'

const CartContext = createContext(null)

// A reducer is a PURE function: (currentState, action) => nextState. No side
// effects, no mutation — it always returns a brand-new array. Because it is pure
// it is trivial to reason about and to unit-test in isolation. The shortlist holds
// full course OBJECTS, so ADD carries the whole course and REMOVE carries an id.
function cartReducer(state, action) {
  switch (action.type) {
    case 'ADD':
      return state.some((c) => c.id === action.course.id)
        ? state
        : [...state, action.course]
    case 'REMOVE':
      return state.filter((c) => c.id !== action.id)
    case 'CLEAR':
      return []
    default:
      throw new Error(`Unknown cart action: ${action.type}`)
  }
}

export function CartProvider({ children }) {
  // useReducer earns its keep here: several named actions change one value, each
  // next state depends on the previous one, and the logic is one testable function.
  const [items, dispatch] = useReducer(cartReducer, [])

  // Memoise the value object so consumers don't re-render just because a parent
  // did. A fresh { } every render is a new reference and would defeat that.
  const value = useMemo(
    () => ({
      items,
      addItem: (course) => dispatch({ type: 'ADD', course }),
      removeItem: (id) => dispatch({ type: 'REMOVE', id }),
      clear: () => dispatch({ type: 'CLEAR' }),
      total: items.reduce((sum, c) => sum + Number(c.fee), 0),
      count: items.length,
    }),
    [items],
  )

  return <CartContext.Provider value={value}>{children}</CartContext.Provider>
}

// The custom-hook guard: if someone calls useCart outside a CartProvider, ctx is
// null. Throwing here turns a confusing far-away "cannot read property of null"
// into an immediate, honest error message.
export function useCart() {
  const ctx = useContext(CartContext)
  if (!ctx) throw new Error('useCart must be used inside <CartProvider>')
  return ctx
}
