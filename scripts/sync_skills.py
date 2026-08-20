from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / ".claude" / "skills"
DST = ROOT / "skills"

if DST.exists():
    shutil.rmtree(DST)
shutil.copytree(SRC, DST)
print(f"Synced {len([p for p in SRC.iterdir() if p.is_dir()])} skills.")
