#HDBSCAN Tuning Notes

### min_cluster_size = 3
- Came up with 20 clusters (including 1 for outliers)
- I printed file names of notes in ranodm clusters and the clusters are pretty inaccurate
  - Cluster 3 was broadly academics (math, cs, books)
  - Cluster 2 was pretty random (some math, some stuff from foreign affairs articles)
- Letting 3 notes be the min of a cluster was way too broad

### min_cluster_size = 4/5
- same output
- it formed 2 clusters that stored all notes
- Too extreme

### min_cluster_size = 3 & min_samples = 2
- 30 clusters
- I printed clusters randomly and got solid groupings so I'll use this for now