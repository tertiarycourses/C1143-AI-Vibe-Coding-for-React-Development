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
