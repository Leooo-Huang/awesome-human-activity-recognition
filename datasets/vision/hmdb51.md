# HMDB-51

- **Modality:** RGB video (movie clips, YouTube, web videos)
- **Primary Tasks:** Action recognition
- **Scale:** 6,849 clips, 51 action classes
- **License:** Research use only (Creative Commons Attribution 4.0 for annotations)
- **Access:** [https://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database/](https://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database/)

## Summary
HMDB-51 (Human Motion DataBase) contains 6,849 video clips organized into 51 action categories. Clips are sourced from digitized movies, the Prelinger archive, YouTube, and Google Videos. The dataset was designed to be more realistic and challenging than earlier benchmarks, featuring significant variation in camera motion, viewpoint, video quality, and occlusion. Each category contains at least 101 clips, and the dataset provides stabilized versions of all videos.

## Reference Paper
- *Hildegard Kuehne, Hueihan Jhuang, Estíbaliz Garrote, Tomaso Poggio, Thomas Serre.* "HMDB: A Large Video Database for Human Motion Recognition." ICCV, 2011. [`PDF`](https://ieeexplore.ieee.org/document/6126543)

## Benchmarks & Baselines
- **Two-Stream ConvNet** - Top-1: 59.4% — *Simonyan & Zisserman, NeurIPS 2014.*
- **I3D (RGB + Flow)** - Top-1: 80.7% — *Carreira & Zisserman, CVPR 2017.*
- **TimeSformer-L** - Top-1: 82.4% — *Bertasius et al., ICML 2021.*
- Standard evaluation uses 3 official train/test splits; accuracy is averaged across all 3 splits.

## Tooling & Ecosystem
- [MMAction2](https://github.com/open-mmlab/mmaction2) includes HMDB-51 configs and pretrained models.
- [PyTorchVideo](https://pytorchvideo.org/) supports HMDB-51 data loading.
- [TensorFlow Datasets](https://www.tensorflow.org/datasets/catalog/hmdb51) provides preprocessed splits.

## Known Challenges
- Low resolution and variable quality of source videos can hinder feature extraction.
- Relatively small dataset size; performance is near saturation with Kinetics pretraining.
- Some clips are very short (< 1 second), making temporal modeling difficult.
- Action categories have inherent visual ambiguity (e.g., "smile" vs "laugh").

## Cite
```bibtex
@inproceedings{kuehne2011hmdb,
  title     = {HMDB: A Large Video Database for Human Motion Recognition},
  author    = {Kuehne, Hildegard and Jhuang, Hueihan and Garrote, Est{\'i}baliz and Poggio, Tomaso and Serre, Thomas},
  booktitle = {IEEE International Conference on Computer Vision (ICCV)},
  year      = {2011}
}
```
