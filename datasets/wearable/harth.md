# HARTH (Human Activity Recognition Trondheim)

- **Modality:** Accelerometer (dual-sensor: thigh and lower back)
- **Primary Tasks:** Free-living human activity recognition, sedentary behavior classification
- **Scale:** 22 subjects, ~5.5 hours of labeled data per subject, 12 activity classes, 50 Hz sampling rate
- **License:** CC BY 4.0 — [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)
- **Access:** [https://archive.ics.uci.edu/dataset/779/harth](https://archive.ics.uci.edu/dataset/779/harth)

## Summary
HARTH is a professionally annotated dataset for human activity recognition collected under free-living (real-world) conditions in Trondheim, Norway. Participants wore two three-axis accelerometers (thigh and lower back) while performing their normal daily routines, with trained annotators labeling activities from synchronized video recordings. This distinguishes HARTH from most HAR datasets that rely on scripted lab protocols: the data captures natural transitions, varying intensities, and interleaved activities as they occur in daily life. The 2024 benchmark update introduced standardized evaluation protocols and cross-subject validation splits, making it a reliable testbed for comparing wearable HAR methods under realistic conditions.

## Reference Paper
- *Aleksej Logacjov, Kerstin Bach, Atle Kongsvold, Hilde Bremseth Bardstu, Paul Jarle Mork.* "HARTH: A Human Activity Recognition Dataset for Machine Learning." Sensors, 2021. [`PDF`](https://doi.org/10.3390/s21237853)

## Benchmarks & Baselines
- **Random Forest** - F1-score: 0.82 (leave-one-subject-out) — *Logacjov et al., 2021.*
- **XGBoost** - F1-score: 0.84 (leave-one-subject-out) — *Logacjov et al., 2021.*
- **DeepConvLSTM** - F1-score: 0.79 (leave-one-subject-out) — *Benchmark update, 2024.*
- Standard protocol: leave-one-subject-out cross-validation; macro-averaged F1 is the primary metric.
- 12 classes include walking, running, cycling, sitting, standing, lying, stairs up/down, and transitions.

## Tooling & Ecosystem
- Official data repository: [https://github.com/aleksejlogacjov/HARTH](https://github.com/aleksejlogacjov/HARTH)
- CSV format with timestamps, accelerometer readings, and activity labels — easy to load with pandas.
- Compatible with standard HAR preprocessing pipelines (sliding window segmentation, feature extraction).
- Works with [TSFEL](https://github.com/fraunhoferportugal/tsfel) for automated time-series feature extraction.

## Known Challenges
- Free-living data contains natural class imbalance: sedentary activities (sitting, standing) dominate over dynamic ones (running, cycling).
- Transitions between activities are gradual and ambiguous, unlike clean lab recordings.
- Only two sensor locations (thigh and lower back); no wrist or ankle data, limiting certain posture-related analyses.
- Inter-subject variability is high due to differences in body composition, gait, and daily routines.
- Video annotations have inherent subjectivity, especially for distinguishing between similar sedentary postures.

## Cite
```bibtex
@article{logacjov2021harth,
  title   = {HARTH: A Human Activity Recognition Dataset for Machine Learning},
  author  = {Logacjov, Aleksej and Bach, Kerstin and Kongsvold, Atle and Bardstu, Hilde Bremseth and Mork, Paul Jarle},
  journal = {Sensors},
  volume  = {21},
  number  = {23},
  pages   = {7853},
  year    = {2021}
}
```
