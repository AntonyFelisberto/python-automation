from pathlib import Path

root_dir = Path("automation\\txts\\files")

for path in root_dir.glob("*.txt"):
    with open(path,"wb") as f:
        f.write(b"")
    path.unlink()