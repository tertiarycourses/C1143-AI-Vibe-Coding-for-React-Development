# Lab 4.1 — Run an Evidence-Led Debugging Loop

> **Topic 4** · approximately 40 minutes · builds on the previous lab checkpoint

## Goal

Reproduce, isolate and fix a controlled stale-state defect with a minimal reviewed patch.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/hooks/useTaskBoard.ts`, `docs/debug-log.md`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Reproduction** — apply it in the current file and explain its effect on user-visible behavior.

- **Hypothesis** — apply it in the current file and explain its effect on user-visible behavior.

- **Root Cause** — apply it in the current file and explain its effect on user-visible behavior.

- **Minimal Patch** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Create a branch and introduce a controlled defect that loses one of two rapid task moves

Create a branch and introduce a controlled defect that loses one of two rapid task moves.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Write exact reproduction steps, expected result, actual result and evidence in the debug log

Write exact reproduction steps, expected result, actual result and evidence in the debug log.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Ask the agent for three ranked hypotheses and the smallest experiment for each; do not request a fix yet

Ask the agent for three ranked hypotheses and the smallest experiment for each; do not request a fix yet.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Run the experiments, identify the stale closure, and approve one functional-update patch

Run the experiments, identify the stale closure, and approve one functional-update patch.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Inspect the diff for unrelated refactors and add a regression test before accepting

Inspect the diff for unrelated refactors and add a regression test before accepting.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Run the complete verification stack and document why the original code failed

Run the complete verification stack and document why the original code failed.

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

Diagnose only. Given this reproduction and the relevant hook, propose three ranked hypotheses, evidence for/against each, and the smallest experiment. Do not edit until I confirm the root cause. After confirmation, propose one minimal patch and one regression test.

```

## Read what the AI wrote

- **Agent rewrites the hook.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Symptom patched without root cause.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Reproduction not repeatable.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Regression test omitted.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects reproduction, hypothesis, root cause, minimal patch to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. Debugging converts uncertainty into evidence. Separating hypothesis from mutation prevents an AI agent from masking the symptom with a broad rewrite. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] Defect fails before fix.

- [ ] One hypothesis is proven.

- [ ] Patch is minimal.

- [ ] Regression test passes.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to reproduction without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| Agent rewrites the hook | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Symptom patched without root cause | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Reproduction not repeatable | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Regression test omitted | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did reproduction change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 4.1

Reproduce, isolate and fix a controlled stale-state defect with a minimal reviewed patch.
