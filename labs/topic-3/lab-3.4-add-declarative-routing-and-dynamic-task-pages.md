# Lab 3.4 — Add Declarative Routing and Dynamic Task Pages

> **Topic 3** · approximately 45 minutes · builds on the previous lab checkpoint

## Goal

Create board, task detail, about and not-found routes with accessible navigation.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/router.tsx`, `src/pages/BoardPage.tsx`, `src/pages/TaskPage.tsx`, `src/pages/NotFoundPage.tsx`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Url As State** — apply it in the current file and explain its effect on user-visible behavior.

- **Route** — apply it in the current file and explain its effect on user-visible behavior.

- **Dynamic Parameter** — apply it in the current file and explain its effect on user-visible behavior.

- **Navigation** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Install the current React Router package and record the version and command

Install the current React Router package and record the version and command.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Plan route objects for `/`, `/tasks/:taskId`, `/about` and a catch-all page

Plan route objects for `/`, `/tasks/:taskId`, `/about` and a catch-all page.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Create a shared layout with navigation and an outlet for child pages

Create a shared layout with navigation and an outlet for child pages.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Link each TaskCard to its detail URL; read the parameter and handle an unknown ID

Link each TaskCard to its detail URL; read the parameter and handle an unknown ID.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Test links, browser back/forward, direct URL entry, refresh and keyboard focus after navigation

Test links, browser back/forward, direct URL entry, refresh and keyboard focus after navigation.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Inspect for anchor misuse, imperative navigation where Link is clearer, and blank not-found output

Inspect for anchor misuse, imperative navigation where Link is clearer, and blank not-found output.

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

Add React Router in data/declarative configuration for board, task detail, about and not-found pages. Use links for user navigation, a shared layout, a dynamic taskId parameter and a useful unknown-task state. Preserve the task hook and avoid unrelated CSS rewrites.

```

## Read what the AI wrote

- **Using window.location for internal navigation.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Missing not-found route.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Unknown ID crashes.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Direct refresh fails in deployment.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects URL as state, route, dynamic parameter, navigation to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. Client-side routing maps the URL to a component tree. Dynamic segments make resource identity shareable and recoverable through the address bar. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] All routes render.

- [ ] Back/forward works.

- [ ] Unknown task is handled.

- [ ] Direct URLs are documented for hosting.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to URL as state without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| Using window.location for internal navigation | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Missing not-found route | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Unknown ID crashes | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Direct refresh fails in deployment | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did URL as state change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 3.4

Create board, task detail, about and not-found routes with accessible navigation.
