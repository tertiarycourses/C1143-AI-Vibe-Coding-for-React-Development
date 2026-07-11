# React AI Vibe Coding for React Development — Learner Guide

- **Course Code:** C1143

- **Duration:** 15 hours / 2 days

- **Level:** Intermediate

## Agentic AI Loop

Specify → Plan → Inspect → Implement → Test → Critique → Refine → Checkpoint

## Topic 1: Getting Started with AI Vibe Coding for React

Set up an AI coding assistant, scaffold a React app from a prompt, and control generated work with an evidence-led engineering loop.

# Lab 1.1 — Prepare the Agentic React Workspace

> **Topic 1** · approximately 35 minutes · builds on nothing; this is the first checkpoint

## Goal

Verify Node, Git, VS Code and an approved coding agent; create a safe project folder and evidence log.

## The build so far

SprintBoard grows through one continuous sequence. Begin from nothing; this is the first checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `training-log/README.md`, `AGENTS.md`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Toolchain** — apply it in the current file and explain its effect on user-visible behavior.

- **Working Directory** — apply it in the current file and explain its effect on user-visible behavior.

- **Agent Scope** — apply it in the current file and explain its effect on user-visible behavior.

- **Evidence Trail** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Run `node -v`, `npm -v`, and `git --version`; record the outputs in `training-log/README

Run `node -v`, `npm -v`, and `git --version`; record the outputs in `training-log/README.md`.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Open a dedicated `sprintboard` parent folder in VS Code and confirm the integrated terminal starts in that folder

Open a dedicated `sprintboard` parent folder in VS Code and confirm the integrated terminal starts in that folder.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Choose Cursor, GitHub Copilot, Claude, or Codex; verify it can read only the folder you intentionally opened

Choose Cursor, GitHub Copilot, Claude, or Codex; verify it can read only the folder you intentionally opened.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Create `AGENTS

Create `AGENTS.md` with plan-first, named-file scope, no-secret, small-diff, and verification-before-acceptance rules.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Ask the agent to restate the rules and list what it is not allowed to do; correct any missing boundary

Ask the agent to restate the rules and list what it is not allowed to do; correct any missing boundary.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Create a baseline Git repository and inspect `git status --short` before the first checkpoint

Create a baseline Git repository and inspect `git status --short` before the first checkpoint.

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

Read AGENTS.md. Do not edit files. Restate the working agreement, identify the commands you will use to verify React changes, and list any assumptions you need me to confirm.

```

## Read what the AI wrote

- **Agent edits before planning.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Credentials copied into chat.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Tool versions asserted without terminal evidence.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Repository initialized in the wrong folder.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects toolchain, working directory, agent scope, evidence trail to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. A coding agent is safest when the repository carries durable constraints. Chat instructions disappear; project instructions travel with the code and can be reviewed like any other engineering artifact. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] Tool versions are recorded.

- [ ] AGENTS.md names scope and acceptance rules.

- [ ] The agent made no unapproved edit.

- [ ] Git status is understood.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to toolchain without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| Agent edits before planning | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Credentials copied into chat | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Tool versions asserted without terminal evidence | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Repository initialized in the wrong folder | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did toolchain change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 1.1

Verify Node, Git, VS Code and an approved coding agent; create a safe project folder and evidence log.


# Lab 1.2 — Scaffold SprintBoard with Vite and React

> **Topic 1** · approximately 40 minutes · builds on the previous lab checkpoint

## Goal

Create a Vite React TypeScript app, run the development server, and explain the boot sequence.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `index.html`, `src/main.tsx`, `src/App.tsx`, `package.json`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Vite** — apply it in the current file and explain its effect on user-visible behavior.

- **Module Graph** — apply it in the current file and explain its effect on user-visible behavior.

- **React Root** — apply it in the current file and explain its effect on user-visible behavior.

- **Hot Module Replacement** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Run `npm create vite@latest sprintboard -- --template react-ts`, enter the folder, and run `npm install`

Run `npm create vite@latest sprintboard -- --template react-ts`, enter the folder, and run `npm install`.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Start `npm run dev`; open the printed local URL and save a screenshot of the starter page

Start `npm run dev`; open the printed local URL and save a screenshot of the starter page.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Trace `index

Trace `index.html` to `src/main.tsx` to `<App />`; annotate the chain in the training log.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Ask the agent for a file-by-file explanation without requesting changes; compare it with the actual imports

