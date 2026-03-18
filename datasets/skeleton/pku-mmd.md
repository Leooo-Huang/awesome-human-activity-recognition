# PKU-MMD

- **Modality:** RGB video, depth, infrared, 3D skeleton (25 joints)
- **Primary Tasks:** Action detection, action recognition, skeleton-based activity understanding
- **Scale:** ~20,000 action instances, 51 action classes, 66 subjects, ~1,076 long video sequences
- **License:** Research use only (PKU terms)
- **Access:** [https://www.icst.pku.edu.cn/struct/Projects/PKUMMD.html](https://www.icst.pku.edu.cn/struct/Projects/PKUMMD.html)

## Summary
PKU-MMD (Peking University Multi-Modality Dataset) is a large-scale benchmark for continuous multi-modality action detection and recognition. Unlike NTU RGB+D which provides pre-segmented clips, PKU-MMD contains long untrimmed sequences where subjects perform multiple actions consecutively, making it suitable for temporal action detection. The dataset was captured using Microsoft Kinect v2 sensors and includes two phases: Phase I with nearly noise-free data and Phase II with more realistic, noisy conditions. Each sample includes synchronized RGB, depth, infrared, and skeleton modalities.

## Reference Paper
- *Chunhui Liu, Yueyu Hu, Yanghao Li, Sijie Song, Jiaying Liu.* "PKU-MMD: A Large Scale Benchmark for Skeleton-Based Human Action Understanding." ACM Multimedia Workshop, 2017. [`PDF`](https://arxiv.org/abs/1703.07475)

## Benchmarks & Baselines
- **ST-GCN (Action Recognition, CS)** - Top-1: 93.7% (Phase I) — *Yan et al., AAAI 2018.*
- **Action Detection (Phase I, mAP@0.5)** - ~85% with two-stage approaches — reported in follow-up works.
- **Phase II** is significantly harder due to larger view variation and noisier skeletons.
- Two evaluation protocols: Cross-Subject and Cross-View, following NTU RGB+D conventions.

## Tooling & Ecosystem
- [Official project page](https://www.icst.pku.edu.cn/struct/Projects/PKUMMD.html) provides data and annotation files.
- Compatible with NTU RGB+D skeleton processing pipelines (same Kinect v2 format, 25 joints).
- [PYSKL](https://github.com/kennymckormick/pyskl) supports PKU-MMD evaluation.

## Known Challenges
- Phase II data contains significant skeleton noise and viewpoint variation, making it substantially harder than Phase I.
- Temporal action detection in continuous sequences is more challenging than classification of pre-segmented clips.
- Some action transitions are ambiguous, making precise boundary annotation difficult.
- Dataset is less widely benchmarked than NTU RGB+D, resulting in fewer published baselines.

## Cite
```bibtex
@article{liu2017pkummd,
  title   = {PKU-MMD: A Large Scale Benchmark for Skeleton-Based Human Action Understanding},
  author  = {Liu, Chunhui and Hu, Yueyu and Li, Yanghao and Song, Sijie and Liu, Jiaying},
  journal = {arXiv preprint arXiv:1703.07475},
  year    = {2017}
}
```
