import { useState } from 'react'

// Two counters, one feature, two philosophies. The kitchen is counting loaves.
//
// LEFT  — the real DOM, by hand: you find a node in the live page and overwrite it.
//         There is no `count` variable anywhere. The DOM *is* the storage.
// RIGHT — React: you change a value and describe the UI for that value. React builds a
//         new Virtual DOM tree, diffs it against the last one, and patches the one text
//         node that actually changed.
//
// useState is a preview here; Topic 4 goes deep on it.
export default function DomVsReact() {
  return (
    <>
      <div className="section__head">
        <p className="eyebrow">Under the hood</p>
        <h2>The real DOM vs the Virtual DOM</h2>
        <p className="muted">
          Both buttons count loaves out of the oven. Watch <em>how</em> each one gets
          there — that difference is the whole reason React exists.
        </p>
      </div>

      <div className="grid">
        <ImperativePanel />
        <ReactPanel />
      </div>
    </>
  )
}

function ImperativePanel() {
  // No state. On every click we reach into the live page, read the current text back
  // OUT of the DOM, add one, and write it back IN. The number is not stored in JS at
  // all — it lives as a string inside a DOM node, and this handler has to know that
  // node's exact id to find it.
  function bake() {
    const node = document.getElementById('loaf-count')
    node.textContent = String(Number(node.textContent) + 1)
  }

  // The same job with innerHTML would be one keystroke shorter — and a security hole.
  // innerHTML parses whatever string you hand it AS HTML, so any user-supplied text in
  // there can smuggle in a live tag. textContent always writes plain text.
  //   node.innerHTML = '<b>' + next + '</b>'   // ❌ never with untrusted input

  return (
    <article className="panel">
      <span className="badge">Imperative · real DOM</span>
      <h3>🍞 You patch the DOM</h3>
      <p style={{ fontSize: '2.2rem', fontWeight: 800, margin: 0 }}>
        Loaves baked: <span id="loaf-count">0</span>
      </p>
      <button type="button" className="btn" onClick={bake}>
        +1 by hand
      </button>
      <p className="muted" style={{ margin: 0 }}>
        The handler says <strong>how</strong>: find node <code>#loaf-count</code>, read
        its text, rewrite its text. Rename that id and the feature silently breaks.
      </p>
    </article>
  )
}

function ReactPanel() {
  const [count, setCount] = useState(0)

  return (
    <article className="panel">
      <span className="badge">Declarative · Virtual DOM</span>
      <h3>🥐 React patches the DOM</h3>
      <p style={{ fontSize: '2.2rem', fontWeight: 800, margin: 0 }}>
        Loaves baked: <span>{count}</span>
      </p>
      <button type="button" className="btn" onClick={() => setCount(count + 1)}>
        +1 with state
      </button>
      <p className="muted" style={{ margin: 0 }}>
        You only say <strong>what</strong> the UI is for a given count. No id, no{' '}
        <code>getElementById</code>, no <code>textContent</code>. React re-renders,
        diffs the two object trees, and touches exactly one text node.
      </p>
    </article>
  )
}
