import fs from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { Presentation, PresentationFile } from '@oai/artifact-tool';

const OUT = fileURLToPath(new URL('../courseware/', import.meta.url));
const QA = fileURLToPath(new URL('../courseware/rendered/slides/', import.meta.url));
await fs.mkdir(QA, { recursive: true });

const deck = Presentation.create({ slideSize: { width: 1280, height: 720 } });
const C = { navy:'#17365D', blue:'#0B6E99', cyan:'#1BA3C6', pale:'#EAF4F8', ink:'#17212B', gray:'#5A6872', white:'#FFFFFF', line:'#C9D8E0', green:'#2E7D5B' };

function box(slide, left, top, width, height, fill=C.white, line=C.line, radius='rounded-lg') {
  return slide.shapes.add({ geometry:'roundRect', position:{left,top,width,height}, fill, line:{style:'solid',fill:line,width:1}, borderRadius:radius });
}
function text(slide, value, left, top, width, height, size=22, color=C.ink, bold=false, align='left') {
  const s=slide.shapes.add({geometry:'textbox',position:{left,top,width,height},fill:'none',line:{style:'solid',fill:'none',width:0}});
  s.text=value; s.text.style={fontFamily:'Arial',fontSize:size,color,bold,alignment:align,verticalAlignment:'middle'}; return s;
}
function chrome(slide, section, n) {
  slide.background.fill=C.white;
  slide.shapes.add({geometry:'rect',position:{left:0,top:0,width:1280,height:720},fill:C.white,line:{style:'solid',fill:C.white,width:0}});
  slide.shapes.add({geometry:'rect',position:{left:0,top:0,width:1280,height:14},fill:C.blue,line:{style:'solid',fill:C.blue,width:0}});
  text(slide,section.toUpperCase(),64,30,500,24,13,C.blue,true);
  text(slide,`C1143  •  React AI Vibe Coding for React Development`,64,674,760,22,12,C.gray,false);
  text(slide,String(n).padStart(2,'0'),1170,674,50,22,12,C.gray,true,'right');
}
function titleSlide(title, subtitle) {
  const s=deck.slides.add(); s.background.fill=C.white;
  s.shapes.add({geometry:'rect',position:{left:0,top:0,width:1280,height:720},fill:C.white,line:{style:'solid',fill:C.white,width:0}});
  s.shapes.add({geometry:'rect',position:{left:0,top:0,width:26,height:720},fill:C.blue,line:{style:'solid',fill:C.blue,width:0}});
  text(s,'TERTIARY INFOTECH ACADEMY',78,72,650,34,16,C.blue,true);
  text(s,title,78,176,1020,160,52,C.navy,true);
  text(s,subtitle,82,355,850,80,24,C.gray,false);
  box(s,82,490,520,78,C.pale,C.pale); text(s,'Two days  •  15 hours  •  Intermediate',108,505,470,45,20,C.blue,true);
  text(s,'Course Code C1143',82,620,300,28,15,C.gray,true);
}
function bulletSlide(section, title, bullets, kicker='') {
  const s=deck.slides.add(); chrome(s,section,deck.slides.items.length);
  text(s,title,64,72,1110,62,36,C.navy,true);
  if(kicker) text(s,kicker,66,136,1060,44,18,C.gray,false);
  const start=kicker?205:175, gap=Math.min(94,440/bullets.length);
  bullets.forEach((b,i)=>{ const y=start+i*gap; box(s,70,y,44,44,C.pale,C.pale); text(s,String(i+1),70,y,44,44,18,C.blue,true,'center'); text(s,b,138,y-3,1010,52,21,C.ink,false); });
  return s;
}
function twoCol(section,title,leftTitle,leftItems,rightTitle,rightItems) {
  const s=deck.slides.add(); chrome(s,section,deck.slides.items.length); text(s,title,64,72,1110,60,36,C.navy,true);
  box(s,64,164,548,448,C.pale,C.pale); box(s,636,164,548,448,C.white,C.line);
  text(s,leftTitle,94,192,470,42,25,C.blue,true); text(s,rightTitle,666,192,470,42,25,C.navy,true);
  leftItems.forEach((x,i)=>text(s,`•  ${x}`,96,252+i*68,470,55,19,C.ink));
  rightItems.forEach((x,i)=>text(s,`•  ${x}`,668,252+i*68,470,55,19,C.ink));
}

