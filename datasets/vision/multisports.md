# MultiSports

- **Modality:** RGB video
- **Primary Tasks:** Fine-grained spatio-temporal action detection in sports videos
- **Scale:** 3,200 video clips, 66 fine-grained sports action classes, 37,701 action instances, 902 video-level labels across 4 sports (basketball, volleyball, football, gymnastics)
- **License:** Research use only (non-commercial)
- **Access:** [https://deeperaction.github.io/multisports/](https://deeperaction.github.io/multisports/)

## Summary
MultiSports is a multi-person spatio-temporal action detection dataset focusing on fine-grained sports actions. Unlike coarse action recognition benchmarks, MultiSports requires distinguishing between visually similar actions within the same sport (e.g., different types of basketball shots or gymnastic moves). Each action instance is annotated with a spatio-temporal tube — bounding boxes across consecutive frames — enabling evaluation of both spatial localization and temporal extent. The dataset was introduced at ICCV 2021 and received a major benchmark update in 2024 with improved annotations and evaluation protocols, establishing it as a key testbed for fine-grained temporal action detection in multi-person sports settings.

## Reference Paper
- *Yixuan Li, Lei Chen, Runyu He, Zhenzhi Wang, Gangshan Wu, Limin Wang.* "MultiSports: A Multi-Person Video Dataset of Spatio-Temporally Localized Sports Actions." ICCV, 2021. [`PDF`](https://arxiv.org/abs/2105.07404)

## Benchmarks & Baselines
- **SlowFast R101** - Frame-mAP@0.5: 17.5 — *Li et al., ICCV 2021.*
- **MOC Detector** - Video-mAP@0.2: 12.4 — *Li et al., ICCV 2021.*
- **TubeR** - Frame-mAP@0.5: 22.3 — *Zhao et al., CVPR 2022.*
- Standard evaluation uses frame-level mAP at IoU 0.5 and video-level mAP at multiple IoU thresholds; official train/val/test splits provided.

## Tooling & Ecosystem
- Official code and annotations: [https://github.com/MCG-NJU/MultiSports](https://github.com/MCG-NJU/MultiSports)
- Compatible with [MMAction2](https://github.com/open-mmlab/mmaction2) and [SlowFast](https://github.com/facebookresearch/SlowFast) frameworks.
- Evaluation toolkit included in the official repository for frame-mAP and video-mAP computation.

## Known Challenges
- Fine-grained distinctions between sports actions require high temporal resolution and precise spatial localization.
- Severe class imbalance: some action categories have far fewer instances than others.
- Multi-person scenes with occlusions, fast motion, and camera movement make detection difficult.
- Videos sourced from broadcast sports footage with varying camera angles and production styles.

## Cite
```bibtex
@inproceedings{li2021multisports,
  title     = {MultiSports: A Multi-Person Video Dataset of Spatio-Temporally Localized Sports Actions},
  author    = {Li, Yixuan and Chen, Lei and He, Runyu and Wang, Zhenzhi and Wu, Gangshan and Wang, Limin},
  booktitle = {IEEE/CVF International Conference on Computer Vision (ICCV)},
  year      = {2021}
}
```
