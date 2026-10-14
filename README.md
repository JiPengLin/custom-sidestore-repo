# iOS 精选应用 SideStore / AltStore 订阅源 (国内镜像加速版)

[![Sync Sources](https://github.com/JiPengLin/custom-sidestore-repo/actions/workflows/sync.yml/badge.svg)](https://github.com/JiPengLin/custom-sidestore-repo/actions/workflows/sync.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Mirror](https://img.shields.io/badge/Mirror-China_Accelerated-green.svg)](#)

专为 **SideStore** 与 **LiveContainer** 适配的精选应用自动更新源。已全面接入国内 CDN 与镜像代理，解决因 SideStore 独占 LocalDevVPN 导致无法翻墙、无法直连 GitHub 下载安装包的问题。

---

## 包含应用

| 应用名称 | 官方上游项目 | 真实包名 (Bundle ID) | 最低系统 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| **PiliPlus** | [bggRGjQaUbCoE/PiliPlus](https://github.com/bggRGjQaUbCoE/PiliPlus) | `com.example.piliplus` | iOS 14.0+ | 第三方轻量 Bilibili 客户端 |
| **知乎--** | [huamurui/zhihu-minus-minus](https://github.com/huamurui/zhihu-minus-minus) | `com.huamu013.ZhihuMinusMinus` | iOS 15.1+ | 轻量、无广告的第三方知乎客户端 |
| **TiebaPure** | [infinityf4p/TiebaPure-iOS](https://github.com/infinityf4p/TiebaPure-iOS) | `com.infinityf4p.TiebaPure` | iOS 16.4+ | 原生 SwiftUI 编写的纯净百度贴吧客户端 |

---

## 订阅源链接

### 方案一：聚合源（推荐，一个链接收录全部应用）

在 iOS 设备上使用 Safari 浏览器点击下方按钮，可直接唤起 SideStore 并添加聚合源：

[![Add to SideStore](https://img.shields.io/badge/Add_Source_to-SideStore-00AEEF?style=for-the-badge&logo=apple)](https://stikstore.app/altdirect/?url=https://JiPengLin.github.io/custom-sidestore-repo/apps.json)

- **GitHub Pages 直链**：
  ```text
  https://JiPengLin.github.io/custom-sidestore-repo/apps.json
  ```
- **国内免代理备用直链**：
  ```text
  https://gh-proxy.com/https://raw.githubusercontent.com/JiPengLin/custom-sidestore-repo/main/apps.json
  ```

---

### 方案二：独立源清单（如需在 SideStore 单独订阅某个应用）

如果你不想把所有应用混在一起，可以单独添加对应的独立源：

* **PiliPlus 独立源**：
  ```text
  https://JiPengLin.github.io/custom-sidestore-repo/piliplus.json
  ```
* **知乎-- 独立源**：
  ```text
  https://JiPengLin.github.io/custom-sidestore-repo/zhihu.json
  ```
* **TiebaPure 贴吧独立源**：
  ```text
  https://JiPengLin.github.io/custom-sidestore-repo/tieba.json
  ```

---


## 特性说明

- **国内全链路加速**：
  - **安装包加速**：下载流量自动经由国内镜像代理中转流式分发，告别 GitHub 官方连接重置与 0% 假死。
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
