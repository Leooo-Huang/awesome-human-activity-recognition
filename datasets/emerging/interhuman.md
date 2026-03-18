# InterHuman

- **Modality:** 3D human motion (two-person interactions) + natural language text descriptions
- **Primary Tasks:** Text-to-interaction motion generation, two-person motion synthesis
- **Scale:** ~7,779 two-person interaction motion sequences, ~23,337 text descriptions
- **License:** Research use only
- **Access:** [https://github.com/tr3e/InterHuman](https://github.com/tr3e/InterHuman)

## Summary
InterHuman is a dataset for text-driven two-person interaction motion generation. While HumanML3D focuses on single-person motions, InterHuman specifically targets the more challenging problem of generating coordinated movements between two interacting people. The dataset contains motion capture data of two-person interactions (e.g., dancing together, fighting, handshaking, helping someone up) paired with natural language descriptions. Each interaction is annotated with multiple text descriptions capturing different aspects of the interaction. InterHuman fills a critical gap in motion generation research by enabling models to learn spatial and temporal coordination between two agents.

## Reference Paper
- *Han Liang, Wenqian Zhang, Wenxuan Li, Jingyi Yu, Lan Xu.* "InterGen: Diffusion-based Multi-human Motion Generation under Complex Interactions." International Journal of Computer Vision (IJCV), 2024. [`PDF`](https://arxiv.org/abs/2304.05684)

## Benchmarks & Baselines
- **InterGen** - FID: 5.90, R-Precision (Top-3): 0.722 — *Liang et al., IJCV 2024.*
- **ComMDM** - reported as baseline for two-person generation tasks.
- **RIG** - improved interaction quality metrics over InterGen — follow-up works.
- Evaluation metrics mirror HumanML3D (FID, R-Precision, Diversity) adapted for two-person settings.

## Tooling & Ecosystem
- [InterGen repo](https://github.com/tr3e/InterHuman) provides data processing, model training, and evaluation code.
- Motion representation follows SMPL-based joint formats compatible with AMASS/HumanML3D pipelines.
- Visualization tools for two-person motion are included in the repository.

## Known Challenges
- Two-person motion generation is fundamentally harder than single-person; models must maintain physical plausibility of interactions (no interpenetration, correct contact).
- Dataset size is smaller than HumanML3D, limiting the diversity of learnable interactions.
- Interaction categories are biased toward simple paired activities; complex multi-step interactions are rare.
- Evaluating interaction quality (e.g., contact accuracy, synchronization) requires metrics beyond standard FID.
- Text descriptions may not fully specify the spatial arrangement and timing of two-person interactions.

## Cite
```bibtex
@article{liang2024intergen,
  title   = {InterGen: Diffusion-based Multi-human Motion Generation under Complex Interactions},
  author  = {Liang, Han and Zhang, Wenqian and Li, Wenxuan and Yu, Jingyi and Xu, Lan},
  journal = {International Journal of Computer Vision},
  year    = {2024}
}
```
