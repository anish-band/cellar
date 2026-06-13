# Cellar

> An ML-powered intelligence layer for your Obsidian vault.

Cellar ingests your markdown notes, embeds them into vector space, clusters them by semantic similarity, and surfaces the hidden structure of your knowledge — what topics you actually think about, what concepts are silently related but never linked, and where your blind spots are.

---

## What It Does

- **Knowledge Map** — Interactive 2D scatter plot of your entire vault. Notes that are semantically similar cluster together, no manual tagging required.
- **Link Recommendations** — Finds notes that are highly similar but have no wikilink between them. The core ML problem.
- **Orphan Detection** — Surfaces notes that are semantically isolated from the rest of your vault.
- **Topic Labeling** — Auto-generated human-readable labels for each cluster via LLM.
- **Temporal Drift** *(stretch goal)* — Tracks how your writing topics shift over time using file timestamps.

---

## Setup

```bash
conda create -n cellar python=3.11
conda activate cellar
pip install -r requirements.txt
```
