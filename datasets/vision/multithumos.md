# MultiTHUMOS

- **Modality:** RGB video (untrimmed sports videos)
- **Primary Tasks:** Dense multi-label temporal action detection, temporal action segmentation
- **Scale:** 413 untrimmed videos, 65 action classes, 38,690 multi-label annotations, 30 hours of video
- **License:** Research use only (non-commercial)
- **Access:** [https://ai.stanford.edu/~syyeung/everymoment.html](https://ai.stanford.edu/~syyeung/everymoment.html)

## Summary
MultiTHUMOS extends the classic THUMOS-14 temporal action detection benchmark by providing dense, multi-label frame-level annotations. While THUMOS-14 annotates 20 action classes with single labels per temporal segment, MultiTHUMOS expands to 65 action classes and allows multiple simultaneous action labels per frame — reflecting the reality that humans often perform several actions concurrently (e.g., "running" while "dribbling" and "looking at ball"). The 2024 update brought renewed attention to the dataset with standardized multi-label evaluation protocols and new baseline results from transformer-based detectors, establishing MultiTHUMOS as the go-to benchmark for multi-label temporal action detection where models must predict overlapping action instances with varying durations.

## Reference Paper
- *Serena Yeung, Olga Russakovsky, Ning Jin, Mykhaylo Andriluka, Greg Mori, Li Fei-Fei.* "Every Moment Counts: Dense Detailed Labeling of Actions in Complex Videos." International Journal of Computer Vision (IJCV), 2018. [`PDF`](https://arxiv.org/abs/1507.05738)

## Benchmarks & Baselines
- **Two-Stream I3D** - Per-frame mAP: 29.7 — *Piergiovanni & Ryoo, CVPR 2019.*
- **TempAgg** - Per-frame mAP: 34.6 — *Piergiovanni & Ryoo, CVPR 2019.*
- **ActionFormer** - Per-frame mAP: 44.7 — *Zhang et al., ECCV 2022.*
- **TriDet** - Per-frame mAP: 47.1 — *Shi et al., CVPR 2023.*
- Primary metric: per-frame mAP averaged over all 65 classes; official validation and test splits follow the original THUMOS-14 partitioning.

## Tooling & Ecosystem
- Official annotations and download: [https://ai.stanford.edu/~syyeung/everymoment.html](https://ai.stanford.edu/~syyeung/everymoment.html)
- Videos sourced from THUMOS-14; requires downloading the original THUMOS-14 videos separately.
- Compatible with [ActionFormer](https://github.com/happyharrycn/actionformer_release) and [MMAction2](https://github.com/open-mmlab/mmaction2) for temporal detection pipelines.
- Pre-extracted I3D and VideoMAE features are shared by the community for feature-based detection methods.

## Known Challenges
- Multi-label evaluation requires careful handling of overlapping actions; standard single-label metrics are insufficient.
- Significant class imbalance: common actions (standing, watching) have orders of magnitude more frames than rare ones.
- Temporal boundaries between overlapping actions are often ambiguous, leading to annotation noise.
- Videos are from sports broadcasts (primarily THUMOS-14 sports), limiting domain diversity.
- Some action classes are highly correlated (co-occurring), making independent class evaluation misleading.

## Cite
```bibtex
@article{yeung2018every,
  title   = {Every Moment Counts: Dense Detailed Labeling of Actions in Complex Videos},
  author  = {Yeung, Serena and Russakovsky, Olga and Jin, Ning and Andriluka, Mykhaylo and Mori, Greg and Fei-Fei, Li},
  journal = {International Journal of Computer Vision},
  volume  = {126},
  number  = {2--4},
  pages   = {375--389},
  year    = {2018}
}
```
