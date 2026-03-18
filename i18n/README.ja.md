# Awesome 人間行動認識（Awesome Human Activity Recognition）

[中文](README.zh.md) | [English](../README.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [français](README.fr.md) | [**日本語**](README.ja.md) | [한국어](README.ko.md) | [Português](README.pt.md) | [Русский](README.ru.md)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Stars](https://img.shields.io/github/stars/Leo-Cyberautonomy/awesome-human-activity-recognition?style=social)](https://github.com/Leo-Cyberautonomy/awesome-human-activity-recognition/stargazers)
[![License](https://img.shields.io/github/license/Leo-Cyberautonomy/awesome-human-activity-recognition)](../LICENSE)
[![Datasets](https://img.shields.io/badge/datasets-42-brightgreen)](#分類概要)

視覚、ウェアラブルセンサ、骨格キャプチャ、マルチモーダルなど多岐にわたる **42 個**の人間行動・動作データセットを厳選したカタログです。各データセットカードにはモダリティ、ライセンス、ベンチマークタスク、代表的なベースライン、ツールエコシステム、および主要論文が記載されており、モデリングや比較評価を迅速に開始できます。

- 機械学習研究者、プロダクトチーム、運動科学研究室を対象としています。
- 最先端のデータセットだけでなく、既存のベンチマークの基盤となった古典的なデータセットも収録しています。
- コントリビューションワークフロー、検証ツール、ロードマップを備え、コミュニティによる共同メンテナンスを支援します。

> 目標：Papers with Code の深度を参考にしつつ、「データセットファースト」の視点を維持した、人間行動データセットの権威的な GitHub リソースを構築すること。

## クイックリンク
- データセットカード一覧：[`datasets/`](../datasets/)
- サーベイ・ベンチマーク論文：[`docs/surveys.md`](../docs/surveys.md)
- ベンチマークスナップショット：[`docs/benchmarking.md`](../docs/benchmarking.md)
- コントリビューションガイド：[`CONTRIBUTING.md`](../CONTRIBUTING.md)
- 自動化ロードマップ：[`docs/roadmap.md`](../docs/roadmap.md)

## 分類概要

### 視覚（RGB／深度）— 11 データセット

| データセット | モダリティ | 主要タスク | 規模 | 入手方法 |
| --- | --- | --- | --- | --- |
| [Kinetics-700](../datasets/vision/kinetics-700.md) | RGB 動画 | 行動認識、事前学習 | 65 万クリップ / 700 クラス | 公開 (CC BY) |
| [UCF-101](../datasets/vision/ucf101.md) | RGB 動画 | 行動認識 | 1.3 万クリップ / 101 クラス | 公開（研究用） |
| [HMDB-51](../datasets/vision/hmdb51.md) | RGB 動画 | 行動認識 | 6800 クリップ / 51 クラス | 公開（研究用） |
| [ActivityNet](../datasets/vision/activitynet.md) | RGB 動画 | 時間的行動検出 | 2 万動画 / 200 クラス | 公開（研究用） |
| [AVA](../datasets/vision/ava.md) | RGB 動画 | 時空間行動検出 | 430 クリップ / 80 アトミック行動 | 公開（研究用） |
| [NTU RGB+D 120](../datasets/vision/ntu-rgbd-120.md) | RGB + 深度 + 骨格 | 3D 行動認識 | 11.4 万シーケンス / 120 クラス | 研究用契約 |
| [Something-Something V2](../datasets/vision/something-something-v2.md) | RGB 動画 | 細粒度インタラクション認識 | 22 万クリップ / 174 ラベル | 公開 (Apache 2.0) |
| [FineGym](../datasets/vision/finegym.md) | RGB 動画 | 細粒度体操動作 | 3.2 万セグメント / 階層アノテーション | 公開（研究用） |
| [Moments in Time](../datasets/vision/moments-in-time.md) | RGB 動画 | イベント／行動認識 | 100 万クリップ / 339 クラス | 公開（研究用） |
| [Diving48](../datasets/vision/diving48.md) | RGB 動画 | 細粒度飛び込み動作 | 1.8 万クリップ / 48 クラス | 公開（研究用） |
| [Toyota Smarthome](../datasets/vision/toyota-smarthome.md) | RGB + 深度 + 骨格 | 日常生活行動 | 1.6 万クリップ / 31 クラス | 研究用契約 |

### 骨格・モーションキャプチャ — 7 データセット

| データセット | モダリティ | 主要タスク | 規模 | 入手方法 |
| --- | --- | --- | --- | --- |
| [NTU RGB+D 60](../datasets/skeleton/ntu-rgbd-60.md) | RGB + 深度 + 骨格 | 骨格行動認識 | 5.7 万シーケンス / 60 クラス | 研究用契約 |
| [AMASS](../datasets/skeleton/amass.md) | パラメトリック人体姿勢 | 動作生成、姿勢推定 | 1.6 万分 / 344 被験者 | 公開 (AMASS ライセンス) |
| [Human3.6M](../datasets/skeleton/human36m.md) | モーキャプ + RGB | 姿勢推定、3D 再構成 | 360 万フレーム 3D データ | 研究用ライセンス |
| [BABEL](../datasets/skeleton/babel.md) | SMPL + テキストラベル | 動作-言語アライメント | 43 時間 / 3.7k シーケンス | 研究用（非商用） |
| [TotalCapture](../datasets/skeleton/totalcapture.md) | モーキャプ + 多視点 RGB + IMU | 3D 姿勢推定、融合 | 5 名 / 多視点 | 公開 (CC BY) |
| [PKU-MMD](../datasets/skeleton/pku-mmd.md) | RGB + 深度 + 骨格 | 行動検出 | 2 万インスタンス / 51 クラス | 研究用契約 |
| [Skeletics-152](../datasets/skeleton/skeletics-152.md) | 推定骨格 | 大規模骨格行動 | 15 万クリップ / 152 クラス | 研究用 |

### ウェアラブルセンサ — 10 データセット

| データセット | モダリティ | 主要タスク | 規模 | 入手方法 |
| --- | --- | --- | --- | --- |
| [UCI-HAR](../datasets/wearable/uci-har.md) | スマートフォン IMU | 行動認識 | 30 名 / 6 行動 | 公開 (CC BY) |
| [PAMAP2](../datasets/wearable/pamap2.md) | IMU + 心拍 | ウェアラブル HAR | 9 名 / 18 行動 | 公開 (CC BY-SA) |
| [WISDM](../datasets/wearable/wisdm.md) | スマートフォン + スマートウォッチ | HAR、ジェスチャー認識 | 51 名 / 百万サンプル超 | 公開（クリエイティブ・コモンズ） |
| [OPPORTUNITY](../datasets/wearable/opportunity.md) | ウェアラブル + 環境センサ | シーン認識 | 4 名 / 72 チャネル | 公開（研究用） |
| [HAPT](../datasets/wearable/hapt.md) | スマートフォン IMU | 行動・姿勢遷移 | 30 名 / 12 行動 | 公開 (CC BY) |
| [RealWorld HAR](../datasets/wearable/realworld-har.md) | スマートフォン + スマートウォッチ IMU | 実環境 HAR | 60 名 / 15 行動 | 公開 (CC BY) |
| [mHealth](../datasets/wearable/mhealth.md) | 体表センサ + ECG | モバイルヘルスモニタリング | 10 名 / 12 行動 | 公開 (CC BY) |
| [UniMiB-SHAR](../datasets/wearable/unimib-shar.md) | スマートフォン加速度計 | 日常行動 + 転倒検出 | 30 名 / 17 行動 | 公開 |
| [Daphnet](../datasets/wearable/daphnet.md) | ウェアラブル加速度計 | すくみ足（パーキンソン病） | 10 名 / 3 センサ | 公開 |
| [Sussex-Huawei Locomotion](../datasets/wearable/shl.md) | スマートフォン + スマートウォッチ | 移動モード認識 | 3 名 / 2800 時間超 | 公開 |

### マルチモーダル／一人称視点 — 6 データセット

| データセット | モダリティ | 主要タスク | 規模 | 入手方法 |
| --- | --- | --- | --- | --- |
| [EPIC-Kitchens-100](../datasets/multimodal/epic-kitchens-100.md) | 一人称 RGB + 音声 | 長時間エゴセントリック行動 | 700 時間 / 90 キッチン | 研究用ライセンス |
| [Ego4D](../datasets/multimodal/ego4d.md) | 一人称 RGB + ステレオ + 音声 | 4D 行動、QA、視聴覚 | 3300 時間 / 74 シーン | 非商用 |
| [Charades](../datasets/multimodal/charades.md) | 室内 RGB + スクリプト | マルチラベル行動 | 9800 動画 / 157 ラベル | 公開 (CC BY-NC) |
| [NTU 相互行動](../datasets/multimodal/ntu-mutual.md) | RGB + 深度 + 骨格 | 二者間インタラクション | 26 インタラクションクラス | 研究用契約 |
| [ActivityNet Captions](../datasets/multimodal/activitynet-captions.md) | RGB 動画 + テキスト | 高密度動画記述 | 2 万動画 / 10 万記述 | 公開（研究用） |
| [How2Sign](../datasets/multimodal/how2sign.md) | RGB + 深度 + 姿勢 | 手話理解 | 80 時間 / ASL | 公開（研究用） |

### 最先端・新興 — 8 データセット

| データセット | モダリティ | 主要タスク | 規模 | 入手方法 |
| --- | --- | --- | --- | --- |
| [BEHAVE](../datasets/emerging/behave.md) | RGB-D + 姿勢 | 人-物インタラクションモデリング | 321 シーケンス / 20 名 | 公開 (BEHAVE ライセンス) |
| [Motion-X](../datasets/emerging/motion-x.md) | マルチセンサモーキャプ | 全身＋手部骨格 | 10 名 / 200 万フレーム | 公開（研究用） |
| [Ego-Exo4D](../datasets/emerging/ego-exo4d.md) | 一人称 + 三人称 RGB + モーキャプ | 視点間変換 | 1400 シーケンス / 20 時間 | 公開（研究用） |
| [HumanML3D](../datasets/emerging/humanml3d.md) | SMPL + テキスト | テキスト-動作生成 | 1.4 万以上の動作シーケンス | 公開（研究用） |
| [InterHuman](../datasets/emerging/interhuman.md) | SMPL-X + テキスト | 二者間インタラクション動作 | 6000 以上のインタラクションシーケンス | 公開（研究用） |
| [HOI4D](../datasets/emerging/hoi4d.md) | 一人称 RGB-D + 手部姿勢 | 手-物インタラクション | 4000 以上の動画クリップ | 公開（研究用） |
| [FineBio](../datasets/emerging/finebio.md) | RGB + 骨格 | 細粒度生物実験操作 | 多段階実験プロセス | 公開（研究用） |
| [HAA500](../datasets/emerging/haa500.md) | RGB 動画 | アトミック行動認識 | 1 万クリップ / 500 クラス | 公開 |

詳細については各データセットカードをご参照ください。ダウンロード方法、引用情報、ベースライン結果、既知の課題が記載されています。

## 本リポジトリの目的
- **課題指向のナビゲーション：** 単なるアルファベット順ではなく、タスクやモダリティからデータセットを検索できます。
- **研究文脈の統合：** 各データセットカードに主要論文、ベンチマーク、最新の後続研究へのリンクを掲載しています。
- **実行可能なツール：** カタログビルダー（JSON/CSV エクスポート）、リンク検証、ASCII 正規化を提供しています。
- **品質保証：** コントリビューションテンプレート、レビューチェックリスト、自動 CI 検証によりカタログの信頼性を確保しています。

## リポジトリ構成
```
.
 datasets/               # 42 個のモダリティ別データセットカード
   vision/               #   11 視覚データセット
   skeleton/             #    7 骨格／モーションキャプチャデータセット
   wearable/             #   10 ウェアラブルセンサデータセット
   multimodal/           #    6 マルチモーダル／一人称視点データセット
   emerging/             #    8 最先端・新興データセット
 docs/                   # サーベイ、ベンチマーク、ロードマップ
 tools/                  # スクリプト（カタログ構築、リンク検証、ASCII 正規化）
 .github/workflows/      # CI（リンクチェック、Markdown lint）
 i18n/                   # 翻訳（zh, de, es, fr, ja, ko, pt, ru）
```

## 厳選論文・サーベイ
- Aggarwal & Ryoo，「Human Activity Analysis: A Review」，ACM Computing Surveys，2011。
- Lara & Labrador，「A Survey on Human Activity Recognition using Wearable Sensors」，IEEE Communications Surveys，2013。
- Li ら，「A Systematic Survey on Deep Learning for Human Activity Recognition」，ACM Computing Surveys，2022。
- Grauman ら，「Ego4D: Around the World in 2,250 Hours of Egocentric Video」，CVPR 2022。（データセット + ベンチマーク）
- Pavlakos ら，「BABEL: Bodies, Actions and Behavior with English Labels」，CVPR 2022。

詳しくは [`docs/surveys.md`](../docs/surveys.md) をご覧ください。

## 本カタログの使い方
1. **データセットを探す：** 上記の分類表を確認するか、[`datasets/`](../datasets/) ディレクトリを参照してください。
2. **データセットカードを読む：** ダウンロード前にライセンス、タスク、ベンチマークプロトコル、データ特性を把握してください。
3. **プロトタイピング：** 各カードに記載されたツールやエコシステムのリンクを活用し、PyTorch / TensorFlow のデータローダーに接続してください。
4. **カタログのエクスポート：** `python tools/catalog_builder.py --format csv --output catalog.csv` を実行して、機械可読なメタデータを取得できます。
5. **最新情報の追跡：** リポジトリを Watch するか Discussions をフォローしてください。リリースごとに新規データセットと SOTA 動向をまとめています。

### 引用
本リポジトリが研究やプロダクトに役立った場合は、以下をご引用ください：

```bibtex
@misc{awesome_har_2025,
  title   = {Awesome Human Activity Recognition: A Curated List},
  author  = {Wenxuan Huang},
  year    = {2025},
  url     = {https://github.com/Leo-Cyberautonomy/awesome-human-activity-recognition},
  note    = {GitHub repository}
}
```

## コントリビューション方法
- [`CONTRIBUTING.md`](../CONTRIBUTING.md) を読み、データセットカードテンプレート、レビュー基準、記述規約をご確認ください。
- Issue を使って新しいデータセットのリクエストやリンク切れの報告ができます。モダリティ別のラベル（例：`modality:wearable`）を使用しています。
- Pull Request はデータ品質レビューと自動リンク検証を経て、5〜7 日以内のマージを目指します。

## ロードマップ
- 毎週の自動リンク検証（GitHub Actions）。
- ウェアラブル・動画ベースラインの Jupyter 入門ノートブック。
- 標準化データセットスキーマ（YAML）と自動バリデーション。
- コミュニティフォーカス：四半期ごとの新規データセット・リーダーボード動向サマリー。
- 長期目標：MkDocs ベースの検索可能な静的サイト構築。

完全なロードマップは [`docs/roadmap.md`](../docs/roadmap.md) をご覧ください。

## 謝辞
すべてのデータセット作成者、アノテーションチーム、ベンチマーク管理者に感謝いたします。彼らの努力が人間行動理解分野のオープンリサーチを推進しています。本カタログを通じて、その成果をより広く活用できるようにすることを目指しています。
