# Lab 3.3 — Extract a Tested Custom Hook

> **Topic 3** · approximately 35 minutes · builds on the previous lab checkpoint

## Goal

Separate reusable board logic into a custom hook without sharing state between consumers.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/hooks/useTaskBoard.ts`, `src/hooks/useTaskBoard.test.ts`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **custom hook** — A function starting with use that packages reusable stateful logic; each caller gets its own independent state.

- **logic reuse** — Sharing behavior between components by extracting hooks or functions, not by copying code.

- **public API** — The deliberate set of values and actions a hook or module exposes; everything else stays private.

- **hook test** — A test that exercises a hook through a consuming component or renderHook, asserting on outputs rather than internals.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — List the smallest public API: tasks, visibleTasks, filter, setFilter, create, move and remove

List the smallest public API: tasks, visibleTasks, filter, setFilter, create, move and remove.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

### Step 2 — Move stateful logic into `useTaskBoard` while keeping presentation in components

Move stateful logic into `useTaskBoard` while keeping presentation in components.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

### Step 3 — Inspect hook naming, top-level hook calls and dependency boundaries

Inspect hook naming, top-level hook calls and dependency boundaries.

**Pause and inspect:** Predict which files this step should touch and what will change on screen; compare that prediction with the actual diff before moving on.

**Evidence:** Run the narrowest check that exercises this step first; only then run the wider lint, type-check and build stack.

### Step 4 — Render two hook consumers and prove they do not share state unless state is lifted

Render two hook consumers and prove they do not share state unless state is lifted.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

### Step 5 — Add focused tests for initial state, filtering and immutable movement

Add focused tests for initial state, filtering and immutable movement.

**Pause and inspect:** Keep the agent inside the declared file scope here — if its proposal reaches further, stop and narrow the request.

**Evidence:** Capture the command, expected result and actual result; if they differ, stop and investigate before the next step.

### Step 6 — Refactor App to consume the hook; compare behavior before and after

Refactor App to consume the hook; compare behavior before and after.

**Pause and inspect:** Where the agent acts, read its output as a reviewer, not a spectator, and note one specific thing you checked.

**Evidence:** If this step touches the interface, re-test at both a narrow and a wide viewport and note anything that clips or overflows.

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

## Independent challenge

Change one constraint related to custom hook without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| Hook called conditionally | A hook was placed behind an if, breaking the rules-of-hooks ordering. | Move the hook to the top level and branch inside its logic instead. |

| Hook returns unstable unnecessary objects | A fresh object was returned each render, causing needless downstream work. | Return only what the API needs and stabilize values only where measurement shows a problem. |

| Custom hook assumed to create global shared state | Reuse of logic was confused with sharing one state instance. | Demonstrate two independent consumers, then lift state to a common owner if sharing is required. |

| Presentation markup moved into logic hook | The extraction dragged JSX along with the state. | Return data and actions from the hook; keep rendering in components. |

## Reflection

How did custom hook change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 3.3

Separate reusable board logic into a custom hook without sharing state between consumers.
