# AI Vibe Coding for React Development — Learner Guide

- **Course Code:** C1143

- **Duration:** 15 hours / 2 days

- **Level:** Intermediate

## Agentic AI Loop

Frame → Plan → Generate → Inspect → Verify → Correct → Commit

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

- **toolchain** — The set of tools — Node.js, npm, Git and the editor — whose versions and availability determine whether a React project can be built and verified.

- **working directory** — The folder a tool or agent currently operates in; opening the wrong folder is how agents read or edit files you never intended to expose.

- **agent scope** — The explicit boundary of files and actions an AI coding agent is allowed to touch in a given request.

- **evidence trail** — A durable record of commands, outputs and screenshots that lets you prove what was verified and when.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Run `node -v`, `npm -v`, and `git --version`; record the outputs in `training-log/README.md`

Run `node -v`, `npm -v`, and `git --version`; record the outputs in `training-log/README.md`.

**Pause and inspect:** Predict which files this step should touch and what will change on screen; compare that prediction with the actual diff before moving on.

**Evidence:** Run the narrowest check that exercises this step first; only then run the wider lint, type-check and build stack.

### Step 2 — Open a dedicated `sprintboard` parent folder in VS Code and confirm the integrated terminal starts in that folder

Open a dedicated `sprintboard` parent folder in VS Code and confirm the integrated terminal starts in that folder.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

### Step 3 — Choose Cursor, GitHub Copilot, Claude, or Codex; verify it can read only the folder you intentionally opened

Choose Cursor, GitHub Copilot, Claude, or Codex; verify it can read only the folder you intentionally opened.

**Pause and inspect:** Keep the agent inside the declared file scope here — if its proposal reaches further, stop and narrow the request.

**Evidence:** Capture the command, expected result and actual result; if they differ, stop and investigate before the next step.

### Step 4 — Create `AGENTS.md` with plan-first, named-file scope, no-secret, small-diff, and verification-before-acceptance rules

Create `AGENTS.md` with plan-first, named-file scope, no-secret, small-diff, and verification-before-acceptance rules.

**Pause and inspect:** Where the agent acts, read its output as a reviewer, not a spectator, and note one specific thing you checked.

**Evidence:** If this step touches the interface, re-test at both a narrow and a wide viewport and note anything that clips or overflows.

### Step 5 — Ask the agent to restate the rules and list what it is not allowed to do; correct any missing boundary

Ask the agent to restate the rules and list what it is not allowed to do; correct any missing boundary.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

### Step 6 — Create a baseline Git repository and inspect `git status --short` before the first checkpoint

Create a baseline Git repository and inspect `git status --short` before the first checkpoint.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

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

## Independent challenge

Change one constraint related to toolchain without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| Agent edits before planning | The request mixed intent with authorization, so the agent treated a description as permission to act. | Revert the unapproved edit, restate the plan-first rule in AGENTS.md, and resend the request ending with 'stop after the plan'. |

| Credentials copied into chat | A real token or password was pasted into the conversation for convenience. | Rotate the credential immediately, scrub it from logs, and use placeholders in every future prompt. |

| Tool versions asserted without terminal evidence | The agent inferred versions from training data instead of running the commands. | Run node -v, npm -v and git --version yourself and record the actual output in the training log. |

| Repository initialized in the wrong folder | VS Code was opened above or beside the intended folder, so git init ran in the wrong directory. | Delete the stray .git folder, open the sprintboard folder directly, and re-run git init there. |

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

- **Vite** — A build tool that serves source files over native ES modules in development and bundles them with Rollup for production.

- **module graph** — The dependency network Vite builds by following import statements from the entry file through every module it reaches.

- **React root** — The single DOM element where React attaches the component tree and takes over rendering.

- **Hot Module Replacement** — A dev-server feature that swaps edited modules into the running page without a full reload, preserving much of the app state.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Run `npm create vite@latest sprintboard -- --template react-ts`, enter the folder, and run `npm install`

Run `npm create vite@latest sprintboard -- --template react-ts`, enter the folder, and run `npm install`.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

### Step 2 — Start `npm run dev`; open the printed local URL and save a screenshot of the starter page

Start `npm run dev`; open the printed local URL and save a screenshot of the starter page.

**Pause and inspect:** Keep the agent inside the declared file scope here — if its proposal reaches further, stop and narrow the request.

**Evidence:** Capture the command, expected result and actual result; if they differ, stop and investigate before the next step.

### Step 3 — Trace `index.html` to `src/main.tsx` to `<App />`; annotate the chain in the training log

Trace `index.html` to `src/main.tsx` to `<App />`; annotate the chain in the training log.

**Pause and inspect:** Where the agent acts, read its output as a reviewer, not a spectator, and note one specific thing you checked.

**Evidence:** If this step touches the interface, re-test at both a narrow and a wide viewport and note anything that clips or overflows.

### Step 4 — Ask the agent for a file-by-file explanation without requesting changes; compare it with the actual imports

Ask the agent for a file-by-file explanation without requesting changes; compare it with the actual imports.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

### Step 5 — Run `npm run build`, inspect `dist/`, then run `npm run preview` and explain how preview differs from dev

Run `npm run build`, inspect `dist/`, then run `npm run preview` and explain how preview differs from dev.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

### Step 6 — Review `git diff` and commit the untouched scaffold as `chore: scaffold SprintBoard`

Review `git diff` and commit the untouched scaffold as `chore: scaffold SprintBoard`.

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

## Independent challenge

Change one constraint related to Vite without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| Using Create React App instructions | The agent reached for the older, deprecated scaffold it saw most in training. | Reject the plan, name Vite explicitly in the prompt, and compare commands against current Vite documentation. |

| Editing node_modules | The agent patched a dependency's source instead of your code. | Discard the change — node_modules is regenerated by npm install — and request the fix inside src instead. |

| Confusing dev output with production output | The dev server transforms modules on demand, so it never proves what the bundled build does. | Run npm run build followed by npm run preview and verify against the served dist output. |

