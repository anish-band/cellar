import hdbscan
import numpy as np
import sys
import json
sys.path.append("/Users/anishbandapelli/Documents/Code/cellar")

with open("data/vault_cache/notes.json", "r") as f:
  notes = json.load(f)



umap_embeddings = np.load("data/vault_cache/umap_embeddings.npy")

clusterer = hdbscan.HDBSCAN(algorithm='best', alpha=1.0, approx_min_span_tree=True,
                            gen_min_span_tree=False, leaf_size=40, metric='euclidean', min_cluster_size=3,
                            min_samples=2, p=None)

clusterer.fit(umap_embeddings)

labels = clusterer.labels_
np.save("data/vault_cache/cluster_labels.npy", labels)

unique_labels, counts = np.unique(labels, return_counts=True)

total = 0

for label, count in zip(unique_labels, counts):
  if label == -1:
    print(f"Noise/Outliers: {count} items")
    #total += count
  else:
    print(f"Cluster {label}: {count} items")
    #total += count



cluster_6_notes = []
for i, label in enumerate(labels):
  if label == 6:
    cluster_6_notes.append(notes[i]["title"])

print(cluster_6_notes)

cluster_12_notes = []
for i, label in enumerate(labels):
  if label == 12:
    cluster_12_notes.append(notes[i]["title"])

print(cluster_12_notes)

#print(set(clusterer.labels_))
#print(f"Total Notes: {total}") 