Ask the agent for a file-by-file explanation without requesting changes; compare it with the actual imports.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Run `npm run build`, inspect `dist/`, then run `npm run preview` and explain how preview differs from dev

Run `npm run build`, inspect `dist/`, then run `npm run preview` and explain how preview differs from dev.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Review `git diff` and commit the untouched scaffold as `chore: scaffold SprintBoard`

Review `git diff` and commit the untouched scaffold as `chore: scaffold SprintBoard`.

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

Explain this Vite React TypeScript scaffold using the actual files. Trace exactly how index.html, main.tsx and App.tsx connect. Do not add packages or edit code. Finish with dev, build and preview verification commands.

```

## Read what the AI wrote

- **Using Create React App instructions.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Editing node_modules.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Confusing dev output with production output.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Inventing files not present in the scaffold.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects Vite, module graph, React root, Hot Module Replacement to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. Vite treats `index.html` as source and follows module imports from the entry script. React creates one root and renders the component tree into the root element. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] Dev server hot-reloads.

- [ ] Production build succeeds.

- [ ] Preview serves dist.

- [ ] Learner can explain the boot chain.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to Vite without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| Using Create React App instructions | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Editing node_modules | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Confusing dev output with production output | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Inventing files not present in the scaffold | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did Vite change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 1.2

Create a Vite React TypeScript app, run the development server, and explain the boot sequence.


# Lab 1.3 — Write a Testable Product Brief and Acceptance Criteria

> **Topic 1** · approximately 35 minutes · builds on the previous lab checkpoint

## Goal

Turn a vague app idea into a bounded SprintBoard brief, non-goals, risks and observable acceptance checks.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `docs/product-brief.md`, `docs/acceptance.md`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Problem Framing** — apply it in the current file and explain its effect on user-visible behavior.

- **Acceptance Criteria** — apply it in the current file and explain its effect on user-visible behavior.

- **Non-Goals** — apply it in the current file and explain its effect on user-visible behavior.

- **Vertical Slice** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Describe the adult learner persona and the problem SprintBoard solves in two sentences

Describe the adult learner persona and the problem SprintBoard solves in two sentences.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Define the first vertical slice: view synthetic tasks grouped by To Do, Doing and Done

Define the first vertical slice: view synthetic tasks grouped by To Do, Doing and Done.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Write five acceptance criteria beginning with an observable verb such as displays, moves, filters, or reports

Write five acceptance criteria beginning with an observable verb such as displays, moves, filters, or reports.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Add non-goals: accounts, payments, real-time sync, production customer data, and backend persistence

Add non-goals: accounts, payments, real-time sync, production customer data, and backend persistence.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Ask the agent to challenge ambiguity and identify edge cases without proposing code

Ask the agent to challenge ambiguity and identify edge cases without proposing code.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Revise the brief, inspect the documentation diff, and checkpoint it before implementation

Revise the brief, inspect the documentation diff, and checkpoint it before implementation.

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

Act as a skeptical product engineer. Review docs/product-brief.md and docs/acceptance.md without editing. Find ambiguous words, missing states, hidden dependencies and acceptance checks that are not observable. Return a corrected proposal and a risk list.

```

## Read what the AI wrote

- **Starting code before agreeing behavior.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Acceptance criteria based on implementation.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Scope expanding into a backend.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Using real employee data.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects problem framing, acceptance criteria, non-goals, vertical slice to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. AI amplifies ambiguity. A narrow vertical slice and observable criteria give both the agent and the learner a shared definition of done. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] Criteria are observable.

- [ ] Non-goals are explicit.

- [ ] Loading/empty/error states are named.

- [ ] No code was generated.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to problem framing without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| Starting code before agreeing behavior | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Acceptance criteria based on implementation | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Scope expanding into a backend | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Using real employee data | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did problem framing change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 1.3

Turn a vague app idea into a bounded SprintBoard brief, non-goals, risks and observable acceptance checks.


# Lab 1.4 — Engineer a Plan–Diff–Verify Prompt Contract

> **Topic 1** · approximately 40 minutes · builds on the previous lab checkpoint

## Goal

Create reusable prompt and review templates that force planning, bounded edits and verification evidence.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `docs/prompt-template.md`, `docs/review-checklist.md`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Context Engineering** — apply it in the current file and explain its effect on user-visible behavior.

