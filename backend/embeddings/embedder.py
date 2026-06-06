import sys
sys.path.append("/Users/anishbandapelli/Documents/Code/cellar")
from backend.ingestion.vault_parser import load_vault
from sentence_transformers import SentenceTransformer
import numpy as np

notes = load_vault()
model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
contents = []

for note in notes:
  contents.append(note["content"])

embeddings = model.encode(contents)
np.save("data/vault_cache/embeddings.npy", embeddings)

# loaded_matrix = np.load("data/vault_cache/embeddings.npy")

print(embeddings.shape)

similarities = model.similarity(embeddings, embeddings)
print(similarities)