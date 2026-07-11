# Lab 2.1 — Model Tasks and Render Lists with Stable Keys

> **Topic 2** · approximately 40 minutes · builds on the previous lab checkpoint

## Goal

Create typed synthetic task data and render it predictably with map and stable identifiers.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/types.ts`, `src/data/tasks.ts`, `src/components/TaskList.tsx`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Typescript Interface** — apply it in the current file and explain its effect on user-visible behavior.

- **Map** — apply it in the current file and explain its effect on user-visible behavior.

- **Stable Key** — apply it in the current file and explain its effect on user-visible behavior.

- **Derived View** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Define `Task` with id, title, owner, status, points and priority; restrict status to a union

Define `Task` with id, title, owner, status, points and priority; restrict status to a union.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Create eight synthetic tasks with unique stable string IDs and no personal data

Create eight synthetic tasks with unique stable string IDs and no personal data.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Plan a TaskList that receives tasks through props and maps each item to visible output

Plan a TaskList that receives tasks through props and maps each item to visible output.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Generate the component, then inspect for `key={index}`, inline mutation and missing empty output

Generate the component, then inspect for `key={index}`, inline mutation and missing empty output.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Reorder the array and verify task identity remains correct; temporarily pass an empty array

Reorder the array and verify task identity remains correct; temporarily pass an empty array.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Run type-check, lint and build; record why a database-style ID is safer than the array index

Run type-check, lint and build; record why a database-style ID is safer than the array index.

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

## Your turn

Change one constraint related to TypeScript interface without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| key={index} | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Duplicate IDs | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Rendering raw objects | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Mutating the source array during render | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did TypeScript interface change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 2.1

Create typed synthetic task data and render it predictably with map and stable identifiers.
