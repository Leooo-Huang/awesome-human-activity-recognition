# NTU RGB+D Mutual Actions

- **Modality:** RGB video, depth maps, 3D skeleton (25 joints per person), infrared
- **Primary Tasks:** Two-person interaction recognition, mutual action recognition
- **Scale:** 26 mutual action classes, ~14,000 interaction samples (subset of NTU RGB+D 120)
- **License:** Research use only (requires signed agreement via NTU)
- **Access:** [https://rose1.ntu.edu.sg/dataset/actionRecognition/](https://rose1.ntu.edu.sg/dataset/actionRecognition/)

## Summary
NTU RGB+D Mutual Actions refers to the subset of mutual/interaction action classes from the NTU RGB+D 60 and NTU RGB+D 120 datasets. These samples involve two-person interactions such as handshaking, hugging, pushing, kicking, and pointing. The original NTU RGB+D 60 includes 11 mutual action classes (A50-A60), and NTU RGB+D 120 extends this to 26 mutual classes (adding A106-A120). Each sample provides synchronized skeleton data for both persons, making it the primary benchmark for skeleton-based interaction recognition. The two-person setting introduces unique challenges including person ordering ambiguity, interaction modeling, and relational reasoning between skeletons.

## Reference Paper
- *Jun Liu, Amir Shahroudy, Mauricio Perez, Gang Wang, Ling-Yu Duan, Alex C. Kot.* "NTU RGB+D 120: A Large-Scale Benchmark for 3D Human Activity Understanding." IEEE TPAMI, 2020. [`PDF`](https://arxiv.org/abs/1905.04757)

## Benchmarks & Baselines
- **ST-GCN (mutual subset, CS)** - Top-1: ~82% — adapted from single-person ST-GCN.
- **2s-AGCN (mutual subset)** - Top-1: ~88% — *Shi et al., CVPR 2019.*
- **IGFormer** - Top-1: ~93% — *Li et al., ECCV 2022* (interaction-specific transformer).
- Evaluation follows NTU RGB+D Cross-Subject and Cross-Setup protocols, filtered to mutual action classes only.

## Tooling & Ecosystem
- Skeleton data is accessed through the NTU RGB+D 60/120 download; mutual action classes can be filtered by action ID.
- [PYSKL](https://github.com/kennymckormick/pyskl) supports multi-person skeleton action recognition.
- Several interaction-specific GCN architectures have open-source implementations on GitHub.

## Known Challenges
- Person ordering: which skeleton is "person 1" vs "person 2" is arbitrary in Kinect capture, requiring order-invariant models.
- Interaction semantics: actions like "pushing" and "patting" differ subtly and require modeling the relationship between two skeletons.
- Some mutual actions are asymmetric (e.g., "pointing at someone"), but standard models treat both persons equivalently.
- Missing or noisy second-person skeleton data when the Kinect fails to track both subjects simultaneously.

## Cite
```bibtex
@article{liu2020ntu120,
  title   = {NTU RGB+D 120: A Large-Scale Benchmark for 3D Human Activity Understanding},
  author  = {Liu, Jun and Shahroudy, Amir and Perez, Mauricio and Wang, Gang and Duan, Ling-Yu and Kot, Alex C.},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
  volume  = {42},
  number  = {10},
  pages   = {2684--2701},
  year    = {2020}
}
```
