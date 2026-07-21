# C1143 — AI Vibe Coding for React Development

[![Course](https://img.shields.io/badge/course-C1143-0B6E99)](https://www.tertiarycourses.com.sg/ai-vibe-coding-for-react-development.html)
[![Duration](https://img.shields.io/badge/duration-2%20days-17365D)](#course-structure)
[![Level](https://img.shields.io/badge/level-intermediate-2E7D5B)](#course-structure)

Professional non-WSQ courseware for a two-day, hands-on React course built around vibe coding: prompting an AI coding agent, then reading, understanding and correcting everything it writes. Learners build one full-stack application — **Cook & Bake Academy**, a cooking & bakery school website over a real Postgres database — from an empty folder to a live deployment.

## Preview

![C1143 courseware preview](screenshot.png)

## About

Across 25 progressive labs in six topics, learners scaffold a Vite + React app, deploy it to the cloud, learn core React (the real DOM vs the Virtual DOM, Babel and JSX, props, lists and keys, events), master hooks, add a serverless API over Neon Postgres with bcrypt + JWT authentication, and ship a multi-page app with React Router — closing with a mini-capstone where they add a whole feature on their own. Every lab runs the same loop: **Prompt → Generate → Read → Understand → Correct**. There is no assessment — learning is verified through each lab's observable "Test it" check and the capstone.

## Course structure

| Item | Detail |
|---|---|
| Course code | C1143 |
| Duration | 2 days · 8 training hours per day |
| Level | Intermediate (working JavaScript assumed) |
| Project | Cook & Bake Academy — full-stack React catalogue on Neon Postgres + Vercel |
| Topics | Vibe coding · Cloud deployment · Core React · Hooks · Backend API & database · React Router |
| Published outline | [Tertiary Courses course page](https://www.tertiarycourses.com.sg/ai-vibe-coding-for-react-development.html) |

## Deliverables

- 214-slide, 16:9 facilitator deck (concept slides with real code + analogies, diagrams, per-lab code walkthroughs)
- 130+ page Learner Guide (DOCX + PDF + aligned Markdown) with deep dives, the AI React Bug Checklist, troubleshooting and a glossary
- Lesson Plan (DOCX + PDF) with colour-coded 480-minute daily schedules
- 25 hands-on labs with README instructions and drop-in `src`/`api` checkpoint snapshots

## Project structure

```text
courseware/
  AI Vibe Coding for React Development-v3.0.pptx / .pdf
  LG-AI Vibe Coding for React Development.docx / .pdf / .md
  LP-AI Vibe Coding for React Development.docx / .pdf
  QA-REPORT.md
  assets/            logos and diagram images
  build/             single-source generators (course_data.py + data_domain1-6.py)
  archive/           superseded versions
labs/
  topic-1-vibe-coding/          topic-4-react-hooks/
  topic-2-deploy-to-cloud/      topic-5-backend-api/
  topic-3-core-react-concepts/  topic-6-react-router/   (25 labs)
```

## Regenerate

All artifacts are generated from one source (`courseware/build/course_data.py` + `data_domain1-6.py`):

```bash
bash courseware/build/build_courseware.sh
```

Requires Python 3 with `python-pptx`, `python-docx` and `pypdf`; PDFs are rendered with LibreOffice and the page-numbered TOCs injected with `build/inject_toc.py`.

## Quality controls

Every build is audited for artifact completeness, topic/lab traceability across the deck, Learner Guide, Lesson Plan and labs, 480-minute daily schedule totals, rendered visual quality, and the absence of any funded-programme or assessment content.

## Credits

Courseware produced for [Tertiary Infotech Academy Pte Ltd](https://www.tertiaryinfotech.com/). Course page: [AI Vibe Coding for React Development](https://www.tertiarycourses.com.sg/ai-vibe-coding-for-react-development.html).
