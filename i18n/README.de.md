# Awesome Erkennung menschlicher Aktivitäten (Awesome Human Activity Recognition)

[中文](README.zh.md) | [English](../README.md) | [**Deutsch**](README.de.md) | [Español](README.es.md) | [français](README.fr.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Português](README.pt.md) | [Русский](README.ru.md)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Stars](https://img.shields.io/github/stars/Leo-Cyberautonomy/awesome-human-activity-recognition?style=social)](https://github.com/Leo-Cyberautonomy/awesome-human-activity-recognition/stargazers)
[![License](https://img.shields.io/github/license/Leo-Cyberautonomy/awesome-human-activity-recognition)](../LICENSE)
[![Datasets](https://img.shields.io/badge/datasets-42-brightgreen)](#taxonomie-überblick)

Ein kuratiertes Verzeichnis von **42** Datensätzen zu menschlicher Aktivität und Bewegung, das die Bereiche visuelles Erkennen, tragbare Sensorik, Skeletterfassung, Multimodalität und weitere abdeckt. Jede Datensatzkarte enthält Informationen zu Modalität, Lizenz, Benchmark-Aufgaben, repräsentativen Baselines, Tool-Ökosystem und maßgeblichen Publikationen, damit Sie schnell mit der Modellierung oder vergleichenden Evaluation beginnen können.

- Ausgerichtet auf Machine-Learning-Forschende, Produktteams und sportwissenschaftliche Labore.
- Zeigt sowohl hochaktuelle Datensätze als auch klassische Datensätze, die bestehende Benchmarks begründen.
- Enthält einen Beitragsworkflow, Validierungstools und eine Entwicklungs-Roadmap für gemeinschaftliche Pflege.

> Ziel: Die maßgebliche GitHub-Ressource für Datensätze zur Erkennung menschlicher Aktivitäten schaffen – mit der Tiefe von Papers with Code, aber aus einer „Datensatz-zuerst"-Perspektive.

## Schnellzugriff
- Datensatzkarten-Verzeichnis: [`datasets/`](../datasets/)
- Übersichtsarbeiten und Benchmark-Papers: [`docs/surveys.md`](../docs/surveys.md)
- Benchmark-Übersicht: [`docs/benchmarking.md`](../docs/benchmarking.md)
- Beitragsleitfaden: [`CONTRIBUTING.md`](../CONTRIBUTING.md)
- Automatisierungs-Roadmap: [`docs/roadmap.md`](../docs/roadmap.md)

## Taxonomie-Überblick

### Visuell (RGB / Tiefe) — 11 Datensätze

| Datensatz | Modalität | Hauptaufgabe | Umfang | Zugang |
| --- | --- | --- | --- | --- |
| [Kinetics-700](../datasets/vision/kinetics-700.md) | RGB-Video | Aktionserkennung, Pretraining | 650k Clips / 700 Klassen | Öffentlich (CC BY) |
| [UCF-101](../datasets/vision/ucf101.md) | RGB-Video | Aktionserkennung | 13k Clips / 101 Klassen | Öffentlich (Forschung) |
| [HMDB-51](../datasets/vision/hmdb51.md) | RGB-Video | Aktionserkennung | 6.800 Clips / 51 Klassen | Öffentlich (Forschung) |
| [ActivityNet](../datasets/vision/activitynet.md) | RGB-Video | Temporale Aktionserkennung | 20k Videos / 200 Klassen | Öffentlich (Forschung) |
| [AVA](../datasets/vision/ava.md) | RGB-Video | Räumlich-temporale Aktionserkennung | 430 Clips / 80 atomare Aktionen | Öffentlich (Forschung) |
| [NTU RGB+D 120](../datasets/vision/ntu-rgbd-120.md) | RGB + Tiefe + Skelett | 3D-Aktionserkennung | 114k Sequenzen / 120 Klassen | Forschungslizenz |
| [Something-Something V2](../datasets/vision/something-something-v2.md) | RGB-Video | Feinkörnige Interaktionserkennung | 220k Clips / 174 Labels | Öffentlich (Apache 2.0) |
| [FineGym](../datasets/vision/finegym.md) | RGB-Video | Feinkörnige Turnbewegungen | 32k Segmente / hierarchische Annotation | Öffentlich (Forschung) |
| [Moments in Time](../datasets/vision/moments-in-time.md) | RGB-Video | Ereignis-/Aktionserkennung | 1M Clips / 339 Klassen | Öffentlich (Forschung) |
| [Diving48](../datasets/vision/diving48.md) | RGB-Video | Feinkörnige Sprungbewegungen | 18k Clips / 48 Klassen | Öffentlich (Forschung) |
| [Toyota Smarthome](../datasets/vision/toyota-smarthome.md) | RGB + Tiefe + Skelett | Alltagsaktivitäten | 16k Clips / 31 Klassen | Forschungslizenz |

### Skelett und Motion Capture — 7 Datensätze

| Datensatz | Modalität | Hauptaufgabe | Umfang | Zugang |
| --- | --- | --- | --- | --- |
| [NTU RGB+D 60](../datasets/skeleton/ntu-rgbd-60.md) | RGB + Tiefe + Skelett | Skelettbasierte Aktionserkennung | 57k Sequenzen / 60 Klassen | Forschungslizenz |
| [AMASS](../datasets/skeleton/amass.md) | Parametrische Körperpose | Bewegungsgenerierung, Posenschätzung | 16k Minuten / 344 Probanden | Öffentlich (AMASS-Lizenz) |
| [Human3.6M](../datasets/skeleton/human36m.md) | Motion Capture + RGB | Posenschätzung, 3D-Rekonstruktion | 3,6M Frames 3D-Daten | Forschungslizenz |
| [BABEL](../datasets/skeleton/babel.md) | SMPL + Textlabels | Bewegung-Sprache-Alignment | 43 Stunden / 3,7k Sequenzen | Forschung (nicht-kommerziell) |
| [TotalCapture](../datasets/skeleton/totalcapture.md) | Motion Capture + Multi-View RGB + IMU | 3D-Posenschätzung, Fusion | 5 Personen / Multi-View | Öffentlich (CC BY) |
| [PKU-MMD](../datasets/skeleton/pku-mmd.md) | RGB + Tiefe + Skelett | Aktionserkennung | 20k Instanzen / 51 Klassen | Forschungslizenz |
| [Skeletics-152](../datasets/skeleton/skeletics-152.md) | Geschätzte Skelette | Großangelegte Skelett-Aktionserkennung | 150k Clips / 152 Klassen | Forschung |

### Tragbare Sensoren — 10 Datensätze

| Datensatz | Modalität | Hauptaufgabe | Umfang | Zugang |
| --- | --- | --- | --- | --- |
| [UCI-HAR](../datasets/wearable/uci-har.md) | Smartphone-IMU | Aktivitätserkennung | 30 Personen / 6 Aktivitäten | Öffentlich (CC BY) |
| [PAMAP2](../datasets/wearable/pamap2.md) | IMU + Herzfrequenz | Wearable-HAR | 9 Personen / 18 Aktivitäten | Öffentlich (CC BY-SA) |
| [WISDM](../datasets/wearable/wisdm.md) | Smartphone + Smartwatch | HAR, Gestenerkennung | 51 Personen / Millionen Samples | Öffentlich (Creative Commons) |
| [OPPORTUNITY](../datasets/wearable/opportunity.md) | Wearable + Umgebungssensoren | Szenarioerkennung | 4 Personen / 72 Kanäle | Öffentlich (Forschung) |
| [HAPT](../datasets/wearable/hapt.md) | Smartphone-IMU | Aktivitäts- und Haltungsübergänge | 30 Personen / 12 Aktivitäten | Öffentlich (CC BY) |
| [RealWorld HAR](../datasets/wearable/realworld-har.md) | Smartphone + Smartwatch IMU | Reale HAR | 60 Personen / 15 Aktivitäten | Öffentlich (CC BY) |
| [mHealth](../datasets/wearable/mhealth.md) | Körpersensoren + EKG | Mobile Gesundheitsüberwachung | 10 Personen / 12 Aktivitäten | Öffentlich (CC BY) |
| [UniMiB-SHAR](../datasets/wearable/unimib-shar.md) | Smartphone-Beschleunigungsmesser | Alltagsaktivitäten + Sturzerkennung | 30 Personen / 17 Aktivitäten | Öffentlich |
| [Daphnet](../datasets/wearable/daphnet.md) | Tragbare Beschleunigungsmesser | Freezing of Gait (Parkinson) | 10 Personen / 3 Sensoren | Öffentlich |
| [Sussex-Huawei Locomotion](../datasets/wearable/shl.md) | Smartphone + Smartwatch | Fortbewegungsart-Erkennung | 3 Personen / 2.800+ Stunden | Öffentlich |

### Multimodal / Egozentrisch — 6 Datensätze

| Datensatz | Modalität | Hauptaufgabe | Umfang | Zugang |
| --- | --- | --- | --- | --- |
| [EPIC-Kitchens-100](../datasets/multimodal/epic-kitchens-100.md) | Ego RGB + Audio | Langzeit-egozentrische Aktivitäten | 700 Stunden / 90 Küchen | Forschungslizenz |
| [Ego4D](../datasets/multimodal/ego4d.md) | Ego RGB + Stereo + Audio | 4D-Verhalten, QA, audiovisuell | 3.300 Stunden / 74 Szenarien | Nicht-kommerziell |
| [Charades](../datasets/multimodal/charades.md) | Indoor-RGB + Skript | Multi-Label-Aktionen | 9.800 Videos / 157 Labels | Öffentlich (CC BY-NC) |
| [NTU Mutual Actions](../datasets/multimodal/ntu-mutual.md) | RGB + Tiefe + Skelett | Zweipersonen-Interaktion | 26 Interaktionsklassen | Forschungslizenz |
| [ActivityNet Captions](../datasets/multimodal/activitynet-captions.md) | RGB-Video + Text | Dichte Videobeschreibung | 20k Videos / 100k Beschreibungen | Öffentlich (Forschung) |
| [How2Sign](../datasets/multimodal/how2sign.md) | RGB + Tiefe + Pose | Gebärdensprachverständnis | 80 Stunden / ASL | Öffentlich (Forschung) |

### Innovativ und Aufkommend — 8 Datensätze

| Datensatz | Modalität | Hauptaufgabe | Umfang | Zugang |
| --- | --- | --- | --- | --- |
| [BEHAVE](../datasets/emerging/behave.md) | RGB-D + Pose | Mensch-Objekt-Interaktionsmodellierung | 321 Sequenzen / 20 Personen | Öffentlich (BEHAVE-Lizenz) |
| [Motion-X](../datasets/emerging/motion-x.md) | Multi-Sensor Motion Capture | Ganzkörper- + Hand-Skelett | 10 Personen / 2M Frames | Öffentlich (Forschung) |
| [Ego-Exo4D](../datasets/emerging/ego-exo4d.md) | Ego + Exo RGB + Motion Capture | Perspektivübersetzung | 1.400 Sequenzen / 20 Stunden | Öffentlich (Forschung) |
| [HumanML3D](../datasets/emerging/humanml3d.md) | SMPL + Text | Text-zu-Bewegung-Generierung | 14k+ Bewegungssequenzen | Öffentlich (Forschung) |
| [InterHuman](../datasets/emerging/interhuman.md) | SMPL-X + Text | Zweipersonen-Interaktionsbewegung | 6.000+ Interaktionssequenzen | Öffentlich (Forschung) |
| [HOI4D](../datasets/emerging/hoi4d.md) | Ego RGB-D + Handpose | Hand-Objekt-Interaktion | 4.000+ Videoclips | Öffentlich (Forschung) |
| [FineBio](../datasets/emerging/finebio.md) | RGB + Skelett | Feinkörnige biologische Laborhandlungen | Mehrstufige Versuchsabläufe | Öffentlich (Forschung) |
| [HAA500](../datasets/emerging/haa500.md) | RGB-Video | Atomare Aktionserkennung | 10k Clips / 500 Klassen | Öffentlich |

Detaillierte Informationen finden Sie in den jeweiligen Datensatzkarten, einschließlich Download-Anleitungen, Zitierhinweisen, Baseline-Ergebnissen und bekannten Herausforderungen.

## Warum dieses Repository

- **Problemorientierte Navigation:** Datensätze nach Aufgabe oder Modalität finden – nicht nur alphabetisch sortiert.
- **Einbettung in den Forschungskontext:** Jede Datensatzkarte verlinkt auf maßgebliche Publikationen, Benchmarks und aktuelle Folgearbeiten.
- **Ausführbare Werkzeuge:** Katalog-Builder (JSON/CSV-Export), Link-Validierung, ASCII-Normalisierung.
- **Qualitätssicherung:** Beitragsvorlagen, Review-Checklisten und automatisierte CI-Prüfungen sorgen für Verlässlichkeit.

## Repository-Struktur
```
.
 datasets/               # 42 Datensatzkarten, gegliedert nach Modalität
   vision/               #   11 visuelle Datensätze
   skeleton/             #    7 Skelett-/Motion-Capture-Datensätze
   wearable/             #   10 Wearable-Sensor-Datensätze
   multimodal/           #    6 multimodale/egozentrische Datensätze
   emerging/             #    8 innovative und aufkommende Datensätze
 docs/                   # Übersichtsarbeiten, Benchmarks, Roadmap
 tools/                  # Skripte (Katalog-Builder, Link-Prüfung, ASCII-Normalisierung)
 .github/workflows/      # CI (Link-Check, Markdown-Lint)
 i18n/                   # Übersetzungen (zh, de, es, fr, ja, ko, pt, ru)
```

## Ausgewählte Publikationen und Übersichtsarbeiten
- Aggarwal & Ryoo, „Human Activity Analysis: A Review", ACM Computing Surveys, 2011.
- Lara & Labrador, „A Survey on Human Activity Recognition using Wearable Sensors", IEEE Communications Surveys, 2013.
- Li et al., „A Systematic Survey on Deep Learning for Human Activity Recognition", ACM Computing Surveys, 2022.
- Grauman et al., „Ego4D: Around the World in 2,250 Hours of Egocentric Video", CVPR 2022. (Datensatz + Benchmark)
- Pavlakos et al., „BABEL: Bodies, Actions and Behavior with English Labels", CVPR 2022.

Weiterführende Literatur finden Sie unter [`docs/surveys.md`](../docs/surveys.md).

## Anleitung zur Nutzung
1. **Datensatz finden:** Verwenden Sie die obige Taxonomie-Tabelle oder durchsuchen Sie das Verzeichnis [`datasets/`](../datasets/).
2. **Datensatzkarte lesen:** Informieren Sie sich vor dem Download über Lizenz, Aufgaben, Benchmark-Protokolle und Dateneigenschaften.
3. **Schnelles Prototyping:** Nutzen Sie die in den Karten verlinkten Tools und Ökosystem-Ressourcen, um PyTorch- / TensorFlow-Datenlader anzubinden.
4. **Katalog exportieren:** Führen Sie `python tools/catalog_builder.py --format csv --output catalog.csv` aus, um maschinenlesbare Metadaten zu erhalten.
5. **Auf dem Laufenden bleiben:** Beobachten Sie das Repository oder verfolgen Sie die Discussions – bei jedem Release fassen wir neue Datensätze und SOTA-Entwicklungen zusammen.

### Zitation
Wenn dieses Repository für Ihre Forschung oder Ihr Produkt hilfreich ist, zitieren Sie es bitte:

```bibtex
@misc{awesome_har_2025,
  title   = {Awesome Human Activity Recognition: A Curated List},
  author  = {Wenxuan Huang},
  year    = {2025},
  url     = {https://github.com/Leo-Cyberautonomy/awesome-human-activity-recognition},
  note    = {GitHub repository}
}
```

## Mitwirken
- Lesen Sie [`CONTRIBUTING.md`](../CONTRIBUTING.md) für Datensatzkarten-Vorlagen, Review-Kriterien und Stilrichtlinien.
- Verwenden Sie Issues, um neue Datensätze vorzuschlagen oder fehlerhafte Links zu melden. Wir verwenden modalitätsbezogene Labels (z. B. `modality:wearable`).
- Pull Requests durchlaufen eine Datenqualitätsprüfung und automatische Link-Validierung; Bearbeitungszeit: ca. 5–7 Tage.

## Entwicklungsplan
- Wöchentliche automatische Link-Prüfung (GitHub Actions).
- Jupyter-Einstiegs-Notebooks für Wearable- und Video-Baselines.
- Standardisiertes Datensatz-Schema (YAML) mit automatischer Validierung.
- Community-Spotlight: Vierteljährliche Zusammenfassungen neuer Datensätze und Bestenlisten-Entwicklungen.
- Langfristig: Durchsuchbare statische Website auf Basis von MkDocs.

Die vollständige Roadmap finden Sie unter [`docs/roadmap.md`](../docs/roadmap.md).

## Danksagung
Wir danken allen Datensatz-Autorinnen und -Autoren, Annotationsteams und Benchmark-Maintainern, deren Arbeit die offene Forschung im Bereich der Erkennung menschlicher Aktivitäten vorantreibt. Mit diesem leicht zugänglichen Verzeichnis möchten wir die Wirkung ihrer Beiträge verstärken.