| Inventing files not present in the scaffold | The explanation was generated from a generic template project, not your repository. | Ask the agent to list only files it can actually read, and cross-check every claim against the file tree. |

## Reflection

How did Vite change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 1.2

Create a Vite React TypeScript app, run the development server, and explain the boot sequence.


# Lab 1.3 — Write a Testable Product Brief and Acceptance Criteria

> **Topic 1** · approximately 30 minutes · builds on the previous lab checkpoint

## Goal

Turn a vague app idea into a bounded SprintBoard brief, non-goals, risks and observable acceptance checks.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `docs/product-brief.md`, `docs/acceptance.md`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **problem framing** — Stating who has what problem and what observable change would solve it, before any solution is designed.

- **acceptance criteria** — Concrete, observable checks that define when a feature is done — phrased so a third party could verify them.

- **non-goals** — Explicitly excluded features that stop a project — or an AI agent — from silently expanding scope.

- **vertical slice** — A thin end-to-end piece of the product that delivers visible value and exercises every layer once.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Describe the adult learner persona and the problem SprintBoard solves in two sentences

Describe the adult learner persona and the problem SprintBoard solves in two sentences.

**Pause and inspect:** Keep the agent inside the declared file scope here — if its proposal reaches further, stop and narrow the request.

**Evidence:** Capture the command, expected result and actual result; if they differ, stop and investigate before the next step.

### Step 2 — Define the first vertical slice: view synthetic tasks grouped by To Do, Doing and Done

Define the first vertical slice: view synthetic tasks grouped by To Do, Doing and Done.

**Pause and inspect:** Where the agent acts, read its output as a reviewer, not a spectator, and note one specific thing you checked.

**Evidence:** If this step touches the interface, re-test at both a narrow and a wide viewport and note anything that clips or overflows.

### Step 3 — Write five acceptance criteria beginning with an observable verb such as displays, moves, filters, or reports

Write five acceptance criteria beginning with an observable verb such as displays, moves, filters, or reports.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

### Step 4 — Add non-goals: accounts, payments, real-time sync, production customer data, and backend persistence

Add non-goals: accounts, payments, real-time sync, production customer data, and backend persistence.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

### Step 5 — Ask the agent to challenge ambiguity and identify edge cases without proposing code

Ask the agent to challenge ambiguity and identify edge cases without proposing code.

**Pause and inspect:** Predict which files this step should touch and what will change on screen; compare that prediction with the actual diff before moving on.

**Evidence:** Run the narrowest check that exercises this step first; only then run the wider lint, type-check and build stack.

### Step 6 — Revise the brief, inspect the documentation diff, and checkpoint it before implementation

Revise the brief, inspect the documentation diff, and checkpoint it before implementation.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

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

## Independent challenge

Change one constraint related to problem framing without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| Starting code before agreeing behavior | Building feels like progress, so ambiguity gets deferred until it is expensive. | Stop implementation, finish the acceptance criteria, and only then authorize a plan. |

| Acceptance criteria based on implementation | Criteria were written from the intended code rather than user-observable behavior. | Rewrite each criterion to start with an observable verb such as displays, moves or filters. |

| Scope expanding into a backend | Persistence and accounts crept in because they were never named as non-goals. | Add them to the non-goals list and cut the slice back to the board view. |

| Using real employee data | Real names were pasted in to make the demo feel authentic. | Replace them with synthetic personas and add a no-real-data rule to the brief. |

## Reflection

How did problem framing change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 1.3

Turn a vague app idea into a bounded SprintBoard brief, non-goals, risks and observable acceptance checks.


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


# Lab 1.5 — Build and Review the First React Screen

> **Topic 1** · approximately 40 minutes · builds on the previous lab checkpoint

## Goal

