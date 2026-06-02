# Cellar

An ML-powered intelligence layer for your Obsidian vault.

Cellar ingests your markdown notes, embeds them into vector space, clusters them by semantic similarity, and surfaces the hidden structure of your knowledge — what topics you actually think about, what concepts are silently related but never linked, and where your blind spots are.

## What It Does

- **Knowledge Map** — Interactive 2D scatter plot of your entire vault. Notes that are semantically similar cluster together, no manual tagging required.
- **Link Recommendations** — Finds notes that are highly similar but have no wikilink between them. The core ML problem.
- **Orphan Detection** — Surfaces notes that are semantically isolated from the rest of your vault.
- **Topic Labeling** — Auto-generated human-readable labels for each cluster via LLM.
- **Temporal Drift** *(stretch goal)* — Tracks how your writing topics shift over time using file timestamps.

## Tech Stack

**Backend**
- `sentence-transformers` — note embeddings
- `hdbscan` — density-based clustering
- `umap-learn` — dimensionality reduction to 2D
- `scikit-learn` — similarity search
- `FastAPI` — REST API layer

**Frontend**
- Next.js + TypeScript
- Plotly.js or D3 for the interactive vault visualization
- Tailwind CSS

## Build Approach

This project is being built from scratch, deliberately. No scaffolding tools no AI-generated code, and no copying boilerplate until I understand what it does (except for readme lol). The goal is to actually understand the full pipeline from raw text to interactive visualization, not just ship something that works.

## Project Status

| Phase | Status |
|-------|--------|
| Vault ingestion & parsing | 🔄 In progress |
| Embeddings | ⬜ Not started |
| Clustering & UMAP | ⬜ Not started |
| Link recommendations | ⬜ Not started |
| FastAPI backend | ⬜ Not started |
| Next.js dashboard | ⬜ Not started |

## Structure

```
cellar/
├── backend/
│   ├── ingestion/      # vault parsing pipeline
│   ├── embeddings/     # sentence-transformer embedding logic
│   ├── clustering/     # HDBSCAN + UMAP
│   └── api/            # FastAPI endpoints
├── frontend/           # Next.js dashboard
├── data/
│   └── vault_cache/    # processed embeddings and metadata
└── notebooks/          # exploration and sanity checks
```

## Setup

```bash
conda create -n cellar python=3.11
conda activate cellar
pip install -r requirements.txt
```
