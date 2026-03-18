# FineSports

- **Modality:** RGB video (NBA basketball broadcast footage)
- **Primary Tasks:** Fine-grained multi-person action recognition, spatial-temporal action detection, hierarchical sports understanding
- **Scale:** 10,000 videos, 52 fine-grained action types, 123K bounding boxes
- **License:** Research use only
- **Access:** [https://github.com/PKU-ICST-MIPL/FineSports_CVPR2024](https://github.com/PKU-ICST-MIPL/FineSports_CVPR2024)

## Summary
FineSports provides hierarchical fine-grained annotations of multi-person basketball activities from NBA game footage. Unlike single-person sports datasets, it addresses the challenge of recognizing concurrent actions by multiple players within the same scene, with spatial bounding boxes linking each action to its performer. The 52 action types span offense, defense, and transition plays, enabling research in group activity recognition, player interaction modeling, and fine-grained sports analytics.

## Reference Paper
- *Xu et al.* "FineSports: A Multi-person Hierarchical Sports Video Dataset for Fine-grained Action Understanding." CVPR, 2024. [`PDF`](https://openaccess.thecvf.com/content/CVPR2024/)

## Benchmarks & Baselines
- **SlowFast + Detection Head** - mAP for action detection reported in official paper; *Xu et al., CVPR 2024.*
- **Hierarchical Classification Baseline** - Top-1 accuracy per action granularity level provided in supplementary.
- Evaluation uses official train/val/test splits with per-person bounding box mAP and video-level classification accuracy.

## Tooling & Ecosystem
- Official [PKU-ICST-MIPL/FineSports_CVPR2024](https://github.com/PKU-ICST-MIPL/FineSports_CVPR2024) repository with annotation tools and baseline code.
- Compatible with [MMAction2](https://github.com/open-mmlab/mmaction2) and [SlowFast](https://github.com/facebookresearch/SlowFast) frameworks for spatial-temporal detection.
- Bounding box annotations align with COCO-style format for straightforward integration with detection pipelines.

## Known Challenges
- NBA footage licensing restricts redistribution; users must follow repository instructions to obtain video data.
- Multi-person scenes with heavy occlusion make spatial annotation alignment challenging; verify bounding box quality per clip.
- Class distribution is imbalanced across action types (common plays vs. rare events); stratified sampling recommended.
- Fine-grained distinctions between similar basketball actions (e.g., different types of passes) require high temporal resolution.

## Cite
```
@inproceedings{xu2024finesports,
  title     = {FineSports: A Multi-person Hierarchical Sports Video Dataset for Fine-grained Action Understanding},
  author    = {Xu, Jinglin and others},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  year      = {2024}
}
```
