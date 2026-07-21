import { useCart } from '../context/CartContext'
import Countdown from './Countdown'

// No items / onRemove props anymore — CartSummary pulls what it needs straight
// from Context. The total comes from the shared cart too.
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

      <Countdown hours={72} />
    </aside>
  )
}
