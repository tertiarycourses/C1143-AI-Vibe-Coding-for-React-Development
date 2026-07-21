import { useState } from 'react'
import StarRating from './StarRating'

// A controlled form for writing or editing your one review of a course. It seeds
// its fields from `existing` when you already have a review, so the same form
// does double duty for "write" and "edit".
export default function ReviewForm({ existing, onSubmit }) {
  const [rating, setRating] = useState(existing?.rating ?? 5)
  const [body, setBody] = useState(existing?.body ?? '')
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState(null)

  const handleSubmit = async (e) => {
    e.preventDefault() // without this the browser reloads the page
    setBusy(true)
    setError(null)
    const { error } = await onSubmit({ rating, body: body.trim() })
    setBusy(false)
    if (error) setError(error.message)
  }

  return (
    <form className="panel" onSubmit={handleSubmit}>
      <h3>{existing ? 'Edit your review' : 'Write a review'}</h3>

      <label>
        Your rating
        <StarRating value={rating} onChange={setRating} />
      </label>

      <label>
        Your review
        <textarea
          value={body}
          onChange={(e) => setBody(e.target.value)}
          required
          minLength={1}
          maxLength={2000}
          rows={4}
          placeholder="How was the class? What did you bake or cook?"
        />
      </label>

      {error && <p className="error">{error}</p>}

      <button type="submit" className="btn" disabled={busy || !body.trim()}>
        {busy ? 'Saving…' : existing ? 'Update review' : 'Post review'}
      </button>
    </form>
  )
}
