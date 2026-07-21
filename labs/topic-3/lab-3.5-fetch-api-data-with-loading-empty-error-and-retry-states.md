# Lab 3.5 — Fetch API Data with Loading, Empty, Error and Retry States

> **Topic 3** · approximately 45 minutes · builds on the previous lab checkpoint

## Goal

Replace local seed data with a controlled fetch pipeline and resilient user-visible states.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `public/tasks.json`, `src/hooks/useTasksApi.ts`, `src/components/AsyncState.tsx`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **fetch** — The browser API that performs HTTP requests and resolves with a Response — rejecting only on network failure, not on HTTP error status.

- **response.ok** — The Response flag that is true only for 2xx status codes; skipping this check treats a 404 page as data.

- **AbortController** — The API that cancels an in-flight fetch, used in effect cleanup to prevent updates after unmount.

- **state machine** — Modeling a process as named states and transitions — idle, loading, success, empty, error — so no combination is ambiguous.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Create a local JSON endpoint with synthetic tasks so the lab needs no credentials

Create a local JSON endpoint with synthetic tasks so the lab needs no credentials.

**Pause and inspect:** Predict which files this step should touch and what will change on screen; compare that prediction with the actual diff before moving on.

**Evidence:** Run the narrowest check that exercises this step first; only then run the wider lint, type-check and build stack.

### Step 2 — Model idle/loading/success/empty/error rather than a single ambiguous boolean

Model idle/loading/success/empty/error rather than a single ambiguous boolean.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

### Step 3 — Fetch inside an effect, check `response.ok`, validate the payload and abort on cleanup

Fetch inside an effect, check `response.ok`, validate the payload and abort on cleanup.

**Pause and inspect:** Keep the agent inside the declared file scope here — if its proposal reaches further, stop and narrow the request.

**Evidence:** Capture the command, expected result and actual result; if they differ, stop and investigate before the next step.

### Step 4 — Expose a retry action and a useful error message without leaking stack traces

Expose a retry action and a useful error message without leaking stack traces.

**Pause and inspect:** Where the agent acts, read its output as a reviewer, not a spectator, and note one specific thing you checked.

**Evidence:** If this step touches the interface, re-test at both a narrow and a wide viewport and note anything that clips or overflows.

### Step 5 — Test normal data, empty array, invalid JSON, 404 path, slow network and component unmount

Test normal data, empty array, invalid JSON, 404 path, slow network and component unmount.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

### Step 6 — Inspect for requests during render, missing cleanup, swallowed errors and endless spinner

Inspect for requests during render, missing cleanup, swallowed errors and endless spinner.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

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

## Independent challenge

Change one constraint related to fetch without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| fetch during render | The request was issued in the component body, firing on every render. | Move the fetch into useEffect with correct dependencies and abort cleanup. |

| No response.ok check | fetch resolves on HTTP errors, so a 404 body was parsed as data. | Branch on response.ok and route failures to the error state. |

| Abort reported as user error | The AbortError raised by cleanup was caught by the generic error handler. | Detect AbortError and return silently instead of setting the error state. |

| Error leaves loading true forever | The failure path never transitioned the state machine. | Set an explicit error state — or use finally — and expose a retry action. |

## Reflection

How did fetch change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 3.5

Replace local seed data with a controlled fetch pipeline and resilient user-visible states.
