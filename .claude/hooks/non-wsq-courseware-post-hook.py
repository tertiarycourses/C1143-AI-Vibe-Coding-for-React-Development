#!/usr/bin/env python3
from pathlib import Path
import re, sys
root=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve()
deliverables=[root/'courseware'/'C1143-Learner-Guide.md',*sorted((root/'courseware'/'labs').rglob('*.md'))]
prohibited=re.compile(r'\b(SSG|TRAQOM)\b|SkillsFuture funding',re.I); errors=[]
for p in deliverables:
    if not p.exists(): errors.append(f'missing: {p}'); continue
    for n,line in enumerate(p.read_text(errors='ignore').splitlines(),1):
        if prohibited.search(line): errors.append(f'{p}:{n}: prohibited programme language')
for folder in [root/'.codex/skills',root/'.claude/commands',root/'.claude/hooks',root/'.claude/agents']:
    if folder.exists():
        for p in folder.iterdir():
            if not p.name.startswith('non-wsq-'): errors.append(f'{p}: custom tooling lacks non-wsq- prefix')
required=[root/'courseware'/f for f in ['C1143-Facilitator-Deck.pptx','C1143-Learner-Guide.docx','C1143-Lesson-Plan.docx']]
for p in required:
    if not p.exists() or p.stat().st_size<10000: errors.append(f'missing or undersized: {p}')
if errors: print('\n'.join(errors)); raise SystemExit(1)
print(f'non-wsq post-hook passed: {len(deliverables)-1} labs and 3 primary artifacts')
