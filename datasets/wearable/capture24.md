# CAPTURE-24

- **Modality:** Wrist-worn Axivity AX3 accelerometer (100 Hz) + wearable camera + sleep diary
- **Primary Tasks:** Free-living activity recognition, wearable HAR benchmarking, sedentary behavior analysis
- **Scale:** 151 participants, 3883 hours total (2562 annotated), 200+ activity labels mapped to Compendium of Physical Activities
- **License:** Creative Commons Attribution 4.0 (CC BY 4.0)
- **Access:** [https://github.com/OxWearables/capture24](https://github.com/OxWearables/capture24)

## Summary
CAPTURE-24 is the largest annotated wrist-worn accelerometer dataset collected in free-living conditions, 2-3 orders of magnitude larger than prior wearable HAR datasets. Participants from the Oxford area wore an Axivity AX3 on the wrist alongside a body-worn camera that provided ground-truth annotations. The combination of scale, ecological validity, and fine-grained labeling (200+ activities) makes it a critical resource for training and evaluating models intended for population-level physical activity epidemiology.

## Reference Paper
- *Matthew Willetts et al.* "CAPTURE-24: A large dataset of wrist-worn activity tracker data collected in the wild for human activity recognition." Scientific Data, 2024. [`PDF`](https://www.nature.com/articles/s41597-024-03960-3)

## Benchmarks & Baselines
- **Random Forest (hand-crafted features)** - Balanced accuracy ~75% on Willetts split; *Willetts et al., 2024.*
- **SSL-pretrained CNN** - Balanced accuracy ~80% (5-class sleep/sedentary/light/moderate/vigorous); Oxford Wearables Group baselines.
- Official evaluation uses per-participant held-out splits; results reported on both 200+ fine-grained and coarser activity groupings.

## Tooling & Ecosystem
- Official [OxWearables/capture24](https://github.com/OxWearables/capture24) repository with data loading and preprocessing scripts.
- [actipy](https://github.com/OxWearables/actipy) library for raw accelerometer signal processing and feature extraction.
- [ssl-wearables](https://github.com/OxWearables/ssl-wearables) provides self-supervised pre-training recipes compatible with CAPTURE-24.

## Known Challenges
- Wearable camera annotations can miss activities performed in low-light or private settings; sleep diary supplements these gaps.
- Label granularity varies across participants depending on camera image quality and annotator agreement.
- Class distribution is heavily skewed toward sedentary and sleep; class-weighted evaluation is recommended.
- Raw data is large (~several GB); plan storage accordingly for full 100 Hz signals.

## Cite
```
@article{willetts2024capture24,
  title   = {CAPTURE-24: A large dataset of wrist-worn activity tracker data collected in the wild for human activity recognition},
  author  = {Willetts, Matthew and Sherlock, Aidan and Sherwood, Owen and others},
  journal = {Scientific Data},
  year    = {2024}
}
```
