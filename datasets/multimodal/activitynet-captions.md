# ActivityNet Captions

- **Modality:** RGB video (untrimmed YouTube videos) + natural language descriptions
- **Primary Tasks:** Dense video captioning, temporal grounding, video paragraph retrieval
- **Scale:** ~20,000 videos, ~100,000 temporally localized captions, 849 hours
- **License:** Research use only (ActivityNet terms)
- **Access:** [https://cs.stanford.edu/people/ranber/densevid/](https://cs.stanford.edu/people/ranber/densevid/)

## Summary
ActivityNet Captions extends the ActivityNet v1.3 dataset with dense temporal descriptions. Each video is annotated with a series of temporally localized natural language sentences that collectively describe the entire video content. Unlike single-sentence video captioning, ActivityNet Captions requires models to detect multiple events, localize their temporal boundaries, and generate descriptive captions for each event. This makes it a cornerstone benchmark for dense video captioning and temporal sentence grounding tasks, bridging video understanding and natural language processing.

## Reference Paper
- *Ranjay Krishna, Kenji Hata, Frederic Ren, Li Fei-Fei, Juan Carlos Niebles.* "Dense-Captioning Events in Videos." ICCV, 2017. [`PDF`](https://arxiv.org/abs/1705.00754)

## Benchmarks & Baselines
- **Dense Captioning (METEOR, val):** PDVC — 7.48 — *Wang et al., ICCV 2021.*
- **Dense Captioning (CIDEr, val):** Vid2Seq — 30.1 — *Yang et al., CVPR 2023.*
- **Temporal Grounding (R@1, IoU=0.5):** 2D-TAN — 44.5% — *Zhang et al., AAAI 2020.*
- Evaluation uses the official val splits; metrics include METEOR, CIDEr, and BLEU for captioning, and Recall@IoU for grounding.

## Tooling & Ecosystem
- [Official project page](https://cs.stanford.edu/people/ranber/densevid/) provides annotations and evaluation tools.
- [ActivityNet Captions evaluation server](http://activity-net.org/challenges/) for challenge submissions.
- [densevid_eval](https://github.com/ranjaykrishna/densevid_eval) — official evaluation scripts.
- Video features (C3D, TSN) are commonly pre-extracted and shared by the community.

## Known Challenges
- Dense captioning requires jointly solving temporal localization and language generation, making it significantly harder than either task alone.
- Caption quality varies; some annotations are generic or lack specificity.
- Evaluation metrics (METEOR, CIDEr) may not fully capture caption quality and temporal precision.
- YouTube video availability degrades over time.
- Long videos with many events create computational challenges for end-to-end models.

## Cite
```bibtex
@inproceedings{krishna2017dense,
  title     = {Dense-Captioning Events in Videos},
  author    = {Krishna, Ranjay and Hata, Kenji and Ren, Frederic and Fei-Fei, Li and Niebles, Juan Carlos},
  booktitle = {IEEE International Conference on Computer Vision (ICCV)},
  year      = {2017}
}
```
