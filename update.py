import os
import re
import json
import urllib.request

# ==================== 配置区 ====================
PILI_REPO = "bggRGjQaUbCoE/PiliPlus"
ZHIHU_SOURCE_URL = "https://github.com/huamurui/zhihu-minus-minus/releases/latest/download/altstore-source.json"

SOURCE_NAME = "JiPengLin 的精选加速源"
SOURCE_IDENTIFIER = "com.jipenglin.custom.source"

# 国内镜像下载代理前缀
IPA_PROXY_PREFIX = "https://gh-proxy.com/"

# PiliPlus 配置
PILI_BUNDLE_ID = "com.example.piliplus"
PILI_CDN = "https://cdn.jsdelivr.net/gh/bggRGjQaUbCoE/PiliPlus@main"
PILI_ICON = f"{PILI_CDN}/assets/images/logo/logo.png"
PILI_SCREENSHOTS = [
    f"{PILI_CDN}/assets/screenshots/510shots_so.png",
    f"{PILI_CDN}/assets/screenshots/174shots_so.png",
    f"{PILI_CDN}/assets/screenshots/850shots_so.png"
]
# ===============================================

def extract_build_version(filename: str) -> str:
    match = re.search(r"\+(\d+)\.ipa$", filename, re.IGNORECASE)
    return match.group(1) if match else "1"

def parse_semver(ver_str: str) -> list[int]:
    return [int(x) for x in re.findall(r"\d+", ver_str)]

def http_get_json(url: str) -> dict | list:
    headers = {"User-Agent": "AltStore-Updater", "Accept": "application/json"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

def build_piliplus_app():
    url = f"https://api.github.com/repos/{PILI_REPO}/releases?per_page=20"
    releases = http_get_json(url)
    
    versions = []
    news = []
    for rel in releases:
        if rel.get("draft"): continue
        version = (rel.get("tag_name") or "").lstrip("v")
        if not version: continue

        ipa_asset = next((a for a in rel.get("assets", []) if a.get("name", "").lower().endswith(".ipa")), None)
        if not ipa_asset: continue

        date_str = rel.get("published_at", "")[:10]
        download_url = f"{IPA_PROXY_PREFIX}{ipa_asset['browser_download_url']}" if IPA_PROXY_PREFIX else ipa_asset['browser_download_url']
        build_ver = extract_build_version(ipa_asset.get("name", ""))

        versions.append({
            "version": version,
            "buildVersion": build_ver,
            "date": date_str,
            "localizedDescription": (rel.get("body") or "").strip() or "PiliPlus iOS 客户端",
            "downloadURL": download_url,
            "size": ipa_asset.get("size", 0),
            "minOSVersion": "14.0"
        })
        news.append({
            "title": f"PiliPlus {version}",
            "identifier": f"pili-{version}",
            "caption": rel.get("name") or f"Version {version} 发布",
            "date": date_str,
            "tintColor": "#00AEEF",
            "notify": True,
            "appID": PILI_BUNDLE_ID,
            "url": rel.get("html_url")
        })

    versions.sort(key=lambda v: (parse_semver(v["version"]), int(v.get("buildVersion", 0))), reverse=True)
    return {
        "name": "PiliPlus",
        "bundleIdentifier": PILI_BUNDLE_ID,
        "developerName": "bggRGjQaUbCoE",
        "subtitle": "第三方 Bilibili 客户端",
        "localizedDescription": "PiliPlus iOS 客户端，基于 GitHub Releases 自动同步（国内镜像加速版）",
        "iconURL": PILI_ICON,
        "screenshots": PILI_SCREENSHOTS,
        "tintColor": "#00AEEF",
        "versions": versions
    }, news

def build_zhihu_app():
    # 直接读取知乎官方现成的 altstore-source.json，避开 GitHub API 跨仓 403 权限问题
    source_json = http_get_json(ZHIHU_SOURCE_URL)
    zhihu_app = source_json["apps"][0]

    # 替换图标为 jsDelivr 国内 CDN
    zhihu_app["iconURL"] = "https://cdn.jsdelivr.net/gh/huamurui/zhihu-minus-minus@main/assets/images/icon.png"
    zhihu_app["subtitle"] = "轻量、无广告的第三方知乎客户端"

    # 为所有版本的下载链接注入国内加速代理
    for v in zhihu_app.get("versions", []):
        raw_url = v.get("downloadURL", "")
        if IPA_PROXY_PREFIX and not raw_url.startswith(IPA_PROXY_PREFIX):
            v["downloadURL"] = f"{IPA_PROXY_PREFIX}{raw_url}"

    news = [
        {
            "title": f"知乎-- {v['version']}",
            "identifier": f"zhihu-{v['version']}",
            "caption": f"Version {v['version']} 发布",
            "date": v.get("date", ""),
            "tintColor": "#0066FF",
            "notify": True,
            "appID": zhihu_app["bundleIdentifier"],
            "url": "https://github.com/huamurui/zhihu-minus-minus/releases"
        }
        for v in zhihu_app.get("versions", [])[:3]
    ]

    return zhihu_app, news

def main():
    print("正在拉取 PiliPlus...")
    pili_app, pili_news = build_piliplus_app()

    print("正在拉取 知乎--...")
    zhihu_app, zhihu_news = build_zhihu_app()

    # 1. 生成聚合源 apps.json (包含两款应用)
    combined_source = {
        "name": SOURCE_NAME,
        "identifier": SOURCE_IDENTIFIER,
        "subtitle": "精选 iOS 应用国内镜像加速源",
        "description": "专为 SideStore 与 LiveContainer 适配的聚合加速源",
        "iconURL": PILI_ICON,
        "apps": [pili_app, zhihu_app],
        "news": sorted(pili_news + zhihu_news, key=lambda n: n["date"], reverse=True)
    }
    with open("apps.json", "w", encoding="utf-8") as f:
        json.dump(combined_source, f, indent=2, ensure_ascii=False)

    # 2. 单独生成 zhihu.json (仅包含知乎)
    zhihu_source = {
        "name": "知乎-- (国内镜像源)",
        "identifier": "com.huamu013.ZhihuMinusMinus.source",
        "subtitle": "轻量、无广告的第三方知乎客户端",
        "iconURL": zhihu_app["iconURL"],
        "apps": [zhihu_app],
        "news": zhihu_news
    }
    with open("zhihu.json", "w", encoding="utf-8") as f:
        json.dump(zhihu_source, f, indent=2, ensure_ascii=False)

    print("已成功更新 apps.json 和 zhihu.json！")

if __name__ == "__main__":
    main()
