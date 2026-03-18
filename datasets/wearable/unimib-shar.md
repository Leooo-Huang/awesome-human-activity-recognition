# UniMiB-SHAR

- **Modality:** Smartphone accelerometer
- **Primary Tasks:** Activity recognition, fall detection
- **Scale:** 30 subjects, 17 activity classes (9 ADL + 8 falls), 11,771 samples
- **License:** Research use only (University of Milano-Bicocca terms)
- **Access:** [http://www.sal.disco.unimib.it/technologies/unimib-shar/](http://www.sal.disco.unimib.it/technologies/unimib-shar/)

## Summary
UniMiB-SHAR (University of Milano-Bicocca Smartphone-based Human Activity Recognition) is a smartphone accelerometer dataset designed to benchmark both activities of daily living (ADL) and fall detection. The dataset includes 9 ADL types (e.g., standing, walking, going up/down stairs) and 8 fall types (e.g., forward fall, backward fall, syncope), collected from 30 subjects with a Samsung Galaxy Nexus I9250 placed in the trouser pocket. The inclusion of diverse fall types alongside normal activities makes it particularly relevant for elderly care and safety monitoring applications.

## Reference Paper
- *Daniela Micucci, Marco Mobilio, Paolo Napoletano.* "UniMiB SHAR: A Dataset for Human Activity Recognition Using Acceleration Data from Smartphones." Applied Sciences, 2017. [`PDF`](https://www.mdpi.com/2076-3417/7/10/1101)

## Benchmarks & Baselines
- **SVM** - Accuracy: ~73% (17 classes) — *Micucci et al., 2017.*
- **k-NN** - Accuracy: ~71% (17 classes) — *Micucci et al., 2017.*
- **1D-CNN** - Accuracy: ~78% (17 classes) — reported in follow-up deep learning studies.
- **Fall detection (binary)** - F1: >95% — commonly achieved by most methods.
- Standard evaluation uses leave-one-subject-out cross-validation.

## Tooling & Ecosystem
- [Official website](http://www.sal.disco.unimib.it/technologies/unimib-shar/) provides MATLAB and CSV data files.
- Data is provided as pre-segmented acceleration windows (151 samples per window).
- Compatible with standard Python ML/DL pipelines (NumPy, scikit-learn, PyTorch).

## Known Challenges
- Accelerometer-only data (no gyroscope) limits the discriminability of certain activities.
- Fall data is simulated (controlled falls), not real-world falls, which may differ in dynamics.
- Significant class imbalance between ADL and fall classes.
- Single sensor placement (trouser pocket) with fixed orientation.
- Distinguishing between 8 fall subtypes is substantially harder than binary fall detection.

## Cite
```bibtex
@article{micucci2017unimib,
  title   = {UniMiB SHAR: A Dataset for Human Activity Recognition Using Acceleration Data from Smartphones},
  author  = {Micucci, Daniela and Mobilio, Marco and Napoletano, Paolo},
  journal = {Applied Sciences},
  volume  = {7},
  number  = {10},
  pages   = {1101},
  year    = {2017}
}
```
