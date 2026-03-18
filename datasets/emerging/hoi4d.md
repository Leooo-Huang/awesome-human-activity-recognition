# HOI4D

- **Modality:** Egocentric RGB-D video, 3D hand pose, object 6DoF pose, point clouds
- **Primary Tasks:** Egocentric hand-object interaction understanding, action segmentation, 3D object reconstruction
- **Scale:** 4,000+ video clips, 800+ object instances, 16 categories, 610 indoor scenes, ~2.4M RGB-D frames
- **License:** Research use only
- **Access:** [https://hoi4d.github.io/](https://hoi4d.github.io/)

## Summary
HOI4D is a large-scale egocentric dataset for 4D (3D + temporal) hand-object interaction understanding. It captures human manipulation of diverse objects in real indoor scenes using head-mounted RGB-D cameras. The dataset provides rich annotations including 3D hand poses, object 6DoF poses, dense 3D point cloud segmentation, action labels, and panoptic segmentation. HOI4D enables research at the intersection of egocentric vision, hand-object interaction, and 3D scene understanding, with applications in robotics, AR/VR, and embodied AI.

## Reference Paper
- *Yunze Liu, Yun Liu, Che Jiang, Kangbo Lyu, Weikang Wan, Hao Shen, Boqiang Liang, Zhoujie Fu, He Wang, Li Yi.* "HOI4D: A 4D Egocentric Dataset for Category-Level Human-Object Interaction." CVPR, 2022. [`PDF`](https://arxiv.org/abs/2203.01577)

## Benchmarks & Baselines
- **Action Segmentation (Edit Score):** MS-TCN++ — 65.1% — *Liu et al., CVPR 2022.*
- **Hand Pose Estimation (MPJPE):** baseline — ~15mm — reported in the paper.
- **Object Pose Estimation:** category-level 6DoF baselines provided.
- Evaluation uses task-specific metrics; the dataset supports multiple tasks with different evaluation protocols.

## Tooling & Ecosystem
- [Official project page](https://hoi4d.github.io/) provides data downloads, annotations, and visualization tools.
- [HOI4D GitHub repo](https://github.com/leolyliu/HOI4D-Instructions) contains data loading and evaluation scripts.
- Compatible with egocentric vision frameworks and hand pose estimation pipelines (e.g., FrankMocap, HaMeR).

## Known Challenges
- Egocentric viewpoint with frequent hand occlusions makes pose estimation difficult.
- Large variation in object shapes within categories challenges category-level pose estimation.
- 4D annotation (temporal 3D) is expensive; some annotations may have noise in rapid manipulation sequences.
- Indoor scenes only; outdoor hand-object interactions are not covered.
- Requires substantial compute for processing high-resolution RGB-D streams with 3D annotations.

## Cite
```bibtex
@inproceedings{liu2022hoi4d,
  title     = {HOI4D: A 4D Egocentric Dataset for Category-Level Human-Object Interaction},
  author    = {Liu, Yunze and Liu, Yun and Jiang, Che and Lyu, Kangbo and Wan, Weikang and Shen, Hao and Liang, Boqiang and Fu, Zhoujie and Wang, He and Yi, Li},
  booktitle = {IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year      = {2022}
}
```
