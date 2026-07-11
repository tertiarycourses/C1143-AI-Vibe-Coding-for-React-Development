# Lab 2.5 — Generate Responsive and Accessible CSS

> **Topic 2** · approximately 40 minutes · builds on the previous lab checkpoint

## Goal

Create a robust visual system with tokens, responsive layout, focus visibility and reduced-motion support.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/index.css`, `src/App.css`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Custom Property** — apply it in the current file and explain its effect on user-visible behavior.

- **Grid** — apply it in the current file and explain its effect on user-visible behavior.

- **Focus-Visible** — apply it in the current file and explain its effect on user-visible behavior.

- **Media Query** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Inventory colors, spacing, type sizes and radii; convert repeated values into CSS custom properties

Inventory colors, spacing, type sizes and radii; convert repeated values into CSS custom properties.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Define a mobile-first single-column board and expand to three columns when space allows

Define a mobile-first single-column board and expand to three columns when space allows.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Add visible `:focus-visible` styles and confirm text/background contrast with browser tools

Add visible `:focus-visible` styles and confirm text/background contrast with browser tools.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Add overflow handling for long task titles and test browser zoom at 200 percent

Add overflow handling for long task titles and test browser zoom at 200 percent.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Respect `prefers-reduced-motion` for transitions introduced by the agent

Respect `prefers-reduced-motion` for transitions introduced by the agent.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Inspect the CSS diff for `!important`, fixed heights, horizontal scroll and low-contrast tokens

Inspect the CSS diff for `!important`, fixed heights, horizontal scroll and low-contrast tokens.

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

Refine SprintBoard CSS using custom properties and mobile-first layout. Requirements: usable at 320px and 1280px, visible focus, 200% zoom, long-title wrapping, no fixed card heights, sufficient contrast, and reduced-motion handling. Preserve semantic HTML and add no framework.

```

## Read what the AI wrote

- **Fixed pixel heights clip content.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Outline removed.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Desktop-first overflow.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Color is the only status cue.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects custom property, grid, focus-visible, media query to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. Responsive CSS adapts to available space rather than a device label. Accessibility is part of the component contract, not a polish pass after generation. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] 320 px has no horizontal scroll.

- [ ] 200% zoom remains usable.

- [ ] Focus is always visible.

- [ ] Reduced-motion preference is respected.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to custom property without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| Fixed pixel heights clip content | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Outline removed | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Desktop-first overflow | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Color is the only status cue | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did custom property change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 2.5

Create a robust visual system with tokens, responsive layout, focus visibility and reduced-motion support.
