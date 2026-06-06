from pathlib import Path
import re

def load_vault():
  files_with_content = []
  file_count = 0
  wl_count = 0
  fm_count = 0
  empty_count = 0

  file_path = Path("/Users/anishbandapelli/Library/Mobile Documents/iCloud~md~obsidian/Documents/Anish's Brain")


  files = file_path.rglob("*.md")
  for f in files:
    file_count += 1 
    with open(f, "r", encoding="utf-8") as file:
      content = file.read()
      if content.strip() == "":
        empty_count += 1
      elif content.startswith("---"):
        fm_count += 1
      content = re.sub(r"\-\-\-(.*?)\-\-\-", "", content, flags=re.DOTALL)

      wikilinks = re.findall(r"\[\[(.*?)\]\]", content)
      if len(wikilinks) >= 1:
        wl_count += 1
      
      files_with_content.append({
        "title": f.name,
        "relative_file_path": str(f.relative_to(file_path)),
        "content": content,
        "wikilinks": wikilinks
      })
      # print(f"Files : {file_count}")
      # print(f"Files With Wikilinks: {wl_count}")
      # print(f"Files With Frontmatter: {fm_count}")
      # print(f"Empty Files: {empty_count}")

  return files_with_content