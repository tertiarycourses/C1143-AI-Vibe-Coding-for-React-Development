// ===========================================================================
// The browser's ONLY way to reach the server.
//
//     React (this file)  --fetch-->  /api/*  --sql-->  Neon Postgres
//
// Notice what is NOT in this file: no connection string, no password, no SQL.
// The browser cannot talk to Postgres and does not know how to. It knows one
// thing — how to call our own /api/* URLs — and the serverless functions on the
// other side decide what is allowed. Every line of security lives over there,
// where the user cannot edit it.
// ===========================================================================

const BASE = '/api'

// The JWT lives in localStorage so a refresh (or a new tab) does not sign you
// out. localStorage is readable by any JS running on this page, which is exactly
// why the token is short-lived and carries no secrets — it is a claim about who
// you are that only the server can verify, not a password.
const TOKEN_KEY = 'cookbake.token'

export const getToken = () => localStorage.getItem(TOKEN_KEY)
export const setToken = (token) => localStorage.setItem(TOKEN_KEY, token)
export const clearToken = () => localStorage.removeItem(TOKEN_KEY)

async function request(method, path, body) {
  const token = getToken()

  const res = await fetch(`${BASE}${path}`, {
    method,
    headers: {
      ...(body ? { 'Content-Type': 'application/json' } : {}),
      // This header is how the server knows who is calling. requireAuth() on the
      // other side verifies the signature before believing a word of it.
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: body ? JSON.stringify(body) : undefined,
  })

  // 204 has no body, and calling res.json() on it throws.
  const data = res.status === 204 ? null : await res.json().catch(() => null)

  // fetch() does NOT throw on 404 or 500 — it only rejects if the network itself
  // failed. A response arrived, so as far as fetch is concerned it worked. If we
  // did not check res.ok here, an error payload like {error: "..."} would sail on
  // into the UI and be rendered as if it were a course.
  if (!res.ok) {
    const err = new Error(data?.error ?? `Request failed (${res.status})`)
    // Carry the status along so a caller can tell "this course does not exist"
    // (404 -> render the not-found page) apart from "the server broke" (500 ->
    // render an error). Both are failures; they are not the same failure.
    err.status = res.status
    throw err
  }

  return data
}

export const api = {
  get: (path) => request('GET', path),
  post: (path, body) => request('POST', path, body),
  patch: (path, body) => request('PATCH', path, body),
  del: (path) => request('DELETE', path),
}
