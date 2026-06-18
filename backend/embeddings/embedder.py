import argparse
import sys
sys.path.append("/Users/anishbandapelli/Documents/Code/cellar")
from backend.ingestion.vault_parser import load_vault
from sentence_transformers import SentenceTransformer
import numpy as np
import json

parser = argparse.ArgumentParser()
parser.add_argument("--vault-path", required=True, help="Path to Obsidian vault")
args = parser.parse_args()

notes = load_vault(args.vault_path)
with open("data/vault_cache/notes.json", "w") as f:
  json.dump(notes, f)

model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
contents = []

for note in notes:
  contents.append(note["content"])

embeddings = model.encode(contents)
np.save("data/vault_cache/embeddings.npy", embeddings)

# loaded_matrix = np.load("data/vault_cache/embeddings.npy")

print(embeddings.shape)

similarities = model.similarity(embeddings, embeddings)
np.save("data/vault_cache/similarities.npy", similarities)

print(similarities)
