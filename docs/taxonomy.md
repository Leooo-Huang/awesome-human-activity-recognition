# Multi-Dimensional Dataset Taxonomy

Beyond the primary modality-based organization, this page provides alternative ways to discover datasets by **task**, **license type**, **scale**, and **application domain**.

## By Primary Task

### Action Recognition (Classify what action is happening)
| Dataset | Modality | Scale |
| --- | --- | --- |
| [Kinetics-700](../datasets/vision/kinetics-700.md) | RGB video | 650k clips / 700 classes |
| [UCF-101](../datasets/vision/ucf101.md) | RGB video | 13.3k clips / 101 classes |
| [HMDB-51](../datasets/vision/hmdb51.md) | RGB video | 6.8k clips / 51 classes |
| [Moments in Time](../datasets/vision/moments-in-time.md) | RGB video | 1M clips / 339 classes |
| [HAA500](../datasets/emerging/haa500.md) | RGB video | 10k clips / 500 classes |
| [NTU RGB+D 60](../datasets/skeleton/ntu-rgbd-60.md) | Skeleton + RGB | 57k seq / 60 classes |
| [NTU RGB+D 120](../datasets/vision/ntu-rgbd-120.md) | Skeleton + RGB + depth | 114k seq / 120 classes |
| [Skeletics-152](../datasets/skeleton/skeletics-152.md) | Estimated skeleton | 150k clips / 152 classes |
| [Toyota Smarthome](../datasets/vision/toyota-smarthome.md) | RGB + depth | 16k clips / 31 classes |

### Temporal Action Detection (Detect when actions happen in untrimmed video)
| Dataset | Modality | Scale |
| --- | --- | --- |
| [ActivityNet](../datasets/vision/activitynet.md) | RGB video | 20k videos / 200 classes |
| [AVA](../datasets/vision/ava.md) | RGB video | 430 clips / 80 atomic actions |
| [PKU-MMD](../datasets/skeleton/pku-mmd.md) | Skeleton + RGB | 20k instances / 51 classes |
| [FineGym](../datasets/vision/finegym.md) | RGB video | 32k segments / hierarchical |
| [Diving48](../datasets/vision/diving48.md) | RGB video | 18k clips / 48 classes |

### Wearable / Sensor-Based HAR
| Dataset | Sensors | Scale |
| --- | --- | --- |
| [UCI-HAR](../datasets/wearable/uci-har.md) | Smartphone IMU | 30 subjects / 6 activities |
| [PAMAP2](../datasets/wearable/pamap2.md) | IMU + HR | 9 subjects / 18 activities |
| [WISDM](../datasets/wearable/wisdm.md) | Phone + watch | 51 subjects / 18 activities |
| [OPPORTUNITY](../datasets/wearable/opportunity.md) | 72-channel wearable + ambient | 4 subjects |
| [HAPT](../datasets/wearable/hapt.md) | Smartphone IMU | 30 subjects / 12 activities |
| [RealWorld HAR](../datasets/wearable/realworld-har.md) | Phone + watch | 60 subjects / 15 activities |
| [mHealth](../datasets/wearable/mhealth.md) | Body sensors + ECG | 10 subjects / 12 activities |
| [UniMiB-SHAR](../datasets/wearable/unimib-shar.md) | Smartphone accelerometer | 30 subjects / 17 activities |
| [Daphnet](../datasets/wearable/daphnet.md) | Wearable accelerometer | 10 subjects / gait freezing |
| [Sussex-Huawei Locomotion](../datasets/wearable/shl.md) | Phone + watch | 3 users / 2800+ hours |

### 3D Pose Estimation & Motion Capture
| Dataset | Modality | Scale |
| --- | --- | --- |
| [AMASS](../datasets/skeleton/amass.md) | SMPL parameters | 16k mins / 344 subjects |
| [Human3.6M](../datasets/skeleton/human36m.md) | Mocap + RGB | 3.6M frames |
| [BABEL](../datasets/skeleton/babel.md) | SMPL + text | 43 hrs / 3.7k sequences |
| [TotalCapture](../datasets/skeleton/totalcapture.md) | Mocap + multi-view + IMU | 5 subjects |

### Egocentric / First-Person Vision
| Dataset | Modality | Scale |
| --- | --- | --- |
| [EPIC-Kitchens-100](../datasets/multimodal/epic-kitchens-100.md) | Ego RGB + audio | 700 hrs / 90 kitchens |
| [Ego4D](../datasets/multimodal/ego4d.md) | Ego RGB + stereo + audio | 3.3k hrs |
| [Ego-Exo4D](../datasets/emerging/ego-exo4d.md) | Ego + exo RGB | 1.4k seq / 20 hrs |
| [HOI4D](../datasets/emerging/hoi4d.md) | Ego RGB-D + hand pose | 4k+ clips |

