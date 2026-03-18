# How2Sign

- **Modality:** RGB video (multi-view), depth, 2D/3D body + hand + face pose, English audio, ASL gloss, English text
- **Primary Tasks:** Sign language recognition, sign language translation, sign language production
- **Scale:** ~80 hours of ASL video, ~35,000 aligned sentence pairs, 11 signers
- **License:** Research use only (requires agreement)
- **Access:** [https://how2sign.github.io/](https://how2sign.github.io/)

## Summary
How2Sign is a large-scale multimodal dataset for American Sign Language (ASL) understanding and generation. It contains approximately 80 hours of sign language video from 11 native ASL signers, captured in a studio setting with multiple synchronized views (frontal, side), depth sensors, and body/hand/face motion capture. Each signing sequence is aligned with English text translations, speech audio, and ASL gloss annotations. The dataset was designed to support continuous sign language recognition and translation (as opposed to isolated sign recognition), making it one of the largest and most comprehensive sign language resources available.

## Reference Paper
- *Amanda Duarte, Shruti Palaskar, Lucas Ventura, Deepti Ghadiyaram, Kenneth DeHaan, Florian Metze, Jordi Torres, Xavier Giro-i-Nieto.* "How2Sign: A Large-scale Multimodal Dataset for Continuous American Sign Language." CVPR, 2021. [`PDF`](https://arxiv.org/abs/2008.08143)

## Benchmarks & Baselines
- **Sign Language Translation (BLEU-4, test):** ~10-12 BLEU — reported in baseline experiments.
- **Sign Language Recognition (WER):** ~50-60% — transformer-based baselines.
- **Sign2Text Transformer** — baseline performance reported in the original paper.
- Evaluation uses the official train/val/test split; BLEU and ROUGE for translation, WER for recognition.

## Tooling & Ecosystem
- [Official project page](https://how2sign.github.io/) provides download links, annotations, and documentation.
- [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) keypoints are pre-extracted and provided.
- MediaPipe hand landmarks can supplement the provided pose data.
- Compatible with sign language translation frameworks built on fairseq or HuggingFace Transformers.

## Known Challenges
- Continuous sign language translation is an extremely challenging task; current models still perform far below human-level.
- Studio conditions with green screen differ from real-world signing environments.
- Limited signer diversity (11 signers) may not capture the full range of ASL dialectal variation.
- Hand and face detail are critical for ASL but difficult to capture accurately at distance.
- Alignment between ASL and English is non-trivial due to fundamental grammatical differences.

## Cite
```bibtex
@inproceedings{duarte2021how2sign,
  title     = {How2Sign: A Large-scale Multimodal Dataset for Continuous American Sign Language},
  author    = {Duarte, Amanda and Palaskar, Shruti and Ventura, Lucas and Ghadiyaram, Deepti and DeHaan, Kenneth and Metze, Florian and Torres, Jordi and Giro-i-Nieto, Xavier},
  booktitle = {IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year      = {2021}
}
```
