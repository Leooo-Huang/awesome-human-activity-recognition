# InterX

- **Modality:** SMPL-X full-body motion capture (body, hands, face), text descriptions, interaction labels
- **Primary Tasks:** Human-human interaction generation, interactive motion prediction, text-to-interaction synthesis
- **Scale:** 11,000+ interaction sequences, 40+ interaction categories, paired SMPL-X parameters for two interacting persons
- **License:** Research use only (non-commercial)
- **Access:** [https://liangxuy.github.io/inter-x/](https://liangxuy.github.io/inter-x/)

## Summary
InterX is a comprehensive dataset for modeling human-human interactions, capturing two-person motion sequences with full SMPL-X body models including detailed hand articulation and facial expressions. Each interaction sequence is paired with natural language descriptions and categorical labels covering a diverse range of social interactions — from handshakes and hugs to cooperative and competitive actions. InterX addresses a key limitation of prior interaction datasets (which typically used simplified body models without hand or face detail) by providing expressive whole-body representations. The dataset supports research in interaction generation, motion prediction, and understanding the fine-grained dynamics of interpersonal physical communication.

## Reference Paper
- *Liang Xu, Xianghui Xie, Boshi Tang, Yiyu Zhuang, Yichao Yan, Gerard Pons-Moll, Xiaokang Yang.* "Inter-X: Towards Versatile Human-Human Interaction Analysis." CVPR, 2024. [`PDF`](https://arxiv.org/abs/2312.16051)

## Benchmarks & Baselines
- **InterGen** - FID: 5.90, R-Precision Top-3: 0.547 (text-to-interaction generation) — *Xu et al., CVPR 2024.*
- **ComMDM** - FID: 8.23, R-Precision Top-3: 0.489 (text-to-interaction generation) — *Xu et al., CVPR 2024.*
- **Interaction Prediction** - ADE: 85.2mm at 2s horizon using STSGCN — *Xu et al., CVPR 2024.*
- Evaluation follows text-to-motion protocol: FID, R-Precision, Diversity; plus interaction-specific metrics for contact accuracy and synchronization.
- Official train/val/test splits with cross-subject partitioning.

## Tooling & Ecosystem
- Official code and tools: [https://github.com/liangxuy/Inter-X](https://github.com/liangxuy/Inter-X)
- Data provided as SMPL-X parameters (`.npz`) with synchronized text annotations in JSON format.
- Requires [SMPL-X body model](https://smpl-x.is.tue.mpg.de/) for rendering and evaluation.
- Visualization scripts for Blender rendering and skeleton overlay included in the official repository.
- Compatible with [InterGen](https://github.com/tr3e/InterGen) and other two-person motion generation frameworks.

## Known Challenges
- Two-person SMPL-X fitting can produce interpenetration artifacts, especially during close-contact interactions.
- Hand and face capture quality varies; some fine manipulation interactions have noisy finger tracking.
- Text descriptions vary in granularity and detail; some interactions have brief labels while others have rich descriptions.
- Modeling the coordination and synchronization between two people is fundamentally harder than single-person motion generation.
- Requires SMPL-X license from MPI in addition to the dataset license.
- Interaction categories have imbalanced instance counts; daily interactions are more frequent than specialized actions.

## Cite
```bibtex
@inproceedings{xu2024interx,
  title     = {Inter-X: Towards Versatile Human-Human Interaction Analysis},
  author    = {Xu, Liang and Xie, Xianghui and Tang, Boshi and Zhuang, Yiyu and Yan, Yichao and Pons-Moll, Gerard and Yang, Xiaokang},
  booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year      = {2024}
}
```