Replace the starter content with a semantic SprintBoard shell while reviewing every generated line.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/App.tsx`, `src/App.css`, `src/index.css`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **function component** — A JavaScript function that accepts props and returns JSX describing part of the interface.

- **JSX** — A syntax extension that lets JavaScript express element trees; it compiles to function calls, not HTML.

- **semantic HTML** — Using elements such as header, nav, main and button for their meaning, so browsers and assistive technology understand the page structure.

- **component tree** — The nested hierarchy of components React renders, mirroring how data flows down through props.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Approve a shell containing header, navigation, main board region and footer; keep content synthetic

Approve a shell containing header, navigation, main board region and footer; keep content synthetic.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

### Step 2 — Ask the agent to implement only `App.tsx` and focused CSS, preserving the Vite entry point

Ask the agent to implement only `App.tsx` and focused CSS, preserving the Vite entry point.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

### Step 3 — Read the JSX aloud as a tree and identify every opening/closing tag and expression boundary

Read the JSX aloud as a tree and identify every opening/closing tag and expression boundary.

**Pause and inspect:** Predict which files this step should touch and what will change on screen; compare that prediction with the actual diff before moving on.

**Evidence:** Run the narrowest check that exercises this step first; only then run the wider lint, type-check and build stack.

### Step 4 — Inspect the diff for removed defaults, global CSS leakage, inaccessible navigation, or unexplained assets

Inspect the diff for removed defaults, global CSS leakage, inaccessible navigation, or unexplained assets.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

### Step 5 — Run dev, lint and build; inspect the console and browser at 375 px and 1280 px

Run dev, lint and build; inspect the console and browser at 375 px and 1280 px.

**Pause and inspect:** Keep the agent inside the declared file scope here — if its proposal reaches further, stop and narrow the request.

**Evidence:** Capture the command, expected result and actual result; if they differ, stop and investigate before the next step.

### Step 6 — Commit only after the screen matches the brief and the learner can explain every changed line

Commit only after the screen matches the brief and the learner can explain every changed line.

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

## Independent challenge

Change one constraint related to function component without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| Nested interactive elements | A button was generated inside a link, producing invalid, inaccessible markup. | Restructure so each interactive control stands alone, then re-check the accessibility tree. |

| Decorative divs instead of semantic landmarks | The model imitates div-heavy training examples unless semantics are demanded. | Require header, nav, main and footer in the prompt and verify landmarks in DevTools. |

| Global wildcard styles with side effects | A universal selector or body rule leaked beyond the shell. | Scope styles to classes owned by the component and re-test the rest of the app. |

| Unexplained generated SVG or dependency | The agent decorated the shell with assets nobody requested. | Delete anything you cannot explain and note the rejection in the training log. |

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

- **TypeScript interface** — A named contract describing the shape of an object so the compiler can catch missing or mistyped fields.

- **map** — The array method that transforms each item into a new value — in React, into an element — without mutating the source array.

- **stable key** — An identifier tied to the data item rather than its position, so React can match list items between renders.

- **derived view** — Data computed from existing state during render instead of stored as a second copy that can drift.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Define `Task` with id, title, owner, status, points and priority; restrict status to a union

Define `Task` with id, title, owner, status, points and priority; restrict status to a union.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

### Step 2 — Create eight synthetic tasks with unique stable string IDs and no personal data

Create eight synthetic tasks with unique stable string IDs and no personal data.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

### Step 3 — Plan a TaskList that receives tasks through props and maps each item to visible output

Plan a TaskList that receives tasks through props and maps each item to visible output.

**Pause and inspect:** Predict which files this step should touch and what will change on screen; compare that prediction with the actual diff before moving on.

**Evidence:** Run the narrowest check that exercises this step first; only then run the wider lint, type-check and build stack.

### Step 4 — Generate the component, then inspect for `key={index}`, inline mutation and missing empty output

Generate the component, then inspect for `key={index}`, inline mutation and missing empty output.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

### Step 5 — Reorder the array and verify task identity remains correct; temporarily pass an empty array

Reorder the array and verify task identity remains correct; temporarily pass an empty array.

**Pause and inspect:** Keep the agent inside the declared file scope here — if its proposal reaches further, stop and narrow the request.

**Evidence:** Capture the command, expected result and actual result; if they differ, stop and investigate before the next step.

### Step 6 — Run type-check, lint and build; record why a database-style ID is safer than the array index

Run type-check, lint and build; record why a database-style ID is safer than the array index.

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

## Independent challenge

Change one constraint related to TypeScript interface without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| key={index} | The array index was the easiest unique-looking value at hand. | Key by task.id and re-test reordering to confirm identity is preserved. |

| Duplicate IDs | Hand-written synthetic data repeated an id after copy-paste. | Deduplicate the ids, then add a check that asserts uniqueness. |

| Rendering raw objects | A task object was interpolated directly into JSX, which React cannot render. | Render named fields such as task.title and task.owner instead. |

| Mutating the source array during render | sort or splice was called on the imported array inside the component. | Copy first — [...tasks].sort(...) — so the source data stays untouched. |

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

- **component boundary** — The dividing line that decides what a component owns, what it receives as props and what it must not know about.

- **props** — Read-only inputs a parent passes to a child component; the child never modifies them.

- **composition** — Building complex UI by nesting simple components rather than configuring one large component with flags.

- **single responsibility** — Each component does one job, so changes and reviews stay local.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Draw the component tree from App to Board, TaskColumn and TaskCard before editing code

Draw the component tree from App to Board, TaskColumn and TaskCard before editing code.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

### Step 2 — Define each prop interface and decide which values are required, optional, or callbacks

Define each prop interface and decide which values are required, optional, or callbacks.

**Pause and inspect:** Predict which files this step should touch and what will change on screen; compare that prediction with the actual diff before moving on.

**Evidence:** Run the narrowest check that exercises this step first; only then run the wider lint, type-check and build stack.

### Step 3 — Ask the agent for a refactor plan that preserves visible behavior and names moves versus edits

Ask the agent for a refactor plan that preserves visible behavior and names moves versus edits.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

### Step 4 — Implement one extraction at a time; run the app after each move to isolate regressions

Implement one extraction at a time; run the app after each move to isolate regressions.

**Pause and inspect:** Keep the agent inside the declared file scope here — if its proposal reaches further, stop and narrow the request.

**Evidence:** Capture the command, expected result and actual result; if they differ, stop and investigate before the next step.

### Step 5 — Inspect for prop drilling caused by misplaced state, duplicated markup and components that read globals

Inspect for prop drilling caused by misplaced state, duplicated markup and components that read globals.

**Pause and inspect:** Where the agent acts, read its output as a reviewer, not a spectator, and note one specific thing you checked.

**Evidence:** If this step touches the interface, re-test at both a narrow and a wide viewport and note anything that clips or overflows.

### Step 6 — Use React DevTools to identify boundaries, then lint/build and commit the refactor separately

Use React DevTools to identify boundaries, then lint/build and commit the refactor separately.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

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

## Independent challenge

Change one constraint related to component boundary without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| Changing behavior during refactor | Extraction and 'improvements' were mixed into one diff. | Revert to the checkpoint and redo the refactor with behavior frozen; improve in a separate commit. |

| Using any for props | any silences the compiler exactly where contracts matter most. | Write a real interface per component and let type errors reveal wrong assumptions. |

| Reading module globals inside TaskCard | Importing the task array directly hid the component's true inputs. | Pass tasks through props so the data path is explicit and testable. |

| One component still owns unrelated responsibilities | The extraction stopped at markup and left logic tangled. | Name each component's single job in one sentence; move anything that does not fit it. |

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

- **children** — The special prop carrying whatever JSX a parent nests inside a component's tags.

- **composition** — Building complex UI by nesting simple components rather than configuring one large component with flags.

- **slot** — A named insertion point — such as a title or actions prop — where a parent supplies custom content to a reusable shell.

- **fallback content** — What a component renders when expected content is absent, such as an empty-state message.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Identify repeated panel chrome and distinguish it from the unique content inside each panel

Identify repeated panel chrome and distinguish it from the unique content inside each panel.

**Pause and inspect:** Predict which files this step should touch and what will change on screen; compare that prediction with the actual diff before moving on.

**Evidence:** Run the narrowest check that exercises this step first; only then run the wider lint, type-check and build stack.

### Step 2 — Create a typed Panel accepting title, optional actions and ReactNode children

Create a typed Panel accepting title, optional actions and ReactNode children.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

### Step 3 — Replace duplicated wrappers without changing the order or semantics of content

Replace duplicated wrappers without changing the order or semantics of content.

**Pause and inspect:** Keep the agent inside the declared file scope here — if its proposal reaches further, stop and narrow the request.

**Evidence:** Capture the command, expected result and actual result; if they differ, stop and investigate before the next step.

### Step 4 — Create an EmptyState that composes a heading, explanation and optional action

Create an EmptyState that composes a heading, explanation and optional action.

**Pause and inspect:** Where the agent acts, read its output as a reviewer, not a spectator, and note one specific thing you checked.

**Evidence:** If this step touches the interface, re-test at both a narrow and a wide viewport and note anything that clips or overflows.

### Step 5 — Inspect generated code for nested ternaries and a proliferation of `showX` boolean props

Inspect generated code for nested ternaries and a proliferation of `showX` boolean props.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

### Step 6 — Render two different Panel contents and two EmptyState variants; lint and build

Render two different Panel contents and two EmptyState variants; lint and build.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

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

## Independent challenge

Change one constraint related to children without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| Over-general component | One Panel tried to cover every future layout with configuration. | Cut it back to the shared chrome and let children express the differences. |

| Children typed as any | The quick type erased what composition should guarantee. | Type the prop as ReactNode and remove the escape hatch. |

| Nested ternaries controlling layout | Boolean props multiplied until rendering became a puzzle. | Replace flag-driven branches with separate composed variants. |

| Heading levels become inconsistent | The reusable panel hard-coded one heading level wherever it was dropped. | Audit the heading outline and let the consumer control the heading level. |

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


# Lab 2.5 — Generate Responsive and Accessible CSS

> **Topic 2** · approximately 40 minutes · builds on the previous lab checkpoint

## Goal

Create a robust visual system with tokens, responsive layout, focus visibility and reduced-motion support.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/index.css`, `src/App.css`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **custom property** — A CSS variable defined once and reused, giving the design system a single point of change.

