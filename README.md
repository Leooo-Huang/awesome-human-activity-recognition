# Awesome Human Activity Recognition

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Datasets](https://img.shields.io/badge/datasets-53-brightgreen)](#taxonomy-snapshot)

> **人体活动识别（HAR）精选资源列表** | A curated list of Human Activity Recognition (HAR), action recognition, motion capture, and pose estimation datasets.

**[中文](i18n/README.zh.md)** | [English](README.md) | [Deutsch](i18n/README.de.md) | [Español](i18n/README.es.md) | [Français](i18n/README.fr.md) | [日本語](i18n/README.ja.md) | [한국어](i18n/README.ko.md) | [Português](i18n/README.pt.md) | [Русский](i18n/README.ru.md)

---

**53 datasets** spanning **vision-based action recognition**, **wearable sensor HAR**, **skeleton/mocap**, and **multimodal egocentric** tasks. Each card includes licensing, benchmark baselines, SOTA leaderboards, download instructions, and canonical paper citations — designed for ML researchers, product teams, and motion science labs.

**Keywords:** Human Activity Recognition · HAR · Action Recognition · Motion Capture · Pose Estimation · Skeleton-based · Wearable Sensors · IMU · Computer Vision · Time-Series · Multimodal · Benchmark Datasets · Deep Learning

- Built for ML researchers, product teams, and motion science labs.
- Highlights state-of-the-art (SOTA) datasets and the foundational classics they build upon.
- Ships with contribution workflows, validation tooling, and roadmap for community stewardship.

> *Goal: become the go-to GitHub resource for human activity datasets, mirroring the depth of Papers with Code while staying dataset-first.*

## Contents

- [Taxonomy Snapshot](#taxonomy-snapshot) — All 48 datasets organized by modality.
- [Multi-Dimensional Taxonomy](docs/taxonomy.md) — Browse by task, license, scale, or year.
- [Surveys & Benchmarks](docs/surveys.md) — Curated survey papers and SOTA snapshots.
- [Benchmark Snapshot](docs/benchmarking.md) — Performance baselines across datasets.
- [Contributing](CONTRIBUTING.md) — How to add datasets, tooling, or translations.
- [Roadmap](docs/roadmap.md) — What's next for this project.
- [Translations](i18n/) — 中文, Deutsch, Español, Français, 日本語, 한국어, Português, Русский.

## Taxonomy Snapshot

### Vision (RGB / Depth) — 14 datasets

| Dataset | Modality | Primary Tasks | Scale | Access |
| --- | --- | --- | --- | --- |
| [Kinetics-700](datasets/vision/kinetics-700.md) | RGB video | Action recognition, pretraining | 650k clips / 700 classes | Public (CC BY) |
| [UCF-101](datasets/vision/ucf101.md) | RGB video | Action recognition | 13.3k clips / 101 classes | Public (research) |
| [HMDB-51](datasets/vision/hmdb51.md) | RGB video | Action recognition | 6.8k clips / 51 classes | Public (research) |
| [ActivityNet](datasets/vision/activitynet.md) | RGB video | Temporal action detection | 20k videos / 200 classes | Public (research) |
| [AVA](datasets/vision/ava.md) | RGB video | Spatio-temporal action detection | 430 clips / 80 atomic actions | Public (research) |
| [NTU RGB+D 120](datasets/vision/ntu-rgbd-120.md) | RGB + depth + skeleton | 3D action recognition | 114k seq / 120 classes | Research license |
| [Something-Something V2](datasets/vision/something-something-v2.md) | RGB video | Fine-grained interactions | 220k clips / 174 labels | Public (Apache 2.0) |
| [FineGym](datasets/vision/finegym.md) | RGB video | Fine-grained sports actions | 32k segments / hierarchical | Public (research) |
| [Moments in Time](datasets/vision/moments-in-time.md) | RGB video | Event/action recognition | 1M clips / 339 classes | Public (research) |
| [Diving48](datasets/vision/diving48.md) | RGB video | Fine-grained diving actions | 18k clips / 48 classes | Public (research) |
| [Toyota Smarthome](datasets/vision/toyota-smarthome.md) | RGB + depth + skeleton | Daily living activities | 16k clips / 31 classes | Research license |
| [MultiSports](datasets/vision/multisports.md) | RGB video | Spatio-temporal sports action detection | 3.2k clips / 66 classes | Public (research) |
| [MultiTHUMOS](datasets/vision/multithumos.md) | RGB video | Dense multi-label temporal action detection | 65 classes / 38k annotations | Public (research) |
| [FineSports](datasets/vision/finesports.md) | RGB video | Multi-person fine-grained sports | 10k NBA videos / 52 actions | Public (research) |

### Skeleton & Mocap — 7 datasets

| Dataset | Modality | Primary Tasks | Scale | Access |
| --- | --- | --- | --- | --- |
| [NTU RGB+D 60](datasets/skeleton/ntu-rgbd-60.md) | RGB + depth + skeleton | Skeleton-based action recognition | 57k seq / 60 classes | Research license |
| [AMASS](datasets/skeleton/amass.md) | Parametric body poses | Motion synthesis, estimation | 16k mins / 344 subjects | Public (AMASS license) |
| [Human3.6M](datasets/skeleton/human36m.md) | Mocap + RGB | Pose estimation, 3D reconstruction | 3.6M 3D frames | Research license |
| [BABEL](datasets/skeleton/babel.md) | SMPL + text labels | Motion-language alignment | 43 hrs / 3.7k seq | Research (non-commercial) |
| [TotalCapture](datasets/skeleton/totalcapture.md) | Mocap + multi-view RGB + IMU | 3D pose estimation, fusion | 5 subjects / multi-view | Public (CC BY) |
| [PKU-MMD](datasets/skeleton/pku-mmd.md) | RGB + depth + skeleton | Action detection | 20k instances / 51 classes | Research license |
| [Skeletics-152](datasets/skeleton/skeletics-152.md) | Estimated skeleton | Large-scale skeleton action | 150k clips / 152 classes | Research |

### Wearable Sensors — 13 datasets

| Dataset | Modality | Primary Tasks | Scale | Access |
| --- | --- | --- | --- | --- |
| [UCI-HAR](datasets/wearable/uci-har.md) | Smartphone IMU | Activity recognition | 30 subjects / 6 activities | Public (CC BY) |
| [PAMAP2](datasets/wearable/pamap2.md) | IMU + HR | Wearable HAR | 9 subjects / 18 activities | Public (CC BY-SA) |
| [WISDM](datasets/wearable/wisdm.md) | Smartphone + smartwatch | HAR, gesture recognition | 51 subjects / 1M+ samples | Public (Creative Commons) |
| [OPPORTUNITY](datasets/wearable/opportunity.md) | Wearable + ambient sensors | Context recognition | 4 subjects / 72 sensors | Public (research) |
| [HAPT](datasets/wearable/hapt.md) | Smartphone IMU | Activity + transitions | 30 subjects / 12 activities | Public (CC BY) |
| [RealWorld HAR](datasets/wearable/realworld-har.md) | Phone + watch IMU | In-the-wild HAR | 60 subjects / 15 activities | Public (CC BY) |
| [mHealth](datasets/wearable/mhealth.md) | Body-worn sensors + ECG | Mobile health monitoring | 10 subjects / 12 activities | Public (CC BY) |
| [UniMiB-SHAR](datasets/wearable/unimib-shar.md) | Smartphone accelerometer | ADL + fall detection | 30 subjects / 17 activities | Public |
| [Daphnet](datasets/wearable/daphnet.md) | Wearable accelerometer | Freezing of gait (Parkinson's) | 10 subjects / 3 sensors | Public |
| [Sussex-Huawei Locomotion](datasets/wearable/shl.md) | Phone + watch sensors | Locomotion mode recognition | 3 users / 2800+ hours | Public |
| [HARTH](datasets/wearable/harth.md) | Accelerometer | Free-living HAR | 22 subjects / real-world | Public |
| [CAPTURE-24](datasets/wearable/capture24.md) | Wrist accelerometer + camera | Free-living HAR (largest) | 151 subjects / 3883 hours | Public (CC BY) |
| [WEAR](datasets/wearable/wear.md) | Smartwatch IMU + ego video | Outdoor sports HAR | 22 subjects / 18 activities | Public (CC BY) |

### Multimodal / Egocentric — 7 datasets

| Dataset | Modality | Primary Tasks | Scale | Access |
| --- | --- | --- | --- | --- |
| [EPIC-Kitchens-100](datasets/multimodal/epic-kitchens-100.md) | Ego RGB + audio | Long-term egocentric actions | 700 hrs / 90 kitchens | Research license |
| [Ego4D](datasets/multimodal/ego4d.md) | Ego RGB + stereo + audio | 4D actions, SQA, AV tasks | 3.3k hrs / 74 scenes | Non-commercial |
| [Charades](datasets/multimodal/charades.md) | Indoor RGB + scripts | Multi-label actions | 9.8k videos / 157 labels | Public (CC BY-NC) |
| [NTU Mutual Actions](datasets/multimodal/ntu-mutual.md) | RGB + depth + skeleton | Two-person interactions | 26 interaction classes | Research license |
| [ActivityNet Captions](datasets/multimodal/activitynet-captions.md) | RGB video + text | Dense video captioning | 20k videos / 100k captions | Public (research) |
| [How2Sign](datasets/multimodal/how2sign.md) | RGB + depth + pose | Sign language understanding | 80 hrs / ASL | Public (research) |
| [EgoExo-Fitness](datasets/multimodal/egoexo-fitness.md) | Ego+exo video + pose | Fitness action quality | 31 hrs / 6k+ actions | Public (research) |

### Emerging & Frontier — 12 datasets

| Dataset | Modality | Primary Tasks | Scale | Access |
| --- | --- | --- | --- | --- |
| [BEHAVE](datasets/emerging/behave.md) | RGB-D + pose | Human-object interaction | 321 seq / 20 subjects | Public (BEHAVE license) |
| [Motion-X](datasets/emerging/motion-x.md) | Multisensor mocap | Full-body & hand joints | 10 subjects / 2M frames | Public (research) |
| [Ego-Exo4D](datasets/emerging/ego-exo4d.md) | Ego+exo RGB + mocap | Cross-view actions | 1.4k seq / 20 hrs ego | Public (research) |
| [HumanML3D](datasets/emerging/humanml3d.md) | SMPL + text | Text-to-motion generation | 14k+ motion sequences | Public (research) |
| [InterHuman](datasets/emerging/interhuman.md) | SMPL-X + text | Two-person interaction motion | 6k+ interaction sequences | Public (research) |
| [HOI4D](datasets/emerging/hoi4d.md) | Ego RGB-D + hand pose | Hand-object interaction | 4k+ video clips | Public (research) |
| [FineBio](datasets/emerging/finebio.md) | RGB + skeleton | Fine-grained biology lab actions | Multi-step lab procedures | Public (research) |
| [HAA500](datasets/emerging/haa500.md) | RGB video | Atomic action recognition | 10k clips / 500 classes | Public |
| [Motion-X++](datasets/emerging/motionx-plus.md) | Full-body mocap + text | Whole-body motion generation | 120k+ sequences | Public (research) |
| [FLAG3D](datasets/emerging/flag3d.md) | Multi-view RGB + skeleton + text | 3D fitness activity understanding | 180k seq / 60 categories | Public (research) |
| [InterX](datasets/emerging/interx.md) | SMPL-X + text | Human-human interaction | 11k+ sequences / 40+ categories | Public (research) |
| [WiMANS](datasets/emerging/wimans.md) | WiFi CSI | WiFi-based multi-user activity sensing | Multi-user benchmark | Public (research) |

Explore every dataset card for download instructions, citation info, baseline scores, and known challenges.

## Why This Repo
- **Problem-first navigation:** start from the task or modality you care about, not just alphabetical lists.
- **Research context included:** every dataset card links the canonical paper, key benchmarks, and follow-up SOTA work.
- **Actionable tooling:** catalog builder (JSON/CSV export), link validation, ASCII normalization.
- **Quality gate:** contribution templates, review checklist, and automated CI validation keep the catalog trustworthy.

## Repository Structure
```
.
 datasets/               # 53 dataset cards grouped by modality
   vision/               #   14 vision datasets
   skeleton/             #    7 skeleton/mocap datasets
   wearable/             #   13 wearable sensor datasets
   multimodal/           #    7 multimodal/egocentric datasets
   emerging/             #   12 emerging & frontier datasets
 docs/                   # Surveys, benchmarks, roadmap
 tools/                  # Scripts (catalog builder, link validator, ASCII normalizer)
 .github/workflows/      # CI (link checking, Markdown linting)
 i18n/                   # Translations (zh, de, es, fr, ja, ko, pt, ru)
```

## Featured Papers & Surveys
- Aggarwal & Ryoo. **Human Activity Analysis: A Review.** ACM Computing Surveys, 2011.
- Lara & Labrador. **A Survey on Human Activity Recognition using Wearable Sensors.** IEEE Communications Surveys, 2013.
- Li et al. **A Systematic Survey on Deep Learning for Human Activity Recognition.** ACM Computing Surveys, 2022.
- Grauman et al. **Ego4D: Around the World in 2,250 Hours of Egocentric Video.** CVPR, 2022. *(Dataset + benchmarks)*
- Pavlakos et al. **BABEL: Bodies, Actions and Behavior with English Labels.** CVPR, 2022.

Extended reading list lives in [`docs/surveys.md`](docs/surveys.md).

## How to Use This Catalog
1. **Find a dataset:** Start with the taxonomy tables above or browse [`datasets/`](datasets/).
2. **Read the dataset card:** Understand licensing, tasks, baseline protocols, and data quirks before downloading.
3. **Prototype faster:** Use the tooling tips and ecosystem links in each card for PyTorch/TF dataloaders.
4. **Generate catalog exports:** Run `python tools/catalog_builder.py --format csv --output catalog.csv` for machine-readable metadata.
5. **Stay current:** Watch the repo or subscribe to Discussions; each release summarizes new datasets and SOTA shifts.

### Citation
If this repository helps your research or product, please cite it:

```bibtex
@misc{awesome_har_2025,
  title   = {Awesome Human Activity Recognition: A Curated List},
  author  = {Wenxuan Huang},
  year    = {2025},
  url     = {https://github.com/Leo-Cyberautonomy/awesome-human-activity-recognition},
  note    = {GitHub repository}
}
```

## Contributing
- Check [`CONTRIBUTING.md`](CONTRIBUTING.md) for dataset card templates, review requirements, and style guide.
- Use issues to request new datasets or report stale links. We track modalities with labels (e.g., `modality:wearable`).
- Pull requests undergo dataset quality review + automated link validation. Expect review within 5-7 days.

## Roadmap Highlights
- Weekly automated link validation via GitHub Actions.
- Jupyter starter notebooks for wearable and video baselines.
- Standardized dataset schema (YAML) with automated validation.
- Community spotlight: quarterly digest of new datasets and leaderboards.
- Long-term: convert catalog into searchable static site via MkDocs.

See the full [`docs/roadmap.md`](docs/roadmap.md) for versioned milestones.

## Acknowledgements
Thanks to dataset authors, annotation teams, and benchmark maintainers who make open research in human activity understanding possible. This project aims to amplify their work by making discovery effortless.
