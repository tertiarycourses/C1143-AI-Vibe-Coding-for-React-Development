# Lab 1.3 — Write a Testable Product Brief and Acceptance Criteria

> **Topic 1** · approximately 35 minutes · builds on the previous lab checkpoint

## Goal

Turn a vague app idea into a bounded SprintBoard brief, non-goals, risks and observable acceptance checks.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `docs/product-brief.md`, `docs/acceptance.md`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Problem Framing** — apply it in the current file and explain its effect on user-visible behavior.

- **Acceptance Criteria** — apply it in the current file and explain its effect on user-visible behavior.

- **Non-Goals** — apply it in the current file and explain its effect on user-visible behavior.

- **Vertical Slice** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Describe the adult learner persona and the problem SprintBoard solves in two sentences

Describe the adult learner persona and the problem SprintBoard solves in two sentences.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Define the first vertical slice: view synthetic tasks grouped by To Do, Doing and Done

Define the first vertical slice: view synthetic tasks grouped by To Do, Doing and Done.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Write five acceptance criteria beginning with an observable verb such as displays, moves, filters, or reports

Write five acceptance criteria beginning with an observable verb such as displays, moves, filters, or reports.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Add non-goals: accounts, payments, real-time sync, production customer data, and backend persistence

Add non-goals: accounts, payments, real-time sync, production customer data, and backend persistence.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Ask the agent to challenge ambiguity and identify edge cases without proposing code

Ask the agent to challenge ambiguity and identify edge cases without proposing code.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Revise the brief, inspect the documentation diff, and checkpoint it before implementation

Revise the brief, inspect the documentation diff, and checkpoint it before implementation.

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

Act as a skeptical product engineer. Review docs/product-brief.md and docs/acceptance.md without editing. Find ambiguous words, missing states, hidden dependencies and acceptance checks that are not observable. Return a corrected proposal and a risk list.

```

## Read what the AI wrote

- **Starting code before agreeing behavior.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Acceptance criteria based on implementation.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Scope expanding into a backend.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Using real employee data.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects problem framing, acceptance criteria, non-goals, vertical slice to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. AI amplifies ambiguity. A narrow vertical slice and observable criteria give both the agent and the learner a shared definition of done. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] Criteria are observable.

- [ ] Non-goals are explicit.

- [ ] Loading/empty/error states are named.

- [ ] No code was generated.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to problem framing without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| Starting code before agreeing behavior | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Acceptance criteria based on implementation | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Scope expanding into a backend | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Using real employee data | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did problem framing change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 1.3

Turn a vague app idea into a bounded SprintBoard brief, non-goals, risks and observable acceptance checks.
