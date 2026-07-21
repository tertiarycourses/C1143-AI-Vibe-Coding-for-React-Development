#!/usr/bin/env python3
"""Generate the C1143 non-WSQ course slide deck (all-white Tertiary house style).

Visual component library ported verbatim from the wsq-slides reference
(cover, section, content, two_col, cards3, tile_grid, flow_h, trainer_slide,
big_statement, activity_overview, step_slide, test_slide, brk) plus a
hyperlink-capable text helper for the "Access the Hands-On Labs" slide.

Content is driven entirely by course_data.py + data_domainN.py so the deck stays
100% aligned with the Lesson Plan, Learner Guide and the labs/ folder.
"""
import os, sys, math, struct
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import course_data as C
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3
from data_domain4 import DOMAIN4
from data_domain5 import DOMAIN5
from data_domain6 import DOMAIN6
from concepts import CONCEPT_SLIDES
from diagrams import DIAGRAM_SLIDES
from code_walkthrough import CODE_WALKTHROUGH
ACTIVITIES = DOMAIN1 + DOMAIN2 + DOMAIN3 + DOMAIN4 + DOMAIN5 + DOMAIN6

REPO = os.path.dirname(os.path.dirname(HERE))
ASSETS = os.path.join(REPO, "courseware", "assets")
DIAGRAMS_DIR = os.path.join(ASSETS, "diagrams")
PORTAL = "https://www.tertiarycourses.com.sg/ai-vibe-coding-for-react-development.html"

DIAGRAMS_BY_TOPIC = {}
for _d in DIAGRAM_SLIDES:
    DIAGRAMS_BY_TOPIC.setdefault(_d["topic"], []).append(_d)

# ---------------- palette ----------------
BLUE=RGBColor(0x1F,0x6F,0xEB); TEAL=RGBColor(0x10,0xB9,0x81); AMBER=RGBColor(0xF5,0x9E,0x0B)
INK=RGBColor(0x16,0x1B,0x26); GREY=RGBColor(0x5B,0x63,0x72); LIGHT=RGBColor(0xF5,0xF8,0xFC)
WHITE=RGBColor(0xFF,0xFF,0xFF); LINE=RGBColor(0xE2,0xE8,0xF0); VIOLET=RGBColor(0x7C,0x3A,0xED)

prs=Presentation(); prs.slide_width=Inches(13.333); prs.slide_height=Inches(7.5)
SW,SH=prs.slide_width,prs.slide_height
BLANK=prs.slide_layouts[6]

def slide(): return prs.slides.add_slide(BLANK)
def rect(s,x,y,w,h,color,line=None):
    sp=s.shapes.add_shape(1,x,y,w,h); sp.fill.solid(); sp.fill.fore_color.rgb=color
    if line is None: sp.line.fill.background()
    else: sp.line.color.rgb=line; sp.line.width=Pt(1)
    sp.shadow.inherit=False; return sp
def oval(s,x,y,w,h,color):
    sp=s.shapes.add_shape(9,x,y,w,h); sp.fill.solid(); sp.fill.fore_color.rgb=color
    sp.line.fill.background(); sp.shadow.inherit=False; return sp
def txt(s,x,y,w,h,runs,align=PP_ALIGN.LEFT,anchor=MSO_ANCHOR.TOP,space=4):
    tb=s.shapes.add_textbox(x,y,w,h); tf=tb.text_frame; tf.word_wrap=True; tf.vertical_anchor=anchor
    for i,line in enumerate(runs):
        p=tf.paragraphs[0] if i==0 else tf.add_paragraph()
        p.alignment=align; p.space_after=Pt(space)
        for t,sz,col,bold in line:
            r=p.add_run(); r.text=t; r.font.size=Pt(sz); r.font.bold=bold
            r.font.color.rgb=col; r.font.name="Arial"
    return tb
def link_txt(s,x,y,w,h,label,url,size=16,color=BLUE,align=PP_ALIGN.LEFT):
    """A REAL clickable hyperlink (house rule: repo/LMS URLs must be clickable)."""
    tb=s.shapes.add_textbox(x,y,w,h); tf=tb.text_frame; tf.word_wrap=True
    p=tf.paragraphs[0]; p.alignment=align
    r=p.add_run(); r.text=label; r.font.size=Pt(size); r.font.bold=True
    r.font.color.rgb=color; r.font.name="Arial"
    r.hyperlink.address=url
    return tb
def bullets(s,x,y,w,h,items,size=18,color=INK,gap=10,mcolor=BLUE):
    tb=s.shapes.add_textbox(x,y,w,h); tf=tb.text_frame; tf.word_wrap=True
    for i,it in enumerate(items):
        p=tf.paragraphs[0] if i==0 else tf.add_paragraph(); p.space_after=Pt(gap)
        lvl=it[1] if isinstance(it,tuple) else 0
        text=it[0] if isinstance(it,tuple) else it
        r=p.add_run(); r.text=("•  " if lvl==0 else "–  ")+text
        r.font.size=Pt(size if lvl==0 else size-2); r.font.color.rgb=color if lvl==0 else GREY
        r.font.name="Arial"; r.font.bold=(lvl==0 and isinstance(it,tuple) and len(it)>2 and it[2])
    return tb

