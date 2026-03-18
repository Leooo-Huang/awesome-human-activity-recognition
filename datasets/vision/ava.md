# AVA (Atomic Visual Actions)

- **Modality:** RGB video (movie clips)
- **Primary Tasks:** Spatio-temporal action detection, action localization
- **Scale:** 430 15-minute movie clips, 80 atomic action classes, ~1.62M action labels, 57.6k video clips
- **License:** Research use only (Google terms)
- **Access:** [https://research.google.com/ava/](https://research.google.com/ava/)

## Summary
AVA (Atomic Visual Actions) provides spatio-temporal annotations of atomic visual actions in movie clips. Each person in a keyframe is localized with a bounding box and labeled with one or more action classes from a set of 80 categories. Actions are annotated at 1 FPS on 15-minute clips sourced from movies, capturing realistic and complex multi-person scenes. AVA has become the standard benchmark for spatio-temporal action detection, requiring models to jointly detect and classify actions for each person in the scene.

## Reference Paper
- *Chunhui Gu, Chen Sun, David A. Ross, Carl Vondrick, Caroline Pantofaru, Yeqing Li, Sudheendra Vijayanarasimhan, George Toderici, Susanna Ricco, Rahul Sukthankar, Cordelia Schmid, Jitendra Malik.* "AVA: A Video Dataset of Spatio-Temporally Localized Atomic Visual Actions." CVPR, 2018. [`PDF`](https://arxiv.org/abs/1801.00868)

## Benchmarks & Baselines
- **SlowFast R101-NL** - mAP: 29.0 (AVA v2.2) — *Feichtenhofer et al., ICCV 2019.*
- **MViTv2-L** - mAP: 34.4 (AVA v2.2) — *Li et al., CVPR 2022.*
- **VideoMAE V2-g** - mAP: 41.4 (AVA v2.2) — *Wang et al., CVPR 2023.*
- Standard evaluation uses frame-level mAP at IoU 0.5 on 60 classes (excluding rare classes).

## Tooling & Ecosystem
- [Detectron2](https://github.com/facebookresearch/detectron2) + [SlowFast](https://github.com/facebookresearch/SlowFast) provide official baseline implementations.
- [MMAction2](https://github.com/open-mmlab/mmaction2) supports AVA spatio-temporal detection.
- [PySlowFast](https://github.com/facebookresearch/SlowFast) includes pretrained models and evaluation scripts.

## Known Challenges
- Highly imbalanced action label distribution; a few classes dominate (e.g., "stand", "watch"), while many are rare.
- Multi-label nature: each person can perform multiple simultaneous actions, complicating evaluation.
- Requires a strong person detector as a prerequisite; detection quality directly impacts action classification.
- Movie clips may have complex cinematography (cuts, zooms) that differs from user-generated video.

## Cite
```bibtex
@inproceedings{gu2018ava,
  title     = {AVA: A Video Dataset of Spatio-Temporally Localized Atomic Visual Actions},
  author    = {Gu, Chunhui and Sun, Chen and Ross, David A. and Vondrick, Carl and Pantofaru, Caroline and Li, Yeqing and Vijayanarasimhan, Sudheendra and Toderici, George and Ricco, Susanna and Sukthankar, Rahul and Schmid, Cordelia and Malik, Jitendra},
  booktitle = {IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year      = {2018}
}
```
