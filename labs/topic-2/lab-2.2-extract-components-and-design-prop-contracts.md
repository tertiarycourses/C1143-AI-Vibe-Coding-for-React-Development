# Lab 2.2 — Extract Components and Design Prop Contracts

> **Topic 2** · approximately 40 minutes · builds on the previous lab checkpoint

## Goal

Split the board into focused typed components and pass data explicitly through props.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/components/Board.tsx`, `src/components/TaskColumn.tsx`, `src/components/TaskCard.tsx`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Component Boundary** — apply it in the current file and explain its effect on user-visible behavior.

- **Props** — apply it in the current file and explain its effect on user-visible behavior.

- **Composition** — apply it in the current file and explain its effect on user-visible behavior.

- **Single Responsibility** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Draw the component tree from App to Board, TaskColumn and TaskCard before editing code

Draw the component tree from App to Board, TaskColumn and TaskCard before editing code.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Define each prop interface and decide which values are required, optional, or callbacks

Define each prop interface and decide which values are required, optional, or callbacks.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Ask the agent for a refactor plan that preserves visible behavior and names moves versus edits

Ask the agent for a refactor plan that preserves visible behavior and names moves versus edits.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Implement one extraction at a time; run the app after each move to isolate regressions

Implement one extraction at a time; run the app after each move to isolate regressions.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Inspect for prop drilling caused by misplaced state, duplicated markup and components that read globals

Inspect for prop drilling caused by misplaced state, duplicated markup and components that read globals.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Use React DevTools to identify boundaries, then lint/build and commit the refactor separately

Use React DevTools to identify boundaries, then lint/build and commit the refactor separately.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

## Agentic AI loop

### 1. Specify

State one observable goal, the current checkpoint, exact file scope, non-goals and stop conditions.

### 2. Plan

Require assumptions, numbered steps, files, risks, verification and rollback. Do not authorize code yet.

### 3. Inspect

Compare the plan with the brief. Reject unrelated dependencies, architecture changes, secret handling or untestable claims.

### 4. Implement

Approve one bounded increment. Keep the development server visible and do not combine refactoring with behavior change.

### 5. Test

Run commands yourself and exercise normal, boundary, empty and failure paths in the browser.

### 6. Critique and refine

Read every changed line, explain data flow, and ask for the smallest correction backed by a failing check.

### 7. Checkpoint

Commit only understood code. Record the commit and a one-sentence rollback instruction.

## Vibe prompt

```text

Refactor the existing task markup into Board, TaskColumn and TaskCard. First provide prop interfaces and a move plan. Preserve behavior and CSS classes. Do not add state, context or packages. Implement one component extraction at a time and stop if a test or build fails.

```

## Read what the AI wrote

- **Changing behavior during refactor.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Using any for props.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Reading module globals inside TaskCard.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **One component still owns unrelated responsibilities.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects component boundary, props, composition, single responsibility to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. A component boundary is an API. Clear prop contracts make generated code easier to inspect, test and replace without hidden coupling. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] UI is unchanged.

- [ ] Props are typed.

- [ ] Components have focused purposes.

- [ ] Build passes after each extraction.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to component boundary without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| Changing behavior during refactor | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Using any for props | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Reading module globals inside TaskCard | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| One component still owns unrelated responsibilities | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did component boundary change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 2.2

Split the board into focused typed components and pass data explicitly through props.
