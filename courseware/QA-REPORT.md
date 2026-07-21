# C1143 Non-WSQ Courseware QA Report — Version 3.0

- **Result:** PASS
- **QA date:** 21 July 2026
- **Course:** AI Vibe Coding for React Development (C1143)

## Package

Version 3.0 mirrors the flagship two-day Full Stack React with Vibe Coding courseware, adapted for non-assessed C1143 delivery. All artifacts are generated from one source (`courseware/build/`):

- 214-slide 16:9 facilitator deck (`AI Vibe Coding for React Development-v3.0.pptx` + PDF)
- 133-page Learner Guide (DOCX + PDF + aligned Markdown) with page-numbered TOC
- Lesson Plan (DOCX + PDF) — two 480-minute training days, page-numbered TOC
- 25 hands-on labs across six topics with README instructions and drop-in checkpoint snapshots

## Content-safety gate (blocking) — PASS

Full-text scan of all 214 slides, the Learner Guide, the Lesson Plan and all 25 lab READMEs: zero occurrences of funded-programme content — no SSG, SkillsFuture, TRAQOM, digital attendance, 75% attendance rule, funding/subsidy text, and no formal assessment instruments. The deck carries the "How You'll Learn" flow and the Lesson Plan a "Learning Reinforcement" section in place of assessment administration.

## Independent audit findings and fixes (this version)

1. **Topic 5 traceability** — the documents' lab split now matches the `labs/topic-5-backend-api` folders one-for-one (5.1 Three Tiers/API routes + injection probe, 5.2 Fetch from React, 5.3 Accounts with bcrypt + JWT, 5.4 Protected CRUD with ownership in SQL), and the Topic-5 code-walkthrough slides sit under the correct labs. Verified against folder READMEs.
2. **Lab-overview slides** — long descriptions now auto-shrink; the previously clipped slides (Labs 3.1, 3.2, 5.1, 6.6) were re-rendered and visually confirmed complete.
3. **Learner Guide TOC** — page numbers corrected for the TOC's own extent; spot-checked entries (Introduction, all four Topic-5 labs) land on the exact printed page.
4. **Wording** — the "exam of the whole course" metaphor removed from the mini-capstone (now "payoff of the whole course").
5. **README** rewritten for the v3.0 package.

## Verified

- Branding: title, code C1143, Version v3.0 · 21 July 2026 on the deck cover and in both Document Version Control Records (rows 2.0 / 2.1 / 3.0); filenames match the version.
- Deck bookends: cover, two About-the-Trainer profile cards, ground rules, Lesson Plan slide, Learning Outcomes, How You'll Learn; wrap-up, Bug Checklist, Course Materials, Thank You as the final slide.
- Lesson Plan: each day totals exactly 480 training minutes (lunch excluded); Day 2 closes with Labs 6.4–6.6 (deploy + mini-capstone) and a wrap-up — no assessment rows.
- Learner Guide: populated page-numbered TOC, per-topic intros, key concepts, concepts-explained sections, 24 deep dives, all 25 labs, three appendices.
- Traceability: deck, LG, LP and the labs/ folder agree on all 25 labs across six topics; footers carry the C1143 title throughout.
- Rendered-page inspection of covers, admin slides, topic sections, previously defective slides and closing slides: no overflow, clipping or blank pages.

## Final status

The C1143 version 3.0 package passed audit and is ready for publication.