- **Bounded Change** — apply it in the current file and explain its effect on user-visible behavior.

- **Diff Review** — apply it in the current file and explain its effect on user-visible behavior.

- **Rollback** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Create a prompt template with Goal, Context, Constraints, Deliverables, Verification and Stop Conditions

Create a prompt template with Goal, Context, Constraints, Deliverables, Verification and Stop Conditions.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Create a review checklist covering file scope, dependencies, types, accessibility, errors, secrets and tests

Create a review checklist covering file scope, dependencies, types, accessibility, errors, secrets and tests.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Ask the agent to plan the SprintBoard shell and name every file it would change; do not authorize implementation

Ask the agent to plan the SprintBoard shell and name every file it would change; do not authorize implementation.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Compare the plan to the product brief; reject any unrequested package or architecture

Compare the plan to the product brief; reject any unrequested package or architecture.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Authorize one small increment and require the agent to summarize the resulting diff

Authorize one small increment and require the agent to summarize the resulting diff.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Run the verification commands yourself; record keep, refine, or revert with the evidence

Run the verification commands yourself; record keep, refine, or revert with the evidence.

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

## Your turn

Change one constraint related to context engineering without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| Prompt asks for the entire app | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Agent silently adds a UI framework | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Summary replaces line-by-line diff review | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Passing build treated as complete evidence | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did context engineering change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 1.4

Create reusable prompt and review templates that force planning, bounded edits and verification evidence.


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


## Topic 2: Building React Components and UI with AI

Generate function components and JSX, compose reusable interfaces, pass data with props, handle events, and refine responsive CSS.

# Lab 2.1 — Model Tasks and Render Lists with Stable Keys

> **Topic 2** · approximately 40 minutes · builds on the previous lab checkpoint

## Goal

Create typed synthetic task data and render it predictably with map and stable identifiers.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/types.ts`, `src/data/tasks.ts`, `src/components/TaskList.tsx`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Typescript Interface** — apply it in the current file and explain its effect on user-visible behavior.

- **Map** — apply it in the current file and explain its effect on user-visible behavior.

- **Stable Key** — apply it in the current file and explain its effect on user-visible behavior.

- **Derived View** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Define `Task` with id, title, owner, status, points and priority; restrict status to a union

Define `Task` with id, title, owner, status, points and priority; restrict status to a union.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Create eight synthetic tasks with unique stable string IDs and no personal data

Create eight synthetic tasks with unique stable string IDs and no personal data.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Plan a TaskList that receives tasks through props and maps each item to visible output

Plan a TaskList that receives tasks through props and maps each item to visible output.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Generate the component, then inspect for `key={index}`, inline mutation and missing empty output

Generate the component, then inspect for `key={index}`, inline mutation and missing empty output.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Reorder the array and verify task identity remains correct; temporarily pass an empty array

Reorder the array and verify task identity remains correct; temporarily pass an empty array.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Run type-check, lint and build; record why a database-style ID is safer than the array index

Run type-check, lint and build; record why a database-style ID is safer than the array index.

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

Create typed synthetic task data and a TaskList component. Use a Task interface, a status union, stable task.id keys, and a meaningful empty state. Do not add state or packages. Explain the key choice after showing the files changed.

```

## Read what the AI wrote

- **key={index}.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Duplicate IDs.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Rendering raw objects.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Mutating the source array during render.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects TypeScript interface, map, stable key, derived view to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. Keys are not display labels; they tell React which item is the same conceptual entity between renders. Stable identity prevents state and DOM from attaching to the wrong row. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] Eight tasks render.

- [ ] Empty state appears.

- [ ] Reorder preserves identity.

- [ ] Type-check passes.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to TypeScript interface without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| key={index} | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Duplicate IDs | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Rendering raw objects | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Mutating the source array during render | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did TypeScript interface change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 2.1

Create typed synthetic task data and render it predictably with map and stable identifiers.


# Lab 2.2 — Extract Components and Design Prop Contracts

> **Topic 2** · approximately 40 minutes · builds on the previous lab checkpoint

## Goal

