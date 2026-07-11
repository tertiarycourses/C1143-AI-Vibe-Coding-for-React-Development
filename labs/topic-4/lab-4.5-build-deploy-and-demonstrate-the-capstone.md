# Lab 4.5 — Build, Deploy and Demonstrate the Capstone

> **Topic 4** · approximately 55 minutes · builds on the previous lab checkpoint

## Goal

Produce and deploy a verified SprintBoard release with SPA routing, rollback instructions and an evidence-backed demonstration.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `dist/`, `docs/release-checklist.md`, `docs/release-notes.md`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Production Build** — apply it in the current file and explain its effect on user-visible behavior.

- **Spa Fallback** — apply it in the current file and explain its effect on user-visible behavior.

- **Release Gate** — apply it in the current file and explain its effect on user-visible behavior.

- **Rollback** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Run clean install, test, lint, type-check and build from the documented commands

Run clean install, test, lint, type-check and build from the documented commands.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Choose an approved static host and configure the correct Vite base path and SPA fallback behavior

Choose an approved static host and configure the correct Vite base path and SPA fallback behavior.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Deploy `dist` through Git integration or the host workflow without exposing credentials

Deploy `dist` through Git integration or the host workflow without exposing credentials.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Open the public URL and verify board, form, filters, dynamic route, refresh, 404 and retry behavior

Open the public URL and verify board, form, filters, dynamic route, refresh, 404 and retry behavior.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Create release notes with features, evidence, limitations, known risks and exact rollback steps

Create release notes with features, evidence, limitations, known risks and exact rollback steps.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Demonstrate the complete agentic loop using one final small improvement and show its plan, diff, tests and checkpoint

Demonstrate the complete agentic loop using one final small improvement and show its plan, diff, tests and checkpoint.

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

Prepare a release plan only. Read package scripts and hosting target. List preflight commands, Vite base/SPA rewrite requirements, environment-variable handling, smoke tests, rollback method and stop conditions. Do not deploy or change external state until I approve.

```

## Read what the AI wrote

- **Deploying untested dist.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Direct route refresh returns 404.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Secrets included in VITE variables.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **No rollback target.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects production build, SPA fallback, release gate, rollback to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. A release is a controlled state transition. Gates prove readiness, smoke tests prove the target environment, and rollback limits the cost of a bad assumption. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] All release gates pass.

- [ ] Public routes survive refresh.

- [ ] No secret appears in bundle or repo.

- [ ] Rollback is documented and feasible.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to production build without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| Deploying untested dist | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Direct route refresh returns 404 | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Secrets included in VITE variables | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| No rollback target | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did production build change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 4.5

Produce and deploy a verified SprintBoard release with SPA routing, rollback instructions and an evidence-backed demonstration.