### Motion Generation & Language-Motion
| Dataset | Modality | Scale |
| --- | --- | --- |
| [HumanML3D](../datasets/emerging/humanml3d.md) | SMPL + text | 14k+ sequences |
| [InterHuman](../datasets/emerging/interhuman.md) | SMPL-X + text | 6k+ interactions |
| [BABEL](../datasets/skeleton/babel.md) | SMPL + text | 43 hrs / 250 action classes |
| [Motion-X](../datasets/emerging/motion-x.md) | Full-body mocap | 2M frames |

### Human-Object Interaction
| Dataset | Modality | Scale |
| --- | --- | --- |
| [BEHAVE](../datasets/emerging/behave.md) | RGB-D + pose | 321 seq / 20 subjects |
| [HOI4D](../datasets/emerging/hoi4d.md) | Ego RGB-D | 4k+ clips |
| [Something-Something V2](../datasets/vision/something-something-v2.md) | RGB video | 220k clips |

### Multi-Person Interaction
| Dataset | Modality | Scale |
| --- | --- | --- |
| [NTU Mutual Actions](../datasets/multimodal/ntu-mutual.md) | RGB + depth + skeleton | 26 interaction classes |
| [InterHuman](../datasets/emerging/interhuman.md) | SMPL-X + text | 6k+ interactions |

### Dense Video Captioning / Video-Language
| Dataset | Modality | Scale |
| --- | --- | --- |
| [ActivityNet Captions](../datasets/multimodal/activitynet-captions.md) | RGB + text | 20k videos / 100k captions |
| [Charades](../datasets/multimodal/charades.md) | RGB + scripts | 9.8k videos |

### Sign Language
| Dataset | Modality | Scale |
| --- | --- | --- |
| [How2Sign](../datasets/multimodal/how2sign.md) | RGB + depth + pose | 80 hrs / ASL |

### Clinical / Health
| Dataset | Application | Scale |
| --- | --- | --- |
| [Daphnet](../datasets/wearable/daphnet.md) | Parkinson's gait freezing | 10 subjects |
| [mHealth](../datasets/wearable/mhealth.md) | Mobile health monitoring | 10 subjects |
| [FineBio](../datasets/emerging/finebio.md) | Biology lab procedures | Multi-step |

---

## By License Type

### Fully Open (CC BY, Apache, MIT)
- Kinetics-700, Something-Something V2, UCI-HAR, PAMAP2, HAPT, RealWorld HAR, mHealth, TotalCapture

### Creative Commons Non-Commercial
- Charades (CC BY-NC), WISDM (CC BY-NC-SA), OPPORTUNITY (CC BY-NC)

### Research-Only (Application Required)
- NTU RGB+D 60/120, Human3.6M, PKU-MMD, EPIC-Kitchens-100, Toyota Smarthome

### Non-Commercial Research License
- Ego4D, BABEL, AMASS, Ego-Exo4D, Motion-X, HumanML3D, InterHuman

### Platform Terms / Custom License
- UCF-101, HMDB-51, ActivityNet, AVA, Moments in Time, BEHAVE

---

## By Scale

### Large-Scale (>100k samples)
- Kinetics-700 (650k), Something-Something V2 (220k), Moments in Time (1M), NTU RGB+D 120 (114k), Skeletics-152 (150k)

### Medium-Scale (10k-100k samples)
- UCF-101 (13.3k), ActivityNet (20k), NTU RGB+D 60 (57k), PKU-MMD (20k), FineGym (32k), Diving48 (18k), Toyota Smarthome (16k), HumanML3D (14k), HAA500 (10k)

### Long-Duration Video (>100 hours)
- Ego4D (3.3k hrs), EPIC-Kitchens-100 (700 hrs), ActivityNet (648 hrs), Sussex-Huawei Locomotion (2800+ hrs)

### Small but Focused (<10k samples)
- HMDB-51 (6.8k), Charades (9.8k), BEHAVE (321 seq), HOI4D (4k), InterHuman (6k), How2Sign (80 hrs)

---

## By Year of Release

### Classics (before 2015)
- UCF-101 (2012), HMDB-51 (2011), Human3.6M (2014), UCI-HAR (2012), PAMAP2 (2012), OPPORTUNITY (2013)

### Established Benchmarks (2015-2019)
- Kinetics-700 (2017→2019), NTU RGB+D 60/120 (2016/2019), Something-Something V2 (2018), ActivityNet (2015), AVA (2018), AMASS (2019), Charades (2016), EPIC-Kitchens-100 (2018→2020), WISDM (2019), HAPT (2015)

### Recent (2020-2023)
- Ego4D (2022), BABEL (2022), Moments in Time (2021), Diving48 (2020), Toyota Smarthome (2020), BEHAVE (2022), Motion-X (2023), Ego-Exo4D (2023), HumanML3D (2022), HOI4D (2022), PKU-MMD (2022), Skeletics-152 (2021)

### Frontier (2024+)
- InterHuman (2024), FineBio (2024), HAA500 (2024)
