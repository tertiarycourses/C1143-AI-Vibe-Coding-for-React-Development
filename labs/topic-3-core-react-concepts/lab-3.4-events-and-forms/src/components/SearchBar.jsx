// A controlled input: React owns the value, and every keystroke calls back up to the
// parent. It holds no state of its own — `value` comes down as a prop and changes go up
// through `onChange`. That is what "controlled" means: React state is the single source of
// truth, not the DOM input.
//
// `inputRef` is passed straight through to the real <input> and left unused for now. In
// Topic 4 the parent creates a useRef and hands it in so it can focus the box on load — but
// nothing in this lab needs it, so the parent simply omits it (ref={undefined} is harmless).
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
