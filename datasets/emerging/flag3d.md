# FLAG3D

- **Modality:** Multi-view RGB video, 3D skeleton (SMPL), language descriptions
- **Primary Tasks:** 3D fitness activity understanding, action recognition, action quality assessment, motion generation
- **Scale:** 180,000+ sequences, 60 fitness action categories, 24 camera views per sequence
- **License:** Research use only (non-commercial)
- **Access:** [https://andytang15.github.io/FLAG3D/](https://andytang15.github.io/FLAG3D/)

## Summary
FLAG3D (Fine-grained Language-Aligned Grounded 3D) is a large-scale dataset for 3D fitness activity understanding that combines multi-view RGB videos, SMPL body parameters, 3D skeletons, and natural language descriptions. Captured in a professional motion capture studio with 24 synchronized cameras, it covers 60 categories of fitness actions performed by diverse subjects. Each sequence is annotated with fine-grained language descriptions at both the sequence and segment level, enabling research in text-driven action recognition, motion quality assessment, and language-conditioned motion generation. FLAG3D bridges the gap between vision-based action understanding and language-grounded motion analysis in the fitness domain.

## Reference Paper
- *Yansong Tang, Jinpeng Liu, Aoyang Liu, Bin Yang, Wenxun Dai, Yongming Rao, Jiwen Lu, Jie Zhou, Xiu Li.* "FLAG3D: A 3D Fitness Activity Dataset with Language Instruction." CVPR, 2024. [`PDF`](https://arxiv.org/abs/2212.04638)

## Benchmarks & Baselines
- **ST-GCN** - Top-1 Accuracy: 86.7% (skeleton-based action recognition) — *Tang et al., CVPR 2024.*
- **MotionBERT** - Top-1 Accuracy: 91.2% (skeleton-based action recognition) — *Tang et al., CVPR 2024.*
- **Action Quality Assessment** - Spearman correlation: 0.71 using CoRe framework — *Tang et al., CVPR 2024.*
- **Text-to-Motion** - FID: 0.89, R-Precision Top-3: 0.68 using T2M-GPT — *Tang et al., CVPR 2024.*
- Official train/val/test splits provided; cross-subject evaluation protocol.

## Tooling & Ecosystem
- Official code and tools: [https://github.com/andytang15/FLAG3D](https://github.com/andytang15/FLAG3D)
- Data includes pre-extracted SMPL parameters, 3D joint positions, and multi-view RGB frames.
- Compatible with [MMAction2](https://github.com/open-mmlab/mmaction2) for video-based recognition and [PyTorch Geometric](https://github.com/pyg-team/pytorch_geometric) for skeleton-based methods.
- Language annotations formatted for direct use with text-to-motion generation pipelines.

## Known Challenges
- Large dataset size (multi-view RGB data requires significant storage, estimated 2+ TB for full resolution).
- Fitness actions can be visually similar (e.g., different squat variations), requiring fine-grained temporal and spatial reasoning.
- Studio capture environment may limit generalization to in-the-wild fitness videos.
- Action quality assessment annotations are inherently subjective; inter-annotator agreement varies by action category.
- SMPL fitting quality varies for fast or complex movements.

## Cite
```bibtex
@inproceedings{tang2024flag3d,
  title     = {FLAG3D: A 3D Fitness Activity Dataset with Language Instruction},
  author    = {Tang, Yansong and Liu, Jinpeng and Liu, Aoyang and Yang, Bin and Dai, Wenxun and Rao, Yongming and Lu, Jiwen and Zhou, Jie and Li, Xiu},
  booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year      = {2024}
}
```
