import fs from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { Presentation, PresentationFile } from '@oai/artifact-tool';

const ROOT=fileURLToPath(new URL('../',import.meta.url));
const OUT=`${ROOT}courseware/`; const QA=`${OUT}rendered/slides/`;
await fs.mkdir(QA,{recursive:true});
const data=JSON.parse(await fs.readFile(`${OUT}course-data.json`,'utf8'));
const deck=Presentation.create({slideSize:{width:1280,height:720}});
const C={navy:'#17365D',blue:'#0B6E99',teal:'#14866D',pale:'#EAF4F8',ink:'#202A35',gray:'#5A6872',white:'#FFFFFF',line:'#C9D8E0',gold:'#D99B2B',red:'#B94A48',code:'#15202B'};

function shape(slide,left,top,width,height,fill=C.white,line=C.line,geometry='roundRect'){
  return slide.shapes.add({geometry,position:{left,top,width,height},fill,line:{style:'solid',fill:line,width:1}});
}
function text(slide,value,left,top,width,height,size=20,color=C.ink,bold=false,align='left',font='Arial'){
  const s=slide.shapes.add({geometry:'textbox',position:{left,top,width,height},fill:'none',line:{style:'solid',fill:'none',width:0}});
  s.text=String(value); s.text.style={fontFamily:font,fontSize:size,color,bold,alignment:align,verticalAlignment:'middle'}; return s;
}
function chrome(slide,section){
  slide.background.fill=C.white; shape(slide,0,0,1280,720,C.white,C.white,'rect'); shape(slide,0,0,1280,12,C.blue,C.blue,'rect');
  text(slide,section.toUpperCase(),70,28,650,25,13,C.blue,true); text(slide,`${data.course.code}  •  ${data.course.title}`,70,676,760,20,11,C.gray); text(slide,String(deck.slides.items.length).padStart(3,'0'),1160,676,55,20,11,C.gray,true,'right');
}
function titleSlide(title,subtitle){
  const s=deck.slides.add(); s.background.fill=C.white; shape(s,0,0,1280,720,C.white,C.white,'rect'); shape(s,0,0,28,720,C.blue,C.blue,'rect');
  text(s,'TERTIARY INFOTECH ACADEMY',82,62,650,34,16,C.blue,true); text(s,title,82,150,1050,180,50,C.navy,true); text(s,subtitle,84,340,980,90,23,C.gray); shape(s,84,490,610,78,C.pale,C.pale); text(s,'20 labs  •  2 days  •  15 hours  •  Intermediate',112,505,555,45,19,C.blue,true); text(s,'Version 2.0  •  Agentic AI Loop Engineering',84,620,520,28,14,C.gray,true);
}
function bullets(section,title,items,kicker=''){
  const s=deck.slides.add(); chrome(s,section); text(s,title,70,72,1120,58,35,C.navy,true); if(kicker) text(s,kicker,72,132,1080,42,17,C.gray);
  const start=kicker?192:168; const gap=Math.min(82,440/items.length);
  items.slice(0,6).forEach((x,i)=>{const y=start+i*gap; shape(s,74,y,42,42,C.pale,C.pale); text(s,i+1,74,y,42,42,16,C.blue,true,'center'); text(s,x,142,y-2,1020,50,19,C.ink);}); return s;
}
function twoCol(section,title,lhead,left,rhead,right){
  const s=deck.slides.add(); chrome(s,section); text(s,title,70,72,1120,58,35,C.navy,true); shape(s,64,160,550,450,C.pale,C.pale); shape(s,638,160,550,450,C.white,C.line); text(s,lhead,96,188,470,40,24,C.blue,true); text(s,rhead,670,188,470,40,24,C.navy,true);
  left.slice(0,5).forEach((x,i)=>text(s,`•  ${x}`,98,248+i*67,470,53,18,C.ink)); right.slice(0,5).forEach((x,i)=>text(s,`•  ${x}`,672,248+i*67,470,53,18,C.ink)); return s;
}
function codeSlide(section,title,label,content){
  const s=deck.slides.add(); chrome(s,section); text(s,title,70,72,1120,58,35,C.navy,true); text(s,label.toUpperCase(),82,154,300,28,12,C.teal,true); shape(s,72,192,1136,405,C.code,C.code); const clipped=content.length>1050?content.slice(0,1047)+'…':content; text(s,clipped,100,218,1080,350,15,C.white,false,'left','Consolas'); return s;
}
function processSlide(section,title,steps){
  const s=deck.slides.add(); chrome(s,section); text(s,title,70,72,1120,58,35,C.navy,true); const cols=4,w=260,h=150,gap=24,x0=72,y0=168;
  steps.slice(0,8).forEach((st,i)=>{const row=Math.floor(i/cols),col=i%cols,x=x0+col*(w+gap),y=y0+row*(h+34); shape(s,x,y,w,h,row===0?C.pale:C.white,C.line); text(s,String(i+1).padStart(2,'0'),x+18,y+14,45,30,15,C.blue,true); text(s,st,x+18,y+48,w-36,h-58,16,C.ink,true);}); return s;
}