- **grid** — The CSS layout model that arranges children in rows and columns from the container — ideal for board layouts.

- **focus-visible** — The CSS pseudo-class that shows focus styles for keyboard users without decorating every mouse click.

- **media query** — A CSS rule that applies styles conditionally — for example by viewport width or a reduced-motion preference.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Inventory colors, spacing, type sizes and radii; convert repeated values into CSS custom properties

Inventory colors, spacing, type sizes and radii; convert repeated values into CSS custom properties.

**Pause and inspect:** Keep the agent inside the declared file scope here — if its proposal reaches further, stop and narrow the request.

**Evidence:** Capture the command, expected result and actual result; if they differ, stop and investigate before the next step.

### Step 2 — Define a mobile-first single-column board and expand to three columns when space allows

Define a mobile-first single-column board and expand to three columns when space allows.

**Pause and inspect:** Where the agent acts, read its output as a reviewer, not a spectator, and note one specific thing you checked.

**Evidence:** If this step touches the interface, re-test at both a narrow and a wide viewport and note anything that clips or overflows.

### Step 3 — Add visible `:focus-visible` styles and confirm text/background contrast with browser tools

Add visible `:focus-visible` styles and confirm text/background contrast with browser tools.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

### Step 4 — Add overflow handling for long task titles and test browser zoom at 200 percent

Add overflow handling for long task titles and test browser zoom at 200 percent.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

### Step 5 — Respect `prefers-reduced-motion` for transitions introduced by the agent

Respect `prefers-reduced-motion` for transitions introduced by the agent.

**Pause and inspect:** Predict which files this step should touch and what will change on screen; compare that prediction with the actual diff before moving on.

**Evidence:** Run the narrowest check that exercises this step first; only then run the wider lint, type-check and build stack.

### Step 6 — Inspect the CSS diff for `!important`, fixed heights, horizontal scroll and low-contrast tokens

Inspect the CSS diff for `!important`, fixed heights, horizontal scroll and low-contrast tokens.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

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

## Independent challenge

Change one constraint related to custom property without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| Fixed pixel heights clip content | Cards were sized to today's sample text. | Replace fixed heights with min-height or natural flow and re-test long titles. |

| Outline removed | outline: none was copied in for aesthetics. | Restore a visible :focus-visible style with sufficient contrast. |

| Desktop-first overflow | The layout was designed at 1280px and squeezed downward. | Rebuild mobile-first and add columns inside a min-width media query. |

| Color is the only status cue | Status was encoded purely in hue. | Add a text label or icon so status survives color-vision differences. |

## Reflection

How did custom property change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 2.5

Create a robust visual system with tokens, responsive layout, focus visibility and reduced-motion support.


## Topic 3: State, Hooks and Routing with AI Assistance

Manage state and effects, build multi-page flows with React Router, fetch data, and refactor generated code safely.

# Lab 3.1 — Manage Immutable Task State with useState

> **Topic 3** · approximately 40 minutes · builds on the previous lab checkpoint

## Goal