titleSlide('React AI Vibe Coding for React Development','Build and deploy a modern React app through reviewed plans, controlled diffs, focused tests and verified code.');
bulletSlide('Start','Two days, one app, four deliberate increments',['Scaffold a Vite React TypeScript project','Compose reusable JSX, props, events and CSS','Add state, hooks, routing and API data','Debug, test, optimize and deploy'],'SprintBoard is the thread that connects every published topic.');
twoCol('Workflow','The agent accelerates coding; you retain engineering judgment','Ask the agent',['Restate the outcome','Propose a small plan','Name changed files','Give verification commands'],'You must',['Challenge scope and assumptions','Inspect dependencies and secrets','Review every diff','Test before accepting']);
bulletSlide('Workflow','Use the plan–diff–verify loop on every change',['Frame the outcome and constraints','Request a plan and exact file list','Approve one small increment','Inspect the diff line by line','Run lint, tests and production build','Keep or revert based on evidence']);
bulletSlide('Topic 1','A good prompt creates an inspectable starting point',['Configure an approved AI coding assistant','Scaffold Vite with React and TypeScript','Know the roles of main.tsx, App.tsx and package.json','State constraints, deliverables and verification']);
bulletSlide('Lab 1','Checkpoint 1: a trusted SprintBoard baseline',['Write AGENTS.md with project constraints','Ask for a three-step shell plan','Reject unrelated dependencies or files','Run dev, lint and build','Commit only the understood change']);
twoCol('Topic 2','Components turn JSX into an adaptable UI','Data contracts',['Typed props','Stable task IDs','Explicit callbacks'],'Presentation contracts',['Semantic HTML','Responsive CSS','Visible focus states']);
bulletSlide('Topic 2','Reusable UI needs observable states',['Compose Board, TaskColumn and TaskCard','Pass data down and events up','Render useful empty states','Test at 375 px and 1280 px','Treat generated CSS as code to review']);
bulletSlide('Lab 2','Checkpoint 2: a responsive SprintBoard',['Create six synthetic tasks','Plan component and event boundaries','Review the allowed file scope','Test filters, events and keyboard flow','Lint and build before committing']);
twoCol('Topic 3','State and effects solve different problems','State',['Represents UI truth','Update immutably','Use functional updates'],'Effects',['Synchronize with fetch','Declare dependencies','Abort and handle failures']);
bulletSlide('Topic 3','Routing and API data make the app real',['Define board, detail, about and not-found routes','Test links and direct URL entry','Model loading, empty and error states','Refactor duplication without behavior drift','Reject any and suppressed lint rules']);
bulletSlide('Lab 3','Checkpoint 3: routed pages and resilient data',['Plan routes and rollback','Create a focused useTasks hook','Observe loading and failure UI','Review effect cleanup and dependencies','Compare refactor before and after']);
twoCol('Topic 4','Debugging starts with evidence','Weak request',['It is broken—fix it','No reproduction','Accept a broad rewrite'],'Strong request',['Exact failing behavior','Relevant files and output','Minimal patch plus regression test']);
bulletSlide('Topic 4','Tests and production checks constrain AI output',['Test behavior, not implementation details','Run Vitest and Testing Library','Keep lint and build green','Remove debug output and document decisions','Verify the deployed public URL']);
bulletSlide('Lab 4','Checkpoint 4: a tested, deployed app',['Capture a controlled regression','Review root cause and minimal fix','Add focused component and route tests','Run test, lint, build and diff checks','Deploy and document rollback']);
twoCol('Quality','A working browser view is evidence—but not enough','Verification stack',['npm test -- --run','npm run lint','npm run build','git diff --check'],'Review questions',['Can I explain every change?','Did dependencies expand?','Are failures accessible and useful?','Can I restore a checkpoint?']);
bulletSlide('Practice','Show the evidence behind SprintBoard',['Demonstrate one complete task flow','Show one failing then passing test','Name one AI suggestion you changed','Explain one effect dependency','Open the deployed app and rollback note']);
bulletSlide('Close','The craft is not prompting—it is controlled acceptance',['Make intent concrete','Keep increments small','Review plans before code','Review diffs before trust','Verify on the real target','Commit only what you can explain'],'Your next build should leave an evidence trail, not just an output.');

for (let i=0;i<deck.slides.items.length;i++) {
  const slide=deck.slides.items[i];
  const png=await deck.export({slide,format:'png',scale:1});
  await fs.writeFile(`${QA}/slide-${String(i+1).padStart(2,'0')}.png`,new Uint8Array(await png.arrayBuffer()));
  const layout=await slide.export({format:'layout'}); await fs.writeFile(`${QA}/slide-${String(i+1).padStart(2,'0')}.layout.json`,await layout.text());
}
const montage=await deck.export({format:'webp',montage:true,scale:0.4}); await fs.writeFile(`${QA}/montage.webp`,new Uint8Array(await montage.arrayBuffer()));
const pptx=await PresentationFile.exportPptx(deck); await pptx.save(`${OUT}/C1143-Facilitator-Deck.pptx`);
console.log(`Built ${deck.slides.items.length} slides`);
