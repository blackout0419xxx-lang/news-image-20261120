"""make.fun bounty: Sum up 20 November's world news in one image.
Stdlib-only entry program (Python 3.13, no network, no random, no time).
It copies the image the repository holds (entry.png) to /output/entry.png.
Usage:
    python3 main.py            # writes /output/entry.png
    python3 main.py OUT.png    # optional output path (for local testing)
"""
import sys
from pathlib import Path

def main():
    src = Path(__file__).resolve().parent / "entry.png"
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.png")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(src.read_bytes())

if __name__ == "__main__":
    main()
