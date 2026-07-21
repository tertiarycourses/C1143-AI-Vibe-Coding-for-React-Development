# Lab 4.5 — Build, Deploy and Demonstrate the Capstone

> **Topic 4** · approximately 40 minutes · builds on the previous lab checkpoint

## Goal

Produce and deploy a verified SprintBoard release with SPA routing, rollback instructions and an evidence-backed demonstration.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `dist/`, `docs/release-checklist.md`, `docs/release-notes.md`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **production build** — The optimized, minified output of npm run build — what users actually download.

- **SPA fallback** — Host configuration that serves index.html for unknown paths so client-side routes survive a direct refresh.

- **release gate** — A check — tests, lint, build, smoke test — that must pass before a release proceeds.

- **rollback** — A known-good state plus the steps to restore it when a change goes wrong.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Run clean install, test, lint, type-check and build from the documented commands

Run clean install, test, lint, type-check and build from the documented commands.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

### Step 2 — Choose an approved static host and configure the correct Vite base path and SPA fallback behavior

Choose an approved static host and configure the correct Vite base path and SPA fallback behavior.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

### Step 3 — Deploy `dist` through Git integration or the host workflow without exposing credentials

Deploy `dist` through Git integration or the host workflow without exposing credentials.

**Pause and inspect:** Predict which files this step should touch and what will change on screen; compare that prediction with the actual diff before moving on.

**Evidence:** Run the narrowest check that exercises this step first; only then run the wider lint, type-check and build stack.

### Step 4 — Open the public URL and verify board, form, filters, dynamic route, refresh, 404 and retry behavior

Open the public URL and verify board, form, filters, dynamic route, refresh, 404 and retry behavior.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

### Step 5 — Create release notes with features, evidence, limitations, known risks and exact rollback steps

Create release notes with features, evidence, limitations, known risks and exact rollback steps.

**Pause and inspect:** Keep the agent inside the declared file scope here — if its proposal reaches further, stop and narrow the request.

**Evidence:** Capture the command, expected result and actual result; if they differ, stop and investigate before the next step.

### Step 6 — Demonstrate the complete agentic loop using one final small improvement and show its plan, diff, tests and checkpoint

Demonstrate the complete agentic loop using one final small improvement and show its plan, diff, tests and checkpoint.

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

## Independent challenge

Change one constraint related to production build without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| Deploying untested dist | The build was deployed straight from a green compile. | Run the full gate — install, test, lint, type-check, build, preview — before deploying. |

| Direct route refresh returns 404 | The host has no SPA fallback for client-side routes. | Configure the rewrite to index.html and re-test a deep URL refresh. |

| Secrets included in VITE variables | VITE_-prefixed variables are compiled into the public bundle. | Remove the secret, rotate it, and keep only public configuration client-side. |

| No rollback target | The release replaced the previous version without a way back. | Record the last good commit or deploy id and the exact restore steps in the release notes. |

## Reflection

How did production build change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 4.5

Produce and deploy a verified SprintBoard release with SPA routing, rollback instructions and an evidence-backed demonstration.
