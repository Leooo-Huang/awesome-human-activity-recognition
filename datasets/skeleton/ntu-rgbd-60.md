# NTU RGB+D 60

- **Modality:** RGB video, depth maps, 3D skeleton (25 joints), infrared
- **Primary Tasks:** Skeleton-based action recognition, cross-subject and cross-view evaluation
- **Scale:** 56,880 video samples, 60 action classes, 40 subjects, 80 viewpoints
- **License:** Research use only (requires signed agreement)
- **Access:** [https://rose1.ntu.edu.sg/dataset/actionRecognition/](https://rose1.ntu.edu.sg/dataset/actionRecognition/)

## Summary
NTU RGB+D 60 is the foundational large-scale dataset for skeleton-based action recognition, captured using Microsoft Kinect v2 sensors. It contains 56,880 action samples across 60 classes, including daily actions, mutual actions, and health-related activities. Each sample provides RGB frames, depth maps, infrared sequences, and 3D skeleton data (25 body joints per frame). Captured from 80 viewpoints with 40 distinct subjects, the dataset established the standard Cross-Subject (CS) and Cross-View (CV) evaluation protocols that are now ubiquitous in skeleton-based action recognition research. It was later extended to NTU RGB+D 120.

## Reference Paper
- *Amir Shahroudy, Jun Liu, Tian-Tsong Ng, Gang Wang.* "NTU RGB+D: A Large Scale Dataset for 3D Human Activity Analysis." CVPR, 2016. [`PDF`](https://arxiv.org/abs/1604.02808)

## Benchmarks & Baselines
- **ST-GCN** - CS: 81.5%, CV: 88.3% — *Yan et al., AAAI 2018.*
- **MS-G3D** - CS: 91.5%, CV: 96.2% — *Liu et al., CVPR 2020.*
- **CTR-GCN** - CS: 92.4%, CV: 96.8% — *Chen et al., ICCV 2021.*
- **HD-GCN** - CS: 93.4%, CV: 97.2% — *Lee et al., ICCV 2023.*
- Two standard protocols: Cross-Subject (20/20 subject split) and Cross-View (2 views train / 1 view test).

## Tooling & Ecosystem
- [MMSkeleton](https://github.com/open-mmlab/mmskeleton) and its successor provide skeleton action recognition pipelines.
- [ST-GCN](https://github.com/yysijie/st-gcn) — the original graph convolution baseline code.
- [PYSKL](https://github.com/kennymckormick/pyskl) — comprehensive skeleton action recognition toolbox.
- Skeleton data is provided in `.skeleton` format; community converters to NumPy are widely available.

## Known Challenges
- Kinect skeleton noise: occluded joints and tracking failures produce noisy skeleton sequences.
- Lab-controlled environment limits generalization to in-the-wild scenarios.
- Some missing skeleton files (~300 samples with corrupted data); community lists of excluded samples exist.
- Cross-view protocol is considered largely solved; Cross-Subject remains more discriminative.

## Cite
```bibtex
@inproceedings{shahroudy2016ntu,
  title     = {NTU RGB+D: A Large Scale Dataset for 3D Human Activity Analysis},
  author    = {Shahroudy, Amir and Liu, Jun and Ng, Tian-Tsong and Wang, Gang},
  booktitle = {IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year      = {2016}
}
```
