# Lab 3.1 — Manage Immutable Task State with useState

> **Topic 3** · approximately 45 minutes · builds on the previous lab checkpoint

## Goal

Create, move and delete tasks with functional updates and immutable array transformations.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/App.tsx`, `src/lib/taskTransitions.ts`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **State Snapshot** — apply it in the current file and explain its effect on user-visible behavior.

- **Functional Update** — apply it in the current file and explain its effect on user-visible behavior.

- **Immutability** — apply it in the current file and explain its effect on user-visible behavior.

- **Derived State** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Move the initial tasks into `useState` and keep filters as derived data rather than a second task array

Move the initial tasks into `useState` and keep filters as derived data rather than a second task array.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Write pure create, move and delete transition helpers before connecting buttons

Write pure create, move and delete transition helpers before connecting buttons.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Use functional state updates whenever the next value depends on the previous array

Use functional state updates whenever the next value depends on the previous array.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Inspect the agent diff for push, splice, direct property assignment and stale closure reads

Inspect the agent diff for push, splice, direct property assignment and stale closure reads.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Test two rapid moves, delete after filter, duplicate title and empty-column behavior

Test two rapid moves, delete after filter, duplicate title and empty-column behavior.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Explain why state behaves as a snapshot, then lint, type-check and build

Explain why state behaves as a snapshot, then lint, type-check and build.

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

Add task create, move-forward and delete behavior with useState. Use pure immutable transition helpers and functional updates. Do not store filtered tasks in state. Preserve stable IDs and status order. Include tests or console-free verification examples for transition edge cases.

```

## Read what the AI wrote

- **tasks.push mutates state.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Duplicated filtered state drifts.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **setTasks([...tasks]) uses stale closure.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Index used as identity.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects state snapshot, functional update, immutability, derived state to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. Each render sees a snapshot of state. Functional updates receive the latest committed value and immutable transformations give React a new reference to reconcile. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] Rapid updates are not lost.

- [ ] Original arrays are unchanged.

- [ ] Filter follows source state.

- [ ] Transitions stop at Done.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to state snapshot without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| tasks.push mutates state | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Duplicated filtered state drifts | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| setTasks([...tasks]) uses stale closure | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Index used as identity | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did state snapshot change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 3.1

Create, move and delete tasks with functional updates and immutable array transformations.