Split the board into focused typed components and pass data explicitly through props.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/components/Board.tsx`, `src/components/TaskColumn.tsx`, `src/components/TaskCard.tsx`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Component Boundary** — apply it in the current file and explain its effect on user-visible behavior.

- **Props** — apply it in the current file and explain its effect on user-visible behavior.

- **Composition** — apply it in the current file and explain its effect on user-visible behavior.

- **Single Responsibility** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Draw the component tree from App to Board, TaskColumn and TaskCard before editing code

Draw the component tree from App to Board, TaskColumn and TaskCard before editing code.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Define each prop interface and decide which values are required, optional, or callbacks

Define each prop interface and decide which values are required, optional, or callbacks.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Ask the agent for a refactor plan that preserves visible behavior and names moves versus edits

Ask the agent for a refactor plan that preserves visible behavior and names moves versus edits.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Implement one extraction at a time; run the app after each move to isolate regressions

Implement one extraction at a time; run the app after each move to isolate regressions.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Inspect for prop drilling caused by misplaced state, duplicated markup and components that read globals

Inspect for prop drilling caused by misplaced state, duplicated markup and components that read globals.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Use React DevTools to identify boundaries, then lint/build and commit the refactor separately

Use React DevTools to identify boundaries, then lint/build and commit the refactor separately.

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

Refactor the existing task markup into Board, TaskColumn and TaskCard. First provide prop interfaces and a move plan. Preserve behavior and CSS classes. Do not add state, context or packages. Implement one component extraction at a time and stop if a test or build fails.

```

## Read what the AI wrote

- **Changing behavior during refactor.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Using any for props.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Reading module globals inside TaskCard.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **One component still owns unrelated responsibilities.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects component boundary, props, composition, single responsibility to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. A component boundary is an API. Clear prop contracts make generated code easier to inspect, test and replace without hidden coupling. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] UI is unchanged.

- [ ] Props are typed.

- [ ] Components have focused purposes.

- [ ] Build passes after each extraction.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to component boundary without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| Changing behavior during refactor | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Using any for props | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Reading module globals inside TaskCard | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| One component still owns unrelated responsibilities | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did component boundary change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 2.2

Split the board into focused typed components and pass data explicitly through props.


# Lab 2.3 — Compose Reusable Layouts with children

> **Topic 2** · approximately 35 minutes · builds on the previous lab checkpoint

## Goal

Use composition and children to build reusable sections without boolean-prop complexity.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/components/Panel.tsx`, `src/components/EmptyState.tsx`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Children** — apply it in the current file and explain its effect on user-visible behavior.

- **Composition** — apply it in the current file and explain its effect on user-visible behavior.

- **Slot** — apply it in the current file and explain its effect on user-visible behavior.

- **Fallback Content** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Identify repeated panel chrome and distinguish it from the unique content inside each panel

Identify repeated panel chrome and distinguish it from the unique content inside each panel.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Create a typed Panel accepting title, optional actions and ReactNode children

Create a typed Panel accepting title, optional actions and ReactNode children.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Replace duplicated wrappers without changing the order or semantics of content

Replace duplicated wrappers without changing the order or semantics of content.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Create an EmptyState that composes a heading, explanation and optional action

Create an EmptyState that composes a heading, explanation and optional action.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Inspect generated code for nested ternaries and a proliferation of `showX` boolean props

Inspect generated code for nested ternaries and a proliferation of `showX` boolean props.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Render two different Panel contents and two EmptyState variants; lint and build

Render two different Panel contents and two EmptyState variants; lint and build.

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

Create a typed Panel component using composition. It accepts title, optional actions and children: ReactNode. Create an EmptyState with optional action content. Replace repeated wrappers but preserve semantics and visible behavior. Avoid boolean props that switch unrelated layouts.

```

## Read what the AI wrote

- **Over-general component.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Children typed as any.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Nested ternaries controlling layout.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Heading levels become inconsistent.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects children, composition, slot, fallback content to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. Composition passes UI as data. It keeps the reusable shell ignorant of the content and avoids an ever-growing matrix of configuration flags. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] Two distinct panels compose correctly.

- [ ] Optional actions disappear cleanly.

- [ ] Heading order remains logical.

- [ ] No behavior change.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to children without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| Over-general component | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Children typed as any | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Nested ternaries controlling layout | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Heading levels become inconsistent | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did children change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 2.3

Use composition and children to build reusable sections without boolean-prop complexity.


# Lab 2.4 — Handle Events and Controlled Forms

