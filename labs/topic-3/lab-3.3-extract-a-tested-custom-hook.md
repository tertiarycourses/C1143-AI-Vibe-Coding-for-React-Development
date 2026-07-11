# Lab 3.3 — Extract a Tested Custom Hook

> **Topic 3** · approximately 40 minutes · builds on the previous lab checkpoint

## Goal

Separate reusable board logic into a custom hook without sharing state between consumers.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/hooks/useTaskBoard.ts`, `src/hooks/useTaskBoard.test.ts`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Custom Hook** — apply it in the current file and explain its effect on user-visible behavior.

- **Logic Reuse** — apply it in the current file and explain its effect on user-visible behavior.

- **Public Api** — apply it in the current file and explain its effect on user-visible behavior.

- **Hook Test** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — List the smallest public API: tasks, visibleTasks, filter, setFilter, create, move and remove

List the smallest public API: tasks, visibleTasks, filter, setFilter, create, move and remove.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Move stateful logic into `useTaskBoard` while keeping presentation in components

Move stateful logic into `useTaskBoard` while keeping presentation in components.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Inspect hook naming, top-level hook calls and dependency boundaries

Inspect hook naming, top-level hook calls and dependency boundaries.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Render two hook consumers and prove they do not share state unless state is lifted

Render two hook consumers and prove they do not share state unless state is lifted.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Add focused tests for initial state, filtering and immutable movement

Add focused tests for initial state, filtering and immutable movement.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Refactor App to consume the hook; compare behavior before and after

Refactor App to consume the hook; compare behavior before and after.

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

Extract useTaskBoard from App. Define a small typed return API, keep hooks at the top level, derive visibleTasks, and expose named actions. Add tests for initial tasks, filtering and moving. Preserve all visible behavior and do not introduce context.

```

## Read what the AI wrote

- **Hook called conditionally.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Hook returns unstable unnecessary objects.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Custom hook assumed to create global shared state.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Presentation markup moved into logic hook.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects custom hook, logic reuse, public API, hook test to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. Custom hooks share stateful logic, not state instances. Each call runs its own hook state unless a common owner or context deliberately shares it. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] Two instances are independent.

- [ ] Hook tests pass.

- [ ] App becomes simpler.

- [ ] Behavior is unchanged.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to custom hook without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| Hook called conditionally | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Hook returns unstable unnecessary objects | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Custom hook assumed to create global shared state | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Presentation markup moved into logic hook | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did custom hook change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 3.3

Separate reusable board logic into a custom hook without sharing state between consumers.
