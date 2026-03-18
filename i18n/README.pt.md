# Awesome Reconhecimento de Atividades Humanas (Awesome Human Activity Recognition)

[中文](README.zh.md) | [English](../README.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [français](README.fr.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [**Português**](README.pt.md) | [Русский](README.ru.md)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Stars](https://img.shields.io/github/stars/Leo-Cyberautonomy/awesome-human-activity-recognition?style=social)](https://github.com/Leo-Cyberautonomy/awesome-human-activity-recognition/stargazers)
[![License](https://img.shields.io/github/license/Leo-Cyberautonomy/awesome-human-activity-recognition)](../LICENSE)
[![Datasets](https://img.shields.io/badge/datasets-42-brightgreen)](#visao-geral-por-categoria)

Um catalogo curado de **42** conjuntos de dados sobre atividade e movimento humano, abrangendo visao computacional, sensores vestiveis, captura de esqueleto, multimodal e muito mais. Cada ficha de conjunto de dados inclui modalidades, licenca, tarefas de referencia, baselines representativas, ecossistema de ferramentas e publicacoes de referencia, para ajuda-lo a iniciar rapidamente a modelagem ou a avaliacao comparativa.

- Destinado a pesquisadores de aprendizado de maquina, equipes de produto e laboratorios de ciencia do movimento.
- Apresenta tanto os conjuntos de dados mais recentes quanto os classicos que fundamentaram os benchmarks atuais.
- Acompanhado de um fluxo de contribuicao, ferramentas de validacao e um roteiro para manutencao colaborativa pela comunidade.

> Objetivo: tornar-se o recurso GitHub de referencia para conjuntos de dados de atividade humana, com a profundidade do Papers with Code, mantendo uma perspectiva "conjuntos de dados em primeiro lugar".

## Acesso rapido
- Diretorio de fichas de conjuntos de dados: [`datasets/`](../datasets/)
- Artigos de revisao e benchmarks: [`docs/surveys.md`](../docs/surveys.md)
- Panorama de benchmarks: [`docs/benchmarking.md`](../docs/benchmarking.md)
- Guia de contribuicao: [`CONTRIBUTING.md`](../CONTRIBUTING.md)
- Roteiro de automacao: [`docs/roadmap.md`](../docs/roadmap.md)

## Visao geral por categoria

### Visao (RGB / Profundidade) — 11 conjuntos de dados

| Conjunto de dados | Modalidade | Tarefa principal | Escala | Acesso |
| --- | --- | --- | --- | --- |
| [Kinetics-700](../datasets/vision/kinetics-700.md) | Video RGB | Reconhecimento de acoes, pre-treinamento | 650k clips / 700 classes | Publico (CC BY) |
| [UCF-101](../datasets/vision/ucf101.md) | Video RGB | Reconhecimento de acoes | 13k clips / 101 classes | Publico (pesquisa) |
| [HMDB-51](../datasets/vision/hmdb51.md) | Video RGB | Reconhecimento de acoes | 6800 clips / 51 classes | Publico (pesquisa) |
| [ActivityNet](../datasets/vision/activitynet.md) | Video RGB | Deteccao temporal de acoes | 20k videos / 200 classes | Publico (pesquisa) |
| [AVA](../datasets/vision/ava.md) | Video RGB | Deteccao espaco-temporal de acoes | 430 clips / 80 acoes atomicas | Publico (pesquisa) |
| [NTU RGB+D 120](../datasets/vision/ntu-rgbd-120.md) | RGB + Profundidade + Esqueleto | Reconhecimento de acoes 3D | 114k sequencias / 120 classes | Acordo de pesquisa |
| [Something-Something V2](../datasets/vision/something-something-v2.md) | Video RGB | Reconhecimento de interacoes finas | 220k clips / 174 rotulos | Publico (Apache 2.0) |
| [FineGym](../datasets/vision/finegym.md) | Video RGB | Acoes de ginastica finas | 32k segmentos / anotacoes hierarquicas | Publico (pesquisa) |
| [Moments in Time](../datasets/vision/moments-in-time.md) | Video RGB | Reconhecimento de eventos/acoes | 1M clips / 339 classes | Publico (pesquisa) |
| [Diving48](../datasets/vision/diving48.md) | Video RGB | Acoes de salto ornamental finas | 18k clips / 48 classes | Publico (pesquisa) |
| [Toyota Smarthome](../datasets/vision/toyota-smarthome.md) | RGB + Profundidade + Esqueleto | Atividades da vida diaria | 16k clips / 31 classes | Acordo de pesquisa |

### Esqueleto e captura de movimento — 7 conjuntos de dados

| Conjunto de dados | Modalidade | Tarefa principal | Escala | Acesso |
| --- | --- | --- | --- | --- |
| [NTU RGB+D 60](../datasets/skeleton/ntu-rgbd-60.md) | RGB + Profundidade + Esqueleto | Reconhecimento de acoes por esqueleto | 57k sequencias / 60 classes | Acordo de pesquisa |
| [AMASS](../datasets/skeleton/amass.md) | Pose corporal parametrizada | Geracao de movimento, estimacao de pose | 16k minutos / 344 sujeitos | Publico (licenca AMASS) |
| [Human3.6M](../datasets/skeleton/human36m.md) | Captura de movimento + RGB | Estimacao de pose, reconstrucao 3D | 3,6M quadros 3D | Licenca de pesquisa |
| [BABEL](../datasets/skeleton/babel.md) | SMPL + rotulos textuais | Alinhamento acao-linguagem | 43 horas / 3,7k sequencias | Pesquisa (nao comercial) |
| [TotalCapture](../datasets/skeleton/totalcapture.md) | Captura de movimento + multi-vista RGB + IMU | Estimacao de pose 3D, fusao | 5 sujeitos / multi-vista | Publico (CC BY) |
| [PKU-MMD](../datasets/skeleton/pku-mmd.md) | RGB + Profundidade + Esqueleto | Deteccao de acoes | 20k instancias / 51 classes | Acordo de pesquisa |
| [Skeletics-152](../datasets/skeleton/skeletics-152.md) | Esqueleto estimado | Reconhecimento de acoes em larga escala | 150k clips / 152 classes | Pesquisa |

### Sensores vestiveis — 10 conjuntos de dados

| Conjunto de dados | Modalidade | Tarefa principal | Escala | Acesso |
| --- | --- | --- | --- | --- |
| [UCI-HAR](../datasets/wearable/uci-har.md) | IMU de smartphone | Reconhecimento de atividades | 30 sujeitos / 6 atividades | Publico (CC BY) |
| [PAMAP2](../datasets/wearable/pamap2.md) | IMU + frequencia cardiaca | HAR vestivel | 9 sujeitos / 18 atividades | Publico (CC BY-SA) |
| [WISDM](../datasets/wearable/wisdm.md) | Celular + relogio | HAR, reconhecimento de gestos | 51 sujeitos / milhoes de amostras | Publico (Creative Commons) |
| [OPPORTUNITY](../datasets/wearable/opportunity.md) | Sensores vestiveis + ambientais | Reconhecimento de cenarios | 4 sujeitos / 72 canais | Publico (pesquisa) |
| [HAPT](../datasets/wearable/hapt.md) | IMU de smartphone | Atividades e transicoes posturais | 30 sujeitos / 12 atividades | Publico (CC BY) |
| [RealWorld HAR](../datasets/wearable/realworld-har.md) | IMU de celular + relogio | HAR em condicoes reais | 60 sujeitos / 15 atividades | Publico (CC BY) |
| [mHealth](../datasets/wearable/mhealth.md) | Sensores corporais + ECG | Monitoramento de saude movel | 10 sujeitos / 12 atividades | Publico (CC BY) |
| [UniMiB-SHAR](../datasets/wearable/unimib-shar.md) | Acelerometro de smartphone | Atividades diarias + deteccao de quedas | 30 sujeitos / 17 atividades | Publico |
| [Daphnet](../datasets/wearable/daphnet.md) | Acelerometro vestivel | Congelamento de marcha (Parkinson) | 10 sujeitos / 3 sensores | Publico |
| [Sussex-Huawei Locomotion](../datasets/wearable/shl.md) | Celular + relogio | Reconhecimento do modo de locomocao | 3 sujeitos / 2800+ horas | Publico |

### Multimodal / Primeira pessoa — 6 conjuntos de dados

| Conjunto de dados | Modalidade | Tarefa principal | Escala | Acesso |
| --- | --- | --- | --- | --- |
| [EPIC-Kitchens-100](../datasets/multimodal/epic-kitchens-100.md) | RGB egocentrico + audio | Comportamento egocentrico de longa duracao | 700 horas / 90 cozinhas | Licenca de pesquisa |
| [Ego4D](../datasets/multimodal/ego4d.md) | RGB egocentrico + estereo + audio | Comportamento 4D, QA, audiovisual | 3300 horas / 74 cenarios | Nao comercial |
| [Charades](../datasets/multimodal/charades.md) | RGB interno + roteiros | Acoes multi-rotulo | 9800 videos / 157 rotulos | Publico (CC BY-NC) |
| [NTU Mutual Actions](../datasets/multimodal/ntu-mutual.md) | RGB + Profundidade + Esqueleto | Interacao entre duas pessoas | 26 classes de interacao | Acordo de pesquisa |
| [ActivityNet Captions](../datasets/multimodal/activitynet-captions.md) | Video RGB + texto | Descricao densa de video | 20k videos / 100k descricoes | Publico (pesquisa) |
| [How2Sign](../datasets/multimodal/how2sign.md) | RGB + Profundidade + Pose | Compreensao de lingua de sinais | 80 horas / ASL | Publico (pesquisa) |

### Fronteiras e emergentes — 8 conjuntos de dados

| Conjunto de dados | Modalidade | Tarefa principal | Escala | Acesso |
| --- | --- | --- | --- | --- |
| [BEHAVE](../datasets/emerging/behave.md) | RGB-D + Pose | Modelagem de interacao humano-objeto | 321 sequencias / 20 sujeitos | Publico (licenca BEHAVE) |
| [Motion-X](../datasets/emerging/motion-x.md) | Captura de movimento multi-sensor | Esqueleto corpo inteiro + maos | 10 sujeitos / 2M quadros | Publico (pesquisa) |
| [Ego-Exo4D](../datasets/emerging/ego-exo4d.md) | RGB ego + exo + captura de movimento | Traducao de pontos de vista | 1400 sequencias / 20 horas | Publico (pesquisa) |
| [HumanML3D](../datasets/emerging/humanml3d.md) | SMPL + texto | Geracao de movimento a partir de texto | 14k+ sequencias de movimento | Publico (pesquisa) |
| [InterHuman](../datasets/emerging/interhuman.md) | SMPL-X + texto | Movimento de interacao entre duas pessoas | 6000+ sequencias de interacao | Publico (pesquisa) |
| [HOI4D](../datasets/emerging/hoi4d.md) | RGB-D egocentrico + pose da mao | Interacao mao-objeto | 4000+ clips de video | Publico (pesquisa) |
| [FineBio](../datasets/emerging/finebio.md) | RGB + Esqueleto | Manipulacao fina em experimentos biologicos | Protocolos experimentais multi-etapa | Publico (pesquisa) |
| [HAA500](../datasets/emerging/haa500.md) | Video RGB | Reconhecimento de acoes atomicas | 10k clips / 500 classes | Publico |

Para mais detalhes, consulte a ficha correspondente de cada conjunto de dados, incluindo metodos de download, informacoes de citacao, resultados de referencia e desafios conhecidos.

## Por que este repositorio
- **Navegacao por problema:** Busque conjuntos de dados por tarefa ou modalidade, e nao apenas por ordem alfabetica.
- **Contexto de pesquisa:** Cada ficha conecta a publicacoes de referencia, benchmarks e trabalhos mais recentes.
- **Ferramentas uteis:** Gerador de catalogo (exportacao JSON/CSV), verificacao de links, normalizacao ASCII.
- **Garantia de qualidade:** Modelos de contribuicao, listas de verificacao e CI automatizado para um catalogo confiavel e fidedigno.

## Estrutura do repositorio
```
.
 datasets/               # 42 fichas de conjuntos de dados organizadas por modalidade
   vision/               #   11 conjuntos de dados visuais
   skeleton/             #    7 conjuntos de dados de esqueleto/captura de movimento
   wearable/             #   10 conjuntos de dados de sensores vestiveis
   multimodal/           #    6 conjuntos de dados multimodais/primeira pessoa
   emerging/             #    8 conjuntos de dados de fronteiras e emergentes
 docs/                   # Revisoes, benchmarks, roteiro
 tools/                  # Scripts (gerador de catalogo, verificacao de links, normalizacao ASCII)
 .github/workflows/      # CI (verificacao de links, lint Markdown)
 i18n/                   # Traducoes (zh, de, es, fr, ja, ko, pt, ru)
```

## Artigos e revisoes selecionados
- Aggarwal & Ryoo, "Human Activity Analysis: A Review", ACM Computing Surveys, 2011.
- Lara & Labrador, "A Survey on Human Activity Recognition using Wearable Sensors", IEEE Communications Surveys, 2013.
- Li et al., "A Systematic Survey on Deep Learning for Human Activity Recognition", ACM Computing Surveys, 2022.
- Grauman et al., "Ego4D: Around the World in 2,250 Hours of Egocentric Video", CVPR 2022. (conjunto de dados + benchmark)
- Pavlakos et al., "BABEL: Bodies, Actions and Behavior with English Labels", CVPR 2022.

Para leitura complementar, consulte [`docs/surveys.md`](../docs/surveys.md).

## Como utilizar este catalogo
1. **Encontrar um conjunto de dados:** Consulte primeiro a tabela de classificacao acima ou navegue pelo diretorio [`datasets/`](../datasets/).
2. **Ler a ficha do conjunto de dados:** Antes de fazer o download, informe-se sobre a licenca, tarefas, protocolo de benchmark e caracteristicas dos dados.
3. **Prototipagem rapida:** Utilize os links para ferramentas e ecossistema em cada ficha para integrar os carregadores de dados PyTorch / TensorFlow.
4. **Gerar exportacao do catalogo:** Execute `python tools/catalog_builder.py --format csv --output catalog.csv` para obter metadados legiveis por maquina.
5. **Manter-se atualizado:** Faca Watch no repositorio ou acompanhe as Discussions; resumimos novos conjuntos de dados e avancos SOTA a cada lancamento.

### Citacao
Se este repositorio for util para sua pesquisa ou produto, por favor cite:

```bibtex
@misc{awesome_har_2025,
  title   = {Awesome Human Activity Recognition: A Curated List},
  author  = {Wenxuan Huang},
  year    = {2025},
  url     = {https://github.com/Leo-Cyberautonomy/awesome-human-activity-recognition},
  note    = {GitHub repository}
}
```

## Contribuir
- Leia [`CONTRIBUTING.md`](../CONTRIBUTING.md) para obter o modelo de ficha, criterios de avaliacao e convencoes de redacao.
- Utilize Issues para solicitar um novo conjunto de dados ou relatar um link quebrado. Usamos etiquetas por modalidade (ex.: `modality:wearable`).
- Pull Requests passam por revisao de qualidade de dados e verificacao automatizada de links, com prazo estimado de 5 a 7 dias.

## Roteiro
- Verificacao automatica semanal de links (GitHub Actions).
- Notebooks Jupyter introdutorios para baselines de sensores vestiveis e video.
- Esquema padronizado de conjuntos de dados (YAML) com validacao automatica.
- Destaque comunitario: resumo trimestral de novos conjuntos de dados e rankings.
- Objetivo de longo prazo: site estatico pesquisavel baseado em MkDocs.

Consulte o roteiro completo em [`docs/roadmap.md`](../docs/roadmap.md).

## Agradecimentos
Agradecemos a todos os autores de conjuntos de dados, equipes de anotacao e mantenedores de benchmarks que impulsionam a pesquisa aberta no campo da compreensao da atividade humana. Esperamos amplificar suas contribuicoes por meio de um catalogo facil de usar.
