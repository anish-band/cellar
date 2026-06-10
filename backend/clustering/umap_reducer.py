import umap
import numpy as np

embeddings = np.load("data/vault_cache/embeddings.npy")
reducer = umap.UMAP(n_neighbors=15, min_dist=0.1, metric="cosine")

umap_embeddings = reducer.fit_transform(embeddings)
np.save("data/vault_cache/umap_embeddings.npy", umap_embeddings)

print(umap_embeddings.shape)