> **Topic 2** · approximately 45 minutes · builds on the previous lab checkpoint

## Goal

Add a controlled task form with validation and explicit submit behavior.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/components/TaskForm.tsx`, `src/App.tsx`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Event Handler** — apply it in the current file and explain its effect on user-visible behavior.

- **Controlled Input** — apply it in the current file and explain its effect on user-visible behavior.

- **Validation** — apply it in the current file and explain its effect on user-visible behavior.

- **Preventdefault** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Define form fields and acceptance rules: nonblank title, owner placeholder, priority and points range

Define form fields and acceptance rules: nonblank title, owner placeholder, priority and points range.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Plan controlled state for each field and an `onCreate` callback owned by the parent

Plan controlled state for each field and an `onCreate` callback owned by the parent.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Generate labels, inputs, select, error region and submit button using semantic form controls

Generate labels, inputs, select, error region and submit button using semantic form controls.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Inspect for missing labels, mutation, stale state, uncontrolled-to-controlled warnings and page reload

Inspect for missing labels, mutation, stale state, uncontrolled-to-controlled warnings and page reload.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Test keyboard-only completion, invalid title, boundary points, successful submit and form reset

Test keyboard-only completion, invalid title, boundary points, successful submit and form reset.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Run lint/build and use the accessibility tree to confirm label-control relationships

Run lint/build and use the accessibility tree to confirm label-control relationships.

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

## Your turn

Change one constraint related to event handler without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| Button defaults reload the page | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Input lacks label | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Number remains a string | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Form clears even when validation fails | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did event handler change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 2.4

Add a controlled task form with validation and explicit submit behavior.


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


## Topic 3: State, Hooks and Routing with AI Assistance

Manage state and effects, build multi-page flows with React Router, fetch data, and refactor generated code safely.

# Lab 3.1 — Manage Immutable Task State with useState

> **Topic 3** · approximately 45 minutes · builds on the previous lab checkpoint

## Goal

Create, move and delete tasks with functional updates and immutable array transformations.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/App.tsx`, `src/lib/taskTransitions.ts`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **State Snapshot** — apply it in the current file and explain its effect on user-visible behavior.

- **Functional Update** — apply it in the current file and explain its effect on user-visible behavior.

- **Immutability** — apply it in the current file and explain its effect on user-visible behavior.

- **Derived State** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Move the initial tasks into `useState` and keep filters as derived data rather than a second task array

Move the initial tasks into `useState` and keep filters as derived data rather than a second task array.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Write pure create, move and delete transition helpers before connecting buttons

Write pure create, move and delete transition helpers before connecting buttons.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Use functional state updates whenever the next value depends on the previous array

Use functional state updates whenever the next value depends on the previous array.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Inspect the agent diff for push, splice, direct property assignment and stale closure reads

Inspect the agent diff for push, splice, direct property assignment and stale closure reads.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Test two rapid moves, delete after filter, duplicate title and empty-column behavior

Test two rapid moves, delete after filter, duplicate title and empty-column behavior.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Explain why state behaves as a snapshot, then lint, type-check and build

Explain why state behaves as a snapshot, then lint, type-check and build.

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

Add task create, move-forward and delete behavior with useState. Use pure immutable transition helpers and functional updates. Do not store filtered tasks in state. Preserve stable IDs and status order. Include tests or console-free verification examples for transition edge cases.

```

## Read what the AI wrote

- **tasks.push mutates state.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Duplicated filtered state drifts.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **setTasks([...tasks]) uses stale closure.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Index used as identity.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects state snapshot, functional update, immutability, derived state to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. Each render sees a snapshot of state. Functional updates receive the latest committed value and immutable transformations give React a new reference to reconcile. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] Rapid updates are not lost.

- [ ] Original arrays are unchanged.

- [ ] Filter follows source state.

- [ ] Transitions stop at Done.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to state snapshot without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| tasks.push mutates state | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Duplicated filtered state drifts | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| setTasks([...tasks]) uses stale closure | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Index used as identity | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did state snapshot change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 3.1

Create, move and delete tasks with functional updates and immutable array transformations.


# Lab 3.2 — Synchronize and Clean Up Effects

> **Topic 3** · approximately 45 minutes · builds on the previous lab checkpoint

## Goal

Persist tasks locally with guarded parsing and understand effect dependencies and cleanup.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/hooks/usePersistentTasks.ts`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Useeffect** — apply it in the current file and explain its effect on user-visible behavior.

