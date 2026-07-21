import Countdown from './Countdown'

// The total is still computed DURING RENDER from the items prop — no useEffect
// and no extra state. Deriving during render is the correct pattern; syncing it
// into state with an effect would be the #1 useEffect anti-pattern.
export default function CartSummary({ items, onRemove, onClear }) {
  if (!items.length) return null

  const total = items.reduce((sum, c) => sum + Number(c.fee), 0)

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
                onClick={() => onRemove(c.id)}
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
        <button className="btn btn--sm btn--quiet" onClick={onClear}>
          Clear
        </button>
      </div>

      <Countdown hours={72} />
    </aside>
  )
}
