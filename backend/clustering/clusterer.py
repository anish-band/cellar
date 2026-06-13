import hdbscan
import numpy as np
import sys
sys.path.append("/Users/anishbandapelli/Documents/Code/cellar")
from backend.ingestion.vault_parser import load_vault


umap_embeddings = np.load("data/vault_cache/umap_embeddings.npy")

clusterer = hdbscan.HDBSCAN(algorithm='best', alpha=1.0, approx_min_span_tree=True,
                            gen_min_span_tree=False, leaf_size=40, metric='euclidean', min_cluster_size=3,
                            min_samples=None, p=None)

clusterer.fit(umap_embeddings)
labels = clusterer.labels_
unique_labels, counts = np.unique(labels, return_counts=True)

total = 0

for label, count in zip(unique_labels, counts):
  if label == -1:
    print(f"Noise/Outliers: {count} items")
    #total += count
  else:
    print(f"Cluster {label}: {count} items")
    #total += count

notes = load_vault()

cluster_3_notes = []
for i, label in enumerate(labels):
  if label == 3:
    cluster_3_notes.append(notes[i]["title"])

print(cluster_3_notes)

cluster_2_notes = []
for i, label in enumerate(labels):
  if label == 2:
    cluster_2_notes.append(notes[i]["title"])

print(cluster_2_notes)

#print(set(clusterer.labels_))
#print(f"Total Notes: {total}") 