titleSlide(data.course.title,'Build SprintBoard through a controlled AI engineering loop: specify, plan, inspect, implement, test, critique, refine and checkpoint.');
bullets('Orientation','What you will leave with',['A deployed React capstone','20 recoverable Git checkpoints','A reusable agent prompt contract','An AI-generated-code audit habit','Tests for user-visible behavior','A release and rollback evidence trail']);
processSlide('Orientation','The agentic AI loop',['Specify','Plan','Inspect','Implement','Test','Critique','Refine','Checkpoint']);
twoCol('Orientation','AI accelerates work; the learner owns acceptance','The agent can',['Read repository context','Propose a bounded plan','Generate and refactor code','Suggest verification'],'You must',['Define observable outcomes','Challenge assumptions and scope','Read every changed line','Run checks and decide']);
bullets('Orientation','Evidence hierarchy',['Current browser behavior','Failing and passing automated tests','Lint, type-check and build output','The exact Git diff','Current official documentation','The agent explanation'],'When evidence conflicts with confident prose, investigate the evidence.');
bullets('Orientation','Non-negotiable safety rules',['Never paste credentials or private data','No unapproved dependency','No broad rewrite to fix one defect','No lint or type suppression as a shortcut','No commit before diff review','Always preserve a rollback checkpoint']);
bullets('Orientation','One capstone, twenty increments',['SprintBoard begins as a product brief','Components make the board reusable','State and hooks make it interactive','Routes and data make it navigable','Tests and audits make it trustworthy','Deployment makes the evidence public']);

for(const [tnum,tname,tdesc] of data.topics){
  const labs=data.labs.filter(l=>l.topic===tnum);
  titleSlide(`Topic ${tnum}: ${tname}`,tdesc);
  bullets(`Topic ${tnum}`,'Published topic outcomes',labs.map(l=>`Lab ${l.id} — ${l.title}`),'Five connected labs; every lab ends in a recoverable checkpoint.');
  processSlide(`Topic ${tnum}`,'Topic learning journey',labs.map(l=>`${l.id} ${l.outcome}`));
  for(const lab of labs){
    bullets(`Lab ${lab.id}`,lab.title,[lab.outcome,`Files: ${lab.files.join(', ')}`,`Time: approximately ${lab.mins} minutes`],'Predict the files and behavior before the agent writes code.');
    twoCol(`Lab ${lab.id}`,'Concepts and observable outcome','Concepts',lab.concepts.map(x=>x),'Evidence',lab.verify);
    processSlide(`Lab ${lab.id}`,'Executable lab sequence',lab.steps.map(x=>x.replace(/`/g,'').split('.')[0]));
    codeSlide(`Lab ${lab.id}`,'Vibe prompt','Prompt contract',lab.prompt);
    bullets(`Lab ${lab.id}`,'Read what the AI wrote',lab.traps,'Locate the exact line, missing state or unverified assumption that reveals each failure.');
    twoCol(`Lab ${lab.id}`,'Verification and checkpoint','Prove it',lab.verify,'Submit',['Approved plan','Annotated diff excerpt','Command output','Browser evidence','One corrected agent assumption']);
  }
}
bullets('Close','The professional habit',['Make intent observable','Constrain the plan','Approve one increment','Trust evidence over fluency','Keep checkpoints cheap','Ship only what you can explain']);
processSlide('Close','Your next agentic build',['Specify','Plan','Inspect','Implement','Test','Critique','Refine','Checkpoint']);
titleSlide('Build with speed. Review with care.','The output is a React app. The durable skill is controlled acceptance backed by evidence.');

for(let i=0;i<deck.slides.items.length;i++){
  const slide=deck.slides.items[i]; const png=await deck.export({slide,format:'png',scale:1}); await fs.writeFile(`${QA}/slide-${String(i+1).padStart(3,'0')}.png`,new Uint8Array(await png.arrayBuffer()));
}
const pptx=await PresentationFile.exportPptx(deck); await pptx.save(`${OUT}/${data.course.code}-Facilitator-Deck.pptx`);
console.log(`Built ${deck.slides.items.length} slides from ${data.labs.length} labs`);
