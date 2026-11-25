"""make.fun entry: Sum up 24 November's world news in one image.

Deterministic, stdlib-only, no network: writes the pre-rendered
1024x1024 PNG held in this repository to /output/entry.png.
The image data is stored as base64 text in entry.png.b64 (the
binary entry.png is uploaded alongside it when available and is
used then); either way the written bytes are identical.
"""
import base64
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
PNG = os.path.join(HERE, "entry.png")
B64 = os.path.join(HERE, "entry.png.b64")

def main():
    out = "/output/entry.png"
    try:
        os.makedirs("/output", exist_ok=True)
    except OSError:
        out = os.path.join(HERE, "output", "entry.png")
        os.makedirs(os.path.dirname(out), exist_ok=True)
    if os.path.exists(PNG):
        shutil.copyfile(PNG, out)
    else:
        with open(B64, "r", encoding="ascii") as f:
            data = base64.b64decode("".join(f.read().split()))
        with open(out, "wb") as f:
            f.write(data)
    print(f"wrote {out} ({os.path.getsize(out)} bytes)")

if __name__ == "__main__":
    main()
