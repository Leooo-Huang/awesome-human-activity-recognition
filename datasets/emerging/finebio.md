# FineBio

- **Modality:** Egocentric RGB video, eye gaze, hand pose, object annotations
- **Primary Tasks:** Fine-grained action recognition in biology lab settings, procedural activity understanding
- **Scale:** 32 subjects, ~7 hours of video, 12 biology experiments, multi-level annotations (coarse + fine-grained)
- **License:** Research use only
- **Access:** [https://github.com/aistairc/FineBio](https://github.com/aistairc/FineBio)

## Summary
FineBio is a fine-grained egocentric activity dataset captured in biology laboratory environments. It documents subjects performing real wet-lab biology experiments (e.g., pipetting, centrifugation, microscopy) while wearing head-mounted cameras and eye trackers. The dataset provides hierarchical activity annotations at multiple granularity levels — from high-level experimental protocols down to atomic hand manipulations. FineBio is motivated by the need to understand complex procedural activities in scientific domains, with applications in lab automation, training assessment, and protocol compliance monitoring. The combination of fine-grained manipulation labels, eye gaze data, and real experimental procedures makes it unique among egocentric datasets.

## Reference Paper
- *Takeru Ohta, Yoichi Sato.* "FineBio: A Fine-Grained Video Dataset of Biological Experiments with Hierarchical Annotations." NeurIPS Datasets and Benchmarks, 2023. [`PDF`](https://arxiv.org/abs/2312.12670)

## Benchmarks & Baselines
- **Action Segmentation (F1@50):** MS-TCN — ~35% — reported in the paper.
- **Action Recognition (Top-1):** SlowFast — ~45% — baseline results.
- **Step Recognition:** temporal models show significant room for improvement.
- Evaluation uses standard temporal action segmentation metrics (F1@{10,25,50}, Edit distance).

## Tooling & Ecosystem
- [FineBio GitHub repo](https://github.com/aistairc/FineBio) provides annotations, data loaders, and baseline code.
- Compatible with temporal action segmentation frameworks (ASFormer, MS-TCN).
- Eye gaze data can be integrated for attention-guided action recognition.

## Known Challenges
- Fine-grained manipulation actions (e.g., different pipetting techniques) are extremely difficult to distinguish visually.
- Small objects and tools in biology labs are often occluded by hands in egocentric view.
- Hierarchical annotation structure requires models to operate at multiple temporal scales.
- Limited to biology lab domain; generalization to other procedural domains is untested.
- Relatively small scale (32 subjects, ~7 hours) compared to general egocentric datasets like Ego4D.

## Cite
```bibtex
@inproceedings{ohta2023finebio,
  title     = {FineBio: A Fine-Grained Video Dataset of Biological Experiments with Hierarchical Annotations},
  author    = {Ohta, Takeru and Sato, Yoichi},
  booktitle = {NeurIPS Datasets and Benchmarks Track},
  year      = {2023}
}
```
