# Lab 4.4 — Profile, Refactor and Document Production Code

> **Topic 4** · approximately 45 minutes · builds on the previous lab checkpoint

## Goal

Use measurements to improve unnecessary rendering, bundle quality and maintainability without premature optimization.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `docs/performance-log.md`, `README.md`, `src/components/TaskCard.tsx`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Profiler** — apply it in the current file and explain its effect on user-visible behavior.

- **Memoization** — apply it in the current file and explain its effect on user-visible behavior.

- **Bundle Warning** — apply it in the current file and explain its effect on user-visible behavior.

- **Documentation** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Record a React DevTools Profiler trace while filtering and moving tasks; identify the actual expensive path

Record a React DevTools Profiler trace while filtering and moving tasks; identify the actual expensive path.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Ask the agent to explain the measurement and propose options before adding memoization

Ask the agent to explain the measurement and propose options before adding memoization.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Apply one targeted optimization only if the trace shows meaningful avoidable work

Apply one targeted optimization only if the trace shows meaningful avoidable work.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Run a production build and inspect warnings, asset sizes and source-map policy

Run a production build and inspect warnings, asset sizes and source-map policy.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Remove debug logs, dead code and obsolete comments; add concise component and setup documentation

Remove debug logs, dead code and obsolete comments; add concise component and setup documentation.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Compare profiler evidence and bundle output before and after; revert changes without measurable benefit

Compare profiler evidence and bundle output before and after; revert changes without measurable benefit.

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

Use the profiler evidence and build output I provide. Identify measured bottlenecks and propose the smallest improvement. Do not add memo/useMemo/useCallback by default. Explain trade-offs, then update README setup, architecture, commands, limitations and rollback notes.

```

## Read what the AI wrote

- **Memoizing everything.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Optimizing without a baseline.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Console logs ship to production.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **README commands do not match package.json.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects profiler, memoization, bundle warning, documentation to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. Optimization is an experiment. Measurements define the problem, and before/after evidence decides whether added complexity is justified. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] Change has measured benefit or is reverted.

- [ ] Build has no unexplained warning.

- [ ] README is reproducible.

- [ ] No debug output remains.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to profiler without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| Memoizing everything | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Optimizing without a baseline | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Console logs ship to production | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| README commands do not match package.json | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did profiler change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 4.4

Use measurements to improve unnecessary rendering, bundle quality and maintainability without premature optimization.
