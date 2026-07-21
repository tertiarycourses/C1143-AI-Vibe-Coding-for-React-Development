# Lab 1.4 — Engineer a Plan–Diff–Verify Prompt Contract

> **Topic 1** · approximately 35 minutes · builds on the previous lab checkpoint

## Goal

Create reusable prompt and review templates that force planning, bounded edits and verification evidence.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `docs/prompt-template.md`, `docs/review-checklist.md`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **context engineering** — Deliberately choosing what the agent reads — briefs, rules, named files — so its output is grounded in your constraints rather than its guesses.

- **bounded change** — A change restricted to named files and one behavior, small enough to review line by line.

- **diff review** — Reading the exact line-level changes between repository states before accepting them.

- **rollback** — A known-good state plus the steps to restore it when a change goes wrong.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Create a prompt template with Goal, Context, Constraints, Deliverables, Verification and Stop Conditions

Create a prompt template with Goal, Context, Constraints, Deliverables, Verification and Stop Conditions.

**Pause and inspect:** Where the agent acts, read its output as a reviewer, not a spectator, and note one specific thing you checked.

**Evidence:** If this step touches the interface, re-test at both a narrow and a wide viewport and note anything that clips or overflows.

### Step 2 — Create a review checklist covering file scope, dependencies, types, accessibility, errors, secrets and tests

Create a review checklist covering file scope, dependencies, types, accessibility, errors, secrets and tests.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

### Step 3 — Ask the agent to plan the SprintBoard shell and name every file it would change; do not authorize implementation

Ask the agent to plan the SprintBoard shell and name every file it would change; do not authorize implementation.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

### Step 4 — Compare the plan to the product brief; reject any unrequested package or architecture

Compare the plan to the product brief; reject any unrequested package or architecture.

**Pause and inspect:** Predict which files this step should touch and what will change on screen; compare that prediction with the actual diff before moving on.

**Evidence:** Run the narrowest check that exercises this step first; only then run the wider lint, type-check and build stack.

### Step 5 — Authorize one small increment and require the agent to summarize the resulting diff

Authorize one small increment and require the agent to summarize the resulting diff.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

### Step 6 — Run the verification commands yourself; record keep, refine, or revert with the evidence

Run the verification commands yourself; record keep, refine, or revert with the evidence.

**Pause and inspect:** Keep the agent inside the declared file scope here — if its proposal reaches further, stop and narrow the request.

**Evidence:** Capture the command, expected result and actual result; if they differ, stop and investigate before the next step.

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

## Independent challenge

Change one constraint related to context engineering without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| Prompt asks for the entire app | An unbounded goal invites an unreviewable thousand-line response. | Split the request into one increment with named files and stop conditions. |

| Agent silently adds a UI framework | The plan was approved from its summary, not its dependency list. | Reject the diff, forbid new dependencies in the constraints, and re-request the plan. |

| Summary replaces line-by-line diff review | The agent's fluent description felt equivalent to reading the change. | Open the actual diff and explain each hunk yourself before accepting. |

| Passing build treated as complete evidence | A compiling app was mistaken for a correct app. | Run the acceptance checks in the browser and record what you observed. |

## Reflection

How did context engineering change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 1.4

Create reusable prompt and review templates that force planning, bounded edits and verification evidence.