Create, move and delete tasks with functional updates and immutable array transformations.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/App.tsx`, `src/lib/taskTransitions.ts`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **state snapshot** — The fixed value of state a component sees during one render; updates schedule a new render rather than changing the current one.

- **functional update** — Passing a function to a state setter so the update is computed from the latest committed value, not a stale closure.

- **immutability** — Creating new objects and arrays instead of modifying existing ones, so React can detect changes by reference.

- **derived state** — Values computed from existing state during render — such as a filtered list — rather than stored separately.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Move the initial tasks into `useState` and keep filters as derived data rather than a second task array

Move the initial tasks into `useState` and keep filters as derived data rather than a second task array.

**Pause and inspect:** Keep the agent inside the declared file scope here — if its proposal reaches further, stop and narrow the request.

**Evidence:** Capture the command, expected result and actual result; if they differ, stop and investigate before the next step.

### Step 2 — Write pure create, move and delete transition helpers before connecting buttons

Write pure create, move and delete transition helpers before connecting buttons.

**Pause and inspect:** Where the agent acts, read its output as a reviewer, not a spectator, and note one specific thing you checked.

**Evidence:** If this step touches the interface, re-test at both a narrow and a wide viewport and note anything that clips or overflows.

### Step 3 — Use functional state updates whenever the next value depends on the previous array

Use functional state updates whenever the next value depends on the previous array.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

### Step 4 — Inspect the agent diff for push, splice, direct property assignment and stale closure reads

Inspect the agent diff for push, splice, direct property assignment and stale closure reads.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

### Step 5 — Test two rapid moves, delete after filter, duplicate title and empty-column behavior

Test two rapid moves, delete after filter, duplicate title and empty-column behavior.

**Pause and inspect:** Predict which files this step should touch and what will change on screen; compare that prediction with the actual diff before moving on.

**Evidence:** Run the narrowest check that exercises this step first; only then run the wider lint, type-check and build stack.

### Step 6 — Explain why state behaves as a snapshot, then lint, type-check and build

Explain why state behaves as a snapshot, then lint, type-check and build.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

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

## Independent challenge

Change one constraint related to state snapshot without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| tasks.push mutates state | push mutates in place — the habit most familiar from plain JavaScript. | Use spread or concat to build a new array, then re-run the movement tests. |

| Duplicated filtered state drifts | The filtered list was stored as a second state variable. | Delete the copy and derive visibleTasks during render. |

| setTasks([...tasks]) uses stale closure | The update read the tasks captured at render time, losing rapid consecutive updates. | Switch to the functional form setTasks(prev => ...). |

| Index used as identity | Position stood in for identity inside the transition helpers. | Look items up by stable id in every create, move and delete helper. |

## Reflection

How did state snapshot change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 3.1

Create, move and delete tasks with functional updates and immutable array transformations.


# Lab 3.2 — Synchronize and Clean Up Effects

> **Topic 3** · approximately 40 minutes · builds on the previous lab checkpoint

## Goal

Persist tasks locally with guarded parsing and understand effect dependencies and cleanup.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/hooks/usePersistentTasks.ts`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **useEffect** — The hook that synchronizes a component with an external system after render, such as storage, timers or the network.

- **dependency** — A reactive value listed in an effect's array; when it changes, the effect runs again.

- **cleanup** — The function an effect returns to undo its work before the next run or unmount.

- **localStorage** — A synchronous browser key-value store that persists strings across reloads; unencrypted and scoped per origin.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Define the external system: one versioned localStorage key containing synthetic task JSON

Define the external system: one versioned localStorage key containing synthetic task JSON.

**Pause and inspect:** Where the agent acts, read its output as a reviewer, not a spectator, and note one specific thing you checked.

**Evidence:** If this step touches the interface, re-test at both a narrow and a wide viewport and note anything that clips or overflows.

### Step 2 — Create a lazy state initializer that reads once and falls back safely on missing or malformed data

Create a lazy state initializer that reads once and falls back safely on missing or malformed data.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

### Step 3 — Add a save effect whose dependency reflects the value being synchronized

Add a save effect whose dependency reflects the value being synchronized.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

### Step 4 — Inspect StrictMode behavior and ensure the effect is idempotent rather than disabled

Inspect StrictMode behavior and ensure the effect is idempotent rather than disabled.

**Pause and inspect:** Predict which files this step should touch and what will change on screen; compare that prediction with the actual diff before moving on.

**Evidence:** Run the narrowest check that exercises this step first; only then run the wider lint, type-check and build stack.

### Step 5 — Test reload, cleared storage, malformed JSON, schema mismatch and storage write failure

Test reload, cleared storage, malformed JSON, schema mismatch and storage write failure.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

### Step 6 — Ask the agent to explain every dependency; reject lint suppression as a fix

Ask the agent to explain every dependency; reject lint suppression as a fix.

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

## Independent challenge

Change one constraint related to useEffect without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| Effect reads and writes in a loop | The save effect updated the same state it depended on. | Separate the read (lazy initializer) from the write (effect on tasks) so the cycle breaks. |

| JSON.parse crash blanks the app | Malformed stored data threw during the first render. | Wrap parsing in try/catch and fall back to the initial tasks. |

| Lint rule disabled | exhaustive-deps was suppressed instead of understood. | Remove the suppression and restructure until every dependency is honest. |

| Storage treated as secure | localStorage looked like a database, so sensitive data seemed fine. | Keep only synthetic, non-sensitive data client-side and record that rule in the brief. |

## Reflection

How did useEffect change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 3.2

Persist tasks locally with guarded parsing and understand effect dependencies and cleanup.


# Lab 3.3 — Extract a Tested Custom Hook

> **Topic 3** · approximately 35 minutes · builds on the previous lab checkpoint

## Goal

