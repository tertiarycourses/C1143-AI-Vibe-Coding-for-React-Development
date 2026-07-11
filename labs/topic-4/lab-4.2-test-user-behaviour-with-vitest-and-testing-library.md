# Lab 4.2 — Test User Behaviour with Vitest and Testing Library

> **Topic 4** · approximately 50 minutes · builds on the previous lab checkpoint

## Goal

Build a focused test suite for rendering, filtering, task movement, forms and routes.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/test/setup.ts`, `src/App.test.tsx`, `src/components/TaskForm.test.tsx`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Test** — apply it in the current file and explain its effect on user-visible behavior.

- **Assertion** — apply it in the current file and explain its effect on user-visible behavior.

- **User Event** — apply it in the current file and explain its effect on user-visible behavior.

- **Accessible Query** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Install Vitest, jsdom, Testing Library, jest-dom and user-event; pin and record versions

Install Vitest, jsdom, Testing Library, jest-dom and user-event; pin and record versions.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Configure the test environment and add an explicit `test` script

Configure the test environment and add an explicit `test` script.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Write a smoke test using role and accessible-name queries rather than CSS selectors

Write a smoke test using role and accessible-name queries rather than CSS selectors.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Add behaviour tests for filtering, valid/invalid form submit and moving a task

Add behaviour tests for filtering, valid/invalid form submit and moving a task.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Add a MemoryRouter test for task details and not-found behavior

Add a MemoryRouter test for task details and not-found behavior.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Run tests in watch and single-run modes; inspect generated assertions for false confidence

Run tests in watch and single-run modes; inspect generated assertions for false confidence.

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

Add Vitest and React Testing Library tests for SprintBoard. Query by role/name, drive interactions with user-event, and assert visible behaviour. Cover initial board, filter, invalid and valid create, move, task route and unknown task. Avoid snapshots and implementation-detail selectors.

```

## Read what the AI wrote

- **Testing internal state.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **fireEvent used for realistic typing.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Assertions pass without awaiting user events.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Snapshot replaces behavior checks.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects test, assertion, user event, accessible query to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. Behaviour tests treat the interface like a user does. Accessible queries improve both test resilience and the underlying UI semantics. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] Tests fail for deliberate regressions.

- [ ] Queries reflect accessibility.

- [ ] All required flows pass.

- [ ] Single-run command exits cleanly.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to test without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| Testing internal state | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| fireEvent used for realistic typing | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Assertions pass without awaiting user events | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Snapshot replaces behavior checks | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did test change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 4.2

Build a focused test suite for rendering, filtering, task movement, forms and routes.
