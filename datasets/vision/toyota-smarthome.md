# Toyota Smarthome

- **Modality:** RGB video, depth, 3D skeleton (multi-view)
- **Primary Tasks:** Daily living activity recognition, cross-view action recognition
- **Scale:** 16,115 video clips, 31 activity classes, 18 subjects, 7 camera views
- **License:** Research use only (Toyota terms, requires signed agreement)
- **Access:** [https://project.inria.fr/toyotasmarthome/](https://project.inria.fr/toyotasmarthome/)

## Summary
Toyota Smarthome captures real daily living activities performed by older adults in a smarthome environment. Unlike scripted datasets, subjects were given minimal instructions, resulting in natural and spontaneous activity performance. The dataset includes 31 activity classes (e.g., cooking, eating, watching TV, taking medicine) captured from 7 different camera viewpoints. This multi-view setup and the focus on elderly subjects make it particularly valuable for developing assistive living and smart home monitoring systems. The dataset provides both cross-subject and cross-view evaluation protocols.

## Reference Paper
- *Srijan Das, Rui Dai, Michal Koperski, Luca Minciullo, Lorenzo Garber, Francois Bremond, Gianpiero Francesca.* "Toyota Smarthome: Real-World Activities of Daily Living." ICCV, 2019. [`PDF`](https://arxiv.org/abs/1903.02398)

## Benchmarks & Baselines
- **I3D (CS protocol)** - Top-1: 54.8% — *Das et al., ICCV 2019.*
- **I3D (CV1 protocol)** - Top-1: 35.5% — *Das et al., ICCV 2019.*
- **ST-GCN (skeleton, CS)** - Top-1: 48.2% — *Das et al., ICCV 2019.*
- Two evaluation protocols: Cross-Subject (CS) and Cross-View (CV1, CV2).

## Tooling & Ecosystem
- [Official project page](https://project.inria.fr/toyotasmarthome/) provides download and annotation files.
- Skeleton extraction scripts and evaluation code are provided by the authors.
- Compatible with standard video understanding frameworks (MMAction2, PySlowFast).

## Known Challenges
- Elderly subjects perform activities slowly and with significant variation, differing from younger-subject datasets.
- Large viewpoint variation across 7 cameras makes cross-view recognition particularly difficult.
- Some activities are visually similar (e.g., "sit down" vs "fall down") and differ mainly in speed/context.
- Class imbalance: common activities (sitting, standing) are over-represented.
- Access requires a signed agreement with Toyota.

## Cite
```bibtex
@inproceedings{das2019toyota,
  title     = {Toyota Smarthome: Real-World Activities of Daily Living},
  author    = {Das, Srijan and Dai, Rui and Koperski, Michal and Minciullo, Luca and Garber, Lorenzo and Bremond, Francois and Francesca, Gianpiero},
  booktitle = {IEEE International Conference on Computer Vision (ICCV)},
  year      = {2019}
}
```
