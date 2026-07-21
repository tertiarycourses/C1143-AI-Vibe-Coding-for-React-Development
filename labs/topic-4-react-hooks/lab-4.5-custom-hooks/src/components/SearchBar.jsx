// A controlled input: React owns the value, and every keystroke calls back up to
// the parent. `inputRef` is the parent's useRef, handed down so the parent can
// focus the real <input> DOM node. This is exactly the finished-app SearchBar.
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