Separate reusable board logic into a custom hook without sharing state between consumers.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/hooks/useTaskBoard.ts`, `src/hooks/useTaskBoard.test.ts`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **custom hook** — A function starting with use that packages reusable stateful logic; each caller gets its own independent state.

- **logic reuse** — Sharing behavior between components by extracting hooks or functions, not by copying code.

- **public API** — The deliberate set of values and actions a hook or module exposes; everything else stays private.

- **hook test** — A test that exercises a hook through a consuming component or renderHook, asserting on outputs rather than internals.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — List the smallest public API: tasks, visibleTasks, filter, setFilter, create, move and remove

List the smallest public API: tasks, visibleTasks, filter, setFilter, create, move and remove.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

### Step 2 — Move stateful logic into `useTaskBoard` while keeping presentation in components

Move stateful logic into `useTaskBoard` while keeping presentation in components.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

### Step 3 — Inspect hook naming, top-level hook calls and dependency boundaries

Inspect hook naming, top-level hook calls and dependency boundaries.

**Pause and inspect:** Predict which files this step should touch and what will change on screen; compare that prediction with the actual diff before moving on.

**Evidence:** Run the narrowest check that exercises this step first; only then run the wider lint, type-check and build stack.

### Step 4 — Render two hook consumers and prove they do not share state unless state is lifted

Render two hook consumers and prove they do not share state unless state is lifted.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

### Step 5 — Add focused tests for initial state, filtering and immutable movement

Add focused tests for initial state, filtering and immutable movement.

**Pause and inspect:** Keep the agent inside the declared file scope here — if its proposal reaches further, stop and narrow the request.

**Evidence:** Capture the command, expected result and actual result; if they differ, stop and investigate before the next step.

### Step 6 — Refactor App to consume the hook; compare behavior before and after

Refactor App to consume the hook; compare behavior before and after.

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

## Independent challenge

Change one constraint related to custom hook without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| Hook called conditionally | A hook was placed behind an if, breaking the rules-of-hooks ordering. | Move the hook to the top level and branch inside its logic instead. |

| Hook returns unstable unnecessary objects | A fresh object was returned each render, causing needless downstream work. | Return only what the API needs and stabilize values only where measurement shows a problem. |

| Custom hook assumed to create global shared state | Reuse of logic was confused with sharing one state instance. | Demonstrate two independent consumers, then lift state to a common owner if sharing is required. |

| Presentation markup moved into logic hook | The extraction dragged JSX along with the state. | Return data and actions from the hook; keep rendering in components. |

## Reflection

How did custom hook change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 3.3

Separate reusable board logic into a custom hook without sharing state between consumers.


# Lab 3.4 — Add Declarative Routing and Dynamic Task Pages

> **Topic 3** · approximately 40 minutes · builds on the previous lab checkpoint

## Goal

Create board, task detail, about and not-found routes with accessible navigation.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/router.tsx`, `src/pages/BoardPage.tsx`, `src/pages/TaskPage.tsx`, `src/pages/NotFoundPage.tsx`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **URL as state** — Treating the address bar as application state, so views are shareable, bookmarkable and restorable.

- **route** — A mapping from a URL pattern to the component tree that should render for it.

- **dynamic parameter** — A URL segment such as :taskId whose value is read at render time to select one resource.

- **navigation** — Moving between routes with links or programmatic calls while browser history stays correct.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Install the current React Router package and record the version and command

Install the current React Router package and record the version and command.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

### Step 2 — Plan route objects for `/`, `/tasks/:taskId`, `/about` and a catch-all page

Plan route objects for `/`, `/tasks/:taskId`, `/about` and a catch-all page.

**Pause and inspect:** Predict which files this step should touch and what will change on screen; compare that prediction with the actual diff before moving on.

**Evidence:** Run the narrowest check that exercises this step first; only then run the wider lint, type-check and build stack.

### Step 3 — Create a shared layout with navigation and an outlet for child pages

Create a shared layout with navigation and an outlet for child pages.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

### Step 4 — Link each TaskCard to its detail URL; read the parameter and handle an unknown ID

Link each TaskCard to its detail URL; read the parameter and handle an unknown ID.

**Pause and inspect:** Keep the agent inside the declared file scope here — if its proposal reaches further, stop and narrow the request.

**Evidence:** Capture the command, expected result and actual result; if they differ, stop and investigate before the next step.

### Step 5 — Test links, browser back/forward, direct URL entry, refresh and keyboard focus after navigation

Test links, browser back/forward, direct URL entry, refresh and keyboard focus after navigation.

**Pause and inspect:** Where the agent acts, read its output as a reviewer, not a spectator, and note one specific thing you checked.

**Evidence:** If this step touches the interface, re-test at both a narrow and a wide viewport and note anything that clips or overflows.

### Step 6 — Inspect for anchor misuse, imperative navigation where Link is clearer, and blank not-found output

Inspect for anchor misuse, imperative navigation where Link is clearer, and blank not-found output.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

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

## Independent challenge

Change one constraint related to URL as state without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| Using window.location for internal navigation | A full-page navigation habit carried over from multi-page sites. | Use Link or useNavigate so routing stays client-side and state survives. |

| Missing not-found route | Only the happy paths were mapped. | Add a catch-all route with a useful page and a link back to the board. |

| Unknown ID crashes | The detail page assumed find() always returns a task. | Handle undefined explicitly with a friendly unknown-task state. |

| Direct refresh fails in deployment | Static hosts return 404 for URLs that exist only client-side. | Document and configure an SPA fallback rewrite to index.html for the chosen host. |

## Reflection

How did URL as state change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 3.4

Create board, task detail, about and not-found routes with accessible navigation.


# Lab 3.5 — Fetch API Data with Loading, Empty, Error and Retry States

> **Topic 3** · approximately 45 minutes · builds on the previous lab checkpoint

## Goal

Replace local seed data with a controlled fetch pipeline and resilient user-visible states.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `public/tasks.json`, `src/hooks/useTasksApi.ts`, `src/components/AsyncState.tsx`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **fetch** — The browser API that performs HTTP requests and resolves with a Response — rejecting only on network failure, not on HTTP error status.

- **response.ok** — The Response flag that is true only for 2xx status codes; skipping this check treats a 404 page as data.

- **AbortController** — The API that cancels an in-flight fetch, used in effect cleanup to prevent updates after unmount.

- **state machine** — Modeling a process as named states and transitions — idle, loading, success, empty, error — so no combination is ambiguous.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Create a local JSON endpoint with synthetic tasks so the lab needs no credentials

Create a local JSON endpoint with synthetic tasks so the lab needs no credentials.

**Pause and inspect:** Predict which files this step should touch and what will change on screen; compare that prediction with the actual diff before moving on.

**Evidence:** Run the narrowest check that exercises this step first; only then run the wider lint, type-check and build stack.

### Step 2 — Model idle/loading/success/empty/error rather than a single ambiguous boolean

Model idle/loading/success/empty/error rather than a single ambiguous boolean.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

### Step 3 — Fetch inside an effect, check `response.ok`, validate the payload and abort on cleanup

Fetch inside an effect, check `response.ok`, validate the payload and abort on cleanup.

**Pause and inspect:** Keep the agent inside the declared file scope here — if its proposal reaches further, stop and narrow the request.

**Evidence:** Capture the command, expected result and actual result; if they differ, stop and investigate before the next step.

