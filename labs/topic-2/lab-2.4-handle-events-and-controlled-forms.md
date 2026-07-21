# Lab 2.4 — Handle Events and Controlled Forms

> **Topic 2** · approximately 45 minutes · builds on the previous lab checkpoint

## Goal

Add a controlled task form with validation and explicit submit behavior.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/components/TaskForm.tsx`, `src/App.tsx`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **event handler** — A function passed to an element that React calls when the user acts, receiving a synthetic event object.

- **controlled input** — A form control whose value comes from React state, making state the single source of truth for what is displayed.

- **validation** — Checking user input against rules before it enters application state or triggers behavior.

- **preventDefault** — The event method that stops the browser's built-in behavior, such as a form submit reloading the page.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Define form fields and acceptance rules: nonblank title, owner placeholder, priority and points range

Define form fields and acceptance rules: nonblank title, owner placeholder, priority and points range.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

### Step 2 — Plan controlled state for each field and an `onCreate` callback owned by the parent

Plan controlled state for each field and an `onCreate` callback owned by the parent.

**Pause and inspect:** Keep the agent inside the declared file scope here — if its proposal reaches further, stop and narrow the request.

**Evidence:** Capture the command, expected result and actual result; if they differ, stop and investigate before the next step.

### Step 3 — Generate labels, inputs, select, error region and submit button using semantic form controls

Generate labels, inputs, select, error region and submit button using semantic form controls.

**Pause and inspect:** Where the agent acts, read its output as a reviewer, not a spectator, and note one specific thing you checked.

**Evidence:** If this step touches the interface, re-test at both a narrow and a wide viewport and note anything that clips or overflows.

### Step 4 — Inspect for missing labels, mutation, stale state, uncontrolled-to-controlled warnings and page reload

Inspect for missing labels, mutation, stale state, uncontrolled-to-controlled warnings and page reload.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

### Step 5 — Test keyboard-only completion, invalid title, boundary points, successful submit and form reset

Test keyboard-only completion, invalid title, boundary points, successful submit and form reset.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

### Step 6 — Run lint/build and use the accessibility tree to confirm label-control relationships

Run lint/build and use the accessibility tree to confirm label-control relationships.

**Pause and inspect:** Predict which files this step should touch and what will change on screen; compare that prediction with the actual diff before moving on.

**Evidence:** Run the narrowest check that exercises this step first; only then run the wider lint, type-check and build stack.

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

Build a typed controlled TaskForm. Use real label elements, preventDefault, trimmed title validation, points from 1 to 13, an accessible error message and onCreate callback. The parent owns the task array. Do not use a form library or mutate existing tasks.

```

## Read what the AI wrote

- **Button defaults reload the page.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Input lacks label.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Number remains a string.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Form clears even when validation fails.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects event handler, controlled input, validation, preventDefault to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. A controlled input makes React state the source of truth. Every keystroke updates state, and the rendered value always reflects that state. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] Invalid submit is blocked.

- [ ] Keyboard flow works.

- [ ] Valid task reaches parent callback.

- [ ] No console warnings.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Independent challenge

Change one constraint related to event handler without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| Button defaults reload the page | A button inside a form defaults to type submit, and preventDefault was missing. | Call event.preventDefault() in the submit handler and re-test with the network tab open. |

| Input lacks label | Placeholder text was mistaken for labeling. | Add a real label element tied via htmlFor and confirm the name in the accessibility tree. |

| Number remains a string | Input values are always strings; the conversion was skipped. | Parse with Number() and validate the range before calling onCreate. |

| Form clears even when validation fails | The reset ran unconditionally after submit. | Reset only on the success path so users keep what they typed. |

## Reflection

How did event handler change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 2.4

Add a controlled task form with validation and explicit submit behavior.
