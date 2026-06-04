import sys
sys.path.append("/Users/anishbandapelli/Documents/Code/cellar")
from backend.ingestion.vault_parser import load_vault
from sentence_transformers import SentenceTransformer

notes = load_vault()
model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
contents = []

for note in notes:
  contents.append(note["content"])

embeddings = model.encode(contents)
print(embeddings.shape)

similarities = model.similarity(embeddings, embeddings)
print(similarities)