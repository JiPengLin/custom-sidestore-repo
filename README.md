# iOS 精选应用 SideStore / AltStore 订阅源 (国内镜像加速版)

[![Sync Sources](https://github.com/JiPengLin/piliplus-sidestore-source/actions/workflows/sync.yml/badge.svg)](https://github.com/JiPengLin/piliplus-sidestore-source/actions/workflows/sync.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Mirror](https://img.shields.io/badge/Mirror-China_Accelerated-green.svg)](#)

专为 **SideStore** 与 **LiveContainer** 适配的精选应用自动更新源。已全面接入国内 CDN 与镜像代理，解决因 SideStore 独占 LocalDevVPN 导致无法翻墙、无法直连 GitHub 下载安装包的问题。

---

## 包含应用

| 应用名称 | 官方上游项目 | 真实包名 (Bundle ID) | 最低支持 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| **PiliPlus** | [bggRGjQaUbCoE/PiliPlus](https://github.com/bggRGjQaUbCoE/PiliPlus) | `com.example.piliplus` | iOS 14.0+ | 第三方轻量 Bilibili 客户端 |
| **知乎--** | [huamurui/zhihu-minus-minus](https://github.com/huamurui/zhihu-minus-minus) | `com.huamu013.ZhihuMinusMinus` | iOS 15.1+ | 轻量、无广告的第三方知乎客户端 |
| **TiebaPure** | [infinityf4p/TiebaPure-iOS](https://github.com/infinityf4p/TiebaPure-iOS) | `com.infinityf4p.TiebaPure` | iOS 16.4+ | 原生 SwiftUI 编写的纯净百度贴吧客户端 |

---

## 快速添加订阅（SideStore）

### 方式一：一键添加聚合源（推荐，三款应用全收录）

在 iOS 设备上使用 Safari 浏览器点击下方按钮，直接唤起 SideStore 并添加聚合源：

[![Add to SideStore](https://img.shields.io/badge/Add_Source_to-SideStore-00AEEF?style=for-the-badge&logo=apple)](https://stikstore.app/altdirect/?url=https://JiPengLin.github.io/piliplus-sidestore-source/apps.json)

---

### 方式二：手动复制订阅链接

根据需求复制对应链接，打开 **SideStore** -> 进入底部 **Sources** -> 点击右上角 **`+`** 号粘贴：

#### 1. 聚合源（推荐：PiliPlus + 知乎-- + TiebaPure）
```text
https://JiPengLin.github.io/piliplus-sidestore-source/apps.json
```
*(备用免代理直链：`https://gh-proxy.com/https://raw.githubusercontent.com/JiPengLin/piliplus-sidestore-source/main/apps.json`)*

#### 2. 独立源（如需单独订阅）
- **知乎-- 独立源**：
  ```text
  https://JiPengLin.github.io/piliplus-sidestore-source/zhihu.json
  ```
- **TiebaPure 贴吧独立源**：
  ```text
  https://JiPengLin.github.io/piliplus-sidestore-source/tieba.json
  ```

---

## LiveContainer 免 3-App 限制直装指引

如果你的免费 Apple ID 已经达到 **3 个物理安装应用上限**，请在 **LiveContainer** 内部点击 `+` 号 -> 选择 **从 URL 安装 (Install from URL)**，粘贴加速直链完成安装（计为 0 个名额，不消耗 Apple ID 配额）：

- **知乎-- 最新版国内加速直链**：
  ```text
  https://gh-proxy.com/https://github.com/huamurui/zhihu-minus-minus/releases/latest/download/zhihu-minus-minus-v0.8.1-unsigned.ipa
  ```

---

## 特性说明

- **国内全链路加速**：
  - **安装包加速**：下载流量自动经由国内镜像中转流式分发，告别 GitHub 官方连接重置与 0% 假死。
  - **静态资源 CDN**：应用图标与详情页轮播预览图接入 **jsDelivr 全球 CDN**，极速加载无红叉。
  - **全匿名零门槛**：无需注册任何中转账号，无需配置 Token。
- **全自动同步**：基于 GitHub Actions 错峰定时轮询（每 2 小时 17 分），秒级对齐上游官方 Releases。
- **原生包名严谨对齐**：使用官方实际打包的 Bundle ID，在 LiveContainer 或桌面覆盖安装不会产生重复应用，不破坏既有的沙盒数据及 Launch URL / 快捷指令。

---

## 免责声明与致谢

1. 本项目仅为自动化生成 AltStore / SideStore 规范元数据的索引脚本工具，**不存储、不修改、不分发任何二进制 IPA 文件**。所有应用安装包均来自上游官方仓库 Releases，加速节点仅充当公开网络中转。
2. 原项目版权归属：
   - PiliPlus：[bggRGjQaUbCoE/PiliPlus](https://github.com/bggRGjQaUbCoE/PiliPlus)
   - 知乎--：[huamurui/zhihu-minus-minus](https://github.com/huamurui/zhihu-minus-minus)
   - TiebaPure：[infinityf4p/TiebaPure-iOS](https://github.com/infinityf4p/TiebaPure-iOS)
