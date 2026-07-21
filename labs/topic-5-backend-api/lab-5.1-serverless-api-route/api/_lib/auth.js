import jwt from 'jsonwebtoken'

// ===========================================================================
// Who is calling? — the single source of truth for identity.
//
// THE RULE THIS FILE EXISTS TO ENFORCE:
//   The user id ALWAYS comes from a verified JWT. It NEVER comes from the
//   request body, a query string, or a header the caller can just type.
//
// If POST /api/enrollments trusted `req.body.userId`, anyone could enrol
// anyone. Instead every protected route calls requireAuth(req), which will only
// hand back an id it has cryptographically verified.
// ===========================================================================
const JWT_SECRET = process.env.JWT_SECRET

if (!JWT_SECRET) {
  throw new Error('JWT_SECRET is not set. See .env.example.')
}

// Thrown by requireAuth. Handlers catch it and turn it into an HTTP status,
// which keeps the "is this person allowed?" logic in one place.
export class HttpError extends Error {
  constructor(status, message) {
    super(message)
    this.status = status
  }
}

// A JWT is three base64 chunks: header.payload.signature. The payload is only
// ENCODED, not encrypted — anyone can read it — so never put a secret in it.
// What makes it trustworthy is the signature: it is computed with JWT_SECRET,
// which only the server knows. Change one byte of the payload (say, `sub` from
// your id to somebody else's) and the signature no longer matches, so verify()
// below throws. That is why we can trust `sub` and must not trust req.body.
export function signToken(user) {
  return jwt.sign(
    { sub: String(user.id), email: user.email, name: user.name },
    JWT_SECRET,
    { expiresIn: '7d' },
  )
}

// Reads `Authorization: Bearer <token>`, verifies the signature, and returns
// the caller's user id as a number. Throws 401 for anything else — a missing
// header, a malformed header, a bad signature, an expired token.
//
// Note there is no "is the token expired?" check written here. jwt.verify()
// does it for us and throws TokenExpiredError; hand-rolling that check is how
// people accidentally ship tokens that never expire.
export function requireAuth(req) {
  const header = req.headers?.authorization ?? ''

  if (!header.startsWith('Bearer ')) {
    throw new HttpError(401, 'Missing or malformed Authorization header.')
  }

  const token = header.slice('Bearer '.length).trim()

  try {
    const payload = jwt.verify(token, JWT_SECRET)
    return Number(payload.sub) // the user's id — verified, not claimed
  } catch {
    // Deliberately vague: telling an attacker *why* the token failed (expired
    // vs. bad signature) is free information. The client only needs "sign in".
    throw new HttpError(401, 'Invalid or expired session. Please sign in again.')
  }
}

// The only user shape the browser is ever allowed to see. Defined ONCE and used
// by signup, login and me, so that `password_hash` cannot leak from a route
// somebody wrote in a hurry. Whitelisting the fields you send is much safer than
// deleting the ones you don't: add a column to the table later and it stays
// private by default.
export function toClientUser(user) {
  return {
    id: user.id,
    email: user.email,
    name: user.name,
    createdAt: user.created_at,
  }
}

// ---------------------------------------------------------------------------
// Small shared plumbing so every route reads the same way.
// ---------------------------------------------------------------------------

// Turn any thrown error into a JSON response. HttpError carries its own status;
// anything else is a bug on our side, so it is a 500 and the details stay in
// the server log rather than leaking a stack trace (or a SQL error naming our
// columns) to the browser.
export function sendError(res, err) {
  if (err instanceof HttpError) {
    return res.status(err.status).json({ error: err.message })
  }
  console.error(err)
  return res.status(500).json({ error: 'Something went wrong. Please try again.' })
}

// Vercel parses a JSON body for us, but when this handler is imported directly
// in a test (or called with a text/plain content-type) req.body can still be a
// string. Normalise it so the routes never have to care.
export function readBody(req) {
  if (!req.body) return {}
  if (typeof req.body === 'string') {
    try {
      return JSON.parse(req.body)
    } catch {
      throw new HttpError(400, 'Request body is not valid JSON.')
    }
  }
  return req.body
}

// Reject anything that is not the verb this route implements.
export function requireMethod(req, ...allowed) {
  if (!allowed.includes(req.method)) {
    throw new HttpError(405, `Method ${req.method} not allowed.`)
  }
}
