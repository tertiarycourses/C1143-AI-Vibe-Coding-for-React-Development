// A controlled input: React owns the value, and every keystroke calls back up to
// the parent. It holds no state of its own.
//
// `inputRef` is the parent's useRef, handed down so the parent can talk to the
// real <input> DOM node (to focus it). A ref is the escape hatch for the things
// state cannot express — focus, scroll position, measurements.
export default function SearchBar({ value, onChange, inputRef }) {
  return (
    <div className="search">
      <span className="search__icon" aria-hidden="true">🔎</span>
      <input
        ref={inputRef}
        type="search"
        placeholder="Search sourdough, sushi, macaron…"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        aria-label="Search courses"
      />
    </div>
  )
}
