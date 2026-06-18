from anthropic import Anthropic
import sys
import json
import numpy as np

sys.path.append("/Users/anishbandapelli/Documents/Code/cellar")

with open("data/vault_cache/notes.json", "r") as f:
  notes = json.load(f)

cluster_labels = np.load("data/vault_cache/cluster_labels.npy")
unique_labels = set(cluster_labels)
clusters = {}

for label in unique_labels:
  if label == -1:
    continue
  titles = [notes[i]["title"] for i, l in enumerate(cluster_labels) if l == label]
  clusters[label] = titles

client = Anthropic()
def generate_label(cluster_number):
  message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=25,
    messages=[{"role": "user", "content": f"Respond with ONLY a 3-5 word label for this cluster of note titles, no explanation, no alternatives: {clusters[cluster_number]}"}]
  )
  return message.content[0].text

cluster_names = []
for cluster_number in clusters:
  label_name = generate_label(cluster_number)
  cluster_names.append(label_name)

print(cluster_names)