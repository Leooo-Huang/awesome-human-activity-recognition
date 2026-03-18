# Daphnet Freezing of Gait

- **Modality:** Wearable accelerometers (3 placements: ankle, thigh, trunk)
- **Primary Tasks:** Freezing of gait (FoG) detection in Parkinson's disease
- **Scale:** 10 Parkinson's patients, 8+ hours of walking data, binary labels (freeze / no-freeze)
- **License:** Public domain (UCI Machine Learning Repository)
- **Access:** [https://archive.ics.uci.edu/ml/datasets/Daphnet+Freezing+of+Gait](https://archive.ics.uci.edu/ml/datasets/Daphnet+Freezing+of+Gait)

## Summary
The Daphnet Freezing of Gait dataset was collected as part of the EU Daphnet project to develop wearable systems for detecting freezing of gait (FoG) episodes in Parkinson's disease patients. Ten patients with FoG history performed walking tasks in a lab while wearing tri-axial accelerometers on the ankle, thigh, and trunk. Annotators labeled FoG episodes from synchronized video recordings. This dataset is a key benchmark in health-oriented HAR, particularly for real-time detection systems that could trigger cueing devices to help patients resume walking.

## Reference Paper
- *Marc Bachlin, Meir Plotnik, Daniel Roggen, Inbal Maidan, Jeffrey M. Hausdorff, Nir Giladi, Gerhard Troster.* "Wearable Assistant for Parkinson's Disease Patients With the Freezing of Gait Symptom." IEEE Transactions on Information Technology in Biomedicine, 2010. [`PDF`](https://ieeexplore.ieee.org/document/5325884)

## Benchmarks & Baselines
- **Freeze Index (threshold)** - Sensitivity: 73.1%, Specificity: 81.6% — *Bachlin et al., 2010.*
- **Random Forest** - F1: ~88% — reported in follow-up works.
- **LSTM** - F1: ~90% — reported in deep learning HAR literature.
- Evaluation typically uses leave-one-subject-out cross-validation; some works use per-patient evaluation.

## Tooling & Ecosystem
- Available from the [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/Daphnet+Freezing+of+Gait).
- Simple CSV format; easily loaded with pandas or NumPy.
- Frequently used in tutorials on clinical HAR and time-series classification.

## Known Challenges
- Severe class imbalance: FoG episodes are rare events within long walking sequences.
- Only 10 patients; inter-patient variability in FoG patterns is high, making generalization difficult.
- Not all patients experienced FoG during recording; 3 patients have no freeze events.
- Lab environment may not reflect real-world walking conditions (obstacles, uneven terrain).
- Binary detection task; severity or type of FoG is not annotated.

## Cite
```bibtex
@article{bachlin2010wearable,
  title   = {Wearable Assistant for Parkinson's Disease Patients With the Freezing of Gait Symptom},
  author  = {Bachlin, Marc and Plotnik, Meir and Roggen, Daniel and Maidan, Inbal and Hausdorff, Jeffrey M. and Giladi, Nir and Troster, Gerhard},
  journal = {IEEE Transactions on Information Technology in Biomedicine},
  volume  = {14},
  number  = {2},
  pages   = {436--446},
  year    = {2010}
}
```
