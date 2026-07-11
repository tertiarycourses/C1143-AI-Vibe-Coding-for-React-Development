# Lab 1.5 — Build and Review the First React Screen

> **Topic 1** · approximately 45 minutes · builds on the previous lab checkpoint

## Goal

Replace the starter content with a semantic SprintBoard shell while reviewing every generated line.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/App.tsx`, `src/App.css`, `src/index.css`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Function Component** — apply it in the current file and explain its effect on user-visible behavior.

- **Jsx** — apply it in the current file and explain its effect on user-visible behavior.

- **Semantic Html** — apply it in the current file and explain its effect on user-visible behavior.

- **Component Tree** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Approve a shell containing header, navigation, main board region and footer; keep content synthetic

Approve a shell containing header, navigation, main board region and footer; keep content synthetic.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Ask the agent to implement only `App

Ask the agent to implement only `App.tsx` and focused CSS, preserving the Vite entry point.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Read the JSX aloud as a tree and identify every opening/closing tag and expression boundary

Read the JSX aloud as a tree and identify every opening/closing tag and expression boundary.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Inspect the diff for removed defaults, global CSS leakage, inaccessible navigation, or unexplained assets

Inspect the diff for removed defaults, global CSS leakage, inaccessible navigation, or unexplained assets.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Run dev, lint and build; inspect the console and browser at 375 px and 1280 px

Run dev, lint and build; inspect the console and browser at 375 px and 1280 px.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Commit only after the screen matches the brief and the learner can explain every changed line

Commit only after the screen matches the brief and the learner can explain every changed line.

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

Implement only the approved SprintBoard shell in src/App.tsx, src/App.css and src/index.css. Use semantic header/nav/main/footer elements, TypeScript-safe JSX, no new packages, and responsive CSS. Show the diff summary and verification commands when finished.

```

## Read what the AI wrote

- **Nested interactive elements.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Decorative divs instead of semantic landmarks.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Global wildcard styles with side effects.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Unexplained generated SVG or dependency.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects function component, JSX, semantic HTML, component tree to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. JSX is a declarative description of the interface. React evaluates the component function and reconciles its returned element tree with the browser DOM. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] Landmarks are present.

- [ ] No console errors.

- [ ] Lint and build pass.

- [ ] 375 px and 1280 px views remain usable.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to function component without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| Nested interactive elements | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Decorative divs instead of semantic landmarks | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Global wildcard styles with side effects | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Unexplained generated SVG or dependency | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did function component change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 1.5

Replace the starter content with a semantic SprintBoard shell while reviewing every generated line.