### Step 4 — Expose a retry action and a useful error message without leaking stack traces

Expose a retry action and a useful error message without leaking stack traces.

**Pause and inspect:** Where the agent acts, read its output as a reviewer, not a spectator, and note one specific thing you checked.

**Evidence:** If this step touches the interface, re-test at both a narrow and a wide viewport and note anything that clips or overflows.

### Step 5 — Test normal data, empty array, invalid JSON, 404 path, slow network and component unmount

Test normal data, empty array, invalid JSON, 404 path, slow network and component unmount.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

### Step 6 — Inspect for requests during render, missing cleanup, swallowed errors and endless spinner

Inspect for requests during render, missing cleanup, swallowed errors and endless spinner.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

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

## Independent challenge

Change one constraint related to fetch without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| fetch during render | The request was issued in the component body, firing on every render. | Move the fetch into useEffect with correct dependencies and abort cleanup. |

| No response.ok check | fetch resolves on HTTP errors, so a 404 body was parsed as data. | Branch on response.ok and route failures to the error state. |

| Abort reported as user error | The AbortError raised by cleanup was caught by the generic error handler. | Detect AbortError and return silently instead of setting the error state. |

| Error leaves loading true forever | The failure path never transitioned the state machine. | Set an explicit error state — or use finally — and expose a retry action. |

## Reflection

How did fetch change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 3.5

Replace local seed data with a controlled fetch pipeline and resilient user-visible states.


## Topic 4: Debugging, Testing and Deploying React Apps with AI

Diagnose failures, generate focused tests, optimize and document the app, and deploy a verified production build.

# Lab 4.1 — Run an Evidence-Led Debugging Loop

> **Topic 4** · approximately 35 minutes · builds on the previous lab checkpoint

## Goal

