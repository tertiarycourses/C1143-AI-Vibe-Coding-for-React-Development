# C1143 — React AI Vibe Coding for React Development

[![Course](https://img.shields.io/badge/course-C1143-0B6E99)](https://www.tertiarycourses.com.sg/react-essential-training.html)
[![Duration](https://img.shields.io/badge/duration-15%20hours-17365D)](#course-structure)
[![Level](https://img.shields.io/badge/level-intermediate-2E7D5B)](#course-structure)

Professional non-WSQ courseware for a two-day, hands-on React development course using AI coding assistants and an evidence-led plan–diff–verify workflow.

## Preview

![C1143 courseware preview](screenshot.png)

## About

Learners build one connected capstone, **SprintBoard**, across four labs. They scaffold a Vite React TypeScript project, compose accessible UI, add state/hooks/routing/API data, then debug, test, optimize, and deploy the app. Every lab requires learners to inspect the AI plan and diff before accepting generated code.

## Course structure

| Item | Detail |
|---|---|
| Course code | C1143 |
| Duration | 15 instructional hours / 2 days |
| Level | Intermediate |
| Capstone | SprintBoard React single-page application |
| Published outline | [Tertiary Courses course page](https://www.tertiarycourses.com.sg/react-essential-training.html) |

## Deliverables

- 16:9 facilitator slide deck
- Learner Guide in Markdown and Word
- Word Lesson Plan with aligned 900-minute schedule
- Four connected, executable labs
- Project-scoped `non-wsq-*` generation and QA automation

## Project structure

```text
courseware/
  C1143-Facilitator-Deck.pptx
  C1143-Learner-Guide.docx
  C1143-Learner-Guide.md
  C1143-Lesson-Plan.docx
  QA-REPORT.md
  labs/
scripts/
  non-wsq-build-courseware.py
  non-wsq-build-presentation.mjs
.claude/
  agents/ commands/ hooks/
```

## Regenerate

Run the document generator with Python 3 and `python-docx`. The presentation generator uses the bundled OpenAI artifact tool runtime. Generated artifacts are written to `courseware/`.

## Quality controls

The package checks artifact completeness, duration alignment, topic order, lab structure, prohibited programme language, naming isolation, secret exposure, and rendered visual quality.

## Credits

Courseware produced for [Tertiary Infotech Academy Pte Ltd](https://www.tertiaryinfotech.com/). Source outline: [React AI Vibe Coding for React Development](https://www.tertiarycourses.com.sg/react-essential-training.html).
