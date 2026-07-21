# Lab 4.2 — Test User Behaviour with Vitest and Testing Library

> **Topic 4** · approximately 45 minutes · builds on the previous lab checkpoint

## Goal

Build a focused test suite for rendering, filtering, task movement, forms and routes.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/test/setup.ts`, `src/App.test.tsx`, `src/components/TaskForm.test.tsx`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **test** — An automated check that drives behavior, asserts an observable result and fails loudly when that behavior regresses.

- **assertion** — A single expected-versus-actual claim inside a test; when it fails, it names precisely what broke.

- **user event** — A simulated interaction — typing, clicking, tabbing — that drives tests through the same paths a person uses.

- **accessible query** — Finding elements by role and accessible name, so tests verify what assistive technology can perceive.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Install Vitest, jsdom, Testing Library, jest-dom and user-event; pin and record versions

Install Vitest, jsdom, Testing Library, jest-dom and user-event; pin and record versions.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

### Step 2 — Configure the test environment and add an explicit `test` script

Configure the test environment and add an explicit `test` script.

**Pause and inspect:** Keep the agent inside the declared file scope here — if its proposal reaches further, stop and narrow the request.

**Evidence:** Capture the command, expected result and actual result; if they differ, stop and investigate before the next step.

### Step 3 — Write a smoke test using role and accessible-name queries rather than CSS selectors

Write a smoke test using role and accessible-name queries rather than CSS selectors.

**Pause and inspect:** Where the agent acts, read its output as a reviewer, not a spectator, and note one specific thing you checked.

**Evidence:** If this step touches the interface, re-test at both a narrow and a wide viewport and note anything that clips or overflows.

### Step 4 — Add behaviour tests for filtering, valid/invalid form submit and moving a task

Add behaviour tests for filtering, valid/invalid form submit and moving a task.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

### Step 5 — Add a MemoryRouter test for task details and not-found behavior

Add a MemoryRouter test for task details and not-found behavior.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

### Step 6 — Run tests in watch and single-run modes; inspect generated assertions for false confidence

Run tests in watch and single-run modes; inspect generated assertions for false confidence.

**Pause and inspect:** Predict which files this step should touch and what will change on screen; compare that prediction with the actual diff before moving on.

**Evidence:** Run the narrowest check that exercises this step first; only then run the wider lint, type-check and build stack.

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

## Independent challenge

Change one constraint related to test without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| Testing internal state | Asserting on hook variables felt more precise than the UI. | Rewrite assertions against what the user sees, via accessible queries. |

| fireEvent used for realistic typing | fireEvent skips the keyboard events real typing produces. | Use user-event's type and click helpers and await them. |

| Assertions pass without awaiting user events | The assertion ran before the interaction finished. | await every user-event call and prove the test can fail by breaking the code. |

| Snapshot replaces behavior checks | A snapshot asserted everything and therefore nothing specific. | Replace it with targeted role/name assertions for the flows that matter. |

## Reflection

How did test change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 4.2

Build a focused test suite for rendering, filtering, task movement, forms and routes.