Reproduce, isolate and fix a controlled stale-state defect with a minimal reviewed patch.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/hooks/useTaskBoard.ts`, `docs/debug-log.md`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **reproduction** — An exact sequence of steps that reliably shows a defect, turning a report into an experiment.

- **hypothesis** — A specific, testable explanation of a defect that predicts what an experiment will show.

- **root cause** — The underlying condition that produces a symptom; fixing it prevents recurrence, while patching the symptom does not.

- **minimal patch** — The smallest change that makes the failing check pass, keeping the diff reviewable and the risk bounded.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Create a branch and introduce a controlled defect that loses one of two rapid task moves

Create a branch and introduce a controlled defect that loses one of two rapid task moves.

**Pause and inspect:** Predict which files this step should touch and what will change on screen; compare that prediction with the actual diff before moving on.

**Evidence:** Run the narrowest check that exercises this step first; only then run the wider lint, type-check and build stack.

### Step 2 — Write exact reproduction steps, expected result, actual result and evidence in the debug log

Write exact reproduction steps, expected result, actual result and evidence in the debug log.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

### Step 3 — Ask the agent for three ranked hypotheses and the smallest experiment for each; do not request a fix yet

Ask the agent for three ranked hypotheses and the smallest experiment for each; do not request a fix yet.

**Pause and inspect:** Keep the agent inside the declared file scope here — if its proposal reaches further, stop and narrow the request.

**Evidence:** Capture the command, expected result and actual result; if they differ, stop and investigate before the next step.

### Step 4 — Run the experiments, identify the stale closure, and approve one functional-update patch

Run the experiments, identify the stale closure, and approve one functional-update patch.

**Pause and inspect:** Where the agent acts, read its output as a reviewer, not a spectator, and note one specific thing you checked.

**Evidence:** If this step touches the interface, re-test at both a narrow and a wide viewport and note anything that clips or overflows.

### Step 5 — Inspect the diff for unrelated refactors and add a regression test before accepting

Inspect the diff for unrelated refactors and add a regression test before accepting.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

### Step 6 — Run the complete verification stack and document why the original code failed

Run the complete verification stack and document why the original code failed.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

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

## Independent challenge

Change one constraint related to reproduction without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| Agent rewrites the hook | An open-ended 'fix it' request authorized a broad rewrite. | Restore the checkpoint and re-ask for diagnosis only, then one minimal patch. |

| Symptom patched without root cause | The first plausible change made the visible symptom disappear. | Demand the proven hypothesis first; revert patches that cannot name the cause. |

| Reproduction not repeatable | The defect report described an impression, not exact steps. | Write numbered steps with expected versus actual results before diagnosing. |

| Regression test omitted | The fix felt complete once the app behaved. | Add a test that fails on the old code and passes on the new, then commit both together. |

## Reflection

How did reproduction change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 4.1

Reproduce, isolate and fix a controlled stale-state defect with a minimal reviewed patch.


# Lab 4.2 — Test User Behaviour with Vitest and Testing Library

> **Topic 4** · approximately 45 minutes · builds on the previous lab checkpoint

## Goal

Build a focused test suite for rendering, filtering, task movement, forms and routes.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `src/test/setup.ts`, `src/App.test.tsx`, `src/components/TaskForm.test.tsx`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **test** — An automated check that drives behavior, asserts an observable result and fails loudly when that behavior regresses.

- **assertion** — A single expected-versus-actual claim inside a test; when it fails, it names precisely what broke.

- **user event** — A simulated interaction — typing, clicking, tabbing — that drives tests through the same paths a person uses.

- **accessible query** — Finding elements by role and accessible name, so tests verify what assistive technology can perceive.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Install Vitest, jsdom, Testing Library, jest-dom and user-event; pin and record versions

Install Vitest, jsdom, Testing Library, jest-dom and user-event; pin and record versions.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

### Step 2 — Configure the test environment and add an explicit `test` script

Configure the test environment and add an explicit `test` script.

**Pause and inspect:** Keep the agent inside the declared file scope here — if its proposal reaches further, stop and narrow the request.

**Evidence:** Capture the command, expected result and actual result; if they differ, stop and investigate before the next step.

### Step 3 — Write a smoke test using role and accessible-name queries rather than CSS selectors

Write a smoke test using role and accessible-name queries rather than CSS selectors.

**Pause and inspect:** Where the agent acts, read its output as a reviewer, not a spectator, and note one specific thing you checked.

**Evidence:** If this step touches the interface, re-test at both a narrow and a wide viewport and note anything that clips or overflows.

### Step 4 — Add behaviour tests for filtering, valid/invalid form submit and moving a task

Add behaviour tests for filtering, valid/invalid form submit and moving a task.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

### Step 5 — Add a MemoryRouter test for task details and not-found behavior

Add a MemoryRouter test for task details and not-found behavior.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

### Step 6 — Run tests in watch and single-run modes; inspect generated assertions for false confidence

Run tests in watch and single-run modes; inspect generated assertions for false confidence.

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

## Independent challenge

Change one constraint related to test without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| Testing internal state | Asserting on hook variables felt more precise than the UI. | Rewrite assertions against what the user sees, via accessible queries. |

| fireEvent used for realistic typing | fireEvent skips the keyboard events real typing produces. | Use user-event's type and click helpers and await them. |

| Assertions pass without awaiting user events | The assertion ran before the interaction finished. | await every user-event call and prove the test can fail by breaking the code. |

| Snapshot replaces behavior checks | A snapshot asserted everything and therefore nothing specific. | Replace it with targeted role/name assertions for the flows that matter. |

## Reflection

How did test change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 4.2

Build a focused test suite for rendering, filtering, task movement, forms and routes.


# Lab 4.3 — Audit Accessibility and Error Recovery

> **Topic 4** · approximately 35 minutes · builds on the previous lab checkpoint

## Goal

Perform keyboard, semantics, focus, contrast and recovery checks and fix only evidenced defects.

## The build so far

SprintBoard grows through one continuous sequence. Begin from the previous lab checkpoint. In this lab you add a bounded capability and finish with a recoverable Git checkpoint.

## What you will build

A verified increment touching: `docs/accessibility-audit.md`, `src/components/AsyncState.tsx`. The increment is complete only when the observable checks pass and the generated diff can be explained.

## Concepts you will meet

- **keyboard access** — Every interactive control reachable and operable with Tab, Enter and Space alone.

- **focus management** — Deliberately moving keyboard focus after navigation or errors so users are never stranded.

- **live region** — An area assistive technology announces when its content changes, used for errors and status messages.

- **error recovery** — Giving the user a way back — retry, undo or clear guidance — after something fails.

## Prerequisites

- Complete or restore the previous Git checkpoint.

- Start the development server and confirm the existing flow works.

- Use synthetic data and placeholders. Never paste credentials or private data into an AI prompt.

- Read `AGENTS.md` and keep the agent inside the named file scope.

## Steps

### Step 1 — Navigate the complete app using only Tab, Shift+Tab, Enter, Space and browser back

Navigate the complete app using only Tab, Shift+Tab, Enter, Space and browser back.

**Pause and inspect:** Keep the agent inside the declared file scope here — if its proposal reaches further, stop and narrow the request.

**Evidence:** Capture the command, expected result and actual result; if they differ, stop and investigate before the next step.

### Step 2 — Inspect landmarks, heading order, control names and error announcements in the accessibility tree

Inspect landmarks, heading order, control names and error announcements in the accessibility tree.

**Pause and inspect:** Where the agent acts, read its output as a reviewer, not a spectator, and note one specific thing you checked.

**Evidence:** If this step touches the interface, re-test at both a narrow and a wide viewport and note anything that clips or overflows.

### Step 3 — Check contrast, 200 percent zoom, narrow viewport and prefers-reduced-motion

Check contrast, 200 percent zoom, narrow viewport and prefers-reduced-motion.

**Pause and inspect:** If the result differs from your prediction, treat the gap as information: find the exact line that explains it before continuing.

**Evidence:** Ask the agent to explain any part of this step's diff you cannot explain yourself; unresolved lines block the checkpoint.

### Step 4 — Trigger form and network errors; verify focus and retry guidance lead to recovery

Trigger form and network errors; verify focus and retry guidance lead to recovery.

**Pause and inspect:** Record the evidence for this step while it is still on screen — a command line and its output beat a memory.

**Evidence:** When this step passes, decide keep, refine or revert explicitly and write one sentence recording why.

### Step 5 — Ask the agent to rank findings by user impact and propose one file-scoped patch per finding

Ask the agent to rank findings by user impact and propose one file-scoped patch per finding.

**Pause and inspect:** Predict which files this step should touch and what will change on screen; compare that prediction with the actual diff before moving on.

**Evidence:** Run the narrowest check that exercises this step first; only then run the wider lint, type-check and build stack.

### Step 6 — Retest each corrected behavior and record evidence rather than marking a generic compliance checkbox

Retest each corrected behavior and record evidence rather than marking a generic compliance checkbox.

**Pause and inspect:** Say out loud what success looks like for this step before acting; afterwards capture the command output or screenshot that proves it.

**Evidence:** Verify the failure path as well as the success path — break the input deliberately and confirm the app responds as designed.

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

## Independent challenge

Change one constraint related to keyboard access without widening the product scope. Predict the files and tests first, then run Frame, Plan, Generate, Inspect, Verify, Correct and Commit; compare the prediction with the actual diff.

## Troubleshooting and recovery

| Symptom | Likely cause | Recovery |

|---|---|---|

| Automated scan treated as complete | A clean scanner report was read as full accessibility. | Add manual keyboard and accessibility-tree checks; scanners find only part of the problem. |

| Focus indicator removed | The default focus ring was styled away without a replacement. | Add a high-contrast :focus-visible style and retest the tab order. |

| Error appears visually but is not announced | The message div carried no live-region semantics. | Use role=alert or aria-live and verify the announcement in the accessibility tree. |

| Color-only status | Status meaning lived entirely in the badge color. | Add visible text or an icon and re-check with a grayscale filter. |

## Reflection

How did keyboard access change what the user could observe? Which evidence most increased or reduced your trust in the generated change? What context should the next lab preserve?

### SprintBoard after Lab 4.3

Perform keyboard, semantics, focus, contrast and recovery checks and fix only evidenced defects.


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
