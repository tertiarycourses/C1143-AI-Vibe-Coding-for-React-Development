# Lab 2: Compose a Reusable Sprint UI

## Goal

Build an accessible task board with JSX, components, props, events, and responsive CSS.

## What you will build

A tested increment of the SprintBoard React capstone.

## Prerequisites

Completed Lab 1 Git checkpoint.

## Steps

1. Create `src/data/tasks.ts` with six synthetic tasks using `id`, `title`, `owner`, `status`, and `points`; include no personal or production data.
2. Ask the agent for a component plan covering `Board`, `TaskColumn`, `TaskCard`, and `StatusFilter`. Require props and event contracts plus the exact file list.
3. Inspect the plan and approve only the named components, `src/types.ts`, `src/data/tasks.ts`, `src/App.tsx`, and CSS files.
4. Generate function components with typed props. Render tasks with stable IDs, semantic headings and buttons, and a useful empty state for a column with no tasks.
5. Add a status filter and a Move Forward event. Keep task state in `App` for now and pass data/callbacks explicitly through props.
6. Ask the agent to generate responsive CSS for 375 px and 1280 px widths, visible keyboard focus, and sufficient contrast. Inspect the CSS rather than accepting aesthetic claims.
7. Test every filter, move one task, tab through all controls, then run `npm run lint` and `npm run build`. Review the complete diff before committing.

## Test it

Six tasks render in reusable columns; filtering, event handling, keyboard navigation, empty state, and both target widths work.

## Troubleshooting

- Narrow an oversized agent change and retry one behavior at a time.
- Read the first error, inspect imports and types, then rerun the verification command.
- Revert to the previous Git checkpoint when the diff cannot be explained.
- Use only synthetic data and credential placeholders.

## Evidence to submit

Desktop/mobile screenshots, keyboard checklist, lint/build output, and one paragraph explaining the chosen component boundaries.

## Reflection

What did the agent propose, what did you verify, and what did you change before acceptance?
