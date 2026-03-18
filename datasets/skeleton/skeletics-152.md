# Skeletics-152

- **Modality:** 2D/3D skeleton (estimated from RGB video)
- **Primary Tasks:** Large-scale skeleton action recognition
- **Scale:** ~150,000 clips, 152 action classes
- **License:** Research use only
- **Access:** [https://github.com/skelemoa/quater-gcn](https://github.com/skelemoa/quater-gcn)

## Summary
Skeletics-152 is a large-scale skeleton action recognition dataset created by extracting 2D and 3D pose estimates from a subset of Kinetics videos. With 152 action classes and approximately 150,000 clips, it is significantly larger and more diverse than lab-captured skeleton datasets like NTU RGB+D. The skeletons are estimated using pose estimation models (e.g., OpenPose, HRNet) rather than captured with depth sensors, making the data representative of in-the-wild conditions. This dataset bridges the gap between large-scale video action recognition and skeleton-based methods, enabling evaluation of skeleton models at scale.

## Reference Paper
- *Anuj Gupta, Juhi Monga, Sai Srinivas Kancheti, Gandharv Relan, Ankur Sinha, Saurabh Gupta.* "Quo Vadis, Skeleton Action Recognition?" International Journal of Computer Vision (IJCV), 2021. [`PDF`](https://arxiv.org/abs/2007.02072)

## Benchmarks & Baselines
- **ST-GCN** - Top-1: ~36% — *Gupta et al., IJCV 2021.*
- **QuaterGCN** - Top-1: ~39% — *Gupta et al., IJCV 2021.*
- **MS-G3D** - Top-1: ~41% — reported in follow-up works.
- Standard evaluation uses the official train/val splits provided by the authors.

## Tooling & Ecosystem
- [QuaterGCN repo](https://github.com/skelemoa/quater-gcn) provides data preparation scripts, skeleton extraction pipeline, and baseline code.
- Skeleton extraction relies on [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) or [HRNet](https://github.com/leoxiaobin/deep-high-resolution-net.pytorch).
- Compatible with standard GCN-based skeleton action recognition codebases.

## Known Challenges
- Estimated skeletons are inherently noisier than sensor-captured data (Kinect); pose estimation failures on occluded or small subjects are common.
- Requires downloading the original Kinetics videos, which are subject to YouTube link decay.
- 152-class vocabulary at skeleton level is substantially harder than 60 or 120 classes; many classes are not easily distinguishable from skeleton data alone.
- Multi-person scenes require person tracking and skeleton assignment as preprocessing.

## Cite
```bibtex
@article{gupta2021quovadis,
  title   = {Quo Vadis, Skeleton Action Recognition?},
  author  = {Gupta, Anuj and Monga, Juhi and Kancheti, Sai Srinivas and Relan, Gandharv and Sinha, Ankur and Gupta, Saurabh},
  journal = {International Journal of Computer Vision},
  year    = {2021}
}
```