- **Dependency** — apply it in the current file and explain its effect on user-visible behavior.

- **Cleanup** — apply it in the current file and explain its effect on user-visible behavior.

- **Localstorage** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Define the external system: one versioned localStorage key containing synthetic task JSON

Define the external system: one versioned localStorage key containing synthetic task JSON.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Create a lazy state initializer that reads once and falls back safely on missing or malformed data

Create a lazy state initializer that reads once and falls back safely on missing or malformed data.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Add a save effect whose dependency reflects the value being synchronized

Add a save effect whose dependency reflects the value being synchronized.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Inspect StrictMode behavior and ensure the effect is idempotent rather than disabled

Inspect StrictMode behavior and ensure the effect is idempotent rather than disabled.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Test reload, cleared storage, malformed JSON, schema mismatch and storage write failure

Test reload, cleared storage, malformed JSON, schema mismatch and storage write failure.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Ask the agent to explain every dependency; reject lint suppression as a fix

Ask the agent to explain every dependency; reject lint suppression as a fix.

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

Extract usePersistentTasks. Read localStorage with a lazy initializer, validate parsed data, fall back to provided initial tasks, and save when tasks change. Use one versioned key. Do not suppress exhaustive-deps. Explain StrictMode behavior and all failure paths.

```

## Read what the AI wrote

- **Effect reads and writes in a loop.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **JSON.parse crash blanks the app.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Lint rule disabled.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Storage treated as secure.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects useEffect, dependency, cleanup, localStorage to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. Effects synchronize React with systems outside React. Dependencies describe the reactive values used by that synchronization; cleanup or idempotence prevents duplicate external work. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] Reload restores tasks.

- [ ] Malformed data recovers.

- [ ] No effect loop.

- [ ] Dependencies can be explained.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to useEffect without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| Effect reads and writes in a loop | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| JSON.parse crash blanks the app | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Lint rule disabled | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Storage treated as secure | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did useEffect change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 3.2

Persist tasks locally with guarded parsing and understand effect dependencies and cleanup.


# Lab 3.3 — Extract a Tested Custom Hook

> **Topic 3** · approximately 40 minutes · builds on the previous lab checkpoint

## Goal

Separate reusable board logic into a custom hook without sharing state between consumers.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/hooks/useTaskBoard.ts`, `src/hooks/useTaskBoard.test.ts`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Custom Hook** — apply it in the current file and explain its effect on user-visible behavior.

- **Logic Reuse** — apply it in the current file and explain its effect on user-visible behavior.

- **Public Api** — apply it in the current file and explain its effect on user-visible behavior.

- **Hook Test** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — List the smallest public API: tasks, visibleTasks, filter, setFilter, create, move and remove

List the smallest public API: tasks, visibleTasks, filter, setFilter, create, move and remove.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Move stateful logic into `useTaskBoard` while keeping presentation in components

Move stateful logic into `useTaskBoard` while keeping presentation in components.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Inspect hook naming, top-level hook calls and dependency boundaries

Inspect hook naming, top-level hook calls and dependency boundaries.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Render two hook consumers and prove they do not share state unless state is lifted

Render two hook consumers and prove they do not share state unless state is lifted.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Add focused tests for initial state, filtering and immutable movement

Add focused tests for initial state, filtering and immutable movement.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Refactor App to consume the hook; compare behavior before and after

Refactor App to consume the hook; compare behavior before and after.

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

Extract useTaskBoard from App. Define a small typed return API, keep hooks at the top level, derive visibleTasks, and expose named actions. Add tests for initial tasks, filtering and moving. Preserve all visible behavior and do not introduce context.

