# WiMANS

- **Modality:** WiFi Channel State Information (CSI)
- **Primary Tasks:** Multi-user activity recognition, WiFi-based sensing, privacy-preserving HAR
- **Scale:** Multi-user scenarios, multiple activity categories, varied spatial configurations
- **License:** Research use
- **Access:** Available through the official repository (see reference paper)

## Summary
WiMANS is the first benchmark dataset for WiFi-based multi-user activity sensing presented at a top computer vision venue. By leveraging WiFi CSI signals instead of cameras, it enables human activity recognition without visual sensors, addressing privacy concerns in smart-home and workplace environments. The dataset captures simultaneous activities of multiple users, tackling a significantly harder problem than single-user WiFi sensing. This novel modality opens up research at the intersection of wireless communication and activity understanding.

## Reference Paper
- *Authors et al.* "WiMANS: A Benchmark Dataset for WiFi-based Multi-user Activity Sensing." ECCV, 2024. [`PDF`](https://arxiv.org/abs/2402.09430)

## Benchmarks & Baselines
- **CNN/LSTM baselines on CSI** - Classification accuracy reported for single-user and multi-user settings; *WiMANS paper, ECCV 2024.*
- **Cross-environment evaluation** - Performance under different room layouts and device placements provided.
- Official splits test generalization across spatial configurations and user combinations.

## Tooling & Ecosystem
- Official repository provides data loaders and baseline model implementations for CSI-based recognition.
- CSI extraction tools compatible with commodity WiFi hardware (Intel 5300 NIC / Atheros-based).
- Can be combined with vision-based datasets for multimodal sensor fusion research.

## Known Challenges
- WiFi CSI is sensitive to environmental changes (furniture movement, door state, new objects); models may not generalize across rooms without adaptation.
- Multi-user signal separation is inherently ambiguous when users are spatially close.
- Hardware-specific CSI formats vary across chipsets; preprocessing pipelines must account for antenna configuration and subcarrier count.
- Relatively new modality for the CV community; fewer pretrained models and established best practices compared to video-based HAR.

## Cite
```
@inproceedings{wimans2024,
  title     = {WiMANS: A Benchmark Dataset for WiFi-based Multi-user Activity Sensing},
  author    = {Huang, Shuokang and Li, Kaihan and You, Di and Chen, Yichong and Lin, Arvin and Liu, Siying and Li, Xiaohui and Cheung, Gene},
  booktitle = {Proceedings of the European Conference on Computer Vision},
  year      = {2024}
}
```
