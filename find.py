from pathlib import Path

search = ""

for path in Path(".").rglob("*.script"):
    with path.open(encoding="utf-8", errors="ignore") as f:
        for line_num, line in enumerate(f, 1):
            if search in line:
                print(f"{path}:{line_num} {line.strip()}")