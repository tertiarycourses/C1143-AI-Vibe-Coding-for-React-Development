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
