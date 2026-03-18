# UCI-HAR

- **Modality:** Smartphone IMU (accelerometer + gyroscope)
- **Primary Tasks:** Human activity recognition from inertial sensors
- **Scale:** 30 subjects, 6 activity classes, 10,299 samples (2.56-second windows at 50 Hz)
- **License:** Public domain (UCI Machine Learning Repository)
- **Access:** [https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones](https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones)

## Summary
UCI-HAR is one of the most widely used benchmarks for smartphone-based human activity recognition. The dataset was collected from 30 volunteers (aged 19-48) wearing a Samsung Galaxy S II on the waist. Each subject performed six activities: walking, walking upstairs, walking downstairs, sitting, standing, and lying down. Tri-axial accelerometer and gyroscope signals were captured at 50 Hz, preprocessed with noise filters, and segmented into 2.56-second fixed-width sliding windows with 50% overlap. The dataset provides both raw sensor data and a 561-feature vector of time and frequency domain variables, making it accessible for both deep learning and classical ML approaches.

## Reference Paper
- *Davide Anguita, Alessandro Ghio, Luca Oneto, Xavier Parra, Jorge L. Reyes-Ortiz.* "A Public Domain Dataset for Human Activity Recognition Using Smartphones." ESANN, 2013. [`PDF`](https://www.esann.org/sites/default/files/proceedings/legacy/es2013-84.pdf)

## Benchmarks & Baselines
- **SVM (561 features)** - Accuracy: 96.0% — *Anguita et al., ESANN 2013.*
- **DeepConvLSTM** - Accuracy: ~95.8% — *Ordonez & Roggen, Sensors 2016.*
- **1D-CNN** - Accuracy: ~96.4% — commonly reported in deep learning HAR literature.
- Standard evaluation uses the predefined 70/30 train/test split (21 train subjects, 9 test subjects).

## Tooling & Ecosystem
- Available directly from the [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones).
- Widely available in tutorial form for scikit-learn, TensorFlow, and PyTorch.
- Pre-extracted 561 features enable immediate use without signal processing.
- [TensorFlow Datasets](https://www.tensorflow.org/datasets) community contributions include UCI-HAR.

## Known Challenges
- Only 6 activity classes; the task is considered largely solved for this label set.
- Single sensor placement (waist) limits generalizability to other body positions.
- Lab-controlled conditions do not reflect real-world deployment variability.
- Static activities (sitting vs. standing) are the primary source of confusion.
- The 561 handcrafted features may not generalize; raw signal approaches are preferred for modern work.

## Cite
```bibtex
@inproceedings{anguita2013public,
  title     = {A Public Domain Dataset for Human Activity Recognition Using Smartphones},
  author    = {Anguita, Davide and Ghio, Alessandro and Oneto, Luca and Parra, Xavier and Reyes-Ortiz, Jorge L.},
  booktitle = {European Symposium on Artificial Neural Networks (ESANN)},
  year      = {2013}
}
```
