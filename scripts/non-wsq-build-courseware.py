from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "courseware"
LABS = OUT / "labs"
OUT.mkdir(exist_ok=True); LABS.mkdir(exist_ok=True)

TITLE = "React AI Vibe Coding for React Development"
CODE = "C1143"
VERSION = "1.0"
SOURCE = "https://www.tertiarycourses.com.sg/react-essential-training.html"

topics = [
 ("Topic 1 — Getting Started with AI Vibe Coding for React", "Set up an AI coding assistant, scaffold a Vite React app from a prompt, and establish a plan–diff–verify workflow."),
 ("Topic 2 — Building React Components and UI with AI", "Generate function components and JSX, compose reusable UI, pass data with props, handle events, and refine AI-generated CSS."),
 ("Topic 3 — State, Hooks and Routing with AI Assistance", "Manage state and effects, add React Router, fetch API data, and refactor generated code without changing behavior."),
 ("Topic 4 — Debugging, Testing and Deploying React Apps with AI", "Diagnose failures, generate focused unit tests, optimize and document code, and deploy a verified production build."),
]

labs = [
 (1, "Scaffold SprintBoard with an AI Coding Contract", "Create a Vite React TypeScript app from a bounded prompt and verify a trustworthy baseline.", [
  "Install Node.js LTS, Git, VS Code, and an approved AI coding assistant such as Cursor, GitHub Copilot, or Claude.",
  "Run `npm create vite@latest sprintboard -- --template react-ts`, then `cd sprintboard && npm install && git init`.",
  "Create `AGENTS.md` with these constraints: plan first, name changed files, use TypeScript, add no dependency without justification, use placeholders only, and show verification commands before acceptance.",
  "Ask the agent to explain `src/main.tsx`, `src/App.tsx`, `package.json`, and the Vite scripts, then propose a three-step plan for a SprintBoard shell. Inspect the plan and reject unrelated work.",
  "Approve only the first increment: a semantic header, main area, and footer in `src/App.tsx`, with focused styles in `src/App.css`.",
  "Run `npm run dev`, `npm run lint`, and `npm run build`; inspect the page at desktop and mobile width.",
  "Run `git diff -- src/App.tsx src/App.css AGENTS.md`. Review every line, then commit the checkpoint with `git add AGENTS.md src/App.tsx src/App.css && git commit -m \"feat: scaffold SprintBoard\"`."],
  "The Vite app runs, displays the SprintBoard shell, passes lint/build, and contains only approved changes.",
  "Approved prompt and plan, browser screenshot, lint/build output, and reviewed `git diff --stat`."),
 (2, "Compose a Reusable Sprint UI", "Build an accessible task board with JSX, components, props, events, and responsive CSS.", [
  "Create `src/data/tasks.ts` with six synthetic tasks using `id`, `title`, `owner`, `status`, and `points`; include no personal or production data.",
  "Ask the agent for a component plan covering `Board`, `TaskColumn`, `TaskCard`, and `StatusFilter`. Require props and event contracts plus the exact file list.",
  "Inspect the plan and approve only the named components, `src/types.ts`, `src/data/tasks.ts`, `src/App.tsx`, and CSS files.",
  "Generate function components with typed props. Render tasks with stable IDs, semantic headings and buttons, and a useful empty state for a column with no tasks.",
  "Add a status filter and a Move Forward event. Keep task state in `App` for now and pass data/callbacks explicitly through props.",
  "Ask the agent to generate responsive CSS for 375 px and 1280 px widths, visible keyboard focus, and sufficient contrast. Inspect the CSS rather than accepting aesthetic claims.",
  "Test every filter, move one task, tab through all controls, then run `npm run lint` and `npm run build`. Review the complete diff before committing."],
  "Six tasks render in reusable columns; filtering, event handling, keyboard navigation, empty state, and both target widths work.",
  "Desktop/mobile screenshots, keyboard checklist, lint/build output, and one paragraph explaining the chosen component boundaries."),
 (3, "Add State, Hooks, Routing, and API Data", "Turn SprintBoard into a multi-page app with controlled state, effects, and resilient API fetching.", [
  "Install React Router with `npm install react-router-dom` and record the command in the project README.",
  "Ask the agent to plan routes for `/`, `/tasks/:taskId`, and `/about`, plus a not-found route. Require a rollback note and no unrelated styling rewrite.",
  "Inspect and approve the routing files, then add navigation, a task details view, and a useful not-found page. Test direct URL entry as well as link navigation.",
  "Create `public/tasks.json` with synthetic task data. Ask for a small `useTasks` hook that models loading, success, empty, and error states using `useEffect` and `AbortController`.",
  "Review effect dependencies and cleanup. Reject suppressed lint rules, duplicated state, or use of `any`. Implement immutable status updates with functional `setState`.",
  "Test the normal response, an empty array, and a deliberately broken URL; restore the working URL after observing the error UI.",
  "Ask the agent to refactor one duplicated UI pattern without changing behavior. Compare before/after diffs, then run `npm run lint` and `npm run build`."],
  "All routes work, task data loads with visible state transitions, failures recover cleanly, and the reviewed refactor preserves behavior.",
  "Route screenshots, loading/error evidence, hook explanation, dependency review, and lint/build output."),
 (4, "Debug, Test, Optimize, and Deploy SprintBoard", "Use AI to diagnose a defect, add focused tests, improve production quality, and publish the app.", [
  "Install Vitest and Testing Library using `npm install -D vitest jsdom @testing-library/react @testing-library/jest-dom @testing-library/user-event`; add an explicit `test` script.",
  "Introduce a controlled defect in a branch: make Move Forward skip a status. Capture the failing behavior before asking the agent to diagnose it.",
  "Give the agent the exact reproduction steps and relevant files. Require root-cause reasoning, one minimal patch, and a regression test; inspect the plan and diff before acceptance.",
  "Generate tests for initial rendering, filtering, moving a task, API error UI, and one route. Prefer behavior assertions over implementation details.",
  "Run `npm test -- --run`, `npm run lint`, and `npm run build`. Fix failures one at a time and reject broad rewrites or deleted assertions.",
  "Ask for a production review covering bundle warnings, accessibility, component documentation, error handling, and removal of debug logs. Apply only evidence-backed improvements.",
  "Deploy the `dist` output to an approved static host such as GitHub Pages, Netlify, or Vercel. Verify direct-route behavior and document the public URL and rollback method.",
  "Run `git diff --check` and scan the final diff for secrets, tokens, placeholder mistakes, and unrelated files before the final checkpoint."],
  "All tests, lint, and production build pass; the regression is fixed; the deployed app loads and core flows work at the public URL.",
  "Failing/passing test output, final quality-command output, deployment URL and screenshot, reviewed diff, and reflection on one AI suggestion changed or rejected."),
]

