import numpy as np
import sys
import json
sys.path.append("/Users/anishbandapelli/Documents/Code/cellar")
from backend.clustering.recommender import recommend_links

with open("data/vault_cache/notes.json", "r") as f:
  notes = json.load(f)

similarities = np.load("data/vault_cache/similarities.npy")

def append_recommendations(recommendations):
  block = "\n\n\n\n##### Cellar Recommendations\n"
  for rec in recommendations:
    block += f"- [[{rec}]]\n"
  return block

for i in range(len(notes)):
  if notes[i]["title"] == "Home Base.md": continue

  file_path = "/Users/anishbandapelli/Library/Mobile Documents/iCloud~md~obsidian/Documents/Anish's Brain/" + notes[i]["relative_file_path"]

  recs = recommend_links(i)
  block = append_recommendations(recs)

  with open(file_path, "a+", encoding="utf-8") as f:
    f.seek(0)
    if ("Cellar Recommendations") in f.read(): continue
    f.write(block)
  



