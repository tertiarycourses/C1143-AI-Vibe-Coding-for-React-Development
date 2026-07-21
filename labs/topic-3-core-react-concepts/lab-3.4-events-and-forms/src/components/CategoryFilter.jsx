import { categories } from '../data/courses'

// The All / 🧁 Bakery / 🍳 Cooking chips from the brand mockup.
//
// A *controlled* component: it owns no state. The selected chip comes down as `value` and
// every click goes back up through `onChange`. One source of truth (in the parent) instead
// of two that can disagree. We pass an argument to the handler by wrapping the call in an
// arrow — onClick={() => onChange(cat.value)}. Writing onClick={onChange(cat.value)} would
// CALL it during render, on every render — a bug.
export default function CategoryFilter({ value, onChange }) {
  return (
    <div className="filters">
      {categories.map((cat) => (
        <button
          key={cat.value}
          type="button"
          className={cat.value === value ? 'chip is-active' : 'chip'}
          onClick={() => onChange(cat.value)}
        >
          {cat.label}
        </button>
      ))}
    </div>
  )
}
