import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
//
// `base` is the URL path your assets are served from.
//  - Vercel and local dev serve at the domain root, so base is '/'.
//  - GitHub Pages serves at https://<user>.github.io/<repo>/, so its assets
//    must be requested from '/<repo>/' — otherwise you get a blank page and
//    404s for the JS/CSS bundle.
// One config serves both hosts: we read the base from the VITE_BASE env var.
// The Pages workflow (.github/workflows/deploy.yml) sets VITE_BASE=/cookbake/;
// everywhere else it is unset and falls back to '/'.
//
// Note: VITE_BASE is a *build* switch, not a secret. Like every VITE_ variable
// it is public — it literally ends up written into dist/index.html. That is
// fine: a URL prefix is not a credential. Server secrets (DATABASE_URL,
// JWT_SECRET — Topic 5) never get a VITE_ prefix and never appear in this file.
//
// In Topic 5 you add a `server.proxy` block here to forward /api to the
// serverless functions in dev. The `base` line below stays exactly as it is.
export default defineConfig({
  base: process.env.VITE_BASE ?? '/',
  plugins: [react()],
})
