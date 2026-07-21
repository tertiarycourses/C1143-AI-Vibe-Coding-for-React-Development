// A thin layout wrapper: a centred container with an optional heading. Anything you
// nest between <Section>...</Section> arrives as the `children` prop — which is how a
// component composes content it does not know about in advance. It knows nothing about
// courses; it only knows how to frame a titled block. This is the SAME Section the real
// app uses on every page — props { id, title, eyebrow, alt, children }.
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
