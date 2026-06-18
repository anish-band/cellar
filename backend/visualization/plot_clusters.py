import numpy as np
import json
import matplotlib.pyplot as plt
import sys
sys.path.append("/Users/anishbandapelli/Documents/Code/cellar")



umap_embeddings = np.load("data/vault_cache/umap_embeddings.npy")
cluster_labels = np.load("data/vault_cache/cluster_labels.npy")

plt.figure(figsize=(16, 12))
plt.scatter(umap_embeddings[:, 0], umap_embeddings[:, 1], c=cluster_labels, cmap="tab20")

with open("data/vault_cache/cluster_names.json", "r") as f:
  cluster_names = json.load(f)

unique_clusters = set(cluster_labels)
for cluster in unique_clusters:
  if cluster == -1: continue
  mask = cluster_labels == cluster
  x_center = umap_embeddings[mask, 0].mean()
  y_center = umap_embeddings[mask, 1].mean()
  plt.text(x_center, y_center, cluster_names[str(cluster)], fontsize=8)

plt.savefig("cluster_plot_full.png")

plt.xlim(4, 13)
plt.ylim(4, 17)
plt.savefig("cluster_plot_zoomed.png")
