#!/usr/bin/env python3
"""Decode base64 image payloads into images/ for GitHub Pages."""
from pathlib import Path
import base64
import sys

root = Path(__file__).resolve().parent.parent
enc = root / "images" / "encoded"
out = root / "images"
if not enc.exists():
    print("No encoded images found", file=sys.stderr)
    sys.exit(1)
count = 0
for p in sorted(enc.glob("*.b64")):
    name = p.name[:-4]  # strip .b64
    data = base64.b64decode(p.read_text().strip())
    dest = out / name
    dest.write_bytes(data)
    print(f"wrote {dest} ({len(data)} bytes)")
    count += 1
if count == 0:
    print("No .b64 files decoded", file=sys.stderr)
    sys.exit(1)
