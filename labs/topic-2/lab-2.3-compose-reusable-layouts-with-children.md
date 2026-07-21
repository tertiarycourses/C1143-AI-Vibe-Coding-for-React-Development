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
