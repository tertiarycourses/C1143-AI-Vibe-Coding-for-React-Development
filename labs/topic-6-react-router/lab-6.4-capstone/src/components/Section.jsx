// A thin layout wrapper: a centred container with an optional heading. Anything
// you nest inside <Section>...</Section> arrives as the `children` prop — which
// is how a component composes content it does not know about in advance.
export default function Section({ id, title, eyebrow, alt, children }) {
  return (
    <section id={id} className={alt ? 'section section--alt' : 'section'}>
      {(title || eyebrow) && (
        <div className="section__head">
          {eyebrow && <p className="eyebrow">{eyebrow}</p>}
          {title && <h2>{title}</h2>}
        </div>
      )}
      {children}
    </section>
  )
}
