# Lab 2.1 — Model Tasks and Render Lists with Stable Keys

> **Topic 2** · approximately 40 minutes · builds on the previous lab checkpoint

## Goal

Create typed synthetic task data and render it predictably with map and stable identifiers.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/types.ts`, `src/data/tasks.ts`, `src/components/TaskList.tsx`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **TypeScript interface** — A named contract describing the shape of an object so the compiler can catch missing or mistyped fields.

- **map** — The array method that transforms each item into a new value — in React, into an element — without mutating the source array.

- **stable key** — An identifier tied to the data item rather than its position, so React can match list items between renders.

- **derived view** — Data computed from existing state during render instead of stored as a second copy that can drift.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Define `Task` with id, title, owner, status, points and priority; restrict status to a union

Define `Task` with id, title, owner, status, points and priority; restrict status to a union.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

### Step 2 — Create eight synthetic tasks with unique stable string IDs and no personal data

Create eight synthetic tasks with unique stable string IDs and no personal data.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

### Step 3 — Plan a TaskList that receives tasks through props and maps each item to visible output

Plan a TaskList that receives tasks through props and maps each item to visible output.

**Pause and inspect:** Predict which files this step should touch and what will change on screen; compare that prediction with the actual diff before moving on.

**Evidence:** Run the narrowest check that exercises this step first; only then run the wider lint, type-check and build stack.

### Step 4 — Generate the component, then inspect for `key={index}`, inline mutation and missing empty output

Generate the component, then inspect for `key={index}`, inline mutation and missing empty output.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

### Step 5 — Reorder the array and verify task identity remains correct; temporarily pass an empty array

Reorder the array and verify task identity remains correct; temporarily pass an empty array.

**Pause and inspect:** Keep the agent inside the declared file scope here — if its proposal reaches further, stop and narrow the request.

**Evidence:** Capture the command, expected result and actual result; if they differ, stop and investigate before the next step.

### Step 6 — Run type-check, lint and build; record why a database-style ID is safer than the array index

Run type-check, lint and build; record why a database-style ID is safer than the array index.

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

Create typed synthetic task data and a TaskList component. Use a Task interface, a status union, stable task.id keys, and a meaningful empty state. Do not add state or packages. Explain the key choice after showing the files changed.

```

## Read what the AI wrote

- **key={index}.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Duplicate IDs.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Rendering raw objects.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Mutating the source array during render.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects TypeScript interface, map, stable key, derived view to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. Keys are not display labels; they tell React which item is the same conceptual entity between renders. Stable identity prevents state and DOM from attaching to the wrong row. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] Eight tasks render.

- [ ] Empty state appears.

- [ ] Reorder preserves identity.

- [ ] Type-check passes.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Independent challenge

Change one constraint related to TypeScript interface without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| key={index} | The array index was the easiest unique-looking value at hand. | Key by task.id and re-test reordering to confirm identity is preserved. |

| Duplicate IDs | Hand-written synthetic data repeated an id after copy-paste. | Deduplicate the ids, then add a check that asserts uniqueness. |

| Rendering raw objects | A task object was interpolated directly into JSX, which React cannot render. | Render named fields such as task.title and task.owner instead. |

| Mutating the source array during render | sort or splice was called on the imported array inside the component. | Copy first — [...tasks].sort(...) — so the source data stays untouched. |

## Reflection

How did TypeScript interface change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 2.1

Create typed synthetic task data and render it predictably with map and stable identifiers.
