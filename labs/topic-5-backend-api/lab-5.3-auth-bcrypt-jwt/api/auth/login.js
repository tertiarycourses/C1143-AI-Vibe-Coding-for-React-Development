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

// POST /api/auth/login  { email, password }  -> { token, user }
export default async function handler(req, res) {
  try {
    requireMethod(req, 'POST')

    const { email, password } = readBody(req)

    if (!email || !password) {
      throw new HttpError(400, 'Email and password are required.')
    }

    // password_hash is selected here — and ONLY here — because we need to
    // compare against it. It goes into a local variable and never into `res`.
    const rows = await sql`
      select id::int as id, email, name, password_hash, created_at
      from users
      where email = ${String(email).trim().toLowerCase()}
    `

    const user = rows[0]

    // Verify with bcrypt.compare(), which re-hashes the submitted password with
    // the salt baked into the stored hash and compares the results in constant
    // time. Never do `hash(password) === stored` yourself: bcrypt salts every
    // hash, so that comparison is always false, and a plain === on secrets leaks
    // information through how long it takes to fail.
    const ok = user ? await bcrypt.compare(password, user.password_hash) : false

    // ONE message for both "no such email" and "wrong password". Splitting them
    // hands an attacker a free tool for discovering which emails have accounts.
    if (!ok) {
      throw new HttpError(401, 'Invalid email or password.')
    }

    return res.status(200).json({ token: signToken(user), user: toClientUser(user) })
  } catch (err) {
    return sendError(res, err)
  }
}