def set_cell_shading(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr(); shd = OxmlElement('w:shd'); shd.set(qn('w:fill'), fill); tcPr.append(shd)

def setup(doc, subtitle):
    sec=doc.sections[0]; sec.top_margin=Inches(.75); sec.bottom_margin=Inches(.7); sec.left_margin=Inches(.8); sec.right_margin=Inches(.8)
    styles=doc.styles
    for name,size,color in [('Normal',10.5,'222222'),('Title',28,'17365D'),('Heading 1',18,'0B6E99'),('Heading 2',14,'17365D'),('Heading 3',11.5,'0B6E99')]:
        st=styles[name]; st.font.name='Arial'; st.font.size=Pt(size); st.font.color.rgb=RGBColor.from_string(color)
    footer=sec.footer.paragraphs[0]; footer.alignment=WD_ALIGN_PARAGRAPH.CENTER
    footer.add_run(f"Tertiary Infotech Academy Pte Ltd  |  {CODE}  |  {subtitle}  |  v{VERSION}").font.size=Pt(8)

def cover(doc, docname):
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.space_after=Pt(20)
    r=p.add_run('TERTIARY INFOTECH ACADEMY'); r.bold=True; r.font.name='Arial'; r.font.size=Pt(15); r.font.color.rgb=RGBColor(11,110,153)
    p=doc.add_paragraph(style='Title'); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.add_run(TITLE)
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.add_run(f"{docname}\nCourse Code: {CODE}\nVersion {VERSION}").bold=True
    doc.add_paragraph('')
    t=doc.add_table(rows=4, cols=2); t.style='Table Grid'
    for i,(a,b) in enumerate([('Duration','15 hours / 2 days'),('Level','Intermediate'),('Delivery','Instructor-led with guided hands-on practice'),('Source alignment','Published C1143 React topic sequence')]):
        t.cell(i,0).text=a; t.cell(i,1).text=b; set_cell_shading(t.cell(i,0),'DDEBF7')
    doc.add_page_break()

def frontmatter(doc):
    doc.add_heading('Document Version Control Record',1)
    t=doc.add_table(rows=2, cols=4); t.style='Table Grid'
    for j,x in enumerate(['Version','Date','Author','Change']): t.cell(0,j).text=x; set_cell_shading(t.cell(0,j),'0B6E99'); t.cell(0,j).paragraphs[0].runs[0].font.color.rgb=RGBColor(255,255,255)
    for j,x in enumerate([VERSION,'11 July 2026','Tertiary Infotech Academy','Initial non-WSQ release']): t.cell(1,j).text=x
    doc.add_heading('Table of Contents',1)
    doc.add_paragraph('Update this automatic table in Microsoft Word: References → Update Table.', style=None)

def save_doc(doc, path): doc.save(path)

# Learner Guide
d=Document(); setup(d,'Learner Guide'); cover(d,'Learner Guide'); frontmatter(d)
d.add_heading('Course Overview',1); d.add_paragraph('Build and deploy a modern React single-page application by collaborating responsibly with an AI coding assistant. You will turn product intent into reviewed plans, controlled diffs, tested components, and verified production code. The SprintBoard capstone grows across four connected labs.')
d.add_heading('Learning Outcomes',1)
for x in ['Scaffold and explain a Vite React TypeScript project using an AI coding assistant.','Generate accessible JSX, reusable components, props, events, and responsive CSS.','Manage state and effects, route between pages, and fetch API data with resilient UI states.','Debug, test, optimize, document, and deploy reviewed AI-generated React code.']: d.add_paragraph(x,style='List Bullet')
d.add_heading('Prerequisites and Setup',1); d.add_paragraph('Intermediate level. Learners should know basic HTML, CSS, JavaScript and ES6 or TypeScript. Install Node.js LTS, Git, VS Code, a modern browser, and an approved AI coding assistant. Use synthetic data and placeholders only; never paste credentials, client data, or private source code into prompts.')
for h,desc in topics: d.add_heading(h,1); d.add_paragraph(desc)
d.add_heading('The Vibe Coding Review Loop',1)
for x in ['Frame the outcome and constraints.','Ask for a plan and file list.','Inspect scope, dependencies and risks.','Approve one small increment.','Review the diff line by line.','Run type checks and device tests.','Keep or revert based on evidence.']: d.add_paragraph(x,style='List Number')
d.add_heading('Lab Guide',1)
for n,name,goal,steps,test,evidence in labs:
    d.add_heading(f'Lab {n}: {name}',2); d.add_paragraph(f'Goal: {goal}')
    d.add_paragraph(f'Prerequisite: Complete Lab {n-1} and keep its Git checkpoint.' if n>1 else 'Prerequisite: Required tools installed and a writable working folder.')
    d.add_paragraph('Procedure',style='Heading 3')
    for i,s in enumerate(steps,1): d.add_paragraph(f'{i}. {s}')
    d.add_paragraph(f'Test it: {test}'); d.add_paragraph(f'Evidence: {evidence}')
    d.add_paragraph('Reflection: What did the agent propose, what did you verify, and what did you change before acceptance?')
d.add_heading('Troubleshooting',1)
for x in ['Dev server fails: confirm the working directory, Node version, dependencies, and first terminal error.','Type errors after generation: inspect imports and prop types; do not suppress errors with `any`.','Fetch repeats or updates after unmount: inspect effect dependencies, cleanup, and AbortController use.','Generated change is too large: revert, narrow the request, and approve one file or behavior at a time.','Direct routes fail after deployment: configure the host fallback or use a routing strategy supported by the target host.']: d.add_paragraph(x,style='List Bullet')
d.add_heading('Reference',1); d.add_paragraph(f'Published course page used for duration, level, prerequisites and topic ordering: {SOURCE}')
save_doc(d,OUT/f'{CODE}-Learner-Guide.docx')

# Lesson Plan
d=Document(); setup(d,'Lesson Plan'); cover(d,'Lesson Plan'); frontmatter(d)
d.add_heading('Facilitation Intent',1); d.add_paragraph('Guide learners from a blank Vite project to a tested, deployed React single-page application while modelling safe, reviewable AI collaboration. Progress is checked through demonstrations, questions, and lab evidence.')
d.add_heading('Session Plan — 900 instructional minutes',1)
rows=[('Day 1: welcome, setup and review loop','45','Readiness check; define plan–diff–verify workflow'),('Topic 1 + Lab 1','180','Vite baseline and AI coding contract'),('Topic 2 + Lab 2','210','JSX, components, props, events and responsive UI'),('Day 1 consolidation','15','Demonstrate the reusable SprintBoard UI'),('Day 2: recap and restore checkpoint','30','Re-establish a trusted starting state'),('Topic 3 + Lab 3','240','State, hooks, routing, API states and refactoring'),('Topic 4 + Lab 4','165','Debugging, tests, optimization and deployment'),('Showcase and consolidation','15','Demonstrate deployed app and evidence trail')]
t=d.add_table(rows=1,cols=3); t.style='Table Grid'
for j,x in enumerate(['Segment','Minutes','Observable outcome']): t.cell(0,j).text=x; set_cell_shading(t.cell(0,j),'0B6E99'); t.cell(0,j).paragraphs[0].runs[0].font.color.rgb=RGBColor(255,255,255)
for a,b,c in rows:
    cells=t.add_row().cells; cells[0].text=a; cells[1].text=b; cells[2].text=c
d.add_heading('Facilitator Notes by Topic',1)
for i,(h,desc) in enumerate(topics,1):
    d.add_heading(h,2); d.add_paragraph(desc); d.add_paragraph(f'Demonstration: show the Lab {i} checkpoint. Guided practice: learners execute in pairs, inspect the agent plan and compare diffs. Progress check: ask one learner to explain the verification evidence before accepting the change.')
d.add_heading('Resources and Contingencies',1)
for x in ['Trainer reference project with checkpoint branches lab-1 through lab-4.','Synthetic task data; no live services or credentials.','If internet access fails, use the local JSON fixture and defer deployment while completing the production build.','If an AI service is unavailable, provide prepared plans and diffs for manual critique.']: d.add_paragraph(x,style='List Bullet')
d.add_heading('Closing Reflection',1); d.add_paragraph('Each learner demonstrates one working behavior, identifies one risk in an AI suggestion, and states the command or device check used to verify the final code.')
save_doc(d,OUT/f'{CODE}-Lesson-Plan.docx')

# Markdown learner guide and labs
md=[f'# {TITLE}\n\n- **Course Code:** {CODE}\n- **Duration:** 15 hours / 2 days\n- **Level:** Intermediate\n', '## Course Overview\n\nBuild and deploy SprintBoard through a plan–diff–verify AI coding workflow.\n', '## Topics\n']
for h,desc in topics: md.append(f'### {h}\n\n{desc}\n')
md.append('## Labs\n')
for n,name,goal,steps,test,evidence in labs:
    body=f'# Lab {n}: {name}\n\n## Goal\n\n{goal}\n\n## What you will build\n\nA tested increment of the SprintBoard React capstone.\n\n## Prerequisites\n\n'+('Required tools installed and a writable folder.' if n==1 else f'Completed Lab {n-1} Git checkpoint.')+'\n\n## Steps\n\n'+''.join(f'{i}. {s}\n' for i,s in enumerate(steps,1))+f'\n## Test it\n\n{test}\n\n## Troubleshooting\n\n- Narrow an oversized agent change and retry one behavior at a time.\n- Read the first error, inspect imports and types, then rerun the verification command.\n- Revert to the previous Git checkpoint when the diff cannot be explained.\n- Use only synthetic data and credential placeholders.\n\n## Evidence to submit\n\n{evidence}\n\n## Reflection\n\nWhat did the agent propose, what did you verify, and what did you change before acceptance?\n'
    (LABS/f'Lab-{n:02d}.md').write_text(body)
    md.append(f'- [Lab {n}: {name}](labs/Lab-{n:02d}.md)\n')
(OUT/f'{CODE}-Learner-Guide.md').write_text('\n'.join(md))

print('Generated courseware artifacts in', OUT)
