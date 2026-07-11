# Lab 1.4 — Engineer a Plan–Diff–Verify Prompt Contract

> **Topic 1** · approximately 40 minutes · builds on the previous lab checkpoint

## Goal

Create reusable prompt and review templates that force planning, bounded edits and verification evidence.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `docs/prompt-template.md`, `docs/review-checklist.md`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Context Engineering** — apply it in the current file and explain its effect on user-visible behavior.

- **Bounded Change** — apply it in the current file and explain its effect on user-visible behavior.

- **Diff Review** — apply it in the current file and explain its effect on user-visible behavior.

- **Rollback** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Create a prompt template with Goal, Context, Constraints, Deliverables, Verification and Stop Conditions

Create a prompt template with Goal, Context, Constraints, Deliverables, Verification and Stop Conditions.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Create a review checklist covering file scope, dependencies, types, accessibility, errors, secrets and tests

Create a review checklist covering file scope, dependencies, types, accessibility, errors, secrets and tests.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Ask the agent to plan the SprintBoard shell and name every file it would change; do not authorize implementation

Ask the agent to plan the SprintBoard shell and name every file it would change; do not authorize implementation.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Compare the plan to the product brief; reject any unrequested package or architecture

Compare the plan to the product brief; reject any unrequested package or architecture.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Authorize one small increment and require the agent to summarize the resulting diff

Authorize one small increment and require the agent to summarize the resulting diff.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Run the verification commands yourself; record keep, refine, or revert with the evidence

Run the verification commands yourself; record keep, refine, or revert with the evidence.

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

Goal: propose the smallest SprintBoard shell. Context: read the product brief and AGENTS.md. Constraints: no new dependencies and no implementation yet. Deliverables: numbered plan, exact file list, risks, verification commands and rollback point. Stop after the plan.

```

## Read what the AI wrote

- **Prompt asks for the entire app.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Agent silently adds a UI framework.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Summary replaces line-by-line diff review.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Passing build treated as complete evidence.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects context engineering, bounded change, diff review, rollback to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. The engineering loop separates intent, proposal, mutation and evidence. Each boundary gives the human a meaningful point to intervene. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] Plan names files.

- [ ] Risks and rollback exist.

- [ ] One increment is authorized.

- [ ] Decision is backed by commands and browser evidence.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to context engineering without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| Prompt asks for the entire app | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Agent silently adds a UI framework | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Summary replaces line-by-line diff review | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Passing build treated as complete evidence | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did context engineering change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 1.4

Create reusable prompt and review templates that force planning, bounded edits and verification evidence.
