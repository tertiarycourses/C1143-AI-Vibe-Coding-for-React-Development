import bcrypt from 'bcryptjs'
import { sql } from '../_lib/db.js'
import {
  signToken,
  toClientUser,
  sendError,
  readBody,
  requireMethod,
  HttpError,
} from '../_lib/auth.js'

// POST /api/auth/signup  { email, name, password }  -> { token, user }
export default async function handler(req, res) {
  try {
    requireMethod(req, 'POST')

    const { email, name, password } = readBody(req)

    // Validate on the SERVER. The <input required minLength={8}> in AuthForm.jsx
    // is a convenience for honest users; anyone can POST straight to this URL
    // with curl and skip the form entirely. Server-side checks are the real ones.
    if (!email || !name || !password) {
      throw new HttpError(400, 'Email, name and password are all required.')
    }
    if (typeof password !== 'string' || password.length < 8) {
      throw new HttpError(400, 'Password must be at least 8 characters.')
    }

    // NEVER store the password. bcrypt is a deliberately SLOW one-way hash: you
    // cannot turn the hash back into the password, and the cost factor (10 here,
    // ~100ms) makes brute-forcing a stolen table painfully expensive. bcrypt also
    // salts each hash automatically, so two users with the same password still
    // get different hashes and one cracked password does not unlock the other.
    const passwordHash = await bcrypt.hash(password, 10)

    const rows = await sql`
      insert into users (email, name, password_hash)
      values (${String(email).trim().toLowerCase()}, ${name}, ${passwordHash})
      on conflict (email) do nothing
      returning id::int as id, email, name, created_at
    `
    // Note the RETURNING list: id, email, name, created_at. password_hash is
    // NOT in it. The hash never leaves this function — not in a response body,
    // not in a log line. There is no reason for the browser to ever see it.

    // `on conflict do nothing` returns zero rows when the email is taken, which
    // is how we detect a duplicate without a second round-trip.
    if (rows.length === 0) {
      throw new HttpError(409, 'That email is already registered. Try signing in.')
    }

    const user = rows[0]

    // Sign them straight in — a new account should not have to log in again.
    return res.status(201).json({ token: signToken(user), user: toClientUser(user) })
  } catch (err) {
    return sendError(res, err)
  }
}
