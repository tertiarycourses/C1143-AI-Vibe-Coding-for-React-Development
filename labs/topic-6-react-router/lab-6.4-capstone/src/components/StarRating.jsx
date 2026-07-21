// A star rating that works two ways: read-only when you pass just `value`, and
// interactive when you also pass `onChange`. Interactive stars are real
// <button>s so they are keyboard-accessible — never plain divs with onClick.
export default function StarRating({ value, onChange }) {
  const stars = [1, 2, 3, 4, 5]

  if (!onChange) {
    return (
      <span className="stars" aria-label={`${value} out of 5 stars`}>
        {stars.map((n) => (
          <span key={n} className={n <= value ? 'star is-on' : 'star'}>
            ★
          </span>
        ))}
      </span>
    )
  }

  return (
    <span className="stars">
      {stars.map((n) => (
        <button
          key={n}
          type="button"
          className={n <= value ? 'star star--btn is-on' : 'star star--btn'}
          onClick={() => onChange(n)}
          aria-label={`Rate ${n} star${n > 1 ? 's' : ''}`}
        >
          ★
        </button>
      ))}
    </span>
  )
}
