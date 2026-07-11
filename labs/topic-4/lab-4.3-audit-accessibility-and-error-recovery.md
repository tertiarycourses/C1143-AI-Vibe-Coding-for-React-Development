# Lab 4.3 — Audit Accessibility and Error Recovery

> **Topic 4** · approximately 40 minutes · builds on the previous lab checkpoint

## Goal

Perform keyboard, semantics, focus, contrast and recovery checks and fix only evidenced defects.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `docs/accessibility-audit.md`, `src/components/AsyncState.tsx`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Keyboard Access** — apply it in the current file and explain its effect on user-visible behavior.

- **Focus Management** — apply it in the current file and explain its effect on user-visible behavior.

- **Live Region** — apply it in the current file and explain its effect on user-visible behavior.

- **Error Recovery** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Navigate the complete app using only Tab, Shift+Tab, Enter, Space and browser back

Navigate the complete app using only Tab, Shift+Tab, Enter, Space and browser back.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Inspect landmarks, heading order, control names and error announcements in the accessibility tree

Inspect landmarks, heading order, control names and error announcements in the accessibility tree.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Check contrast, 200 percent zoom, narrow viewport and prefers-reduced-motion

Check contrast, 200 percent zoom, narrow viewport and prefers-reduced-motion.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Trigger form and network errors; verify focus and retry guidance lead to recovery

Trigger form and network errors; verify focus and retry guidance lead to recovery.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Ask the agent to rank findings by user impact and propose one file-scoped patch per finding

Ask the agent to rank findings by user impact and propose one file-scoped patch per finding.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Retest each corrected behavior and record evidence rather than marking a generic compliance checkbox

Retest each corrected behavior and record evidence rather than marking a generic compliance checkbox.

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

Review the supplied accessibility evidence and relevant components. Rank concrete defects by user impact. For each, name the standard interaction that fails, exact file, minimal patch and manual retest. Do not claim compliance and do not change visual style without evidence.

```

## Read what the AI wrote

- **Automated scan treated as complete.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Focus indicator removed.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Error appears visually but is not announced.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Color-only status.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects keyboard access, focus management, live region, error recovery to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. Accessibility is observable interaction quality. Automated tools find only part of the problem; keyboard and assistive-technology semantics require human verification. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] All controls work by keyboard.

- [ ] Errors are announced.

- [ ] Focus remains visible.

- [ ] Zoom and narrow width remain usable.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to keyboard access without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| Automated scan treated as complete | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Focus indicator removed | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Error appears visually but is not announced | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Color-only status | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did keyboard access change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 4.3

Perform keyboard, semantics, focus, contrast and recovery checks and fix only evidenced defects.
