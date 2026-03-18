# ActivityNet

- **Modality:** RGB video (untrimmed YouTube videos)
- **Primary Tasks:** Activity recognition, temporal action detection, temporal action proposal generation
- **Scale:** ~20,000 untrimmed videos, 200 activity classes, ~648 hours
- **License:** Research use only (ActivityNet terms)
- **Access:** [http://activity-net.org/](http://activity-net.org/)

## Summary
ActivityNet is a large-scale benchmark for understanding human activities in untrimmed videos. Unlike trimmed datasets (UCF-101, Kinetics), ActivityNet videos contain long temporal context with multiple activity instances per video. The dataset was collected from YouTube and annotated with temporal boundaries and activity labels. ActivityNet has driven the development of temporal action detection and proposal generation methods, and hosts an annual challenge at CVPR that tracks state-of-the-art progress.

## Reference Paper
- *Fabian Caba Heilbron, Victor Escorcia, Bernard Ghanem, Juan Carlos Niebles.* "ActivityNet: A Large-Scale Video Benchmark for Human Activity Understanding." CVPR, 2015. [`PDF`](https://arxiv.org/abs/1506.01094)

## Benchmarks & Baselines
- **Temporal Action Detection (mAP@0.5):** BMN — 50.07% — *Lin et al., ICCV 2019.*
- **Temporal Action Detection (mAP@0.5):** ActionFormer — 54.7% — *Zhang et al., ECCV 2022.*
- **Activity Classification (Top-1):** TSN — 89.0% — *Wang et al., ECCV 2016.*
- Standard evaluation uses ActivityNet v1.3 with official train/val/test splits; test labels are held out for challenge submission.

## Tooling & Ecosystem
- [ActivityNet Challenge](http://activity-net.org/challenges/) hosts annual competitions with evaluation servers.
- [MMAction2](https://github.com/open-mmlab/mmaction2) supports temporal action detection on ActivityNet.
- [ActivityNet Utils](https://github.com/activitynet/ActivityNet) provides evaluation tools and download scripts.

## Known Challenges
- YouTube video availability degrades over time; some links may be broken.
- Untrimmed videos require robust temporal boundary detection, making training more complex than on trimmed datasets.
- Activity classes have hierarchical relationships that are not fully exploited in standard benchmarks.
- Background segments dominate most videos, creating heavy class imbalance for detection tasks.

## Cite
```bibtex
@inproceedings{heilbron2015activitynet,
  title     = {ActivityNet: A Large-Scale Video Benchmark for Human Activity Understanding},
  author    = {Caba Heilbron, Fabian and Escorcia, Victor and Ghanem, Bernard and Niebles, Juan Carlos},
  booktitle = {IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year      = {2015}
}
```
