# Lab 1: Scaffold SprintBoard with an AI Coding Contract

## Goal

Create a Vite React TypeScript app from a bounded prompt and verify a trustworthy baseline.

## What you will build

A tested increment of the SprintBoard React capstone.

## Prerequisites

Required tools installed and a writable folder.

## Steps

1. Install Node.js LTS, Git, VS Code, and an approved AI coding assistant such as Cursor, GitHub Copilot, or Claude.
2. Run `npm create vite@latest sprintboard -- --template react-ts`, then `cd sprintboard && npm install && git init`.
3. Create `AGENTS.md` with these constraints: plan first, name changed files, use TypeScript, add no dependency without justification, use placeholders only, and show verification commands before acceptance.
4. Ask the agent to explain `src/main.tsx`, `src/App.tsx`, `package.json`, and the Vite scripts, then propose a three-step plan for a SprintBoard shell. Inspect the plan and reject unrelated work.
5. Approve only the first increment: a semantic header, main area, and footer in `src/App.tsx`, with focused styles in `src/App.css`.
6. Run `npm run dev`, `npm run lint`, and `npm run build`; inspect the page at desktop and mobile width.
7. Run `git diff -- src/App.tsx src/App.css AGENTS.md`. Review every line, then commit the checkpoint with `git add AGENTS.md src/App.tsx src/App.css && git commit -m "feat: scaffold SprintBoard"`.

## Test it

The Vite app runs, displays the SprintBoard shell, passes lint/build, and contains only approved changes.

## Troubleshooting

- Narrow an oversized agent change and retry one behavior at a time.
- Read the first error, inspect imports and types, then rerun the verification command.
- Revert to the previous Git checkpoint when the diff cannot be explained.
- Use only synthetic data and credential placeholders.

## Evidence to submit

Approved prompt and plan, browser screenshot, lint/build output, and reviewed `git diff --stat`.

## Reflection

What did the agent propose, what did you verify, and what did you change before acceptance?