PAGE={"n":0}
def footer(s):
    PAGE["n"]+=1
    txt(s,Inches(0.4),Inches(7.05),Inches(7.5),Inches(0.35),
        [[(f"{C.SHORT_TITLE}  ·  {C.COURSE_CODE}",9,GREY,False)]])
    txt(s,Inches(5.0),Inches(7.05),Inches(3.3),Inches(0.35),
        [[("© 2026 Tertiary Infotech Academy Pte Ltd",9,GREY,False)]],align=PP_ALIGN.CENTER)
    txt(s,Inches(12.4),Inches(7.05),Inches(0.6),Inches(0.35),
        [[(str(PAGE["n"]),9,GREY,False)]],align=PP_ALIGN.RIGHT)
def head(s,title,kicker=None,kcolor=BLUE):
    rect(s,0,0,SW,SH,WHITE); rect(s,0,0,Inches(0.28),Inches(1.55),kcolor)
    if kicker: txt(s,Inches(0.85),Inches(0.5),Inches(11.6),Inches(0.4),[[(kicker,14,kcolor,True)]])
    # Auto-shrink long titles so they stay on ONE line. The divider below is fixed
    # at y=1.7 and the content area starts at 1.95, so a wrapped title would
    # collide with both.
    n=len(title)
    size = 29 if n<=46 else (24 if n<=60 else 20)
    txt(s,Inches(0.85),Inches(0.9),Inches(11.9),Inches(0.9),[[(title,size,INK,True)]])
    rect(s,Inches(0.85),Inches(1.7),Inches(11.63),Inches(0.02),LINE)
    return s
def _logo(name):
    p=os.path.join(ASSETS,name)
    return p if os.path.exists(p) else None

# ---------------- slide templates ----------------
def cover():
    s=slide(); rect(s,0,0,SW,SH,WHITE)
    rect(s,0,0,SW,Inches(0.22),BLUE); rect(s,0,Inches(7.28),SW,Inches(0.22),TEAL)
    org=_logo("tertiary-infotech-logo.png")
    if org: s.shapes.add_picture(org,Inches(0.85),Inches(0.7),height=Inches(1.05))
    rect(s,Inches(11.0),Inches(0.72),Inches(1.55),Inches(1.0),BLUE)
    txt(s,Inches(11.0),Inches(0.82),Inches(1.55),Inches(0.5),[[("REACT",19,WHITE,True)]],align=PP_ALIGN.CENTER)
    txt(s,Inches(11.0),Inches(1.28),Inches(1.55),Inches(0.4),[[("VIBE CODING",8,WHITE,True)]],align=PP_ALIGN.CENTER)
    txt(s,Inches(0.9),Inches(2.3),Inches(12),Inches(0.6),[[("COURSE SLIDES",16,BLUE,True)]])
    txt(s,Inches(0.9),Inches(2.85),Inches(12.0),Inches(1.9),[[(C.TITLE,40,INK,True)]])
    rect(s,Inches(0.92),Inches(4.75),Inches(2.4),Inches(0.06),TEAL)
    txt(s,Inches(0.9),Inches(5.05),Inches(12),Inches(1.4),
        [[(f"Course Code: {C.COURSE_CODE}",16,GREY,False)],
         [(f"Conducted by {C.ORG}  ·  {C.UEN.replace('UEN: ','UEN ')}",14,GREY,False)],
         [(f"Trainer: {C.TRAINER}",14,GREY,False)]],space=6)
    txt(s,Inches(0.9),Inches(6.5),Inches(12),Inches(0.4),[[(f"Version {C.VERSION}  ·  {C.VERSION_DATE}",12,GREY,False)]])
    txt(s,Inches(0.9),Inches(6.85),Inches(12),Inches(0.34),[[("© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.  ·  www.tertiarycourses.com.sg",10,GREY,False)]])

def section(kicker,title,n,sub=""):
    s=slide(); rect(s,0,0,SW,SH,WHITE); rect(s,0,0,Inches(0.28),SH,BLUE)
    rect(s,Inches(0.85),Inches(2.5),Inches(0.14),Inches(2.0),TEAL)
    txt(s,Inches(1.25),Inches(2.55),Inches(11),Inches(0.6),[[(kicker,18,BLUE,True)]])
    txt(s,Inches(1.25),Inches(3.0),Inches(11.4),Inches(1.6),[[(title,40,INK,True)]])
    if sub: txt(s,Inches(1.27),Inches(4.55),Inches(11),Inches(0.8),[[(sub,16,GREY,False)]])
    txt(s,Inches(10.0),Inches(0.7),Inches(2.8),Inches(1.6),[[(n,72,RGBColor(0xE2,0xE8,0xF0),True)]],align=PP_ALIGN.RIGHT)
    footer(s)
def content(title,items,kicker=None,size=20):
    s=head(slide(),title,kicker); bullets(s,Inches(0.85),Inches(1.95),Inches(11.6),Inches(4.9),items,size=size); footer(s); return s
def two_col(title,left,right,kicker=None,lhead="",rhead=""):
    s=head(slide(),title,kicker)
    rect(s,Inches(0.85),Inches(1.95),Inches(5.7),Inches(4.7),LIGHT); rect(s,Inches(6.95),Inches(1.95),Inches(5.55),Inches(4.7),LIGHT)
    if lhead: txt(s,Inches(1.1),Inches(2.15),Inches(5.2),Inches(0.4),[[(lhead,16,BLUE,True)]])
    if rhead: txt(s,Inches(7.2),Inches(2.15),Inches(5.0),Inches(0.4),[[(rhead,16,TEAL,True)]])
    bullets(s,Inches(1.1),Inches(2.7),Inches(5.2),Inches(3.8),left,size=16)
    bullets(s,Inches(7.2),Inches(2.7),Inches(5.05),Inches(3.8),right,size=16,mcolor=TEAL); footer(s); return s
