# Lab 3.1 — Manage Immutable Task State with useState

> **Topic 3** · approximately 40 minutes · builds on the previous lab checkpoint

## Goal

Create, move and delete tasks with functional updates and immutable array transformations.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/App.tsx`, `src/lib/taskTransitions.ts`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **state snapshot** — The fixed value of state a component sees during one render; updates schedule a new render rather than changing the current one.

- **functional update** — Passing a function to a state setter so the update is computed from the latest committed value, not a stale closure.

- **immutability** — Creating new objects and arrays instead of modifying existing ones, so React can detect changes by reference.

- **derived state** — Values computed from existing state during render — such as a filtered list — rather than stored separately.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Move the initial tasks into `useState` and keep filters as derived data rather than a second task array

Move the initial tasks into `useState` and keep filters as derived data rather than a second task array.

**Pause and inspect:** Keep the agent inside the declared file scope here — if its proposal reaches further, stop and narrow the request.

**Evidence:** Capture the command, expected result and actual result; if they differ, stop and investigate before the next step.

### Step 2 — Write pure create, move and delete transition helpers before connecting buttons

Write pure create, move and delete transition helpers before connecting buttons.

**Pause and inspect:** Where the agent acts, read its output as a reviewer, not a spectator, and note one specific thing you checked.

**Evidence:** If this step touches the interface, re-test at both a narrow and a wide viewport and note anything that clips or overflows.

### Step 3 — Use functional state updates whenever the next value depends on the previous array

Use functional state updates whenever the next value depends on the previous array.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

### Step 4 — Inspect the agent diff for push, splice, direct property assignment and stale closure reads

Inspect the agent diff for push, splice, direct property assignment and stale closure reads.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

### Step 5 — Test two rapid moves, delete after filter, duplicate title and empty-column behavior

Test two rapid moves, delete after filter, duplicate title and empty-column behavior.

**Pause and inspect:** Predict which files this step should touch and what will change on screen; compare that prediction with the actual diff before moving on.

**Evidence:** Run the narrowest check that exercises this step first; only then run the wider lint, type-check and build stack.

### Step 6 — Explain why state behaves as a snapshot, then lint, type-check and build

Explain why state behaves as a snapshot, then lint, type-check and build.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

## Agentic AI loop

### 1. Frame

State one observable goal, the current checkpoint, exact file scope, non-goals and stop conditions.

### 2. Plan

Require assumptions, numbered steps, files, risks, verification and rollback. Do not authorize code yet.

### 3. Generate

Approve one bounded increment. Keep the development server visible and do not combine refactoring with behavior change.

### 4. Inspect

Compare the plan and diff with the brief. Reject unrelated dependencies, architecture changes, secret handling or untestable claims.

### 5. Verify

Run commands yourself and exercise normal, boundary, empty and failure paths in the browser.

### 6. Correct

Read every changed line, explain data flow, and request the smallest correction backed by a failing check.

### 7. Commit

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

## Independent challenge

Change one constraint related to state snapshot without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| tasks.push mutates state | push mutates in place — the habit most familiar from plain JavaScript. | Use spread or concat to build a new array, then re-run the movement tests. |

| Duplicated filtered state drifts | The filtered list was stored as a second state variable. | Delete the copy and derive visibleTasks during render. |

| setTasks([...tasks]) uses stale closure | The update read the tasks captured at render time, losing rapid consecutive updates. | Switch to the functional form setTasks(prev => ...). |

| Index used as identity | Position stood in for identity inside the transition helpers. | Look items up by stable id in every create, move and delete helper. |

## Reflection

How did state snapshot change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 3.1

Create, move and delete tasks with functional updates and immutable array transformations.
