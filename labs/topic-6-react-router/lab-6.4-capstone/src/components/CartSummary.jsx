import { useCart } from '../context/CartContext'

// The shortlist a visitor builds while browsing. It reads the cart straight from
// context, so it never needs the data passed down through the pages above it.
export default function CartSummary() {
  const { items, removeItem, clear, total } = useCart()

  if (!items.length) return null

  return (
    <aside className="panel">
      <h3>Your shortlist</h3>

      <ul className="stack stack--tight">
        {items.map((c) => (
          <li key={c.id} className="row row--between">
            <span>
              {c.emoji} {c.title}
            </span>
            <span className="row">
              <span className="muted">S${c.fee}</span>
              <button
                className="btn btn--sm btn--quiet"
                onClick={() => removeItem(c.id)}
                aria-label={`Remove ${c.title}`}
              >
                ✕
              </button>
            </span>
          </li>
        ))}
      </ul>

      <div className="row row--between">
        <strong>Total: S${total}</strong>
        <button className="btn btn--sm btn--quiet" onClick={clear}>
          Clear
        </button>
      </div>
    </aside>
  )
}
