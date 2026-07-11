# Lab 3: Add State, Hooks, Routing, and API Data

## Goal

Turn SprintBoard into a multi-page app with controlled state, effects, and resilient API fetching.

## What you will build

A tested increment of the SprintBoard React capstone.

## Prerequisites

Completed Lab 2 Git checkpoint.

## Steps

1. Install React Router with `npm install react-router-dom` and record the command in the project README.
2. Ask the agent to plan routes for `/`, `/tasks/:taskId`, and `/about`, plus a not-found route. Require a rollback note and no unrelated styling rewrite.
3. Inspect and approve the routing files, then add navigation, a task details view, and a useful not-found page. Test direct URL entry as well as link navigation.
4. Create `public/tasks.json` with synthetic task data. Ask for a small `useTasks` hook that models loading, success, empty, and error states using `useEffect` and `AbortController`.
5. Review effect dependencies and cleanup. Reject suppressed lint rules, duplicated state, or use of `any`. Implement immutable status updates with functional `setState`.
6. Test the normal response, an empty array, and a deliberately broken URL; restore the working URL after observing the error UI.
7. Ask the agent to refactor one duplicated UI pattern without changing behavior. Compare before/after diffs, then run `npm run lint` and `npm run build`.

## Test it

All routes work, task data loads with visible state transitions, failures recover cleanly, and the reviewed refactor preserves behavior.

## Troubleshooting

- Narrow an oversized agent change and retry one behavior at a time.
- Read the first error, inspect imports and types, then rerun the verification command.
- Revert to the previous Git checkpoint when the diff cannot be explained.
- Use only synthetic data and credential placeholders.

## Evidence to submit

Route screenshots, loading/error evidence, hook explanation, dependency review, and lint/build output.

## Reflection

What did the agent propose, what did you verify, and what did you change before acceptance?
