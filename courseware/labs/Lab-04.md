# Lab 4: Debug, Test, Optimize, and Deploy SprintBoard

## Goal

Use AI to diagnose a defect, add focused tests, improve production quality, and publish the app.

## What you will build

A tested increment of the SprintBoard React capstone.

## Prerequisites

Completed Lab 3 Git checkpoint.

## Steps

1. Install Vitest and Testing Library using `npm install -D vitest jsdom @testing-library/react @testing-library/jest-dom @testing-library/user-event`; add an explicit `test` script.
2. Introduce a controlled defect in a branch: make Move Forward skip a status. Capture the failing behavior before asking the agent to diagnose it.
3. Give the agent the exact reproduction steps and relevant files. Require root-cause reasoning, one minimal patch, and a regression test; inspect the plan and diff before acceptance.
4. Generate tests for initial rendering, filtering, moving a task, API error UI, and one route. Prefer behavior assertions over implementation details.
5. Run `npm test -- --run`, `npm run lint`, and `npm run build`. Fix failures one at a time and reject broad rewrites or deleted assertions.
6. Ask for a production review covering bundle warnings, accessibility, component documentation, error handling, and removal of debug logs. Apply only evidence-backed improvements.
7. Deploy the `dist` output to an approved static host such as GitHub Pages, Netlify, or Vercel. Verify direct-route behavior and document the public URL and rollback method.
8. Run `git diff --check` and scan the final diff for secrets, tokens, placeholder mistakes, and unrelated files before the final checkpoint.

## Test it

All tests, lint, and production build pass; the regression is fixed; the deployed app loads and core flows work at the public URL.

## Troubleshooting

- Narrow an oversized agent change and retry one behavior at a time.
- Read the first error, inspect imports and types, then rerun the verification command.
- Revert to the previous Git checkpoint when the diff cannot be explained.
- Use only synthetic data and credential placeholders.

## Evidence to submit

Failing/passing test output, final quality-command output, deployment URL and screenshot, reviewed diff, and reflection on one AI suggestion changed or rejected.

## Reflection

What did the agent propose, what did you verify, and what did you change before acceptance?
