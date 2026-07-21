# Lab 4.4 — Profile, Refactor and Document Production Code

> **Topic 4** · approximately 35 minutes · builds on the previous lab checkpoint

## Goal

Use measurements to improve unnecessary rendering, bundle quality and maintainability without premature optimization.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `docs/performance-log.md`, `README.md`, `src/components/TaskCard.tsx`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **profiler** — The React DevTools view that measures which components rendered, when and why.

- **memoization** — Caching a computation or component output for reuse while inputs are unchanged; a measured trade-off, not a default.

- **bundle warning** — Build output flagging oversized or misconfigured assets before users experience them.

- **documentation** — The README and inline notes that let a stranger install, run, verify and safely change the project.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Record a React DevTools Profiler trace while filtering and moving tasks; identify the actual expensive path

Record a React DevTools Profiler trace while filtering and moving tasks; identify the actual expensive path.

**Pause and inspect:** Where the agent acts, read its output as a reviewer, not a spectator, and note one specific thing you checked.

**Evidence:** If this step touches the interface, re-test at both a narrow and a wide viewport and note anything that clips or overflows.

### Step 2 — Ask the agent to explain the measurement and propose options before adding memoization

Ask the agent to explain the measurement and propose options before adding memoization.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

### Step 3 — Apply one targeted optimization only if the trace shows meaningful avoidable work

Apply one targeted optimization only if the trace shows meaningful avoidable work.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

### Step 4 — Run a production build and inspect warnings, asset sizes and source-map policy

Run a production build and inspect warnings, asset sizes and source-map policy.

**Pause and inspect:** Predict which files this step should touch and what will change on screen; compare that prediction with the actual diff before moving on.

**Evidence:** Run the narrowest check that exercises this step first; only then run the wider lint, type-check and build stack.

### Step 5 — Remove debug logs, dead code and obsolete comments; add concise component and setup documentation

Remove debug logs, dead code and obsolete comments; add concise component and setup documentation.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

### Step 6 — Compare profiler evidence and bundle output before and after; revert changes without measurable benefit

Compare profiler evidence and bundle output before and after; revert changes without measurable benefit.

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

## Independent challenge

Change one constraint related to profiler without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| Memoizing everything | memo and useMemo were sprinkled preventively without a baseline. | Remove unmeasured memoization; re-apply only where the profiler shows avoidable work. |

| Optimizing without a baseline | There was no before-trace to compare against. | Record a profiler trace first; keep only changes with measured benefit. |

| Console logs ship to production | Debug output was never scheduled for removal. | Strip the logs, rebuild, and inspect the production console. |

| README commands do not match package.json | Docs were written from memory, not from the scripts block. | Copy commands from package.json and run each one exactly as written. |

## Reflection

How did profiler change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 4.4

Use measurements to improve unnecessary rendering, bundle quality and maintainability without premature optimization.
