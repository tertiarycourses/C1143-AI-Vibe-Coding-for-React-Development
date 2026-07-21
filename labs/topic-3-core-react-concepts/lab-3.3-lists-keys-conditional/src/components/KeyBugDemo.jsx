import { useState } from 'react'

// A runnable demonstration of the key={index} bug.
//
// Drop <KeyBugDemo /> into App temporarily. Each row has an UNCONTROLLED input — React
// does not own its text, the DOM node does. That is the whole point: the typed text lives
// on the DOM node, and `key` is what decides which node React keeps when the list reorders.
//
//   • Flip the toggle to "key={index}" (broken), type a note into each row, then press
//     "Move first to last". The notes stay put while the labels move past them — the text
//     is stranded on the wrong row.
//   • Flip the toggle back to "key={item.id}" (correct) and reorder again. Now the notes
//     travel WITH their row, because React matches nodes by stable id.
export default function KeyBugDemo() {
  const [items, setItems] = useState([
    { id: 'a', label: 'Artisan Sourdough Bread Baking' },
    { id: 'b', label: 'French Pastry & Viennoiserie' },
    { id: 'c', label: 'Macaron Masterclass' },
  ])
  const [useIndexKey, setUseIndexKey] = useState(false)

  const rotate = () => {
    // Move the first item to the end — a reorder, which is exactly what breaks index keys
    // (the labels shift by one slot but the DOM nodes do not).
    setItems((prev) => [...prev.slice(1), prev[0]])
  }

  return (
    <div className="panel">
      <div className="row row--between">
        <h3>🔬 Key bug demo</h3>
        <span className="badge">
          {useIndexKey ? 'key={index} — broken' : 'key={item.id} — correct'}
        </span>
      </div>

      <p className="muted">
        Type a note into each row, then reorder. With index keys the notes get stranded on
        the wrong row; with id keys they follow.
      </p>

      <div className="row" style={{ gap: '0.75rem' }}>
        <button type="button" className="btn btn--sm" onClick={rotate}>
          Move first to last
        </button>
        <button
          type="button"
          className="btn btn--sm btn--quiet"
          onClick={() => setUseIndexKey((v) => !v)}
        >
          Use {useIndexKey ? 'key={item.id}' : 'key={index}'}
        </button>
      </div>

      <ul className="stack" style={{ marginTop: '0.5rem' }}>
        {items.map((item, index) => (
          <li
            // THIS is the line the toggle flips. Same list, same render — only the key
            // strategy changes, and that alone decides the behaviour.
            key={useIndexKey ? index : item.id}
            className="row row--between"
          >
            <span>{item.label}</span>
            <input type="text" placeholder="your notes…" defaultValue="" />
          </li>
        ))}
      </ul>
    </div>
  )
}
