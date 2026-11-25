#!/usr/bin/env python3
"""make.fun entry: sum up 24 November's world news in one image.

Writes the pre-rendered entry.png (1024x1024, <1 MiB) that sits next
to this file to /output/entry.png. Stdlib only, no network, no
randomness: two runs write identical bytes.
"""
import hashlib
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
DST = Path("/output/entry.png")


def main() -> None:
    if not SRC.is_file():
        raise SystemExit("entry.png not found next to main.py")
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)
    digest = hashlib.sha256(DST.read_bytes()).hexdigest()
    assert digest == hashlib.sha256(SRC.read_bytes()).hexdigest(), \
        "output differs from source"
    print(f"wrote {DST} ({DST.stat().st_size} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