```

## Read what the AI wrote

- **Hook called conditionally.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Hook returns unstable unnecessary objects.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Custom hook assumed to create global shared state.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Presentation markup moved into logic hook.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects custom hook, logic reuse, public API, hook test to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. Custom hooks share stateful logic, not state instances. Each call runs its own hook state unless a common owner or context deliberately shares it. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] Two instances are independent.

- [ ] Hook tests pass.

- [ ] App becomes simpler.

- [ ] Behavior is unchanged.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to custom hook without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| Hook called conditionally | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Hook returns unstable unnecessary objects | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Custom hook assumed to create global shared state | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Presentation markup moved into logic hook | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did custom hook change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 3.3

Separate reusable board logic into a custom hook without sharing state between consumers.


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


# Lab 3.5 — Fetch API Data with Loading, Empty, Error and Retry States

> **Topic 3** · approximately 50 minutes · builds on the previous lab checkpoint

## Goal

Replace local seed data with a controlled fetch pipeline and resilient user-visible states.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `public/tasks.json`, `src/hooks/useTasksApi.ts`, `src/components/AsyncState.tsx`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Fetch** — apply it in the current file and explain its effect on user-visible behavior.

- **Response.Ok** — apply it in the current file and explain its effect on user-visible behavior.

- **Abortcontroller** — apply it in the current file and explain its effect on user-visible behavior.

- **State Machine** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Create a local JSON endpoint with synthetic tasks so the lab needs no credentials

Create a local JSON endpoint with synthetic tasks so the lab needs no credentials.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Model idle/loading/success/empty/error rather than a single ambiguous boolean

Model idle/loading/success/empty/error rather than a single ambiguous boolean.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Fetch inside an effect, check `response

Fetch inside an effect, check `response.ok`, validate the payload and abort on cleanup.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Expose a retry action and a useful error message without leaking stack traces

Expose a retry action and a useful error message without leaking stack traces.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Test normal data, empty array, invalid JSON, 404 path, slow network and component unmount

Test normal data, empty array, invalid JSON, 404 path, slow network and component unmount.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Inspect for requests during render, missing cleanup, swallowed errors and endless spinner

Inspect for requests during render, missing cleanup, swallowed errors and endless spinner.

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

Create useTasksApi for /tasks.json with loading, success, empty and error states, response.ok checking, runtime shape validation, AbortController cleanup and retry. Keep synthetic data local and show accessible status messages. Do not hide errors or fetch during render.

```

## Read what the AI wrote

- **fetch during render.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **No response.ok check.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Abort reported as user error.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Error leaves loading true forever.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects fetch, response.ok, AbortController, state machine to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. A network request is a state machine, not a value. Explicit states prevent stale content, endless spinners and blank screens when the happy path fails. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] All four visible states work.

- [ ] Retry recovers.

- [ ] Unmount aborts request.

- [ ] No credentials are required.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to fetch without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| fetch during render | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| No response.ok check | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Abort reported as user error | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Error leaves loading true forever | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did fetch change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 3.5

Replace local seed data with a controlled fetch pipeline and resilient user-visible states.


## Topic 4: Debugging, Testing and Deploying React Apps with AI

Diagnose failures, generate focused tests, optimize and document the app, and deploy a verified production build.

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


# Lab 4.2 — Test User Behaviour with Vitest and Testing Library

> **Topic 4** · approximately 50 minutes · builds on the previous lab checkpoint

## Goal

Build a focused test suite for rendering, filtering, task movement, forms and routes.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/test/setup.ts`, `src/App.test.tsx`, `src/components/TaskForm.test.tsx`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Test** — apply it in the current file and explain its effect on user-visible behavior.

- **Assertion** — apply it in the current file and explain its effect on user-visible behavior.

- **User Event** — apply it in the current file and explain its effect on user-visible behavior.

- **Accessible Query** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Install Vitest, jsdom, Testing Library, jest-dom and user-event; pin and record versions

Install Vitest, jsdom, Testing Library, jest-dom and user-event; pin and record versions.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Configure the test environment and add an explicit `test` script

Configure the test environment and add an explicit `test` script.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Write a smoke test using role and accessible-name queries rather than CSS selectors

Write a smoke test using role and accessible-name queries rather than CSS selectors.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Add behaviour tests for filtering, valid/invalid form submit and moving a task

Add behaviour tests for filtering, valid/invalid form submit and moving a task.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Add a MemoryRouter test for task details and not-found behavior

Add a MemoryRouter test for task details and not-found behavior.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Run tests in watch and single-run modes; inspect generated assertions for false confidence

Run tests in watch and single-run modes; inspect generated assertions for false confidence.

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

Add Vitest and React Testing Library tests for SprintBoard. Query by role/name, drive interactions with user-event, and assert visible behaviour. Cover initial board, filter, invalid and valid create, move, task route and unknown task. Avoid snapshots and implementation-detail selectors.

