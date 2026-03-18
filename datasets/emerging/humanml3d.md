# HumanML3D

- **Modality:** 3D human motion (SMPL joint positions and rotations) + natural language text descriptions
- **Primary Tasks:** Text-to-motion generation, motion-to-text retrieval, motion captioning
- **Scale:** 14,616 motion sequences, 44,970 text descriptions, ~28.6 hours of motion data
- **License:** Research use only
- **Access:** [https://github.com/EricGuo5513/HumanML3D](https://github.com/EricGuo5513/HumanML3D)

## Summary
HumanML3D is the primary benchmark for text-conditioned human motion generation. It combines motion capture data from HumanAct12 and AMASS, re-processed into a unified representation, and paired with 44,970 natural language descriptions (approximately 3 descriptions per motion). The text annotations describe what the person is doing, how they move, and the direction/speed of movement. HumanML3D has become the standard evaluation dataset for text-to-motion models (MDM, MotionDiffuse, T2M-GPT, MLD), establishing metrics like FID, R-Precision, and Diversity that are now used across the field.

## Reference Paper
- *Chuan Guo, Shihao Zou, Xinxin Zuo, Sen Wang, Tianyu Ji, Xingyu Li, Li Cheng.* "Generating Diverse and Natural 3D Human Motions from Text." CVPR, 2022. [`PDF`](https://arxiv.org/abs/2212.04048)

## Benchmarks & Baselines
- **MDM** - FID: 0.544, R-Precision (Top-3): 0.611 — *Tevet et al., ICLR 2023.*
- **T2M-GPT** - FID: 0.116, R-Precision (Top-3): 0.775 — *Zhang et al., CVPR 2023.*
- **MLD** - FID: 0.473, R-Precision (Top-3): 0.772 — *Chen et al., CVPR 2023.*
- **MotionDiffuse** - FID: 0.630, R-Precision (Top-3): 0.782 — *Zhang et al., 2022.*
- Standard evaluation uses FID, R-Precision (Top 1/2/3), Diversity, and MultiModality metrics with the official test split.

## Tooling & Ecosystem
- [HumanML3D repo](https://github.com/EricGuo5513/HumanML3D) provides data processing, feature extraction, and evaluation scripts.
- [T2M-GPT](https://github.com/Mael-zys/T2M-GPT), [MDM](https://github.com/GuyTevet/motion-diffusion-model), [MLD](https://github.com/ChenFengYe/motion-latent-diffusion) all use HumanML3D as the primary benchmark.
- Motion representation uses 263-dimensional feature vectors (joint positions, velocities, rotations, foot contact).

## Known Challenges
- Motion data originates from AMASS mocap recordings, which are lab-captured and may not represent diverse real-world movements.
- Text descriptions are crowd-sourced and vary in specificity and quality.
- Standard metrics (FID, R-Precision) rely on a learned feature extractor whose quality directly affects evaluation reliability.
- Limited action diversity: most motions are locomotion, gestures, and basic interactions; complex or domain-specific motions are underrepresented.
- Evaluation protocol is sensitive to random seeds; variance across runs should be reported.

## Cite
```bibtex
@inproceedings{guo2022generating,
  title     = {Generating Diverse and Natural 3D Human Motions from Text},
  author    = {Guo, Chuan and Zou, Shihao and Zuo, Xinxin and Wang, Sen and Ji, Tianyu and Li, Xingyu and Cheng, Li},
  booktitle = {IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year      = {2022}
}
```
