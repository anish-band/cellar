from pathlib import Path

files_with_content = {}
file_path = Path("/Users/anishbandapelli/Library/Mobile Documents/iCloud~md~obsidian/Documents/Anish's Brain")


files = file_path.rglob("*.md")
for f in files:
  with open(f, "r", encoding="utf-8") as file:
    content = file.read()
    files_with_content[f.name] = content

for k, v in list(files_with_content.items())[:20]:
  print(k, v)