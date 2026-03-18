# Awesome Reconnaissance d'Activites Humaines (Awesome Human Activity Recognition)

[中文](README.zh.md) | [English](../README.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [**français**](README.fr.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Português](README.pt.md) | [Русский](README.ru.md)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Stars](https://img.shields.io/github/stars/Leo-Cyberautonomy/awesome-human-activity-recognition?style=social)](https://github.com/Leo-Cyberautonomy/awesome-human-activity-recognition/stargazers)
[![License](https://img.shields.io/github/license/Leo-Cyberautonomy/awesome-human-activity-recognition)](../LICENSE)
[![Datasets](https://img.shields.io/badge/datasets-42-brightgreen)](#apercu-par-categorie)

Un repertoire organise de **42** jeux de donnees sur l'activite et le mouvement humains, couvrant la vision, les capteurs portables, la capture de squelette, le multimodal et bien plus. Chaque fiche de jeu de donnees inclut les modalites, la licence, les taches de reference, les baselines representatives, l'ecosysteme d'outils et les publications de reference, pour vous aider a demarrer rapidement la modelisation ou l'evaluation comparative.

- Destine aux chercheurs en apprentissage automatique, aux equipes produit et aux laboratoires de science du mouvement.
- Presente a la fois les jeux de donnees les plus recents et les classiques qui ont fonde les benchmarks actuels.
- Accompagne d'un workflow de contribution, d'outils de validation et d'une feuille de route pour une maintenance collaborative par la communaute.

> Objectif : devenir la ressource GitHub de reference pour les jeux de donnees d'activite humaine, avec la profondeur de Papers with Code tout en conservant une perspective « jeux de donnees d'abord ».

## Acces rapide
- Repertoire des fiches de jeux de donnees : [`datasets/`](../datasets/)
- Articles de synthese et benchmarks : [`docs/surveys.md`](../docs/surveys.md)
- Apercu des benchmarks : [`docs/benchmarking.md`](../docs/benchmarking.md)
- Guide de contribution : [`CONTRIBUTING.md`](../CONTRIBUTING.md)
- Feuille de route de l'automatisation : [`docs/roadmap.md`](../docs/roadmap.md)

## Apercu par categorie

### Vision (RGB / Profondeur) — 11 jeux de donnees

| Jeu de donnees | Modalite | Tache principale | Echelle | Acces |
| --- | --- | --- | --- | --- |
| [Kinetics-700](../datasets/vision/kinetics-700.md) | Video RGB | Reconnaissance d'actions, pre-entrainement | 650k clips / 700 classes | Public (CC BY) |
| [UCF-101](../datasets/vision/ucf101.md) | Video RGB | Reconnaissance d'actions | 13k clips / 101 classes | Public (recherche) |
| [HMDB-51](../datasets/vision/hmdb51.md) | Video RGB | Reconnaissance d'actions | 6800 clips / 51 classes | Public (recherche) |
| [ActivityNet](../datasets/vision/activitynet.md) | Video RGB | Detection temporelle d'actions | 20k videos / 200 classes | Public (recherche) |
| [AVA](../datasets/vision/ava.md) | Video RGB | Detection spatio-temporelle d'actions | 430 clips / 80 actions atomiques | Public (recherche) |
| [NTU RGB+D 120](../datasets/vision/ntu-rgbd-120.md) | RGB + Profondeur + Squelette | Reconnaissance d'actions 3D | 114k sequences / 120 classes | Accord de recherche |
| [Something-Something V2](../datasets/vision/something-something-v2.md) | Video RGB | Reconnaissance d'interactions fines | 220k clips / 174 etiquettes | Public (Apache 2.0) |
| [FineGym](../datasets/vision/finegym.md) | Video RGB | Actions gymnastiques fines | 32k segments / annotations hierarchiques | Public (recherche) |
| [Moments in Time](../datasets/vision/moments-in-time.md) | Video RGB | Reconnaissance d'evenements/actions | 1M clips / 339 classes | Public (recherche) |
| [Diving48](../datasets/vision/diving48.md) | Video RGB | Actions de plongeon fines | 18k clips / 48 classes | Public (recherche) |
| [Toyota Smarthome](../datasets/vision/toyota-smarthome.md) | RGB + Profondeur + Squelette | Activites de la vie quotidienne | 16k clips / 31 classes | Accord de recherche |

### Squelette et capture de mouvement — 7 jeux de donnees

| Jeu de donnees | Modalite | Tache principale | Echelle | Acces |
| --- | --- | --- | --- | --- |
| [NTU RGB+D 60](../datasets/skeleton/ntu-rgbd-60.md) | RGB + Profondeur + Squelette | Reconnaissance d'actions par squelette | 57k sequences / 60 classes | Accord de recherche |
| [AMASS](../datasets/skeleton/amass.md) | Pose corporelle parametree | Generation de mouvement, estimation de pose | 16k minutes / 344 sujets | Public (licence AMASS) |
| [Human3.6M](../datasets/skeleton/human36m.md) | Capture de mouvement + RGB | Estimation de pose, reconstruction 3D | 3,6M images 3D | Licence de recherche |
| [BABEL](../datasets/skeleton/babel.md) | SMPL + etiquettes textuelles | Alignement action-langage | 43 heures / 3,7k sequences | Recherche (non commercial) |
| [TotalCapture](../datasets/skeleton/totalcapture.md) | Capture de mouvement + multi-vues RGB + IMU | Estimation de pose 3D, fusion | 5 sujets / multi-vues | Public (CC BY) |
| [PKU-MMD](../datasets/skeleton/pku-mmd.md) | RGB + Profondeur + Squelette | Detection d'actions | 20k instances / 51 classes | Accord de recherche |
| [Skeletics-152](../datasets/skeleton/skeletics-152.md) | Squelette estime | Reconnaissance d'actions a grande echelle | 150k clips / 152 classes | Recherche |

### Capteurs portables — 10 jeux de donnees

| Jeu de donnees | Modalite | Tache principale | Echelle | Acces |
| --- | --- | --- | --- | --- |
| [UCI-HAR](../datasets/wearable/uci-har.md) | IMU smartphone | Reconnaissance d'activites | 30 sujets / 6 activites | Public (CC BY) |
| [PAMAP2](../datasets/wearable/pamap2.md) | IMU + frequence cardiaque | HAR portable | 9 sujets / 18 activites | Public (CC BY-SA) |
| [WISDM](../datasets/wearable/wisdm.md) | Telephone + montre | HAR, reconnaissance gestuelle | 51 sujets / millions d'echantillons | Public (Creative Commons) |
| [OPPORTUNITY](../datasets/wearable/opportunity.md) | Capteurs portables + ambiants | Reconnaissance de scenarios | 4 sujets / 72 canaux | Public (recherche) |
| [HAPT](../datasets/wearable/hapt.md) | IMU smartphone | Activites et transitions posturales | 30 sujets / 12 activites | Public (CC BY) |
| [RealWorld HAR](../datasets/wearable/realworld-har.md) | IMU telephone + montre | HAR en conditions reelles | 60 sujets / 15 activites | Public (CC BY) |
| [mHealth](../datasets/wearable/mhealth.md) | Capteurs corporels + ECG | Suivi de sante mobile | 10 sujets / 12 activites | Public (CC BY) |
| [UniMiB-SHAR](../datasets/wearable/unimib-shar.md) | Accelerometre smartphone | Activites quotidiennes + detection de chutes | 30 sujets / 17 activites | Public |
| [Daphnet](../datasets/wearable/daphnet.md) | Accelerometre portable | Gel de la marche (Parkinson) | 10 sujets / 3 capteurs | Public |
| [Sussex-Huawei Locomotion](../datasets/wearable/shl.md) | Telephone + montre | Reconnaissance du mode de locomotion | 3 sujets / 2800+ heures | Public |

### Multimodal / Premiere personne — 6 jeux de donnees

| Jeu de donnees | Modalite | Tache principale | Echelle | Acces |
| --- | --- | --- | --- | --- |
| [EPIC-Kitchens-100](../datasets/multimodal/epic-kitchens-100.md) | RGB egocentrique + audio | Comportement egocentrique longue duree | 700 heures / 90 cuisines | Licence de recherche |
| [Ego4D](../datasets/multimodal/ego4d.md) | RGB egocentrique + stereo + audio | Comportement 4D, QA, audiovisuel | 3300 heures / 74 scenarios | Non commercial |
| [Charades](../datasets/multimodal/charades.md) | RGB interieur + scenarios | Actions multi-etiquettes | 9800 videos / 157 etiquettes | Public (CC BY-NC) |
| [NTU Mutual Actions](../datasets/multimodal/ntu-mutual.md) | RGB + Profondeur + Squelette | Interaction entre deux personnes | 26 classes d'interaction | Accord de recherche |
| [ActivityNet Captions](../datasets/multimodal/activitynet-captions.md) | Video RGB + texte | Description video dense | 20k videos / 100k descriptions | Public (recherche) |
| [How2Sign](../datasets/multimodal/how2sign.md) | RGB + Profondeur + Pose | Comprehension de la langue des signes | 80 heures / ASL | Public (recherche) |

### Frontieres et emergents — 8 jeux de donnees

| Jeu de donnees | Modalite | Tache principale | Echelle | Acces |
| --- | --- | --- | --- | --- |
| [BEHAVE](../datasets/emerging/behave.md) | RGB-D + Pose | Modelisation interaction humain-objet | 321 sequences / 20 sujets | Public (licence BEHAVE) |
| [Motion-X](../datasets/emerging/motion-x.md) | Capture de mouvement multi-capteurs | Squelette corps entier + mains | 10 sujets / 2M images | Public (recherche) |
| [Ego-Exo4D](../datasets/emerging/ego-exo4d.md) | RGB ego + exo + capture de mouvement | Traduction de points de vue | 1400 sequences / 20 heures | Public (recherche) |
| [HumanML3D](../datasets/emerging/humanml3d.md) | SMPL + texte | Generation de mouvement a partir de texte | 14k+ sequences de mouvement | Public (recherche) |
| [InterHuman](../datasets/emerging/interhuman.md) | SMPL-X + texte | Mouvement d'interaction a deux personnes | 6000+ sequences d'interaction | Public (recherche) |
| [HOI4D](../datasets/emerging/hoi4d.md) | RGB-D egocentrique + pose de la main | Interaction main-objet | 4000+ clips video | Public (recherche) |
| [FineBio](../datasets/emerging/finebio.md) | RGB + Squelette | Manipulation fine en experiences biologiques | Protocoles experimentaux multi-etapes | Public (recherche) |
| [HAA500](../datasets/emerging/haa500.md) | Video RGB | Reconnaissance d'actions atomiques | 10k clips / 500 classes | Public |

Pour plus de details, consultez la fiche correspondante de chaque jeu de donnees, incluant les methodes de telechargement, les informations de citation, les resultats de reference et les defis connus.

## Pourquoi ce depot
- **Navigation par probleme :** Recherchez les jeux de donnees par tache ou modalite, et non par simple ordre alphabetique.
- **Contexte de recherche :** Chaque fiche renvoie aux publications de reference, aux benchmarks et aux travaux les plus recents.
- **Outils exploitables :** Generateur de catalogue (export JSON/CSV), verification des liens, normalisation ASCII.
- **Assurance qualite :** Modeles de contribution, listes de verification et CI automatisee pour un repertoire fiable et credible.

## Structure du depot
```
.
 datasets/               # 42 fiches de jeux de donnees organisees par modalite
   vision/               #   11 jeux de donnees visuels
   skeleton/             #    7 jeux de donnees squelette/capture de mouvement
   wearable/             #   10 jeux de donnees capteurs portables
   multimodal/           #    6 jeux de donnees multimodaux/premiere personne
   emerging/             #    8 jeux de donnees frontieres et emergents
 docs/                   # Syntheses, benchmarks, feuille de route
 tools/                  # Scripts (generateur de catalogue, verification de liens, normalisation ASCII)
 .github/workflows/      # CI (verification de liens, lint Markdown)
 i18n/                   # Traductions (zh, de, es, fr, ja, ko, pt, ru)
```

## Articles et syntheses selectionnes
- Aggarwal & Ryoo, « Human Activity Analysis: A Review », ACM Computing Surveys, 2011.
- Lara & Labrador, « A Survey on Human Activity Recognition using Wearable Sensors », IEEE Communications Surveys, 2013.
- Li et al., « A Systematic Survey on Deep Learning for Human Activity Recognition », ACM Computing Surveys, 2022.
- Grauman et al., « Ego4D: Around the World in 2,250 Hours of Egocentric Video », CVPR 2022. (jeu de donnees + benchmark)
- Pavlakos et al., « BABEL: Bodies, Actions and Behavior with English Labels », CVPR 2022.

Pour aller plus loin, consultez [`docs/surveys.md`](../docs/surveys.md).

## Comment utiliser ce repertoire
1. **Trouver un jeu de donnees :** Consultez d'abord le tableau de classification ci-dessus ou parcourez le repertoire [`datasets/`](../datasets/).
2. **Lire la fiche du jeu de donnees :** Avant le telechargement, informez-vous sur la licence, les taches, le protocole de benchmark et les caracteristiques des donnees.
3. **Prototypage rapide :** Utilisez les liens vers les outils et l'ecosysteme dans chaque fiche pour integrer les chargeurs de donnees PyTorch / TensorFlow.
4. **Generer un export du catalogue :** Executez `python tools/catalog_builder.py --format csv --output catalog.csv` pour obtenir des metadonnees lisibles par machine.
5. **Rester informe :** Suivez (Watch) le depot ou rejoignez les Discussions ; nous resumons les nouveaux jeux de donnees et les avancees SOTA a chaque publication.

### Citation
Si ce depot s'avere utile pour votre recherche ou votre produit, veuillez citer :

```bibtex
@misc{awesome_har_2025,
  title   = {Awesome Human Activity Recognition: A Curated List},
  author  = {Wenxuan Huang},
  year    = {2025},
  url     = {https://github.com/Leo-Cyberautonomy/awesome-human-activity-recognition},
  note    = {GitHub repository}
}
```

## Contribuer
- Lisez [`CONTRIBUTING.md`](../CONTRIBUTING.md) pour obtenir le modele de fiche, les criteres d'evaluation et les conventions de redaction.
- Utilisez les Issues pour demander un nouveau jeu de donnees ou signaler un lien casse. Nous utilisons des etiquettes par modalite (par ex. `modality:wearable`).
- Les Pull Requests font l'objet d'une revue qualite des donnees et d'une verification automatisee des liens, avec un objectif de traitement sous 5 a 7 jours.

## Feuille de route
- Verification automatique hebdomadaire des liens (GitHub Actions).
- Notebooks Jupyter d'introduction pour les baselines portables et video.
- Schema standardise des jeux de donnees (YAML) avec validation automatique.
- Point communautaire : resume trimestriel des nouveaux jeux de donnees et des classements.
- Objectif a long terme : site statique consultable base sur MkDocs.

Consultez la feuille de route complete dans [`docs/roadmap.md`](../docs/roadmap.md).

## Remerciements
Merci a tous les auteurs de jeux de donnees, aux equipes d'annotation et aux mainteneurs de benchmarks qui font avancer la recherche ouverte dans le domaine de la comprehension de l'activite humaine. Nous esperons amplifier leurs contributions grace a un repertoire facile a utiliser.
