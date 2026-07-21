import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],

  // ==========================================================================
  // In DEVELOPMENT there are two servers, not one:
  //
  //   vite        :5173   serves React (and hot-reloads it)
  //   vercel dev  :3000   runs the api/ serverless functions against Neon
  //
  // Our frontend fetches relative URLs like `/api/courses`. Without the proxy
  // below those hit :5173, which knows nothing about api/ and answers with
  // index.html — so `await res.json()` blows up on a page of HTML. (If you ever
  // see "Unexpected token '<'", this is why: you fetched a URL and got a web
  // page back.)
  //
  // The proxy forwards anything starting with /api to :3000. The browser still
  // only ever sees ONE origin (localhost:5173), so there is no CORS to
  // configure — and in production it really is one origin, because Vercel serves
  // the built site and the functions from the same domain. Dev matches prod.
  //
  // So in dev, run BOTH:
  //     npx vercel dev --listen 3000    (terminal 1 — the API)
  //     npm run dev                     (terminal 2 — the React app)
  //
  // vercel dev reads DATABASE_URL and JWT_SECRET from .env.local.
  // ==========================================================================
  server: {
    proxy: {
      '/api': 'http://localhost:3000',
    },
  },
})
