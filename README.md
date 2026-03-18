# Awesome Human Activity Recognition [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of 53 Human Activity Recognition (HAR), action recognition, motion capture, and pose estimation datasets — with licensing, benchmarks, SOTA leaderboards, and download instructions.

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

**[中文](i18n/README.zh.md)** | [Deutsch](i18n/README.de.md) | [Español](i18n/README.es.md) | [Français](i18n/README.fr.md) | [日本語](i18n/README.ja.md) | [한국어](i18n/README.ko.md) | [Português](i18n/README.pt.md) | [Русский](i18n/README.ru.md)

## Contents

- [Vision (RGB / Depth)](#vision-rgb--depth)
- [Skeleton and Mocap](#skeleton-and-mocap)
- [Wearable Sensors](#wearable-sensors)
- [Multimodal and Egocentric](#multimodal-and-egocentric)
- [Emerging and Frontier](#emerging-and-frontier)

## Vision (RGB / Depth)

- [Kinetics-700](https://deepmind.com/research/open-source/kinetics) - Large-scale pretraining benchmark with 650k YouTube clips across 700 action classes.
- [UCF-101](https://www.crcv.ucf.edu/data/UCF101.php) - Classic action recognition benchmark with 13.3k clips across 101 classes.
- [HMDB-51](https://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database/) - Diverse action recognition dataset with 6.8k clips from movies and web videos across 51 classes.
- [ActivityNet](http://activity-net.org/) - Temporal action detection benchmark with 20k untrimmed YouTube videos across 200 classes.
- [AVA](https://research.google.com/ava/) - Spatio-temporal action detection with 430 movie clips and 80 atomic action labels with bounding boxes.
- [NTU RGB+D 120](http://rose1.ntu.edu.sg/datasets/actionrecognition.asp) - Multi-view 3D action recognition with 114k sequences across 120 classes using RGB, depth, and skeleton.
- [Something-Something V2](https://developer.qualcomm.com/software/ai-datasets/something-something) - Fine-grained object interaction dataset with 220k clips across 174 labels requiring temporal reasoning.
- [FineGym](https://sdolivia.github.io/FineGym/) - Fine-grained gymnastics action recognition with 32k hierarchically labeled segments.
- [Moments in Time](http://moments.csail.mit.edu/) - Extremely diverse event and action recognition dataset with 1M labeled 3-second video clips across 339 classes.
- [Diving48](http://www.svcl.ucsd.edu/projects/resound/dataset.html) - Fine-grained diving action recognition with 18k clips across 48 classes requiring temporal reasoning.
- [Toyota Smarthome](https://project.inria.fr/toyotasmarthome/) - Daily living activity recognition with 16k multi-view clips across 31 classes using RGB, depth, and skeleton.
- [MultiSports](https://deeperaction.github.io/multisports/) - Spatio-temporal action detection across 4 sports with 3.2k clips and 66 fine-grained action classes.
- [MultiTHUMOS](https://ai.stanford.edu/~syyeung/everymoment.html) - Dense multi-label temporal action detection with 65 classes and 38k annotations.
- [FineSports](https://github.com/PKU-ICST-MIPL/FineSports_CVPR2024) - Multi-person fine-grained sports understanding with 10k NBA videos and 52 action types from CVPR 2024.

## Skeleton and Mocap

- [NTU RGB+D 60](https://rose1.ntu.edu.sg/dataset/actionRecognition/) - Foundation dataset for skeleton-based action recognition with 57k sequences across 60 classes.
- [AMASS](https://amass.is.tue.mpg.de/) - Unified SMPL motion capture parameters from 40+ datasets covering 16k minutes and 344 subjects.
- [Human3.6M](http://vision.imar.ro/human3.6m/description.php) - De facto standard for 3D pose estimation with 3.6M frames from 11 professional actors.
- [Babel](https://babel.is.tue.mpg.de/) - Motion-language alignment dataset with 43 hours and 3.7k sequences annotated with SMPL and text labels.
- [TotalCapture](http://totalcapture.net/) - Multi-modal 3D pose estimation benchmark combining mocap, multi-view RGB, and IMU from 5 subjects.
- [PKU-MMD](https://www.icst.pku.edu.cn/struct/Projects/PKUMMD.html) - Multi-modality action detection benchmark with 20k instances across 51 classes.
- [Skeletics-152](https://github.com/skelemoa/quater-gcn) - Large-scale skeleton action recognition from estimated poses with 150k clips across 152 classes.

## Wearable Sensors

- [UCI-HAR](https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones) - Classic smartphone IMU benchmark with 30 subjects and 6 activities, near-saturated.
- [PAMAP2](https://archive.ics.uci.edu/ml/datasets/pamap2+physical+activity+monitoring) - Wearable HAR standard with multi-IMU and heart rate from 9 subjects across 18 activities.
- [WISDM](https://www.cis.fordham.edu/wisdm/dataset.php) - Phone and smartwatch sensor data mining with 51 subjects and over 1 million samples.
- [OPPORTUNITY](https://archive.ics.uci.edu/ml/datasets/OPPORTUNITY+Activity+Recognition) - Rich context-aware activity recognition with 72 wearable and ambient sensors from 4 subjects.
- [HAPT](https://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones) - Smartphone IMU dataset with postural transition detection from 30 subjects across 12 activities.
- [RealWorld HAR](https://sensor.informatik.uni-mannheim.de/#dataset_realworld) - In-the-wild activity recognition with multiple device placements from 60 subjects across 15 activities.
- [mHealth](https://archive.ics.uci.edu/ml/datasets/MHEALTH+Dataset) - Body-worn sensors with ECG for mobile health monitoring from 10 subjects across 12 activities.
- [UniMiB-SHAR](http://www.sal.disco.unimib.it/technologies/unimib-shar/) - Smartphone accelerometer dataset for daily activities and fall detection from 30 subjects across 17 activities.
- [Daphnet](https://archive.ics.uci.edu/ml/datasets/Daphnet+Freezing+of+Gait) - Freezing of gait detection for Parkinson's patients using 3 wearable accelerometers from 10 subjects.
- [Sussex-Huawei Locomotion](http://www.shl-dataset.org/) - Large-scale locomotion mode recognition with 2800+ hours from 3 users with phone and watch sensors.
- [HARTH](https://archive.ics.uci.edu/dataset/779/harth) - Professional video-annotated free-living accelerometer HAR from 22 subjects in real-world conditions.
- [CAPTURE-24](https://github.com/OxWearables/capture24) - Largest free-living wrist accelerometer dataset with 151 subjects and 3883 hours from Nature Scientific Data 2024.
- [WEAR](https://github.com/mariusbock/wear) - Outdoor sports dataset with smartwatch IMU and egocentric video from 22 subjects across 18 activities, published at IMWUT 2024.

## Multimodal and Egocentric

- [EPIC-Kitchens-100](https://epic-kitchens.github.io/2021) - Long-term egocentric kitchen actions with audio spanning 700 hours across 90 kitchens.
- [Ego4D](https://ego4d-data.org/docs/data/) - Largest egocentric dataset with multi-task benchmarks spanning 3.3k hours across 74 scenes.
- [Charades](https://allenai.org/plato/charades/) - Indoor multi-label action recognition with scripted descriptions spanning 9.8k videos across 157 labels.
- [NTU Mutual Actions](https://arxiv.org/abs/1905.04757) - Two-person interactions from NTU RGB+D with skeleton data across 26 interaction classes.
- [ActivityNet Captions](https://cs.stanford.edu/people/ranber/densevid/) - Dense video captioning and temporal grounding with 20k videos and 100k captions.
- [How2Sign](https://how2sign.github.io/) - Multimodal American Sign Language dataset with RGB, depth, and pose spanning 80 hours.
- [EgoExo-Fitness](https://github.com/iSEE-Laboratory/EgoExo-Fitness) - Ego and exo fitness action quality assessment with 31 hours and 6k+ actions from ECCV 2024.

## Emerging and Frontier

- [BEHAVE](https://virtualhumans.mpi-inf.mpg.de/behave/) - RGB-D human-object interaction with 3D pose spanning 321 sequences from 20 subjects.
- [Motion-X](https://caizhongang.github.io/projects/Motion-X/) - Full-body and hand joint motion from multisensor mocap with 2M frames from 10 subjects.
- [Ego-Exo4D](https://ego-exo4d-data.org/) - Cross-view action understanding with synchronized ego and exo video spanning 1.4k sequences.
- [HumanML3D](https://github.com/EricGuo5513/HumanML3D) - Text-to-motion generation dataset with SMPL annotations spanning 14k+ motion sequences.
- [InterHuman](https://github.com/tr3e/InterHuman) - Two-person interaction motion with SMPL-X and text descriptions spanning 6k+ sequences.
- [HOI4D](https://hoi4d.github.io/) - Egocentric hand-object interaction with RGB-D and hand pose spanning 4k+ video clips.
- [FineBio](https://github.com/aistairc/FineBio) - Fine-grained biology lab action understanding with multi-step procedure annotations.
- [HAA500](https://www.cse.ust.hk/haa/) - Diverse fine-grained atomic action recognition with 10k clips across 500 classes.
- [Motion-X++](https://motion-x-dataset.github.io/) - Whole-body motion generation with text and audio spanning 120k+ sequences.
- [FLAG3D](https://andytang15.github.io/FLAG3D/) - 3D fitness activity understanding with multi-view RGB, skeleton, and text spanning 180k sequences from CVPR 2024.
- [InterX](https://liangxuy.github.io/inter-x/) - Comprehensive human-human interaction dataset with SMPL-X spanning 11k+ sequences from CVPR 2024.
- [WiMANS](https://arxiv.org/abs/2402.09430) - First WiFi-based multi-user activity sensing benchmark at a top venue from ECCV 2024.

## Footnotes

See also: [Multi-dimensional taxonomy](docs/taxonomy.md) | [Surveys](docs/surveys.md) | [Benchmarks](docs/benchmarking.md) | [Catalog builder](tools/) | [Roadmap](docs/roadmap.md) | [Contributing](CONTRIBUTING.md)

### Citation

```bibtex
@misc{awesome_har_2025,
  title   = {Awesome Human Activity Recognition: A Curated List},
  author  = {Wenxuan Huang},
  year    = {2025},
  url     = {https://github.com/Leo-Cyberautonomy/awesome-human-activity-recognition},
  note    = {GitHub repository}
}
```

### Acknowledgements

Thanks to dataset authors, annotation teams, and benchmark maintainers who make open research in human activity understanding possible.
