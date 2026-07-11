# Lab 3.2 — Synchronize and Clean Up Effects

> **Topic 3** · approximately 45 minutes · builds on the previous lab checkpoint

## Goal

Persist tasks locally with guarded parsing and understand effect dependencies and cleanup.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/hooks/usePersistentTasks.ts`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Useeffect** — apply it in the current file and explain its effect on user-visible behavior.

- **Dependency** — apply it in the current file and explain its effect on user-visible behavior.

- **Cleanup** — apply it in the current file and explain its effect on user-visible behavior.

- **Localstorage** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Define the external system: one versioned localStorage key containing synthetic task JSON

Define the external system: one versioned localStorage key containing synthetic task JSON.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Create a lazy state initializer that reads once and falls back safely on missing or malformed data

Create a lazy state initializer that reads once and falls back safely on missing or malformed data.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Add a save effect whose dependency reflects the value being synchronized

Add a save effect whose dependency reflects the value being synchronized.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Inspect StrictMode behavior and ensure the effect is idempotent rather than disabled

Inspect StrictMode behavior and ensure the effect is idempotent rather than disabled.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Test reload, cleared storage, malformed JSON, schema mismatch and storage write failure

Test reload, cleared storage, malformed JSON, schema mismatch and storage write failure.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Ask the agent to explain every dependency; reject lint suppression as a fix

Ask the agent to explain every dependency; reject lint suppression as a fix.

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

Extract usePersistentTasks. Read localStorage with a lazy initializer, validate parsed data, fall back to provided initial tasks, and save when tasks change. Use one versioned key. Do not suppress exhaustive-deps. Explain StrictMode behavior and all failure paths.

```

## Read what the AI wrote

- **Effect reads and writes in a loop.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **JSON.parse crash blanks the app.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Lint rule disabled.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Storage treated as secure.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects useEffect, dependency, cleanup, localStorage to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. Effects synchronize React with systems outside React. Dependencies describe the reactive values used by that synchronization; cleanup or idempotence prevents duplicate external work. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] Reload restores tasks.

- [ ] Malformed data recovers.

- [ ] No effect loop.

- [ ] Dependencies can be explained.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to useEffect without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| Effect reads and writes in a loop | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| JSON.parse crash blanks the app | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Lint rule disabled | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Storage treated as secure | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did useEffect change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 3.2

Persist tasks locally with guarded parsing and understand effect dependencies and cleanup.
