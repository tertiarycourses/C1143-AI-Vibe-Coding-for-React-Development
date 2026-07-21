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
