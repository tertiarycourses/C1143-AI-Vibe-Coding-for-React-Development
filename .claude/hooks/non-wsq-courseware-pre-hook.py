#!/usr/bin/env python3
from pathlib import Path
import sys
root=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve()
bad=[p for p in root.rglob('*') if p.is_file() and any(part.startswith('wsq-') for part in p.parts)]
if bad:
    print('Refusing to operate on WSQ-prefixed files:')
    print('\n'.join(str(p) for p in bad)); raise SystemExit(2)
print('non-wsq pre-hook passed')
