# Motion-X++

- **Modality:** Whole-body motion capture (SMPL-X), text descriptions, facial expressions, hand poses
- **Primary Tasks:** Whole-body motion generation, text-to-motion synthesis, facial expression generation
- **Scale:** 120,900+ motion sequences, multi-granularity text labels (sequence-level and segment-level), covering diverse action categories
- **License:** Research use only (non-commercial); requires SMPL-X license
- **Access:** [https://motion-x-dataset.github.io/](https://motion-x-dataset.github.io/)

## Summary
Motion-X++ is a substantial extension of the Motion-X dataset, designed to advance whole-body motion generation including facial expressions and hand gestures. It unifies motion data from multiple sources into SMPL-X format and pairs each sequence with multi-granularity text annotations — from coarse action labels to fine-grained natural language descriptions of body, hand, and face movements. The dataset supports text-driven generation of expressive full-body motions, filling a gap left by earlier datasets that focused only on body pose without facial or hand detail. Motion-X++ enables research in controllable motion synthesis, motion-language alignment, and expressive avatar animation.

## Reference Paper
- *Jing Lin, Ailing Zeng, Shunlin Lu, Yuanhao Cai, Ruimao Zhang, Haoqian Wang, Lei Zhang.* "Motion-X: A Large-scale 3D Expressive Whole-body Human Motion Dataset." NeurIPS, 2024. [`PDF`](https://arxiv.org/abs/2307.00818)

## Benchmarks & Baselines
- **T2M-GPT** - FID: 0.116 on Motion-X test split — *Lin et al., 2024.*
- **MotionGPT** - FID: 0.232, R-Precision Top-3: 0.782 — *Jiang et al., 2024.*
- Evaluation follows text-to-motion generation protocol: FID, R-Precision, Diversity, and Multi-modality on the official test split.
- Separate evaluation tracks for body-only and whole-body (body + hands + face) generation.

## Tooling & Ecosystem
- Official toolkit: [https://github.com/IDEA-Research/Motion-X](https://github.com/IDEA-Research/Motion-X) — includes data processing, visualization, and baseline training scripts.
- Requires [SMPL-X body model](https://smpl-x.is.tue.mpg.de/) for interpreting motion parameters.
- Compatible with [HumanML3D](https://github.com/EricGuo5513/HumanML3D) evaluation pipeline for body-only benchmarks.
- Visualization tools support rendering in Blender and PyTorch3D.

## Known Challenges
- Large storage requirements (hundreds of GB for the full dataset including all modalities).
- Facial expression and hand pose annotations have higher noise levels than body pose due to capture limitations.
- Multi-granularity text alignment is non-trivial: segment-level descriptions may not perfectly match temporal boundaries.
- Requires separate SMPL-X license agreement from MPI, adding friction to data access.

## Cite
```bibtex
@inproceedings{lin2024motionx,
  title     = {Motion-X: A Large-scale 3D Expressive Whole-body Human Motion Dataset},
  author    = {Lin, Jing and Zeng, Ailing and Lu, Shunlin and Cai, Yuanhao and Zhang, Ruimao and Wang, Haoqian and Zhang, Lei},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  year      = {2024}
}
```
