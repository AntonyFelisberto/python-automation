from pathlib import Path

root_dir = Path("automation\\txts\\files")

for i in range(10,21):
    filename = f"{i}.txt"
    filepath = root_dir / Path(filename)
    filepath.touch()