def cards3(title,cards,kicker):
    s=head(slide(),title,kicker); xs=[Inches(0.85),Inches(5.0),Inches(9.15)]
    for i,c in enumerate(cards[:3]):
        x=xs[i]; col=c[0]
        rect(s,x,Inches(1.95),Inches(3.65),Inches(4.7),LIGHT); rect(s,x,Inches(1.95),Inches(3.65),Inches(0.12),col)
        txt(s,x+Inches(0.25),Inches(2.2),Inches(3.2),Inches(0.6),[[(c[1],19,col,True)]])
        bullets(s,x+Inches(0.25),Inches(2.95),Inches(3.2),Inches(3.4),c[2],size=14,mcolor=col,gap=9)
    footer(s); return s
def big_statement(line1,line2,kicker,color=BLUE):
    s=slide(); rect(s,0,0,SW,SH,WHITE); rect(s,0,0,Inches(0.28),SH,color)
    txt(s,Inches(1.1),Inches(2.2),Inches(11),Inches(0.5),[[(kicker,16,color,True)]])
    txt(s,Inches(1.1),Inches(2.8),Inches(11.3),Inches(2.4),[[(line1,38,INK,True)]])
    if line2: txt(s,Inches(1.12),Inches(4.9),Inches(11),Inches(1.2),[[(line2,20,GREY,False)]])
    footer(s); return s

