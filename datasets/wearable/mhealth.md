# mHealth

- **Modality:** IMU (accelerometer, gyroscope, magnetometer), ECG (electrocardiogram)
- **Primary Tasks:** Mobile health activity recognition, physiological monitoring
- **Scale:** 10 subjects, 12 activity classes, body-worn sensors at 3 placements
- **License:** Public domain (UCI Machine Learning Repository)
- **Access:** [https://archive.ics.uci.edu/ml/datasets/MHEALTH+Dataset](https://archive.ics.uci.edu/ml/datasets/MHEALTH+Dataset)

## Summary
The mHealth (Mobile Health) dataset was collected to evaluate activity recognition for mobile health applications. Ten volunteers performed 12 physical activities while wearing sensors on the chest, right wrist, and left ankle. Each sensor unit recorded tri-axial accelerometer, gyroscope, and magnetometer data, and the chest sensor additionally captured 2-lead ECG signals. The combination of motion and physiological signals, multiple body placements, and health-oriented activity classes makes mHealth a useful benchmark for wearable health monitoring research.

## Reference Paper
- *Oresti Banos, Rafael Garcia, Juan A. Holgado-Terriza, Miguel Damas, Hector Pomares, Ignacio Rojas, Alejandro Saez, Claudia Villalonga.* "mHealthDroid: A Novel Framework for Agile Development of Mobile Health Applications." IWAAL, 2014. [`PDF`](https://link.springer.com/chapter/10.1007/978-3-319-13105-4_14)

## Benchmarks & Baselines
- **Random Forest** - Accuracy: ~99% — commonly reported due to the dataset's relative simplicity.
- **1D-CNN** - Accuracy: ~98% — reported in various HAR deep learning studies.
- **SVM** - Accuracy: ~97% — *Banos et al., 2014.*
- No standardized evaluation protocol; most works use leave-one-subject-out or random train/test splits.

## Tooling & Ecosystem
- Available from the [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/MHEALTH+Dataset).
- [mHealthDroid](https://github.com/mHealthDroid) — Android framework for mobile health data collection.
- Easy to load with pandas; each subject's data is in a separate text file.

## Known Challenges
- Dataset is small (10 subjects) and achievable accuracies are very high, limiting its discriminative value for modern methods.
- Activities are performed in a controlled setting; transitions between activities are not captured.
- Class 0 (null/no activity) dominates the dataset, requiring careful handling.
- ECG data is underutilized in most benchmarks; fusion approaches are still underexplored.
- No standardized evaluation protocol leads to inconsistent cross-paper comparisons.

## Cite
```bibtex
@inproceedings{banos2014mhealthdroid,
  title     = {mHealthDroid: A Novel Framework for Agile Development of Mobile Health Applications},
  author    = {Banos, Oresti and Garcia, Rafael and Holgado-Terriza, Juan A. and Damas, Miguel and Pomares, Hector and Rojas, Ignacio and Saez, Alejandro and Villalonga, Claudia},
  booktitle = {International Workshop on Ambient Assisted Living (IWAAL)},
  year      = {2014}
}
```
