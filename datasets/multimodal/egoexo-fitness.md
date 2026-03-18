# EgoExo-Fitness

- **Modality:** Synchronized egocentric + exocentric RGB video, body pose (keypoints)
- **Primary Tasks:** Action quality assessment, ego-exo action understanding, keypoint verification, natural language action commentary
- **Scale:** 31 hours of video, 1248 video sequences, 6000+ action instances
- **License:** Research use only (non-commercial)
- **Access:** [https://github.com/iSEE-Laboratory/EgoExo-Fitness](https://github.com/iSEE-Laboratory/EgoExo-Fitness)

## Summary
EgoExo-Fitness captures synchronized first-person and third-person views of fitness exercises, annotated with body keypoints, action quality scores, keypoint-level correctness verification, and natural language comments describing form errors. This combination supports a unique research direction: not just recognizing what action is performed, but assessing how well it is performed from complementary viewpoints. The dataset targets applications in AI coaching, rehabilitation monitoring, and embodied action understanding.

## Reference Paper
- *Li et al.* "EgoExo-Fitness: Towards Egocentric and Exocentric Full-Body Action Understanding." ECCV, 2024. [`PDF`](https://arxiv.org/abs/2406.08877)

## Benchmarks & Baselines
- **Action Quality Assessment Baseline** - Spearman correlation reported for ego, exo, and fused settings; *Li et al., ECCV 2024.*
- **Keypoint Verification** - Per-joint correctness accuracy provided in official evaluation.
- **NL Comment Generation** - BLEU / CIDEr scores for generated form-correction comments.
- Official splits separate participants for train/val/test to prevent identity leakage.

## Tooling & Ecosystem
- Official [iSEE-Laboratory/EgoExo-Fitness](https://github.com/iSEE-Laboratory/EgoExo-Fitness) repository with data loaders, annotation tools, and baseline models.
- Keypoint annotations compatible with COCO pose format for use with [MMPose](https://github.com/open-mmlab/mmpose) and [ViTPose](https://github.com/ViTAE-Transformer/ViTPose).
- Ego-exo pairing structure aligns with [Ego-Exo4D](../emerging/ego-exo4d.md) conventions for cross-dataset transfer experiments.

## Known Challenges
- Egocentric view suffers from heavy self-occlusion during many fitness exercises; keypoint estimation quality degrades for limbs behind the body.
- Action quality is subjective; inter-annotator agreement varies across exercise types.
- Synchronization between ego and exo cameras must be carefully verified at the frame level for quality assessment tasks.
- Dataset focuses on fitness exercises; generalization to other action domains is not guaranteed.

## Cite
```
@inproceedings{li2024egoexofitness,
  title     = {EgoExo-Fitness: Towards Egocentric and Exocentric Full-Body Action Understanding},
  author    = {Li, Yuan and others},
  booktitle = {Proceedings of the European Conference on Computer Vision},
  year      = {2024}
}
```