PALETTE=[BLUE,TEAL,VIOLET,AMBER]
def tile_grid(title,items,kicker=None,cols=2,size=15,icons=None,accent=BLUE):
    s=head(slide(),title,kicker,kcolor=accent)
    n=len(items); rows=math.ceil(n/cols)
    X0=Inches(0.85); Y0=Inches(1.95); TOTW=Inches(11.63); AREAH=Inches(4.78)
    gx=Inches(0.3); gy=Inches(0.26)
    cw=int((TOTW-gx*(cols-1))/cols); ch=int((AREAH-gy*(rows-1))/rows)
    bd=Inches(0.6)
    for i,it in enumerate(items):
        r=i//cols; c=i%cols
        x=int(X0+(cw+gx)*c); y=int(Y0+(ch+gy)*r); col=PALETTE[i%len(PALETTE)]
        rect(s,x,y,cw,ch,LIGHT); rect(s,x,y,Inches(0.1),ch,col)
        oval(s,x+Inches(0.28),int(y+ch/2-bd/2),bd,bd,col)
        ic=icons[i] if icons else str(i+1)
        txt(s,x+Inches(0.28),int(y+ch/2-bd/2),bd,bd,[[(ic,19,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        tx=x+Inches(1.08); tw=cw-Inches(1.32)
        if isinstance(it,tuple):
            txt(s,tx,int(y+Inches(0.14)),tw,int(ch-Inches(0.2)),
                [[(it[0],size+2,INK,True)],[(it[1],size-2,GREY,False)]],anchor=MSO_ANCHOR.MIDDLE,space=3)
        else:
            txt(s,tx,int(y+Inches(0.1)),tw,int(ch-Inches(0.16)),[[(it,size,INK,False)]],anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s
def flow_h(title,steps,kicker=None,color=BLUE):
    s=head(slide(),title,kicker,kcolor=color)
    n=len(steps); X0=Inches(0.85); TOTW=Inches(11.63); gap=Inches(0.34)
    cw=int((TOTW-gap*(n-1))/n); y=Inches(2.55); ch=Inches(3.15); bd=Inches(0.82)
    for i,st in enumerate(steps):
        x=int(X0+(cw+gap)*i)
        rect(s,x,y,cw,ch,LIGHT); rect(s,x,y,cw,Inches(0.1),color)
        oval(s,int(x+cw/2-bd/2),int(y+Inches(0.42)),bd,bd,color)
        txt(s,int(x+cw/2-bd/2),int(y+Inches(0.42)),bd,bd,[[(str(i+1),30,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        txt(s,x+Inches(0.16),int(y+Inches(1.55)),cw-Inches(0.32),int(ch-Inches(1.7)),[[(st,14,INK,False)]],align=PP_ALIGN.CENTER)
        if i<n-1:
            txt(s,int(x+cw-Inches(0.04)),int(y+ch/2-Inches(0.3)),int(gap+Inches(0.08)),Inches(0.6),
                [[("▶",15,color,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s
def trainer_slide(kicker,name,role,rows,initials,accent=BLUE):
    s=head(slide(),"About the Trainer",kicker,kcolor=accent)
    lx=Inches(0.85); lw=Inches(3.65)
    rect(s,lx,Inches(1.95),lw,Inches(4.7),LIGHT); rect(s,lx,Inches(1.95),lw,Inches(0.12),accent)
    bd=Inches(1.7); ax=int(lx+(lw-bd)/2)
    oval(s,ax,Inches(2.5),bd,bd,accent)
    txt(s,ax,Inches(2.5),bd,bd,[[(initials,44,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    txt(s,lx+Inches(0.15),Inches(4.55),lw-Inches(0.3),Inches(0.6),[[(name,21,INK,True)]],align=PP_ALIGN.CENTER)
    txt(s,lx+Inches(0.15),Inches(5.2),lw-Inches(0.3),Inches(1.2),[[(role,13,GREY,False)]],align=PP_ALIGN.CENTER)
    rx=Inches(4.9); rw=Inches(7.6); ry=Inches(1.95); rh=Inches(4.7)
    n=len(rows); gy=Inches(0.2); th=int((rh-gy*(n-1))/n)
    for i,(label,val) in enumerate(rows):
        y=int(ry+(th+gy)*i); col=PALETTE[i%len(PALETTE)]
        rect(s,rx,y,rw,th,LIGHT); rect(s,rx,y,Inches(0.1),th,col)
        vruns=[(val,14,INK,False)] if val else [("____________________________________________",13,LINE,False)]
        txt(s,rx+Inches(0.32),y,rw-Inches(0.6),th,
            [[(label.upper(),11,col,True)],vruns],anchor=MSO_ANCHOR.MIDDLE,space=3)
    footer(s); return s
def activity_overview(tag,title,desc,build,services,kicker):
    s=head(slide(),title,kicker,kcolor=TEAL)
    rect(s,Inches(0.85),Inches(1.85),Inches(1.7),Inches(0.5),TEAL)
    txt(s,Inches(0.85),Inches(1.9),Inches(1.7),Inches(0.4),[[(tag,16,WHITE,True)]],align=PP_ALIGN.CENTER)
    # Auto-shrink long descriptions so they never run under the "You'll build" card at y=4.3.
    n=len(desc); dsize = 21 if n<=270 else (18 if n<=360 else (15 if n<=470 else 13))
    txt(s,Inches(0.85),Inches(2.5),Inches(11.7),Inches(1.7),[[(desc,dsize,INK,False)]])
    rect(s,Inches(0.85),Inches(4.3),Inches(11.7),Inches(2.0),LIGHT)
    txt(s,Inches(1.1),Inches(4.5),Inches(11),Inches(0.4),[[("You'll build",14,BLUE,True)]])
    txt(s,Inches(1.1),Inches(4.9),Inches(11),Inches(0.6),[[(build,18,INK,True)]])
    txt(s,Inches(1.1),Inches(5.6),Inches(11.2),Inches(0.6),[[("Tech & files:  ",13,GREY,True),(services,13,GREY,False)]]); footer(s); return s
def step_slide(kicker,act_title,n,total,text,cmd=""):
    s=head(slide(),act_title,kicker,TEAL)
    oval(s,Inches(0.85),Inches(2.5),Inches(1.4),Inches(1.4),TEAL)
    txt(s,Inches(0.85),Inches(2.74),Inches(1.4),Inches(0.9),[[(str(n),38,WHITE,True)]],align=PP_ALIGN.CENTER)
    txt(s,Inches(0.95),Inches(1.95),Inches(11),Inches(0.4),[[(f"STEP {n} OF {total}",13,GREY,True)]])
    txt(s,Inches(2.55),Inches(2.4),Inches(10.1),Inches(1.3),[[(text,23,INK,False)]],anchor=MSO_ANCHOR.MIDDLE)
    if cmd:
        rect(s,Inches(2.55),Inches(4.15),Inches(10.1),Inches(1.15),RGBColor(0x0B,0x12,0x20))
        txt(s,Inches(2.8),Inches(4.28),Inches(9.7),Inches(0.9),[[(cmd,12,RGBColor(0x9C,0xDC,0xFE),False)]],anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s
def test_slide(act_title,text,kicker):
    s=head(slide(),act_title,kicker,TEAL)
    rect(s,Inches(0.85),Inches(2.3),Inches(11.7),Inches(2.9),RGBColor(0xE8,0xF7,0xEE))
    txt(s,Inches(1.2),Inches(2.6),Inches(11),Inches(0.5),[[("✅  Test it",20,RGBColor(0x12,0x7A,0x3E),True)]])
    txt(s,Inches(1.2),Inches(3.3),Inches(11),Inches(1.7),[[(text,18,INK,False)]]); footer(s); return s
def brk(kind,dur,color=AMBER):
    s=slide(); rect(s,0,0,SW,SH,WHITE)
    rect(s,0,0,SW,Inches(0.22),color); rect(s,0,Inches(7.28),SW,Inches(0.22),color)
    rect(s,Inches(5.4),Inches(2.35),Inches(2.53),Inches(0.1),color)
    txt(s,0,Inches(2.75),SW,Inches(1.2),[[(kind,48,INK,True)]],align=PP_ALIGN.CENTER)
    txt(s,0,Inches(4.05),SW,Inches(0.8),[[(dur,22,color,True)]],align=PP_ALIGN.CENTER); PAGE["n"]+=1

# ---------------- explained-concept slides (bullets + code + analogy + takeaway) ----------------
CODEBG=RGBColor(0x0B,0x12,0x20); CODEFG=RGBColor(0x9C,0xDC,0xFE)
AMBER_SOFT=RGBColor(0xFF,0xF7,0xE8); TEAL_SOFT=RGBColor(0xE8,0xF7,0xEE)

def _code_box(s,x,y,w,h,code,size=11.5):
    rect(s,x,y,w,h,CODEBG)
    raw=code.split("\n")
    # Auto-shrink so tall listings never spill past the panel onto the footer.
    # Vertical budget: panel height minus the 0.16" top+bottom insets, in points.
    space=2
    avail_pt=(h/914400.0-0.32)*72.0
    n=max(1,len(raw))
    # line advance ≈ size*1.18 + space; solve n*(size*1.18+space) <= avail_pt for size
    fit=(avail_pt/n-space)/1.18
    size=max(7.5,min(size,fit))
    lines=[[(ln if ln else " ",size,CODEFG,False)] for ln in raw]
    txt(s,x+Inches(0.22),y+Inches(0.16),w-Inches(0.44),h-Inches(0.32),lines,space=space)

def concept_slide(title,kicker,bullets_,code,analogy,takeaway,accent=BLUE):
    """The teaching workhorse: 5-6 explained bullets on the left with a takeaway bar,
    a real code snippet top-right, and a plain-English analogy beneath it."""
    s=head(slide(),title,kicker,kcolor=accent)
    # left: the explanation
    bullets(s,Inches(0.85),Inches(2.0),Inches(5.75),Inches(3.6),bullets_,size=13,gap=9,mcolor=accent)
    # left bottom: the one thing to remember
    rect(s,Inches(0.85),Inches(5.72),Inches(5.75),Inches(0.85),TEAL_SOFT)
    rect(s,Inches(0.85),Inches(5.72),Inches(0.1),Inches(0.85),TEAL)
    txt(s,Inches(1.12),Inches(5.72),Inches(5.35),Inches(0.85),
        [[("REMEMBER  ",10,TEAL,True),(takeaway,12,INK,False)]],anchor=MSO_ANCHOR.MIDDLE,space=2)
    # right top: the code
    if code:
        _code_box(s,Inches(6.85),Inches(2.0),Inches(5.63),Inches(2.6),code)
        ay,ah=Inches(4.78),Inches(1.79)
    else:
        ay,ah=Inches(2.0),Inches(4.57)
    # right bottom: the analogy
    rect(s,Inches(6.85),ay,Inches(5.63),ah,AMBER_SOFT)
    rect(s,Inches(6.85),ay,Inches(0.1),ah,AMBER)
    txt(s,Inches(7.15),ay+Inches(0.12),Inches(5.15),ah-Inches(0.24),
        [[("THINK OF IT LIKE…",10,AMBER,True)],[(analogy,13,INK,False)]],
        anchor=MSO_ANCHOR.MIDDLE,space=5)
    footer(s); return s

# ---------------- build-phase intro (the story so far → what we build now) ----------------
def phase_intro(num, b):
    """Frames each topic as a phase of ONE continuous build: where the app is, what
    we add now, and the ideas this phase forces us to learn."""
    s=head(slide(),b["phase"],f"THE BUILD · PHASE {num} OF 6",kcolor=TEAL)
    # story so far
    rect(s,Inches(0.85),Inches(2.0),Inches(11.63),Inches(1.15),LIGHT)
    rect(s,Inches(0.85),Inches(2.0),Inches(0.1),Inches(1.15),GREY)
    txt(s,Inches(1.12),Inches(2.0),Inches(11.1),Inches(1.15),
        [[("THE STORY SO FAR",10,GREY,True)],[(b["so_far"],15,INK,False)]],
        anchor=MSO_ANCHOR.MIDDLE,space=4)
    # what we build now
    rect(s,Inches(0.85),Inches(3.35),Inches(11.63),Inches(1.55),RGBColor(0xEE,0xF2,0xFF))
    rect(s,Inches(0.85),Inches(3.35),Inches(0.1),Inches(1.55),BLUE)
    txt(s,Inches(1.12),Inches(3.35),Inches(11.1),Inches(1.55),
        [[("WHAT WE BUILD NOW",10,BLUE,True)],[("We add "+b["now"]+".",18,INK,True)]],
        anchor=MSO_ANCHOR.MIDDLE,space=5)
    # concepts this phase needs
    rect(s,Inches(0.85),Inches(5.1),Inches(11.63),Inches(1.15),AMBER_SOFT)
    rect(s,Inches(0.85),Inches(5.1),Inches(0.1),Inches(1.15),AMBER)
    txt(s,Inches(1.12),Inches(5.1),Inches(11.1),Inches(1.15),
        [[("THE IDEAS THIS PHASE NEEDS",10,AMBER,True)],
         [("To build it, you will learn "+b["needs"]+".",15,INK,False)]],
        anchor=MSO_ANCHOR.MIDDLE,space=4)
    footer(s); return s

# ---------------- code walkthrough (real code from the lab, code-forward) ----------------
def code_slide(title, kicker, file, code, points, accent=TEAL):
    """Code-forward slide: a large real-code block on the left, annotation bullets on
    the right. This replaces the old one-line 'step' slides — the learner sees the
    actual code that goes into the Cook & Bake app."""
    s=head(slide(),title,kicker,kcolor=accent)
    # file-name chip
    rect(s,Inches(0.85),Inches(1.95),Inches(7.5),Inches(0.42),RGBColor(0x1E,0x29,0x3B))
    txt(s,Inches(1.05),Inches(1.95),Inches(7.2),Inches(0.42),
        [[("FILE  "+file,12,RGBColor(0xCB,0xD5,0xE1),False)]],anchor=MSO_ANCHOR.MIDDLE)
    # the code
    _code_box(s,Inches(0.85),Inches(2.45),Inches(7.5),Inches(4.15),code,size=12.5)
    # annotations
    txt(s,Inches(8.6),Inches(1.95),Inches(3.9),Inches(0.4),[[("What this shows",13,accent,True)]])
    bullets(s,Inches(8.6),Inches(2.5),Inches(3.9),Inches(4.1),points,size=12.5,gap=10,mcolor=accent)
    footer(s); return s

# ---------------- diagram slides (aspect-fit an image beside the explanation) ----------------
def _png_size(path):
    with open(path,"rb") as f: head=f.read(24)
    return struct.unpack(">II", head[16:24])

def _fit_picture(s,path,bx,by,bw,bh):
    """Scale the image to fit INSIDE the box, preserving aspect ratio, and centre it.
    Image aspect ratios here range from 0.75 to 2.63, so fixed-width placement would
    overflow the slide."""
    iw,ih=_png_size(path)
    scale=min(bw/iw, bh/ih)
    w,h=int(iw*scale), int(ih*scale)
    x=int(bx+(bw-w)/2); y=int(by+(bh-h)/2)
    s.shapes.add_picture(path,x,y,width=w,height=h)

def diagram_slide(title,kicker,image,bullets_,caption,accent=VIOLET):
    s=head(slide(),title,kicker,kcolor=accent)
    bullets(s,Inches(0.85),Inches(2.05),Inches(5.1),Inches(4.3),bullets_,size=13,gap=10,mcolor=accent)
    bx,by,bw,bh=Inches(6.35),Inches(1.95),Inches(6.13),Inches(4.15)
    rect(s,bx,by,bw,bh,LIGHT)
    _fit_picture(s,os.path.join(DIAGRAMS_DIR,image),bx+Inches(0.12),by+Inches(0.12),
                 bw-Inches(0.24),bh-Inches(0.24))
    txt(s,bx,by+bh+Inches(0.12),bw,Inches(0.75),[[(caption,11,GREY,False)]],align=PP_ALIGN.CENTER)
    footer(s); return s

# ---------------- reusable admin blocks ----------------
HOW_YOULL_LEARN = [
 "Watch — the trainer demonstrates the concept with real code",
 "Build — you add the feature to your own app in the lab",
 "Verify — every lab ends with an observable 'Test it' check",
 "Discuss — compare what your AI agent wrote with the class",
 "Recap — each day closes with a recap, Q&A and a checkpoint"]

# ============================================================ BUILD
cover()

# ---------------- FRONT ADMIN ----------------
section("COURSE ADMINISTRATION","Welcome & Housekeeping","")
trainer_slide("YOUR TRAINER · GENERAL","Your Trainer","General Trainer template —\nto be completed by the trainer",
 [("Name",""),("Title / Designation",""),("Qualifications",""),
  ("Areas of expertise",""),("Training & industry experience",""),("Contact","")],
 initials="?",accent=GREY)
trainer_slide("YOUR TRAINER",C.TRAINER,"Principal Trainer\nTertiary Infotech Academy Pte. Ltd.",
 [("Role","Principal Trainer, Tertiary Infotech Academy Pte. Ltd."),
  ("Certification","Full-stack web development, AI-assisted engineering and cloud."),
  ("Delivers","Professional courses on React, vibe coding, AI agents and software engineering."),
  ("Founder","Founder and lead instructor at Tertiary Infotech / Tertiary Courses.")],
 initials="AA",accent=BLUE)
content("Let's Know Each Other",[
 "Your name and organisation / role.",
 "Your experience with JavaScript, React or any AI coding assistant.",
 "What you want to build after this course."],kicker="ICE-BREAKER")
tile_grid("Ground Rules",[
 "Set your mobile phone to silent mode.","Participate actively — no question is too small.",
 "Mutual respect: agree to disagree.","One conversation at a time.",
 "Be punctual; return from breaks on time.","Commit your code before every AI prompt."],
 kicker="HOUSEKEEPING",cols=2,size=15)
two_col(f"Lesson Plan — {C.DAYS} Days, 8 hours/day",[
 (f"Day 1 — {C.DAY_THEMES[1]}",0),
 ("Topic 1: Build a React App with Vibe Coding (Labs 1.1–1.3)",1),
 ("Topic 2: Deploy to the Cloud (Labs 2.1–2.3)",1),
 ("Topic 3: Core React Concepts (Labs 3.1–3.4)",1)],
 [(f"Day 2 — {C.DAY_THEMES[2]}",0),
 ("Topic 4: React Hooks (Labs 4.1–4.5)",1),
 ("Topic 5: APIs & Neon Database (Labs 5.1–5.4)",1),
 ("Topic 6: React Router & Deployment (Labs 6.1–6.6)",1),
 ("Mini-capstone — Day 2 afternoon: add a whole feature yourself",1),
 ("Daily timing: 9:00am–6:00pm · 1-hour lunch · tea breaks within",1)],
 kicker="SCHEDULE",lhead="Day 1",rhead="Day 2")
tile_grid("Learning Outcomes",[
 ("LO1 · Vibe Coding","Scaffold a Vite + React app and run the Prompt → Read → Correct loop."),
 ("LO2 · Cloud Deployment","Version with Git, build for production, publish to Vercel and GitHub Pages."),
 ("LO3 · Core React","Components, JSX & Babel, the real DOM vs the Virtual DOM, props, lists and keys, events."),
 ("LO4 · React Hooks","useState, useEffect with cleanup, useRef for the DOM, useContext, useReducer, custom hooks."),
 ("LO5 · Backend & Database","A serverless API over Neon Postgres; fetch with three states; bcrypt + JWT auth."),
 ("LO6 · Routing & Ship","Routes, layouts, dynamic params, protected routes — and a live deployment.")],
 kicker="WHAT YOU'LL ACHIEVE",cols=2,size=14)
flow_h("How You'll Learn",HOW_YOULL_LEARN,kicker="NO EXAMS — YOU LEARN BY BUILDING")

# Access the hands-on labs (clickable link — house rule)
s=head(slide(),"Access the Hands-On Labs","YOUR WORKBENCH",kcolor=VIOLET)
rect(s,Inches(0.85),Inches(1.95),Inches(5.7),Inches(2.5),LIGHT); rect(s,Inches(0.85),Inches(1.95),Inches(5.7),Inches(0.12),BLUE)
txt(s,Inches(1.15),Inches(2.25),Inches(5.1),Inches(0.5),[[("Option A — Download the courseware",17,BLUE,True)]])
bullets(s,Inches(1.15),Inches(2.85),Inches(5.1),Inches(1.4),
 ["Download the course pack from the course materials links.","Unzip it — every lab lives in labs/topic-N/."],size=13)
rect(s,Inches(6.95),Inches(1.95),Inches(5.55),Inches(2.5),LIGHT); rect(s,Inches(6.95),Inches(1.95),Inches(5.55),Inches(0.12),TEAL)
txt(s,Inches(7.25),Inches(2.25),Inches(5.0),Inches(0.5),[[("Option B — Build it yourself",17,TEAL,True)]])
bullets(s,Inches(7.25),Inches(2.85),Inches(5.0),Inches(1.4),
 ["npm create vite@latest cookbake -- --template react","Each lab folder holds a drop-in src/ snapshot."],size=13)
txt(s,Inches(0.85),Inches(4.75),Inches(11.6),Inches(0.4),[[("Course page & materials:",14,GREY,True)]])
link_txt(s,Inches(0.85),Inches(5.15),Inches(11.6),Inches(0.5),PORTAL,PORTAL,size=18)
txt(s,Inches(0.85),Inches(5.75),Inches(11.6),Inches(0.9),
 [[("Every lab folder is a checkpoint: if an AI edit breaks your app, copy that lab's src/ over your own and carry on.",14,GREY,False)]])
footer(s)

# ---------------- CORE CONCEPTS ----------------
section("CORE CONCEPTS","Vibe Coding & the React Model","")
big_statement("The AI writes the code. You supply the judgement.",
  "An agent will hand you working React in seconds — and a key={index} that corrupts your list on delete. If you cannot read it, you cannot ship it.",
  "WHY THIS COURSE EXISTS",color=BLUE)
flow_h("The Vibe Coding Loop",[
 "Prompt — name the file, the exports and the traps",
 "Generate — let the agent write it",
 "Read — audit against a checklist",
 "Understand — learn the concept underneath",
 "Correct — fix what the agent got wrong"],kicker="HOW YOU WILL WORK",color=VIOLET)
tile_grid("The React Mental Model",[
 ("A component is a function","It takes props and returns JSX describing the UI for the current state."),
 ("JSX is not HTML","It compiles to function calls returning plain JavaScript objects."),
 ("State drives the UI","You change state; React works out the minimum DOM edit to match."),
 ("The Virtual DOM","An in-memory object tree. Cheap to build, cheap to diff — the real DOM is what's slow."),
 ("Props flow down","Parent to child, read-only. A child calls a callback instead of writing to a prop."),
 ("Hooks add memory","useState remembers, useEffect synchronises with the outside world.")],
 kicker="FIVE IDEAS, ONE LIBRARY",cols=2,size=14)
cards3("The Stack You Will Build On",[
 (BLUE,"Front end",["Vite — dev server & build","React 19 — function components","React Router 7 — navigation"]),
 (TEAL,"Back end",["Vercel Functions — the /api tier","Neon — serverless Postgres","bcrypt + JWT — accounts & auth"]),
 (VIOLET,"Ship it",["Git & GitHub — your safety net","Vercel — deploy on every push","An AI agent — Claude Code / Cursor"])],
 kicker="TOOLING")
two_col("The Project: "+C.PROJECT,[
 ("What it is",0),("A cooking & bakery school website",1),("20 courses, enrolments, reviews",1),
 ("Day 1",0),("Vibe-coded landing page, deployed",1),("Refactored into real components",1)],
 [("Day 2",0),("Made interactive with hooks",1),("A serverless API over Neon Postgres",1),
 ("Accounts, a private dashboard, routing",1),("Deployed live to Vercel + Neon",1)],
 kicker="ONE APP, SIX TOPICS",lhead="The app",rhead="How it grows")
flow_h("The Build — One App, Six Phases",[
 "PHASE 1 · Make the first screen — components, JSX, props",
 "PHASE 2 · Put it on the internet — Git, build, Vercel",
 "PHASE 3 · Make it real — DOM vs Virtual DOM, Babel, lists, events",
 "PHASE 4 · Make it react — the hooks",
 "PHASE 5 · Give it a backend — an API over Neon, auth",
 "PHASE 6 · Ship it — routing, deploy, your own feature"],
 kicker="FROM EMPTY FOLDER TO DEPLOYED FULL-STACK APP",color=TEAL)
big_statement("Security is not hiding a key. It is trusting the token, not the request.",
  "A VITE_ variable is compiled into the bundle every visitor downloads, so DATABASE_URL lives only on the server. The user id comes from the verified JWT — never from the request body.",
  "THE ONE SECURITY RULE",color=AMBER)

# ---------------- TOPIC 0 — how the browser really renders (DOM · Virtual DOM · Babel) ----------------
section("FOUNDATIONS","How React Really Renders","00",
        "The real DOM · Updating a page without React · The Virtual DOM · Babel & JSX")
big_statement("The page you see IS the DOM. React just decides how to change it.",
  "You already know JavaScript. What makes React click is one layer down: what the DOM is, why touching it by hand hurts, and how Babel turns your JSX into plain objects React can diff.",
  "BEFORE WE START",color=VIOLET)
for cs in CONCEPT_SLIDES[0]:
    concept_slide(cs["title"],cs["kicker"],cs["bullets"],cs["code"],cs["analogy"],cs["takeaway"],accent=VIOLET)

# ---------------- TOPICS + ACTIVITIES ----------------
TOPIC_ACTS = {t["num"]: [a for a in ACTIVITIES if a["topic"]==t["num"]] for t in C.TOPICS}
CARD_COLORS=[BLUE,TEAL,VIOLET]
BREAKS = {1:("Tea Break","15 minutes"), 2:("Lunch Break","1 hour"),
          3:("End of Day 1","See you tomorrow at 9:00am"),
          4:("Lunch Break","1 hour"), 5:("Tea Break","10 minutes")}

for t in C.TOPICS:
    b = C.BUILD[t["num"]]
    acts = TOPIC_ACTS[t["num"]]
    # --- The phase, framed as the next step in building ONE app ---
    section(f"PHASE {t['code']}", b["phase"], t["code"],
            "Building "+C.PROJECT+" — we add "+b["now"])
    phase_intro(t["num"], b)

    # --- The ideas this phase needs, each explained with real code + an analogy ---
    for cs in CONCEPT_SLIDES.get(t["num"], []):
        concept_slide(cs["title"],cs["kicker"],cs["bullets"],cs["code"],cs["analogy"],cs["takeaway"])
    for dg in DIAGRAMS_BY_TOPIC.get(t["num"], []):
        diagram_slide(dg["title"],dg["kicker"],dg["image"],dg["bullets"],dg["caption"])

    # --- The build itself: for each lab, WHAT we add, the REAL CODE, and the check ---
    for a in acts:
        activity_overview(f"LAB {a['num']}", a["title"], a["desc"], a["build"], a["services"],
                          kicker=f"BUILD STEP · LAB {a['num']}")
        # code-forward walkthrough slides (real code from the lab). Config-only labs
        # have no code_walkthrough entry — they show just the overview + verify.
        for w in CODE_WALKTHROUGH.get(a["num"], []):
            code_slide(w["title"], f"LAB {a['num']} · CODE", w["file"], w["code"], w["points"])
        test_slide(a["title"], a["test"], kicker=f"LAB {a['num']} · VERIFY")

    # --- What the app can do now (the payoff of the phase) ---
    big_statement(f"{C.PROJECT} can now {b['payoff']}.",
                  "Every lab in this phase added to the SAME app — one project, growing, not a pile of throwaway demos.",
                  f"END OF PHASE {t['code']}", color=TEAL)
    if t["num"] in BREAKS:
        k,d = BREAKS[t["num"]]
        brk(k,d,color=(TEAL if t["num"]==3 else AMBER))

# ---------------- CLOSE ----------------
section("WRAP-UP","Course Summary & Next Steps","")
tile_grid("What You Achieved",[
 ("Vibe Coding","Scaffolded a React app with an AI agent — and learned to audit what it wrote."),
 ("Cloud Deployment","Versioned with Git, built for production and published to Vercel."),
 ("Core React","Components, JSX & Babel, the real DOM vs the Virtual DOM, props, lists, events."),
 ("React Hooks","useState, useEffect with cleanup, useRef, useContext, useReducer, custom hooks."),
 ("Backend & Database","A serverless API over Neon Postgres; fetch with three states; bcrypt + JWT auth."),
 ("Routing & Shipping","Nested layouts, dynamic params, protected routes — deployed live.")],
 kicker="LEARNING OUTCOMES",cols=2,size=14)
tile_grid("The AI React Bug Checklist",[
 ("key={index}","Corrupts list state on reorder or delete. Use a stable id."),
 ("No error branch","Every remote read has three states. Agents write two."),
 ("useEffect with no cleanup","Timers and subscriptions leak. StrictMode exposes it."),
 ("Derived state in useState","If you can compute it during render, compute it."),
 ("Unparameterised SQL","sql(`... '${x}'`) invites injection. Always use the sql`` tagged template."),
 ("DATABASE_URL in the browser","A VITE_ var ships to every visitor. Keep the connection string server-side.")],
 kicker="WHAT YOU CAN NOW CATCH",cols=2,size=14)
content("Where to Go Next",[
 "Redo the capstone from an empty folder, prompting only — then audit every file you generated.",
 "Add TanStack Query so you stop hand-rolling loading and error state in every hook.",
 "Add tests with Vitest and React Testing Library.",
 "Learn TypeScript, and generate types from your Neon schema.",
 "Explore React Router framework mode or Next.js when you need server rendering."],kicker="NEXT STEPS")
s=head(slide(),"Course Materials & Keep Building","COURSE PORTAL",kcolor=BLUE)
bullets(s,Inches(0.85),Inches(2.0),Inches(11.6),Inches(2.2),[
 "Download the slides, the Learner Guide and the lab pack from the course materials links.",
 "Every lab folder is a checkpoint — keep the pack and rebuild the app on your own.",
 "Your live app and its repository are yours: extend the mini-capstone after class."],size=17)
txt(s,Inches(0.85),Inches(4.4),Inches(11.6),Inches(0.4),[[("Course page:",14,GREY,True)]])
link_txt(s,Inches(0.85),Inches(4.8),Inches(11.6),Inches(0.5),PORTAL,PORTAL,size=18)
footer(s)

flow_h("How You'll Keep Learning",HOW_YOULL_LEARN,kicker="THE HABIT TO KEEP")
big_statement("Thank You!","You can now build, understand and ship a full-stack React application — with an AI agent as your fastest colleague, not your blind spot.","HAPPY VIBE CODING",color=TEAL)

OUT=os.path.join(REPO,"courseware",f"{C.SHORT_TITLE}-{C.VERSION}.pptx")
prs.save(OUT)
print(f"Saved {OUT}  ({len(prs.slides._sldIdLst)} slides)")
