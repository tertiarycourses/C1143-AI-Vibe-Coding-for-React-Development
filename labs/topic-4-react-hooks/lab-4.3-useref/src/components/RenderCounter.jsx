import { useRef, useState } from 'react'

// A live demonstration of the difference between a ref and state.
export default function RenderCounter() {
  // useRef gives a mutable box that survives every render. Bumping .current does
  // NOT schedule a re-render — that is the whole point of a ref.
  const renders = useRef(0)
  renders.current += 1

  // useState is the opposite: calling the setter DOES schedule a re-render.
  // We only use it here to force renders so you can watch the ref count climb.
  const [, forceRender] = useState(0)

  return (
    <span className="badge" title="A ref survives renders but never causes one">
      renders: {renders.current}
      <button
        className="btn btn--sm btn--quiet"
        style={{ marginLeft: '0.5rem' }}
        onClick={() => forceRender((n) => n + 1)}
      >
        re-render
      </button>
    </span>
  )
}
