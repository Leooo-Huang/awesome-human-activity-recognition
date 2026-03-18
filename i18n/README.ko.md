# Awesome 인간 활동 인식 (Awesome Human Activity Recognition)

[中文](README.zh.md) | [English](../README.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [français](README.fr.md) | [日本語](README.ja.md) | [**한국어**](README.ko.md) | [Português](README.pt.md) | [Русский](README.ru.md)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Stars](https://img.shields.io/github/stars/Leo-Cyberautonomy/awesome-human-activity-recognition?style=social)](https://github.com/Leo-Cyberautonomy/awesome-human-activity-recognition/stargazers)
[![License](https://img.shields.io/github/license/Leo-Cyberautonomy/awesome-human-activity-recognition)](../LICENSE)
[![Datasets](https://img.shields.io/badge/datasets-42-brightgreen)](#분류-개요)

비전, 웨어러블 센서, 스켈레톤 캡처, 멀티모달 등 다양한 분야를 아우르는 **42개** 인간 활동 및 동작 데이터셋의 엄선된 목록입니다. 각 데이터셋 카드에는 모달리티, 라이선스, 벤치마크 태스크, 대표 베이스라인, 도구 생태계, 그리고 주요 논문이 포함되어 있어 모델링이나 비교 평가를 빠르게 시작할 수 있습니다.

- 머신러닝 연구자, 제품 팀, 그리고 운동과학 연구실을 위해 제작되었습니다.
- 최신 데이터셋뿐만 아니라 기존 벤치마크의 기반이 되는 고전 데이터셋도 함께 수록합니다.
- 기여 워크플로, 검증 도구, 로드맵을 갖추어 커뮤니티 협업 유지가 가능합니다.

> 목표: 인간 활동 데이터셋의 권위 있는 GitHub 리소스를 구축하는 것으로, Papers with Code의 깊이를 참고하되 "데이터셋 우선" 관점을 유지합니다.

## 바로가기
- 데이터셋 카드 디렉토리: [`datasets/`](../datasets/)
- 서베이 및 벤치마크 논문: [`docs/surveys.md`](../docs/surveys.md)
- 벤치마크 스냅샷: [`docs/benchmarking.md`](../docs/benchmarking.md)
- 기여 가이드: [`CONTRIBUTING.md`](../CONTRIBUTING.md)
- 자동화 로드맵: [`docs/roadmap.md`](../docs/roadmap.md)

## 분류 개요

### 비전 (RGB / 깊이) — 11개 데이터셋

| 데이터셋 | 모달리티 | 주요 태스크 | 규모 | 접근 방식 |
| --- | --- | --- | --- | --- |
| [Kinetics-700](../datasets/vision/kinetics-700.md) | RGB 비디오 | 행동 인식, 사전학습 | 65만 클립 / 700 클래스 | 공개 (CC BY) |
| [UCF-101](../datasets/vision/ucf101.md) | RGB 비디오 | 행동 인식 | 1.3만 클립 / 101 클래스 | 공개 (연구용) |
| [HMDB-51](../datasets/vision/hmdb51.md) | RGB 비디오 | 행동 인식 | 6800 클립 / 51 클래스 | 공개 (연구용) |
| [ActivityNet](../datasets/vision/activitynet.md) | RGB 비디오 | 시간적 행동 탐지 | 2만 비디오 / 200 클래스 | 공개 (연구용) |
| [AVA](../datasets/vision/ava.md) | RGB 비디오 | 시공간 행동 탐지 | 430 클립 / 80 원자 행동 | 공개 (연구용) |
| [NTU RGB+D 120](../datasets/vision/ntu-rgbd-120.md) | RGB + 깊이 + 스켈레톤 | 3D 행동 인식 | 11.4만 시퀀스 / 120 클래스 | 연구 협약 |
| [Something-Something V2](../datasets/vision/something-something-v2.md) | RGB 비디오 | 세밀한 상호작용 인식 | 22만 클립 / 174 레이블 | 공개 (Apache 2.0) |
| [FineGym](../datasets/vision/finegym.md) | RGB 비디오 | 세밀한 체조 동작 | 3.2만 세그먼트 / 계층적 주석 | 공개 (연구용) |
| [Moments in Time](../datasets/vision/moments-in-time.md) | RGB 비디오 | 이벤트/행동 인식 | 100만 클립 / 339 클래스 | 공개 (연구용) |
| [Diving48](../datasets/vision/diving48.md) | RGB 비디오 | 세밀한 다이빙 동작 | 1.8만 클립 / 48 클래스 | 공개 (연구용) |
| [Toyota Smarthome](../datasets/vision/toyota-smarthome.md) | RGB + 깊이 + 스켈레톤 | 일상생활 활동 | 1.6만 클립 / 31 클래스 | 연구 협약 |

### 스켈레톤 및 모션 캡처 — 7개 데이터셋

| 데이터셋 | 모달리티 | 주요 태스크 | 규모 | 접근 방식 |
| --- | --- | --- | --- | --- |
| [NTU RGB+D 60](../datasets/skeleton/ntu-rgbd-60.md) | RGB + 깊이 + 스켈레톤 | 스켈레톤 행동 인식 | 5.7만 시퀀스 / 60 클래스 | 연구 협약 |
| [AMASS](../datasets/skeleton/amass.md) | 파라메트릭 인체 자세 | 모션 생성, 자세 추정 | 1.6만 분 / 344 피험자 | 공개 (AMASS 라이선스) |
| [Human3.6M](../datasets/skeleton/human36m.md) | 모션 캡처 + RGB | 자세 추정, 3D 복원 | 360만 프레임 3D 데이터 | 연구 라이선스 |
| [BABEL](../datasets/skeleton/babel.md) | SMPL + 텍스트 레이블 | 모션-언어 정렬 | 43시간 / 3.7k 시퀀스 | 연구용 (비상업) |
| [TotalCapture](../datasets/skeleton/totalcapture.md) | 모션 캡처 + 다시점 RGB + IMU | 3D 자세 추정, 융합 | 5명 / 다시점 | 공개 (CC BY) |
| [PKU-MMD](../datasets/skeleton/pku-mmd.md) | RGB + 깊이 + 스켈레톤 | 행동 탐지 | 2만 인스턴스 / 51 클래스 | 연구 협약 |
| [Skeletics-152](../datasets/skeleton/skeletics-152.md) | 추정 스켈레톤 | 대규모 스켈레톤 행동 | 15만 클립 / 152 클래스 | 연구용 |

### 웨어러블 센서 — 10개 데이터셋

| 데이터셋 | 모달리티 | 주요 태스크 | 규모 | 접근 방식 |
| --- | --- | --- | --- | --- |
| [UCI-HAR](../datasets/wearable/uci-har.md) | 스마트폰 IMU | 활동 인식 | 30명 / 6종 활동 | 공개 (CC BY) |
| [PAMAP2](../datasets/wearable/pamap2.md) | IMU + 심박수 | 웨어러블 HAR | 9명 / 18종 활동 | 공개 (CC BY-SA) |
| [WISDM](../datasets/wearable/wisdm.md) | 스마트폰 + 스마트워치 | HAR, 제스처 인식 | 51명 / 백만 단위 샘플 | 공개 (크리에이티브 커먼즈) |
| [OPPORTUNITY](../datasets/wearable/opportunity.md) | 웨어러블 + 환경 센서 | 상황 인식 | 4명 / 72 채널 | 공개 (연구용) |
| [HAPT](../datasets/wearable/hapt.md) | 스마트폰 IMU | 활동 및 자세 전환 | 30명 / 12종 활동 | 공개 (CC BY) |
| [RealWorld HAR](../datasets/wearable/realworld-har.md) | 스마트폰 + 스마트워치 IMU | 실환경 HAR | 60명 / 15종 활동 | 공개 (CC BY) |
| [mHealth](../datasets/wearable/mhealth.md) | 체표 센서 + ECG | 모바일 건강 모니터링 | 10명 / 12종 활동 | 공개 (CC BY) |
| [UniMiB-SHAR](../datasets/wearable/unimib-shar.md) | 스마트폰 가속도계 | 일상 활동 + 낙상 탐지 | 30명 / 17종 활동 | 공개 |
| [Daphnet](../datasets/wearable/daphnet.md) | 웨어러블 가속도계 | 보행 동결 (파킨슨) | 10명 / 3 센서 | 공개 |
| [Sussex-Huawei Locomotion](../datasets/wearable/shl.md) | 스마트폰 + 스마트워치 | 이동 모드 인식 | 3명 / 2800시간 이상 | 공개 |

### 멀티모달 / 1인칭 시점 — 6개 데이터셋

| 데이터셋 | 모달리티 | 주요 태스크 | 규모 | 접근 방식 |
| --- | --- | --- | --- | --- |
| [EPIC-Kitchens-100](../datasets/multimodal/epic-kitchens-100.md) | Ego RGB + 오디오 | 장시간 자기중심 행동 | 700시간 / 90 주방 | 연구 라이선스 |
| [Ego4D](../datasets/multimodal/ego4d.md) | Ego RGB + 스테레오 + 오디오 | 4D 행동, QA, 시청각 | 3300시간 / 74 시나리오 | 비상업용 |
| [Charades](../datasets/multimodal/charades.md) | 실내 RGB + 스크립트 | 다중 레이블 행동 | 9800 비디오 / 157 레이블 | 공개 (CC BY-NC) |
| [NTU 상호작용 행동](../datasets/multimodal/ntu-mutual.md) | RGB + 깊이 + 스켈레톤 | 2인 상호작용 | 26종 상호작용 클래스 | 연구 협약 |
| [ActivityNet Captions](../datasets/multimodal/activitynet-captions.md) | RGB 비디오 + 텍스트 | 밀집 비디오 캡셔닝 | 2만 비디오 / 10만 캡션 | 공개 (연구용) |
| [How2Sign](../datasets/multimodal/how2sign.md) | RGB + 깊이 + 자세 | 수어 이해 | 80시간 / ASL | 공개 (연구용) |

### 최신 및 신흥 — 8개 데이터셋

| 데이터셋 | 모달리티 | 주요 태스크 | 규모 | 접근 방식 |
| --- | --- | --- | --- | --- |
| [BEHAVE](../datasets/emerging/behave.md) | RGB-D + 자세 | 인간-객체 상호작용 모델링 | 321 시퀀스 / 20명 | 공개 (BEHAVE 라이선스) |
| [Motion-X](../datasets/emerging/motion-x.md) | 다중 센서 모션 캡처 | 전신+손 스켈레톤 | 10명 / 200만 프레임 | 공개 (연구용) |
| [Ego-Exo4D](../datasets/emerging/ego-exo4d.md) | Ego + Exo RGB + 모션 캡처 | 시점 간 변환 | 1400 시퀀스 / 20시간 | 공개 (연구용) |
| [HumanML3D](../datasets/emerging/humanml3d.md) | SMPL + 텍스트 | 텍스트-모션 생성 | 1.4만+ 모션 시퀀스 | 공개 (연구용) |
| [InterHuman](../datasets/emerging/interhuman.md) | SMPL-X + 텍스트 | 2인 상호작용 모션 | 6000+ 상호작용 시퀀스 | 공개 (연구용) |
| [HOI4D](../datasets/emerging/hoi4d.md) | Ego RGB-D + 손 자세 | 손-객체 상호작용 | 4000+ 비디오 클립 | 공개 (연구용) |
| [FineBio](../datasets/emerging/finebio.md) | RGB + 스켈레톤 | 세밀한 생물학 실험 조작 | 다단계 실험 프로세스 | 공개 (연구용) |
| [HAA500](../datasets/emerging/haa500.md) | RGB 비디오 | 원자 행동 인식 | 1만 클립 / 500 클래스 | 공개 |

자세한 정보는 각 데이터셋 카드를 참조하십시오. 다운로드 방법, 인용 정보, 베이스라인 결과 및 알려진 과제가 포함되어 있습니다.

## 이 저장소를 만든 이유
- **문제 중심 탐색:** 단순 알파벳순이 아니라 태스크나 모달리티 기준으로 데이터셋을 검색할 수 있습니다.
- **연구 맥락 통합:** 각 데이터셋 카드에 주요 논문, 벤치마크, 최신 후속 연구가 링크되어 있습니다.
- **실행 가능한 도구:** 카탈로그 빌더 (JSON/CSV 내보내기), 링크 검증, ASCII 정규화를 제공합니다.
- **품질 보증:** 기여 템플릿, 리뷰 체크리스트, 자동화 CI 검증으로 카탈로그의 신뢰성을 보장합니다.

## 저장소 구조
```
.
 datasets/               # 모달리티별로 분류된 42개 데이터셋 카드
   vision/               #   11개 비전 데이터셋
   skeleton/             #    7개 스켈레톤/모션 캡처 데이터셋
   wearable/             #   10개 웨어러블 센서 데이터셋
   multimodal/           #    6개 멀티모달/1인칭 시점 데이터셋
   emerging/             #    8개 최신 및 신흥 데이터셋
 docs/                   # 서베이, 벤치마크, 로드맵
 tools/                  # 스크립트 (카탈로그 빌더, 링크 검증, ASCII 정규화)
 .github/workflows/      # CI (링크 검사, Markdown 린트)
 i18n/                   # 번역 (zh, de, es, fr, ja, ko, pt, ru)
```

## 주요 논문 및 서베이
- Aggarwal & Ryoo, "Human Activity Analysis: A Review", ACM Computing Surveys, 2011.
- Lara & Labrador, "A Survey on Human Activity Recognition using Wearable Sensors", IEEE Communications Surveys, 2013.
- Li 등, "A Systematic Survey on Deep Learning for Human Activity Recognition", ACM Computing Surveys, 2022.
- Grauman 등, "Ego4D: Around the World in 2,250 Hours of Egocentric Video", CVPR 2022. (데이터셋 + 벤치마크)
- Pavlakos 등, "BABEL: Bodies, Actions and Behavior with English Labels", CVPR 2022.

추가 자료는 [`docs/surveys.md`](../docs/surveys.md)를 참조하십시오.

## 카탈로그 사용 방법
1. **데이터셋 찾기:** 상단 분류 표를 확인하거나 [`datasets/`](../datasets/) 디렉토리를 탐색하십시오.
2. **데이터셋 카드 읽기:** 다운로드 전에 라이선스, 태스크, 벤치마크 프로토콜 및 데이터 특성을 파악하십시오.
3. **빠른 프로토타이핑:** 각 카드에 포함된 도구 및 생태계 링크를 활용하여 PyTorch / TensorFlow 데이터 로더에 연결하십시오.
4. **카탈로그 내보내기:** `python tools/catalog_builder.py --format csv --output catalog.csv`를 실행하여 기계 판독 가능한 메타데이터를 생성하십시오.
5. **최신 동향 파악:** 저장소를 Watch하거나 Discussions를 구독하면 새로운 데이터셋 추가 및 SOTA 동향을 릴리스마다 요약해 드립니다.

### 인용
본 저장소가 연구나 제품에 도움이 되었다면 다음과 같이 인용해 주십시오:

```bibtex
@misc{awesome_har_2025,
  title   = {Awesome Human Activity Recognition: A Curated List},
  author  = {Wenxuan Huang},
  year    = {2025},
  url     = {https://github.com/Leo-Cyberautonomy/awesome-human-activity-recognition},
  note    = {GitHub repository}
}
```

## 기여 방법
- [`CONTRIBUTING.md`](../CONTRIBUTING.md)를 읽고 데이터셋 카드 템플릿, 리뷰 기준, 작성 규범을 확인하십시오.
- Issue를 통해 새로운 데이터셋을 요청하거나 깨진 링크를 신고할 수 있습니다. 모달리티별 레이블 (예: `modality:wearable`)을 사용합니다.
- Pull Request는 데이터 품질 리뷰와 자동화 링크 검증을 거치며, 5-7일 이내에 처리하는 것을 목표로 합니다.

## 로드맵
- 주간 자동 링크 검증 (GitHub Actions).
- 웨어러블 및 비디오 베이스라인을 위한 Jupyter 입문 노트북.
- 표준화된 데이터셋 스키마 (YAML) 및 자동 검증.
- 커뮤니티 하이라이트: 분기별 신규 데이터셋 및 리더보드 동향 요약 발행.
- 장기 목표: MkDocs 기반의 검색 가능한 정적 사이트 구축.

전체 로드맵은 [`docs/roadmap.md`](../docs/roadmap.md)를 참조하십시오.

## 감사의 말
모든 데이터셋 저자, 주석 팀, 벤치마크 관리자분들께 감사드립니다. 이분들이 인간 활동 이해 분야의 오픈 연구를 이끌어 왔습니다. 우리는 사용하기 쉬운 카탈로그를 통해 그 성과를 널리 알리고자 합니다.
