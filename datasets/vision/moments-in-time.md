# Moments in Time

- **Modality:** RGB video (web-sourced clips)
- **Primary Tasks:** Action/event recognition, temporal understanding
- **Scale:** ~1,000,000 labeled 3-second video clips, 339 classes
- **License:** Research use only (MIT terms)
- **Access:** [http://moments.csail.mit.edu/](http://moments.csail.mit.edu/)

## Summary
Moments in Time is a large-scale dataset of one million 3-second video clips, each labeled with one of 339 action/activity labels. The dataset was designed to capture the diversity of visual and auditory events, covering actions performed by people, animals, objects, and nature. The short clip duration and broad class vocabulary make the dataset uniquely challenging, as models must recognize events from minimal temporal context across a wide variety of visual domains. The dataset emphasizes that understanding "moments" requires both visual and auditory reasoning.

## Reference Paper
- *Mathew Monfort, Alex Andonian, Bolei Zhou, Kandan Ramakrishnan, Sarah Adel Bargal, Tom Yan, Lisa Brown, Quanfu Fan, Dan Gutfruend, Carl Vondrick, Aude Oliva.* "Moments in Time Dataset: One Million Videos for Event Understanding." IEEE TPAMI, 2019. [`PDF`](https://arxiv.org/abs/1801.03150)

## Benchmarks & Baselines
- **TSN (RGB)** - Top-1: 25.3%, Top-5: 50.1% — *Monfort et al., TPAMI 2019.*
- **TRN** - Top-1: 28.3%, Top-5: 53.4% — *Monfort et al., TPAMI 2019.*
- **Video Swin Transformer** - Top-1: ~34% — reported in follow-up works.
- Standard evaluation uses the official val set; test set labels are withheld for the Moments in Time challenge.

## Tooling & Ecosystem
- [Official website](http://moments.csail.mit.edu/) provides download links and evaluation tools.
- [MMAction2](https://github.com/open-mmlab/mmaction2) supports training on Moments in Time.
- [TorchVision](https://pytorch.org/vision/) can be used with custom dataset loaders.

## Known Challenges
- 3-second clips provide very limited temporal context, making some actions inherently ambiguous.
- Class vocabulary spans agents beyond humans (animals, objects, natural phenomena), broadening the recognition task.
- Label noise is higher than curated datasets due to web sourcing and crowd annotation at scale.
- Severe class imbalance across the 339 categories.

## Cite
```bibtex
@article{monfort2019moments,
  title   = {Moments in Time Dataset: One Million Videos for Event Understanding},
  author  = {Monfort, Mathew and Andonian, Alex and Zhou, Bolei and Ramakrishnan, Kandan and Bargal, Sarah Adel and Yan, Tom and Brown, Lisa and Fan, Quanfu and Gutfruend, Dan and Vondrick, Carl and Oliva, Aude},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
  year    = {2019}
}
```
