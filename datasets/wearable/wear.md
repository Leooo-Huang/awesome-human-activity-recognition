# WEAR

- **Modality:** 4x Bangle.js smartwatches (accelerometer + gyroscope, 50 Hz) + GoPro egocentric video
- **Primary Tasks:** Outdoor sports activity recognition, wearable HAR benchmarking, egocentric activity verification
- **Scale:** 22 participants, 18 workout activities, 11 outdoor locations, ~18 hours of data
- **License:** Creative Commons Attribution 4.0 (CC BY 4.0)
- **Access:** [https://github.com/mariusbock/wear](https://github.com/mariusbock/wear)

## Summary
WEAR is an outdoor sports dataset combining data from four open-source Bangle.js smartwatches (both wrists and ankles) with synchronized egocentric GoPro video. The focus on outdoor workout activities across diverse real-world locations distinguishes it from lab-based wearable datasets. The use of affordable, open-source hardware (Bangle.js) lowers the barrier for replication and extension. WEAR supports research in multi-device wearable fusion, egocentric video verification of IMU-based predictions, and robust HAR under uncontrolled outdoor conditions.

## Reference Paper
- *Marius Bock et al.* "WEAR: An Outdoor Sports Dataset for Wearable and Egocentric Activity Recognition." IMWUT, 2024. [`PDF`](https://dl.acm.org/doi/10.1145/3659597)

## Benchmarks & Baselines
- **DeepConvLSTM** - F1-score reported on LOSO evaluation; *Bock et al., IMWUT 2024.*
- **Transformer baseline** - Competitive F1 with attention-based temporal modeling on inertial streams.
- **Video baseline** - Egocentric video recognition accuracy provided for comparison with wearable-only models.
- Official evaluation protocol uses leave-one-subject-out (LOSO) cross-validation.

## Tooling & Ecosystem
- Official [mariusbock/wear](https://github.com/mariusbock/wear) repository with data loaders, preprocessing scripts, and baseline implementations.
- Built on [Bangle.js](https://banglejs.com/) open-source smartwatch platform; firmware and data collection apps are publicly available.
- Compatible with [PyTorch](https://pytorch.org/) and standard wearable HAR pipelines; sliding window segmentation scripts included.

## Known Challenges
- Outdoor recording introduces GPS drift, variable lighting for video, and environmental noise in accelerometer signals (e.g., wind, uneven terrain).
- Bangle.js consumer-grade sensors have higher noise floors compared to research-grade IMUs; calibration may improve results.
- Activity transitions and rest periods between exercises require careful segmentation.
- 22 participants is moderate; cross-dataset evaluation recommended for generalization claims.

## Cite
```
@article{bock2024wear,
  title   = {WEAR: An Outdoor Sports Dataset for Wearable and Egocentric Activity Recognition},
  author  = {Bock, Marius and Malmgren-Hansen, David and Moeslund, Thomas B. and others},
  journal = {Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies},
  year    = {2024}
}
```
