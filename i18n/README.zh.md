# Awesome 人体活动识别（Awesome Human Activity Recognition）

[**中文**](README.zh.md) | [English](../README.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [français](README.fr.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Português](README.pt.md) | [Русский](README.ru.md)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Stars](https://img.shields.io/github/stars/Leo-Cyberautonomy/awesome-human-activity-recognition?style=social)](https://github.com/Leo-Cyberautonomy/awesome-human-activity-recognition/stargazers)
[![License](https://img.shields.io/github/license/Leo-Cyberautonomy/awesome-human-activity-recognition)](../LICENSE)
[![Datasets](https://img.shields.io/badge/datasets-42-brightgreen)](#分类概览)

一个覆盖视觉、可穿戴传感、骨架捕获、多模态等领域的 **42 个**人体活动与动作数据集的精选目录。每份数据集卡片都包含模态、许可协议、基准任务、代表性基线、工具生态以及权威论文，帮助你快速着手建模或对比评测。

- 针对机器学习研究者、产品团队以及运动科学实验室。
- 既展示最前沿的数据集，也保留构建现有基准的经典数据集。
- 配套贡献工作流、校验工具与发展路线图，便于社区协同维护。

> 目标：打造人体活动数据集的权威 GitHub 资源，参考 Papers with Code 的深度，同时保持"数据集优先"的视角。

## 快速入口
- 数据集卡片目录：[`datasets/`](../datasets/)
- 综述与基准论文：[`docs/surveys.md`](../docs/surveys.md)
- 基准快照：[`docs/benchmarking.md`](../docs/benchmarking.md)
- 贡献指南：[`CONTRIBUTING.md`](../CONTRIBUTING.md)
- 自动化路线图：[`docs/roadmap.md`](../docs/roadmap.md)

## 分类概览

### 视觉（RGB / 深度）— 11 个数据集

| 数据集 | 模态 | 主要任务 | 规模 | 获取方式 |
| --- | --- | --- | --- | --- |
| [Kinetics-700](../datasets/vision/kinetics-700.md) | RGB 视频 | 动作识别、预训练 | 65 万片段 / 700 类别 | 公共 (CC BY) |
| [UCF-101](../datasets/vision/ucf101.md) | RGB 视频 | 动作识别 | 1.3 万片段 / 101 类别 | 公共 (科研) |
| [HMDB-51](../datasets/vision/hmdb51.md) | RGB 视频 | 动作识别 | 6800 片段 / 51 类别 | 公共 (科研) |
| [ActivityNet](../datasets/vision/activitynet.md) | RGB 视频 | 时序动作检测 | 2 万视频 / 200 类别 | 公共 (科研) |
| [AVA](../datasets/vision/ava.md) | RGB 视频 | 时空动作检测 | 430 片段 / 80 原子动作 | 公共 (科研) |
| [NTU RGB+D 120](../datasets/vision/ntu-rgbd-120.md) | RGB + 深度 + 骨架 | 3D 动作识别 | 11.4 万序列 / 120 类别 | 科研协议 |
| [Something-Something V2](../datasets/vision/something-something-v2.md) | RGB 视频 | 精细交互识别 | 22 万片段 / 174 标签 | 公共 (Apache 2.0) |
| [FineGym](../datasets/vision/finegym.md) | RGB 视频 | 精细体操动作 | 3.2 万段 / 层级标注 | 公共 (科研) |
| [Moments in Time](../datasets/vision/moments-in-time.md) | RGB 视频 | 事件/动作识别 | 100 万片段 / 339 类别 | 公共 (科研) |
| [Diving48](../datasets/vision/diving48.md) | RGB 视频 | 精细跳水动作 | 1.8 万片段 / 48 类别 | 公共 (科研) |
| [Toyota Smarthome](../datasets/vision/toyota-smarthome.md) | RGB + 深度 + 骨架 | 日常生活活动 | 1.6 万片段 / 31 类别 | 科研协议 |

### 骨架与动捕 — 7 个数据集

| 数据集 | 模态 | 主要任务 | 规模 | 获取方式 |
| --- | --- | --- | --- | --- |
| [NTU RGB+D 60](../datasets/skeleton/ntu-rgbd-60.md) | RGB + 深度 + 骨架 | 骨架动作识别 | 5.7 万序列 / 60 类别 | 科研协议 |
| [AMASS](../datasets/skeleton/amass.md) | 参数化人体姿态 | 动作生成、姿态估计 | 1.6 万分钟 / 344 受试者 | 公共 (AMASS 许可) |
| [Human3.6M](../datasets/skeleton/human36m.md) | 动捕 + RGB | 姿态估计、3D 重建 | 360 万帧 3D 数据 | 科研许可 |
| [BABEL](../datasets/skeleton/babel.md) | SMPL + 文本标签 | 动作-语言对齐 | 43 小时 / 3.7k 序列 | 科研 (非商业) |
| [TotalCapture](../datasets/skeleton/totalcapture.md) | 动捕 + 多视角 RGB + IMU | 3D 姿态估计、融合 | 5 人 / 多视角 | 公共 (CC BY) |
| [PKU-MMD](../datasets/skeleton/pku-mmd.md) | RGB + 深度 + 骨架 | 动作检测 | 2 万实例 / 51 类别 | 科研协议 |
| [Skeletics-152](../datasets/skeleton/skeletics-152.md) | 估计骨架 | 大规模骨架动作 | 15 万片段 / 152 类别 | 科研 |

### 可穿戴传感器 — 10 个数据集

| 数据集 | 模态 | 主要任务 | 规模 | 获取方式 |
| --- | --- | --- | --- | --- |
| [UCI-HAR](../datasets/wearable/uci-har.md) | 智能手机 IMU | 活动识别 | 30 人 / 6 种活动 | 公共 (CC BY) |
| [PAMAP2](../datasets/wearable/pamap2.md) | IMU + 心率 | 可穿戴 HAR | 9 人 / 18 种活动 | 公共 (CC BY-SA) |
| [WISDM](../datasets/wearable/wisdm.md) | 手机 + 手表 | HAR、手势识别 | 51 人 / 百万级样本 | 公共 (知识共享) |
| [OPPORTUNITY](../datasets/wearable/opportunity.md) | 可穿戴 + 环境传感 | 场景识别 | 4 人 / 72 通道 | 公共 (科研) |
| [HAPT](../datasets/wearable/hapt.md) | 智能手机 IMU | 活动与姿态转换 | 30 人 / 12 种活动 | 公共 (CC BY) |
| [RealWorld HAR](../datasets/wearable/realworld-har.md) | 手机 + 手表 IMU | 真实场景 HAR | 60 人 / 15 种活动 | 公共 (CC BY) |
| [mHealth](../datasets/wearable/mhealth.md) | 体表传感器 + ECG | 移动健康监测 | 10 人 / 12 种活动 | 公共 (CC BY) |
| [UniMiB-SHAR](../datasets/wearable/unimib-shar.md) | 手机加速度计 | 日常活动 + 跌倒检测 | 30 人 / 17 种活动 | 公共 |
| [Daphnet](../datasets/wearable/daphnet.md) | 可穿戴加速度计 | 冻结步态（帕金森） | 10 人 / 3 传感器 | 公共 |
| [Sussex-Huawei Locomotion](../datasets/wearable/shl.md) | 手机 + 手表 | 运动模式识别 | 3 人 / 2800+ 小时 | 公共 |

### 多模态 / 第一视角 — 6 个数据集

| 数据集 | 模态 | 主要任务 | 规模 | 获取方式 |
| --- | --- | --- | --- | --- |
| [EPIC-Kitchens-100](../datasets/multimodal/epic-kitchens-100.md) | Ego RGB + 音频 | 长时 egocentric 行为 | 700 小时 / 90 厨房 | 科研许可 |
| [Ego4D](../datasets/multimodal/ego4d.md) | Ego RGB + 立体 + 音频 | 4D 行为、问答、视听 | 3300 小时 / 74 场景 | 非商业 |
| [Charades](../datasets/multimodal/charades.md) | 室内 RGB + 剧本 | 多标签动作 | 9800 视频 / 157 标签 | 公共 (CC BY-NC) |
| [NTU 交互动作](../datasets/multimodal/ntu-mutual.md) | RGB + 深度 + 骨架 | 双人交互 | 26 种交互类别 | 科研协议 |
| [ActivityNet Captions](../datasets/multimodal/activitynet-captions.md) | RGB 视频 + 文本 | 密集视频描述 | 2 万视频 / 10 万描述 | 公共 (科研) |
| [How2Sign](../datasets/multimodal/how2sign.md) | RGB + 深度 + 姿态 | 手语理解 | 80 小时 / ASL | 公共 (科研) |

### 前沿与新兴 — 8 个数据集

| 数据集 | 模态 | 主要任务 | 规模 | 获取方式 |
| --- | --- | --- | --- | --- |
| [BEHAVE](../datasets/emerging/behave.md) | RGB-D + 姿态 | 人-物交互建模 | 321 序列 / 20 人 | 公共 (BEHAVE 许可) |
| [Motion-X](../datasets/emerging/motion-x.md) | 多传感动捕 | 全身+手部骨架 | 10 人 / 200 万帧 | 公共 (科研) |
| [Ego-Exo4D](../datasets/emerging/ego-exo4d.md) | Ego + Exo RGB + 动捕 | 视角互译 | 1400 序列 / 20 小时 | 公共 (科研) |
| [HumanML3D](../datasets/emerging/humanml3d.md) | SMPL + 文本 | 文本-动作生成 | 1.4 万+ 动作序列 | 公共 (科研) |
| [InterHuman](../datasets/emerging/interhuman.md) | SMPL-X + 文本 | 双人交互动作 | 6000+ 交互序列 | 公共 (科研) |
| [HOI4D](../datasets/emerging/hoi4d.md) | Ego RGB-D + 手部姿态 | 手-物交互 | 4000+ 视频片段 | 公共 (科研) |
| [FineBio](../datasets/emerging/finebio.md) | RGB + 骨架 | 精细生物实验操作 | 多步骤实验流程 | 公共 (科研) |
| [HAA500](../datasets/emerging/haa500.md) | RGB 视频 | 原子动作识别 | 1 万片段 / 500 类别 | 公共 |

详细信息请查阅对应数据集卡片，包括下载方法、引用信息、基线结果与已知挑战。

## 为什么要做这个仓库
- **问题优先导航：** 按任务或模态检索数据集，而不仅仅是字母排序。
- **结合研究语境：** 每个数据集卡片都链接到权威论文、基准与最新跟进工作。
- **可执行工具：** 目录构建器（JSON/CSV 导出）、链接校验、ASCII 规范化。
- **质量保障：** 贡献模板、评审清单与自动化 CI 校验让目录可靠可信。

## 仓库结构
```
.
 datasets/               # 42 个按模态划分的数据集卡片
   vision/               #   11 个视觉数据集
   skeleton/             #    7 个骨架/动捕数据集
   wearable/             #   10 个可穿戴传感器数据集
   multimodal/           #    6 个多模态/第一视角数据集
   emerging/             #    8 个前沿与新兴数据集
 docs/                   # 综述、基准、路线图
 tools/                  # 脚本（目录构建、链接校验、ASCII 规范化）
 .github/workflows/      # CI（链接检查、Markdown lint）
 i18n/                   # 翻译（zh, de, es, fr, ja, ko, pt, ru）
```

## 精选论文与综述
- Aggarwal & Ryoo，《Human Activity Analysis: A Review》，ACM Computing Surveys，2011。
- Lara & Labrador，《A Survey on Human Activity Recognition using Wearable Sensors》，IEEE Communications Surveys，2013。
- Li 等，《A Systematic Survey on Deep Learning for Human Activity Recognition》，ACM Computing Surveys，2022。
- Grauman 等，《Ego4D: Around the World in 2,250 Hours of Egocentric Video》，CVPR 2022。（数据集 + 基准）
- Pavlakos 等，《BABEL: Bodies, Actions and Behavior with English Labels》，CVPR 2022。

扩展阅读请见 [`docs/surveys.md`](../docs/surveys.md)。

## 如何使用本目录
1. **定位数据集：** 先查上方分类表，或按 [`datasets/`](../datasets/) 目录浏览。
2. **阅读数据集卡片：** 在下载前了解许可、任务、基准协议和数据特点。
3. **快速原型：** 利用各卡片中的工具与生态链接，接入 PyTorch / TensorFlow 数据加载器。
4. **生成目录导出：** 运行 `python tools/catalog_builder.py --format csv --output catalog.csv` 获取机器可读元数据。
5. **持续跟进：** Watch 仓库或关注 Discussions，我们会在每次发布时总结新增数据集与 SOTA 动态。

### 引用
若本仓库对你的研究或产品有所帮助，请引用：

```bibtex
@misc{awesome_har_2025,
  title   = {Awesome Human Activity Recognition: A Curated List},
  author  = {Wenxuan Huang},
  year    = {2025},
  url     = {https://github.com/Leo-Cyberautonomy/awesome-human-activity-recognition},
  note    = {GitHub repository}
}
```

## 贡献方式
- 阅读 [`CONTRIBUTING.md`](../CONTRIBUTING.md)，获取数据集卡片模板、评审标准与写作规范。
- 使用 Issue 请求新数据集或报告失效链接。我们按模态使用标签（如 `modality:wearable`）。
- Pull Request 将接受数据质量评审与自动化链接校验，力争 5-7 天内完成。

## 发展路线
- 每周自动链接校验（GitHub Actions）。
- 可穿戴与视频基线的 Jupyter 入门笔记。
- 标准化数据集 schema（YAML）与自动校验。
- 社区焦点：每季度发布新数据集与排行榜动态摘要。
- 长期目标：基于 MkDocs 构建可搜索的静态站点。

完整路线图请见 [`docs/roadmap.md`](../docs/roadmap.md)。

## 致谢
感谢所有数据集作者、标注团队与基准维护者，正是他们推动了人体活动理解领域的开放研究。我们希望通过易用的目录放大他们的成果。
