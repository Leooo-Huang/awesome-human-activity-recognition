# Diving48

- **Modality:** RGB video
- **Primary Tasks:** Fine-grained action recognition, temporal reasoning
- **Scale:** ~18,000 video clips, 48 diving action classes
- **License:** Research use only
- **Access:** [http://www.svcl.ucsd.edu/projects/resound/dataset.html](http://www.svcl.ucsd.edu/projects/resound/dataset.html)

## Summary
Diving48 is a fine-grained video classification dataset focusing on competitive diving. It contains approximately 18,000 trimmed video clips of 48 unambiguous dive sequences, defined by FINA (the international swimming federation) dive vocabulary. The dataset is specifically designed to test temporal reasoning capabilities, as the 48 classes differ primarily in the ordering and composition of atomic movements (takeoff, somersaults, twists, entry). Static frame-level features are largely uninformative, making Diving48 a strong benchmark for evaluating temporal modeling architectures.

## Reference Paper
- *Yingwei Li, Yi Li, Nuno Vasconcelos.* "RESOUND: Towards Action Recognition without Representation Bias." ECCV, 2018. [`PDF`](https://arxiv.org/abs/1807.06168)

## Benchmarks & Baselines
- **TSN (RGB)** - Top-1: 16.8% — *Li et al., ECCV 2018.*
- **TDN** - Top-1: 87.6% — *Wang et al., CVPR 2021.*
- **Video Swin-B** - Top-1: 88.0% — *Liu et al., CVPR 2022.*
- **GSF** - Top-1: 83.1% — *Sudhakaran et al., ICCV 2021.*
- Standard evaluation uses the official V2 train/test split.

## Tooling & Ecosystem
- [MMAction2](https://github.com/open-mmlab/mmaction2) includes Diving48 dataset configs.
- [TimeSformer](https://github.com/facebookresearch/TimeSformer) reports Diving48 results.
- Annotations and splits available from the official project page.

## Known Challenges
- Static appearance cues are nearly useless; models must rely on temporal order and dynamics.
- Some dive classes are extremely rare, leading to significant class imbalance.
- V1 annotations contained label noise; V2 cleaned annotations are recommended.
- All clips are from a single domain (competitive diving), limiting generalization studies.

## Cite
```bibtex
@inproceedings{li2018resound,
  title     = {RESOUND: Towards Action Recognition without Representation Bias},
  author    = {Li, Yingwei and Li, Yi and Vasconcelos, Nuno},
  booktitle = {European Conference on Computer Vision (ECCV)},
  year      = {2018}
}
```
