# Roadmap

This roadmap tracks high-priority milestones to mature the Awesome Human Activity Recognition list into a best-in-class open resource. Timelines are quarter-based targets; adapt as contributors join.

## v0.2.0 — Q1 2026 ✅ (Current Release)
- [x] Publish 40+ dataset cards spanning all modalities with canonical references.
- [x] Add MIT LICENSE file and fix all badge/citation URLs.
- [x] Finalize link validation pipeline (GitHub Action using `lycheeverse/lychee`).
- [x] Add Markdown lint CI workflow for consistent formatting.
- [x] Fix data inconsistencies across README, dataset cards, and i18n files.
- [x] Update roadmap to reflect actual project state.

## v0.3.0 — Q2 2026
- Launch GitHub Discussions with channels for dataset requests and SOTA tracking.
- Ship `tools/catalog_builder.py` JSON + CSV export with GitHub Action auto-generation.
- Release quick-start Jupyter notebooks:
  - Wearable HAR baseline on PAMAP2 / UCI-HAR (PyTorch).
  - Video action recognition on Kinetics-700 (PyTorchVideo).
- Introduce automated badge generation (dataset counts, modalities) via GitHub Action + Shields endpoint.
- Provide standardized dataset schema (YAML frontmatter) with validation to support API consumers.

## v0.4.0 — Q3 2026
- Add baseline reproducibility scripts (PyTorch) covering at least:
  - Skeleton-based GCN on NTU RGB+D 120.
  - Transformer video model on Something-Something V2.
  - Self-supervised wearable baseline on WISDM.
- Expand dataset coverage to synthetic human simulations (e.g., SAPIEN, Habitat, ManiSkill2).
- Introduce monthly digest (via Discussions) summarizing new datasets, papers, and PR highlights.
- Provide standardized dataset schema (YAML/JSON) with validation to support API consumers.

## v1.0.0 — Q4 2026
- Publish MkDocs documentation site served via GitHub Pages, synced with repository metadata.
- Build interactive web explorer with filtering by modality, license, tasks, and download size.
- Offer dataset health metrics (link uptime, missing files, version notes).
- Host community benchmarking challenge (e.g., wearable activity recognition transfer) with partner labs.

## Beyond
- Collaborate with dataset authors to host official mirrors or metadata updates.
- Explore plugin integrations (Weights & Biases, Hugging Face Datasets) to keep entries live.
- Apply to [awesome list](https://github.com/sindresorhus/awesome) for official inclusion.
- Multilingual dataset card translations (beyond README-level i18n).

Contributors can propose roadmap updates via issues tagged `type:roadmap`. Priorities adjust as the community scales.
