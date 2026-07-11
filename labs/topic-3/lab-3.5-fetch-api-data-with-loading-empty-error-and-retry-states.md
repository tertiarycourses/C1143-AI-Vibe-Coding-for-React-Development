# Lab 3.5 — Fetch API Data with Loading, Empty, Error and Retry States

> **Topic 3** · approximately 50 minutes · builds on the previous lab checkpoint

## Goal

Replace local seed data with a controlled fetch pipeline and resilient user-visible states.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `public/tasks.json`, `src/hooks/useTasksApi.ts`, `src/components/AsyncState.tsx`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Fetch** — apply it in the current file and explain its effect on user-visible behavior.

- **Response.Ok** — apply it in the current file and explain its effect on user-visible behavior.

- **Abortcontroller** — apply it in the current file and explain its effect on user-visible behavior.

- **State Machine** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Create a local JSON endpoint with synthetic tasks so the lab needs no credentials

Create a local JSON endpoint with synthetic tasks so the lab needs no credentials.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Model idle/loading/success/empty/error rather than a single ambiguous boolean

Model idle/loading/success/empty/error rather than a single ambiguous boolean.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Fetch inside an effect, check `response

Fetch inside an effect, check `response.ok`, validate the payload and abort on cleanup.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Expose a retry action and a useful error message without leaking stack traces

Expose a retry action and a useful error message without leaking stack traces.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Test normal data, empty array, invalid JSON, 404 path, slow network and component unmount

Test normal data, empty array, invalid JSON, 404 path, slow network and component unmount.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Inspect for requests during render, missing cleanup, swallowed errors and endless spinner

Inspect for requests during render, missing cleanup, swallowed errors and endless spinner.

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

Create useTasksApi for /tasks.json with loading, success, empty and error states, response.ok checking, runtime shape validation, AbortController cleanup and retry. Keep synthetic data local and show accessible status messages. Do not hide errors or fetch during render.

```

## Read what the AI wrote

- **fetch during render.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **No response.ok check.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Abort reported as user error.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Error leaves loading true forever.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects fetch, response.ok, AbortController, state machine to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. A network request is a state machine, not a value. Explicit states prevent stale content, endless spinners and blank screens when the happy path fails. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] All four visible states work.

- [ ] Retry recovers.

- [ ] Unmount aborts request.

- [ ] No credentials are required.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to fetch without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| fetch during render | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| No response.ok check | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Abort reported as user error | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Error leaves loading true forever | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did fetch change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 3.5

Replace local seed data with a controlled fetch pipeline and resilient user-visible states.
