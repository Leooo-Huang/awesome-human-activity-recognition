# Sussex-Huawei Locomotion (SHL)

- **Modality:** Smartphone IMU (accelerometer, gyroscope, magnetometer, linear acceleration, gravity, orientation), barometer, GPS
- **Primary Tasks:** Locomotion mode recognition, transportation mode detection
- **Scale:** 3 users, 8 locomotion modes, 2,812 hours of labeled data over 7 months
- **License:** Research use only (SHL terms)
- **Access:** [http://www.shl-dataset.org/](http://www.shl-dataset.org/)

## Summary
The Sussex-Huawei Locomotion (SHL) dataset is one of the largest and most comprehensive datasets for locomotion and transportation mode recognition. Three participants carried smartphones at four body positions (hand, torso, hip pocket, backpack) over a 7-month period during their daily routines in the UK. The dataset covers 8 locomotion modes: still, walk, run, bike, car, bus, train, and subway. With over 2,800 hours of data collected in completely naturalistic conditions, SHL is uniquely suited for studying real-world variability, sensor placement sensitivity, and long-term user adaptation. An annual recognition challenge is hosted at UbiComp/ISWC.

## Reference Paper
- *Hristijan Gjoreski, Mathias Ciliberto, Lin Wang, Francisco Javier Ordonez Morales, Sami Mekki, Stefan Valentin, Daniel Roggen.* "The University of Sussex-Huawei Locomotion and Transportation Dataset for Multimodal Analytics with Mobile Devices." IEEE Access, 2018. [`PDF`](https://ieeexplore.ieee.org/document/8478392)

## Benchmarks & Baselines
- **Random Forest (hand position)** - F1: ~95% — *Gjoreski et al., IEEE Access 2018.*
- **CNN-LSTM** - F1: ~92% (cross-position) — reported in SHL Challenge papers.
- **SHL Challenge 2018 winner** - F1: 93.9% — *Wang et al., UbiComp 2018 workshop.*
- The SHL Challenge provides standardized evaluation with held-out test data; cross-position and cross-user settings are evaluated separately.

## Tooling & Ecosystem
- [SHL Challenge](http://www.shl-dataset.org/activity-recognition-challenge/) provides annual competition data and evaluation scripts.
- [Official dataset page](http://www.shl-dataset.org/) hosts download links and documentation.
- Data is provided in text format; straightforward to load with Python.

## Known Challenges
- Cross-position generalization: models trained on one body position degrade significantly on others.
- Cross-user generalization: with only 3 users, individual movement patterns heavily influence results.
- Distinguishing motorized transport modes (car, bus, train, subway) is the primary difficulty.
- Very large dataset size (~270 GB) can be challenging to download and process.
- GPS and barometer data have missing segments due to real-world collection conditions.

## Cite
```bibtex
@article{gjoreski2018shl,
  title   = {The University of Sussex-Huawei Locomotion and Transportation Dataset for Multimodal Analytics with Mobile Devices},
  author  = {Gjoreski, Hristijan and Ciliberto, Mathias and Wang, Lin and Morales, Francisco Javier Ordonez and Mekki, Sami and Valentin, Stefan and Roggen, Daniel},
  journal = {IEEE Access},
  volume  = {6},
  pages   = {42592--42604},
  year    = {2018}
}
```
