"""make.fun entry: Sum up 24 November's world news in one image.

Deterministic, stdlib-only, no network: copies the pre-rendered
entry.png held in this repository to /output/entry.png.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")

def main():
    out = "/output/entry.png"
    try:
        os.makedirs("/output", exist_ok=True)
    except OSError:
        out = os.path.join(HERE, "output", "entry.png")
        os.makedirs(os.path.dirname(out), exist_ok=True)
    shutil.copyfile(SRC, out)
    print(f"wrote {out} ({os.path.getsize(out)} bytes)")

if __name__ == "__main__":
    main()
