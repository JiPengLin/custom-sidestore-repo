# PiliPlus SideStore / AltStore 订阅源 (国内镜像加速版)

[![Sync PiliPlus Source](https://github.com/JiPengLin/piliplus-sidestore-source/actions/workflows/sync.yml/badge.svg)](https://github.com/JiPengLin/piliplus-sidestore-source/actions/workflows/sync.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Mirror](https://img.shields.io/badge/Mirror-China_Accelerated-green.svg)](#)

专为 **SideStore** 与 **LiveContainer** 适配的非官方 [PiliPlus](https://github.com/bggRGjQaUbCoE/PiliPlus) 自动更新源。已全面集成国内 CDN 与镜像代理，无需挂代理即可直接拉取源并高速下载 IPA 安装包。

---

## 快速添加订阅

### 方式一：一键唤起添加（推荐）

在 iOS 设备上使用 Safari 浏览器点击下方按钮，可直接呼起 SideStore 并添加源：

[![Add to SideStore](https://img.shields.io/badge/Add_Source_to-SideStore-00AEEF?style=for-the-badge&logo=apple)](https://stikstore.app/altdirect/?url=https://JiPengLin.github.io/piliplus-sidestore-source/apps.json)

---

### 方式二：手动复制订阅链接

根据你的网络环境二选一，复制后粘贴至 SideStore 即可：

#### 1. 推荐直链（GitHub Pages 官方镜像，下载走高速通道）
```text
https://JiPengLin.github.io/piliplus-sidestore-source/apps.json
```

#### 2. 国内免代理备用直链（适合完全打不开 github.io 的网络）
```text
https://ghfast.top/https://raw.githubusercontent.com/JiPengLin/piliplus-sidestore-source/main/apps.json
```

**添加步骤：**
1. 复制上述任意一条链接；
2. 打开 iPhone 上的 **SideStore**；
3. 进入底部的 **Sources** 标签页；
4. 点击右上角 **`+`** 号，粘贴链接并点击 **Add** 保存。

---

## 特性说明

- **国内全链路加速**：
  - **安装包加速**：内置公共反代节点，下载 IPA 安装包告别 GitHub 官方连接重置与几 KB 龟速。
  - **媒体资源加速**：应用图标与详情页轮播预览图全面接入 **jsDelivr CDN**，告别加载空白与红叉。
  - **无需注册**：全匿名访问，零账号、零配置门槛。
- **全自动同步**：基于 GitHub Actions，每 2 小时定时轮询官方上游 Releases 并在有更新时自动生成清单。
- **原生包名对齐**：精准匹配官方 iOS 包名 `com.example.piliplus`。在 LiveContainer 中覆盖升级不会生成重复应用，不丢失本地数据，不破坏既有的 Launch URL / 快捷方式。
- **规范元数据**：包含语义化版本精准排序、更新日志详情提取与应用截图轮播。

---

## 免责声明与致谢

1. 本项目仅为自动化生成 AltStore / SideStore 规范元数据的索引脚本工具，**不存储、不修改、不分发任何二进制 IPA 文件**。所有应用安装包均来自上游官方仓库 Releases，加速节点仅充当公开网络中转。
2. 原项目版权归 [bggRGjQaUbCoE/PiliPlus](https://github.com/bggRGjQaUbCoE/PiliPlus) 及原作者所有。
