# Awesome Reconocimiento de Actividad Humana (Awesome Human Activity Recognition)

[中文](README.zh.md) | [English](../README.md) | [Deutsch](README.de.md) | [**Español**](README.es.md) | [français](README.fr.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Português](README.pt.md) | [Русский](README.ru.md)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Stars](https://img.shields.io/github/stars/Leo-Cyberautonomy/awesome-human-activity-recognition?style=social)](https://github.com/Leo-Cyberautonomy/awesome-human-activity-recognition/stargazers)
[![License](https://img.shields.io/github/license/Leo-Cyberautonomy/awesome-human-activity-recognition)](../LICENSE)
[![Datasets](https://img.shields.io/badge/datasets-42-brightgreen)](#panorama-por-categorías)

Un catálogo curado de **42** conjuntos de datos de actividad y movimiento humano que abarca visión, sensores vestibles, captura de esqueleto, multimodalidad y más. Cada ficha de conjunto de datos incluye modalidad, licencia, tareas de referencia, líneas base representativas, ecosistema de herramientas y publicaciones clave, para que puedas comenzar a modelar o realizar evaluaciones comparativas rápidamente.

- Dirigido a investigadores en aprendizaje automático, equipos de producto y laboratorios de ciencias del movimiento.
- Presenta tanto los conjuntos de datos más recientes como los clásicos que fundamentan los benchmarks existentes.
- Incluye flujos de trabajo de contribución, herramientas de validación y una hoja de ruta para el mantenimiento colaborativo por parte de la comunidad.

> Objetivo: crear el recurso de referencia en GitHub para conjuntos de datos de actividad humana, con la profundidad de Papers with Code y una perspectiva centrada en los datos.

## Acceso rápido
- Directorio de fichas de conjuntos de datos: [`datasets/`](../datasets/)
- Artículos de revisión y benchmarks: [`docs/surveys.md`](../docs/surveys.md)
- Resumen de benchmarks: [`docs/benchmarking.md`](../docs/benchmarking.md)
- Guía de contribución: [`CONTRIBUTING.md`](../CONTRIBUTING.md)
- Hoja de ruta de automatización: [`docs/roadmap.md`](../docs/roadmap.md)

## Panorama por categorías

### Visión (RGB / Profundidad) — 11 conjuntos de datos

| Conjunto de datos | Modalidad | Tarea principal | Escala | Acceso |
| --- | --- | --- | --- | --- |
| [Kinetics-700](../datasets/vision/kinetics-700.md) | Vídeo RGB | Reconocimiento de acciones, preentrenamiento | 650k clips / 700 clases | Público (CC BY) |
| [UCF-101](../datasets/vision/ucf101.md) | Vídeo RGB | Reconocimiento de acciones | 13k clips / 101 clases | Público (investigación) |
| [HMDB-51](../datasets/vision/hmdb51.md) | Vídeo RGB | Reconocimiento de acciones | 6800 clips / 51 clases | Público (investigación) |
| [ActivityNet](../datasets/vision/activitynet.md) | Vídeo RGB | Detección temporal de acciones | 20k vídeos / 200 clases | Público (investigación) |
| [AVA](../datasets/vision/ava.md) | Vídeo RGB | Detección espacio-temporal de acciones | 430 clips / 80 acciones atómicas | Público (investigación) |
| [NTU RGB+D 120](../datasets/vision/ntu-rgbd-120.md) | RGB + Profundidad + Esqueleto | Reconocimiento de acciones 3D | 114k secuencias / 120 clases | Acuerdo de investigación |
| [Something-Something V2](../datasets/vision/something-something-v2.md) | Vídeo RGB | Reconocimiento de interacciones finas | 220k clips / 174 etiquetas | Público (Apache 2.0) |
| [FineGym](../datasets/vision/finegym.md) | Vídeo RGB | Acciones de gimnasia de grano fino | 32k segmentos / anotación jerárquica | Público (investigación) |
| [Moments in Time](../datasets/vision/moments-in-time.md) | Vídeo RGB | Reconocimiento de eventos/acciones | 1M clips / 339 clases | Público (investigación) |
| [Diving48](../datasets/vision/diving48.md) | Vídeo RGB | Acciones de clavados de grano fino | 18k clips / 48 clases | Público (investigación) |
| [Toyota Smarthome](../datasets/vision/toyota-smarthome.md) | RGB + Profundidad + Esqueleto | Actividades de la vida diaria | 16k clips / 31 clases | Acuerdo de investigación |

### Esqueleto y captura de movimiento — 7 conjuntos de datos

| Conjunto de datos | Modalidad | Tarea principal | Escala | Acceso |
| --- | --- | --- | --- | --- |
| [NTU RGB+D 60](../datasets/skeleton/ntu-rgbd-60.md) | RGB + Profundidad + Esqueleto | Reconocimiento de acciones por esqueleto | 57k secuencias / 60 clases | Acuerdo de investigación |
| [AMASS](../datasets/skeleton/amass.md) | Pose corporal parametrizada | Generación de movimiento, estimación de pose | 16k minutos / 344 sujetos | Público (licencia AMASS) |
| [Human3.6M](../datasets/skeleton/human36m.md) | Captura de movimiento + RGB | Estimación de pose, reconstrucción 3D | 3,6M fotogramas 3D | Licencia de investigación |
| [BABEL](../datasets/skeleton/babel.md) | SMPL + etiquetas textuales | Alineación movimiento-lenguaje | 43 horas / 3,7k secuencias | Investigación (no comercial) |
| [TotalCapture](../datasets/skeleton/totalcapture.md) | Captura de movimiento + RGB multivista + IMU | Estimación de pose 3D, fusión | 5 sujetos / multivista | Público (CC BY) |
| [PKU-MMD](../datasets/skeleton/pku-mmd.md) | RGB + Profundidad + Esqueleto | Detección de acciones | 20k instancias / 51 clases | Acuerdo de investigación |
| [Skeletics-152](../datasets/skeleton/skeletics-152.md) | Esqueleto estimado | Acciones por esqueleto a gran escala | 150k clips / 152 clases | Investigación |

### Sensores vestibles — 10 conjuntos de datos

| Conjunto de datos | Modalidad | Tarea principal | Escala | Acceso |
| --- | --- | --- | --- | --- |
| [UCI-HAR](../datasets/wearable/uci-har.md) | IMU de teléfono inteligente | Reconocimiento de actividad | 30 sujetos / 6 actividades | Público (CC BY) |
| [PAMAP2](../datasets/wearable/pamap2.md) | IMU + frecuencia cardíaca | HAR vestible | 9 sujetos / 18 actividades | Público (CC BY-SA) |
| [WISDM](../datasets/wearable/wisdm.md) | Teléfono + reloj | HAR, reconocimiento de gestos | 51 sujetos / millones de muestras | Público (Creative Commons) |
| [OPPORTUNITY](../datasets/wearable/opportunity.md) | Vestible + sensores ambientales | Reconocimiento de escenarios | 4 sujetos / 72 canales | Público (investigación) |
| [HAPT](../datasets/wearable/hapt.md) | IMU de teléfono inteligente | Actividad y transiciones posturales | 30 sujetos / 12 actividades | Público (CC BY) |
| [RealWorld HAR](../datasets/wearable/realworld-har.md) | IMU de teléfono + reloj | HAR en entorno real | 60 sujetos / 15 actividades | Público (CC BY) |
| [mHealth](../datasets/wearable/mhealth.md) | Sensores corporales + ECG | Monitorización de salud móvil | 10 sujetos / 12 actividades | Público (CC BY) |
| [UniMiB-SHAR](../datasets/wearable/unimib-shar.md) | Acelerómetro de teléfono | Actividades diarias + detección de caídas | 30 sujetos / 17 actividades | Público |
| [Daphnet](../datasets/wearable/daphnet.md) | Acelerómetros vestibles | Congelación de la marcha (Parkinson) | 10 sujetos / 3 sensores | Público |
| [Sussex-Huawei Locomotion](../datasets/wearable/shl.md) | Teléfono + reloj | Reconocimiento de modos de locomoción | 3 sujetos / 2800+ horas | Público |

### Multimodal / Primera persona — 6 conjuntos de datos

| Conjunto de datos | Modalidad | Tarea principal | Escala | Acceso |
| --- | --- | --- | --- | --- |
| [EPIC-Kitchens-100](../datasets/multimodal/epic-kitchens-100.md) | Ego RGB + Audio | Comportamiento egocéntrico prolongado | 700 horas / 90 cocinas | Licencia de investigación |
| [Ego4D](../datasets/multimodal/ego4d.md) | Ego RGB + Estéreo + Audio | Comportamiento 4D, QA, audiovisual | 3300 horas / 74 escenarios | No comercial |
| [Charades](../datasets/multimodal/charades.md) | RGB interior + guion | Acciones multietiqueta | 9800 vídeos / 157 etiquetas | Público (CC BY-NC) |
| [NTU Mutual Actions](../datasets/multimodal/ntu-mutual.md) | RGB + Profundidad + Esqueleto | Interacción entre dos personas | 26 clases de interacción | Acuerdo de investigación |
| [ActivityNet Captions](../datasets/multimodal/activitynet-captions.md) | Vídeo RGB + Texto | Descripción densa de vídeo | 20k vídeos / 100k descripciones | Público (investigación) |
| [How2Sign](../datasets/multimodal/how2sign.md) | RGB + Profundidad + Pose | Comprensión de lengua de señas | 80 horas / ASL | Público (investigación) |

### Frontera y emergentes — 8 conjuntos de datos

| Conjunto de datos | Modalidad | Tarea principal | Escala | Acceso |
| --- | --- | --- | --- | --- |
| [BEHAVE](../datasets/emerging/behave.md) | RGB-D + Pose | Modelado de interacción persona-objeto | 321 secuencias / 20 sujetos | Público (licencia BEHAVE) |
| [Motion-X](../datasets/emerging/motion-x.md) | Captura de movimiento multisensor | Esqueleto de cuerpo completo + manos | 10 sujetos / 2M fotogramas | Público (investigación) |
| [Ego-Exo4D](../datasets/emerging/ego-exo4d.md) | Ego + Exo RGB + Captura de movimiento | Traducción entre perspectivas | 1400 secuencias / 20 horas | Público (investigación) |
| [HumanML3D](../datasets/emerging/humanml3d.md) | SMPL + Texto | Generación de movimiento a partir de texto | 14k+ secuencias de movimiento | Público (investigación) |
| [InterHuman](../datasets/emerging/interhuman.md) | SMPL-X + Texto | Movimiento de interacción entre dos personas | 6000+ secuencias de interacción | Público (investigación) |
| [HOI4D](../datasets/emerging/hoi4d.md) | Ego RGB-D + Pose de mano | Interacción mano-objeto | 4000+ clips de vídeo | Público (investigación) |
| [FineBio](../datasets/emerging/finebio.md) | RGB + Esqueleto | Operaciones finas de laboratorio biológico | Flujos de trabajo experimentales de múltiples pasos | Público (investigación) |
| [HAA500](../datasets/emerging/haa500.md) | Vídeo RGB | Reconocimiento de acciones atómicas | 10k clips / 500 clases | Público |

Para información detallada, consulte la ficha correspondiente de cada conjunto de datos, que incluye instrucciones de descarga, información de citación, resultados de línea base y desafíos conocidos.

## ¿Por qué este repositorio?
- **Navegación orientada al problema:** Busque conjuntos de datos por tarea o modalidad, no solo por orden alfabético.
- **Contexto investigador:** Cada ficha enlaza a publicaciones clave, benchmarks y trabajos de seguimiento recientes.
- **Herramientas ejecutables:** Constructor de catálogo (exportación JSON/CSV), validación de enlaces y normalización ASCII.
- **Garantía de calidad:** Plantillas de contribución, listas de revisión y validación automatizada por CI mantienen el catálogo fiable y actualizado.

## Estructura del repositorio
```
.
 datasets/               # 42 fichas de conjuntos de datos organizadas por modalidad
   vision/               #   11 conjuntos de datos de visión
   skeleton/             #    7 conjuntos de datos de esqueleto/captura de movimiento
   wearable/             #   10 conjuntos de datos de sensores vestibles
   multimodal/           #    6 conjuntos de datos multimodales/primera persona
   emerging/             #    8 conjuntos de datos de frontera y emergentes
 docs/                   # Revisiones, benchmarks, hoja de ruta
 tools/                  # Scripts (constructor de catálogo, validación de enlaces, normalización ASCII)
 .github/workflows/      # CI (verificación de enlaces, lint de Markdown)
 i18n/                   # Traducciones (zh, de, es, fr, ja, ko, pt, ru)
```

## Publicaciones y revisiones destacadas
- Aggarwal y Ryoo, «Human Activity Analysis: A Review», ACM Computing Surveys, 2011.
- Lara y Labrador, «A Survey on Human Activity Recognition using Wearable Sensors», IEEE Communications Surveys, 2013.
- Li et al., «A Systematic Survey on Deep Learning for Human Activity Recognition», ACM Computing Surveys, 2022.
- Grauman et al., «Ego4D: Around the World in 2,250 Hours of Egocentric Video», CVPR 2022. (Conjunto de datos + benchmark)
- Pavlakos et al., «BABEL: Bodies, Actions and Behavior with English Labels», CVPR 2022.

Para más lecturas, consulte [`docs/surveys.md`](../docs/surveys.md).

## Cómo utilizar este catálogo
1. **Localice un conjunto de datos:** Consulte la tabla de categorías anterior o navegue por el directorio [`datasets/`](../datasets/).
2. **Lea la ficha del conjunto de datos:** Antes de descargar, infórmese sobre la licencia, las tareas, el protocolo de benchmark y las características de los datos.
3. **Prototipado rápido:** Utilice los enlaces a herramientas y ecosistema de cada ficha para conectar con cargadores de datos de PyTorch / TensorFlow.
4. **Genere una exportación del catálogo:** Ejecute `python tools/catalog_builder.py --format csv --output catalog.csv` para obtener metadatos en formato legible por máquina.
5. **Manténgase al día:** Haga Watch en el repositorio o siga las Discussions; resumimos los nuevos conjuntos de datos y las novedades del estado del arte en cada versión.

### Citación
Si este repositorio ha sido útil para su investigación o producto, por favor cite:

```bibtex
@misc{awesome_har_2025,
  title   = {Awesome Human Activity Recognition: A Curated List},
  author  = {Wenxuan Huang},
  year    = {2025},
  url     = {https://github.com/Leo-Cyberautonomy/awesome-human-activity-recognition},
  note    = {GitHub repository}
}
```

## Cómo contribuir
- Lea [`CONTRIBUTING.md`](../CONTRIBUTING.md) para obtener la plantilla de ficha de conjunto de datos, los criterios de revisión y las convenciones de redacción.
- Utilice Issues para solicitar nuevos conjuntos de datos o reportar enlaces rotos. Usamos etiquetas por modalidad (p. ej., `modality:wearable`).
- Los Pull Requests pasarán por una revisión de calidad de datos y validación automatizada de enlaces, con el objetivo de completarse en 5-7 días.

## Hoja de ruta
- Validación automática semanal de enlaces (GitHub Actions).
- Notebooks Jupyter introductorios para líneas base de sensores vestibles y vídeo.
- Esquema estandarizado de conjuntos de datos (YAML) con validación automática.
- Enfoque comunitario: resumen trimestral de nuevos conjuntos de datos y novedades en tablas de clasificación.
- Objetivo a largo plazo: sitio estático con búsqueda basado en MkDocs.

Consulte la hoja de ruta completa en [`docs/roadmap.md`](../docs/roadmap.md).

## Agradecimientos
Agradecemos a todos los autores de conjuntos de datos, equipos de anotación y mantenedores de benchmarks que impulsan la investigación abierta en el campo de la comprensión de la actividad humana. Esperamos amplificar su impacto a través de un catálogo accesible y fácil de usar.
