# Benchmark Snapshots

High-level view of representative baselines and state-of-the-art (SOTA) models for key datasets. Use this to understand reasonable performance bands before planning experiments. Last updated: 2026-Q1.

## Vision Datasets

| Dataset | Metric | Baseline (paper) | SOTA (2025+) | Notes |
| --- | --- | --- | --- | --- |
| Kinetics-700 | Top-1 | SlowFast R101 (65.7) | InternVideo2-6B (85.4) | Foundation model pretraining now dominant; pure RGB. |
| UCF-101 | Top-1 | Two-Stream (88.0) | VideoMAE V2-g (99.6) | Near-saturated; mainly used for pretraining validation. |
| HMDB-51 | Top-1 | IDT+FV (61.7) | VideoMAE V2-g (88.1) | Harder than UCF-101 due to viewpoint/scene variation. |
| ActivityNet | mAP | TSN (89.0) | InternVideo2 (93.2) | Temporal proposals + classification; untrimmed videos. |
| AVA | mAP @0.5 | SlowFast R101 (24.5) | VideoMAEv2 + MViTv2 (42.6) | Spatio-temporal; person-level detection required. |
| NTU RGB+D 120 | CS Top-1 | Shift-GCN (85.9) | InfoGCN (93.0) | Cross-setup SOTA trails by ~2 points; skeleton methods lead. |
| Something-Something V2 | Top-1 | TSM (63.4) | InternVideo2 (77.1) | Temporal reasoning critical; longer clips help. |
| FineGym | Event Top-1 | TSM hierarchy (86.2) | UniFormerV2-L (90.4) | Hierarchical loss required; pose priors help on sub-actions. |
| Moments in Time | Top-1 | TSN (25.3) | InternVideo2 (48.8) | Extreme class diversity; multi-label noise present. |
| Diving48 | Top-1 | TSN (35.1) | VideoMAE V2 (88.7) | Fine-grained temporal structure; no appearance shortcut. |
| Toyota Smarthome | CS Top-1 | I3D (54.8) | MS-G3D (73.2) | Cross-view generalization is the hard evaluation. |

## Skeleton & Mocap

| Dataset | Metric | Baseline | SOTA (2025+) | Notes |
| --- | --- | --- | --- | --- |
| NTU RGB+D 60 | CS Top-1 | ST-GCN (81.5) | InfoGCN (93.0) | Foundation dataset for skeleton-based action recognition. |
| AMASS | MPJPE | VPoser prior (70 mm) | MotionDiffuse (42 mm) | Generative diffusion models dominate long sequence synthesis. |
| Human3.6M | MPJPE | Martinez et al. (67.5 mm) | MotionBERT (37.2 mm) | Report protocol matters; leaderboard splits differ by joints. |
| BABEL | Seg. mIOU | Transformer baseline (77.1) | MotionBERT (84.3) | Text-aligned supervision improves segmentation + retrieval. |
| TotalCapture | MPJPE | TotalCapture baseline (19 mm) | PoseFormerV3D (13.6 mm) | Multi-view fusion with transformer aggregation leads. |
| PKU-MMD | mAP | ST-GCN (93.7) | FR-Head (96.2) | Phase II (cross-subject) is the harder split. |

## Wearable Sensors

| Dataset | Metric | Baseline | SOTA (2025+) | Notes |
| --- | --- | --- | --- | --- |
| UCI-HAR | Accuracy | SVM (96.0) | UniHAR (97.5) | Near-saturated; 6 basic activities, smartphone only. |
| PAMAP2 | Accuracy | DeepConvLSTM (94.2) | HARFormer (96.8) | Domain augmentation (SpecAugment, jitter) helps >1 point. |
| WISDM | Accuracy | Random Forest (91.7) | SelfHAR (96.1) | Subject splits matter; report LOSO + random for comparability. |
| HAPT | Accuracy | SVM (96.3) | MetaSenseNet (97.5) | Postural transitions remain hardest; model F1 in addition to accuracy. |
| RealWorld HAR | F1 | Position-aware (86.7) | AdaHAR (92.4) | Evaluate across device placements; cross-location generalization critical. |
| OPPORTUNITY | F1 (Gestures) | DeepConvLSTM (70.1) | CPM-Net (77.8) | Data imbalance; class-weighted losses still recommended. |

## Multimodal & Egocentric

| Dataset | Metric | Baseline | SOTA (2025+) | Notes |
| --- | --- | --- | --- | --- |
| EPIC-Kitchens-100 | Action mAP | TSN RGB+Flow (38.9) | InternVideo2 (52.6) | Multi-modal (audio/text) pretraining narrows gap. |
| Ego4D | Recall@5 (Episodic) | CLIP retrieval (25.4) | EgoVLP v2 (42.3) | Foundation models fine-tuned on ego data lead. |
| Charades | mAP | Two-Stream I3D (32.9) | InternVideo2 (52.8) | Consider multi-label calibration for threshold selection. |
| Ego-Exo4D | Top-1 (Cross-view) | Baseline (46.5) | CrossFormer++ (57.4) | Joint ego-exo transformers are emerging; numbers moving fast. |

## Using This Table
- Cite the relevant paper when referencing SOTA metrics; numbers change quickly.
- Reproduce baselines with provided configs in `tools/` (planned) to validate reproducibility.
- Open an issue tagged `type:benchmark` when updating numbers, including validation logs or leaderboard links.