```

## Read what the AI wrote

- **Testing internal state.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **fireEvent used for realistic typing.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Assertions pass without awaiting user events.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

- **Snapshot replaces behavior checks.** Locate the exact line or absence that would reveal this failure. Ask for an explanation before accepting a change.

## Why it works

This lab connects test, assertion, user event, accessible query to an observable SprintBoard increment. The important adult-learning move is not memorising syntax; it is predicting what the code should do, comparing that prediction with generated output, and using evidence to resolve the gap. The agent can accelerate typing and suggest structures, but the learner owns the product rule, file boundary, safety decision and acceptance evidence. Behaviour tests treat the interface like a user does. Accessible queries improve both test resilience and the underlying UI semantics. When reviewing, trace information from its source through props, state, effects or routes to the visible result. Then trace every user action back through its handler and state transition. This two-way trace exposes hidden coupling and plausible-looking code that does not satisfy the brief.

## Test it

- [ ] Tests fail for deliberate regressions.

- [ ] Queries reflect accessibility.

- [ ] All required flows pass.

- [ ] Single-run command exits cleanly.

- [ ] `npm run lint` completes without an unexplained suppression.

- [ ] `npm run build` completes and the browser console has no new error.

- [ ] `git diff --check` is clean and every changed file was in the approved plan.

## Evidence to submit

- The final prompt and approved plan.

- `git diff --stat` plus one annotated excerpt showing a reviewed decision.

- Verification command output and a screenshot of the observable result.

- A short note naming one AI suggestion accepted, corrected or rejected and why.

## Your turn

Change one constraint related to test without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| Testing internal state | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| fireEvent used for realistic typing | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Assertions pass without awaiting user events | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Snapshot replaces behavior checks | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did test change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 4.2

Build a focused test suite for rendering, filtering, task movement, forms and routes.


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


# Lab 4.5 — Build, Deploy and Demonstrate the Capstone

> **Topic 4** · approximately 55 minutes · builds on the previous lab checkpoint

## Goal

Produce and deploy a verified SprintBoard release with SPA routing, rollback instructions and an evidence-backed demonstration.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `dist/`, `docs/release-checklist.md`, `docs/release-notes.md`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **Production Build** — apply it in the current file and explain its effect on user-visible behavior.

- **Spa Fallback** — apply it in the current file and explain its effect on user-visible behavior.

- **Release Gate** — apply it in the current file and explain its effect on user-visible behavior.

- **Rollback** — apply it in the current file and explain its effect on user-visible behavior.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Run clean install, test, lint, type-check and build from the documented commands

Run clean install, test, lint, type-check and build from the documented commands.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 2 — Choose an approved static host and configure the correct Vite base path and SPA fallback behavior

Choose an approved static host and configure the correct Vite base path and SPA fallback behavior.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 3 — Deploy `dist` through Git integration or the host workflow without exposing credentials

Deploy `dist` through Git integration or the host workflow without exposing credentials.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 4 — Open the public URL and verify board, form, filters, dynamic route, refresh, 404 and retry behavior

Open the public URL and verify board, form, filters, dynamic route, refresh, 404 and retry behavior.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 5 — Create release notes with features, evidence, limitations, known risks and exact rollback steps

Create release notes with features, evidence, limitations, known risks and exact rollback steps.

**Pause and inspect:** predict the changed files and visible result before continuing. If the agent proposes broader work, stop and narrow the request.

**Evidence:** save the relevant command output, browser observation or diff note in the training log.

### Step 6 — Demonstrate the complete agentic loop using one final small improvement and show its plan, diff, tests and checkpoint

Demonstrate the complete agentic loop using one final small improvement and show its plan, diff, tests and checkpoint.

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

## Your turn

Change one constraint related to production build without widening the product scope. Predict the files and tests first, then run the complete loop and compare the prediction with the actual diff.

## Common errors

| Symptom | Likely cause | Recovery |

|---|---|---|

| Deploying untested dist | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Direct route refresh returns 404 | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| Secrets included in VITE variables | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

| No rollback target | The generated plan or diff ignored an explicit constraint. | Restore the checkpoint, narrow the prompt to one file or behavior, and rerun the failing verification. |

## Reflection

How did production build change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 4.5

Produce and deploy a verified SprintBoard release with SPA routing, rollback instructions and an evidence-backed demonstration.
