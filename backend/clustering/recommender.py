import numpy as np
import sys
import json
sys.path.append("/Users/anishbandapelli/Documents/Code/cellar")

with open("data/vault_cache/notes.json", "r") as f:
  notes = json.load(f)

embeddings = np.load("data/vault_cache/embeddings.npy")
similarities = np.load("data/vault_cache/similarities.npy")

def recommend_links(note_index, top_k=5):
  row = similarities[note_index]
  sorted_by_similarity = np.argsort(row)
  top_indices = sorted_by_similarity[-(top_k+1):-1]

  reccomendations = []
  for i in top_indices:
    title = notes[i]["title"].replace(".md", "")
    if title not in notes[note_index]["wikilinks"] and title != notes[note_index]["title"].replace(".md", ""):
      reccomendations.append(title)

  return reccomendations

all_recs = {}
for i in range(len(notes)):
  title = notes[i]["title"].replace("md", "")
  all_recs[title] = recommend_links(i)

print(all_recs)