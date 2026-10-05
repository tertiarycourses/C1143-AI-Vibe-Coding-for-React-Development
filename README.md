# AI Vibe Coding for React Development

Build and deploy a full-stack React web app by prompting an AI coding agent, then reading, understanding and correcting what it writes.

| Course detail | Information |
|---|---|
| Course code | `C1143` |
| Programme | Non-WSQ |
| Duration | 2 days · 15 hours (9:30am – 5:30pm) |
| Registration | [View course details and register](https://www.tertiarycourses.com.sg/ai-vibe-coding-for-react-development.html) |

## About the course

Across two hands-on days, learners build **Cook & Bake Academy**, a full-stack website for a cooking and bakery school, from an empty folder to a live deployment. The app has a 20-course catalogue, a Neon Postgres database, a serverless API, authentication and multi-page navigation. Every lab runs the same loop: **Prompt → Generate → Read → Understand → Correct**. The AI writes the code and you supply the judgement.

The course teaches React, not JavaScript. It assumes you are already comfortable with modern JavaScript (arrow functions, destructuring, `map`/`filter`, template literals and `async`/`await`).

## Learning outcomes

On completion of this course, learners will be able to:

1. Build a React web app using vibe coding: scaffold a Vite + React project, prompt an AI coding agent, and read, understand and correct the code it generates.
2. Deploy a React web app to the cloud: version the project with Git and GitHub, produce a production build, and publish it to Vercel or GitHub Pages.
3. Apply core React concepts: components, JSX and how Babel compiles it, the real DOM versus the Virtual DOM, props, composition, lists and keys, conditional rendering, events and controlled forms.
4. Apply React Hooks: `useState`, `useEffect` with cleanup, `useRef` for direct DOM access, `useContext`, `useReducer`, and custom hooks that share logic.
5. Integrate a backend API and database: build serverless API routes over Neon Postgres, fetch them from React with loading and error states, and add password hashing and JWT authentication.
6. Implement real application navigation with React Router (routes, nested layouts, dynamic parameters, URL state and protected routes) and deploy the full-stack app.

## Topics covered

| Topic | Day | Labs |
|---|---|---|
| 1 — Build a React Web App Using Vibe Coding | 1 | 1.1 – 1.3 |
| 2 — Deploy Your React Web App to the Cloud | 1 | 2.1 – 2.3 |
| 3 — Improving Your App by Learning Core React Concepts | 1 | 3.1 – 3.4 |
| 4 — React Hooks (The Vibe Way) | 2 | 4.1 – 4.5 |
| 5 — Giving Your App a Backend API and a Database | 2 | 5.1 – 5.4 |
| 6 — React Router for Real App Navigation | 2 | 6.1 – 6.6 |

## Labs

Each lab builds on the app you had at the end of the previous one. Every lab folder holds a README and, where code changes, a drop-in `src/` (or `api/`) checkpoint you can restore from.

**Topic 1 — Vibe coding**
- [Lab 1.1 — Set Up Your Vibe-Coding Workspace](labs/topic-1-vibe-coding/lab-1.1-setup-workspace/)
- [Lab 1.2 — Vibe-Code Your First Component](labs/topic-1-vibe-coding/lab-1.2-first-component/)
- [Lab 1.3 — Vibe-Code the Cook & Bake Landing Page](labs/topic-1-vibe-coding/lab-1.3-landing-page/)

**Topic 2 — Deploy to the cloud**
- [Lab 2.1 — Git and GitHub](labs/topic-2-deploy-to-cloud/lab-2.1-git-and-github/)
- [Lab 2.2 — Deploy to Vercel](labs/topic-2-deploy-to-cloud/lab-2.2-deploy-to-vercel/)
- [Lab 2.3 — GitHub Pages with GitHub Actions](labs/topic-2-deploy-to-cloud/lab-2.3-github-pages-actions/)

**Topic 3 — Core React concepts**
- [Lab 3.1 — JSX, the Real DOM and the Virtual DOM](labs/topic-3-core-react-concepts/lab-3.1-jsx-and-the-dom/)
- [Lab 3.2 — Components and Props](labs/topic-3-core-react-concepts/lab-3.2-components-and-props/)
- [Lab 3.3 — Lists, Keys and Conditional Rendering](labs/topic-3-core-react-concepts/lab-3.3-lists-keys-conditional/)
- [Lab 3.4 — Events and Forms](labs/topic-3-core-react-concepts/lab-3.4-events-and-forms/)

**Topic 4 — React Hooks**
- [Lab 4.1 — State with `useState`](labs/topic-4-react-hooks/lab-4.1-usestate/)
- [Lab 4.2 — Side effects with `useEffect`](labs/topic-4-react-hooks/lab-4.2-useeffect/)
- [Lab 4.3 — Escape hatches with `useRef`](labs/topic-4-react-hooks/lab-4.3-useref/)
- [Lab 4.4 — Global state with `useContext` + `useReducer`](labs/topic-4-react-hooks/lab-4.4-usecontext-usereducer/)
- [Lab 4.5 — Write your own hooks](labs/topic-4-react-hooks/lab-4.5-custom-hooks/)

**Topic 5 — Backend API and database**
- [Lab 5.1 — The Three Tiers: Your First API Route over Neon](labs/topic-5-backend-api/lab-5.1-serverless-api-route/)
- [Lab 5.2 — Fetch the Catalogue From React](labs/topic-5-backend-api/lab-5.2-fetch-from-react/)
- [Lab 5.3 — Accounts: Password Hashing With bcrypt, Sessions With JWT](labs/topic-5-backend-api/lab-5.3-auth-bcrypt-jwt/)
- [Lab 5.4 — Protected CRUD: Enrollments Scoped to the Signed-in User](labs/topic-5-backend-api/lab-5.4-protected-crud/)

**Topic 6 — React Router**
- [Lab 6.1 — Routes and Links](labs/topic-6-react-router/lab-6.1-routes-and-links/)
- [Lab 6.2 — Dynamic Routes](labs/topic-6-react-router/lab-6.2-dynamic-routes/)
- [Lab 6.3 — Protected Routes](labs/topic-6-react-router/lab-6.3-protected-routes/)
- [Lab 6.4 — Capstone: Assemble the Full-Stack App](labs/topic-6-react-router/lab-6.4-capstone/)
- [Lab 6.5 — Deploy the Full-Stack App to Vercel + Neon](labs/topic-6-react-router/lab-6.5-deploy-full-stack/)
- [Lab 6.6 — Mini-Capstone: Add Course Reviews, On Your Own](labs/topic-6-react-router/lab-6.6-mini-capstone/)

The database schema and seed data used from Topic 5 onwards is in [`neon/schema.sql`](neon/schema.sql).

## Courseware package

| Artifact | Files |
|---|---|
| Slide deck | [PPTX](courseware/AI%20Vibe%20Coding%20for%20React%20Development-v4.0.pptx) · [PDF](courseware/AI%20Vibe%20Coding%20for%20React%20Development-v4.0.pdf) |
| Learner Guide | [DOCX](courseware/LG-AI%20Vibe%20Coding%20for%20React%20Development.docx) · [PDF](courseware/LG-AI%20Vibe%20Coding%20for%20React%20Development.pdf) · [Markdown](courseware/LG-AI%20Vibe%20Coding%20for%20React%20Development.md) |
| Lesson Plan | [DOCX](courseware/LP-AI%20Vibe%20Coding%20for%20React%20Development.docx) · [PDF](courseware/LP-AI%20Vibe%20Coding%20for%20React%20Development.pdf) |
| Labs | [`labs/`](labs/) (25 labs across six topics) |

This is a non-assessed short course. Learning is checked through each lab's "Test it" step and the capstone.

## Distribution

The slides, Learner Guide, Lesson Plan and labs in this repository are published for course participants. Superseded versions, credentials and source reference material are not published here.

## Provider

Courseware by [Tertiary Infotech Academy Pte Ltd](https://www.tertiaryinfotech.com/) (UEN 201200696W). Course page: [AI Vibe Coding for React Development](https://www.tertiarycourses.com.sg/ai-vibe-coding-for-react-development.html).
