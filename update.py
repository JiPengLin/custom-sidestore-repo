import os
import re
import json
import urllib.request

SOURCE_REPO = "bggRGjQaUbCoE/PiliPlus"
OUTPUT_FILE = "apps.json"

# ==================== 国内加速配置 ====================
# 下载加速代理前缀（末尾带 /），若填 "" 则使用 GitHub 官方原始下载直链
# 常用稳定备选节点：
# "https://ghfast.top/"
# "https://ghproxy.net/"
# "https://hub.gitmirror.com/"
IPA_PROXY_PREFIX = "https://ghfast.top/"

# 静态资源改用 jsDelivr CDN 加速（彻底替代被污染的 raw.githubusercontent.com）
CDN_BASE = "https://cdn.jsdelivr.net/gh/bggRGjQaUbCoE/PiliPlus@main"
APP_ICON_URL = f"{CDN_BASE}/assets/images/logo/logo.png"

APP_SCREENSHOTS = [
    f"{CDN_BASE}/assets/screenshots/510shots_so.png",
    f"{CDN_BASE}/assets/screenshots/174shots_so.png",
    f"{CDN_BASE}/assets/screenshots/850shots_so.png"
]
# =====================================================

REPO_NAME = "PiliPlus Source (国内加速)"
REPO_IDENTIFIER = "com.custom.piliplus.source"
REPO_WEBSITE = "https://github.com/bggRGjQaUbCoE/PiliPlus"

APP_NAME = "PiliPlus"
APP_BUNDLE_ID = "com.example.piliplus"
APP_DEVELOPER = "bggRGjQaUbCoE"
APP_SUBTITLE = "第三方 Bilibili 客户端"
APP_DESCRIPTION = "PiliPlus iOS 客户端，基于 GitHub Releases 自动同步（国内镜像加速版）"
APP_TINT_COLOR = "#00AEEF"
APP_MIN_OS = "14.0"

def extract_build_version(filename: str) -> str:
    match = re.search(r"\+(\d+)\.ipa$", filename, re.IGNORECASE)
    return match.group(1) if match else ""

def parse_semver(ver_str: str) -> list[int]:
    return [int(x) for x in re.findall(r"\d+", ver_str)]

def fetch_releases() -> list[dict]:
    url = f"https://api.github.com/repos/{SOURCE_REPO}/releases?per_page=30"
    headers = {"User-Agent": "AltStore-Source-Updater", "Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

def main():
    releases = fetch_releases()
    versions = []
    news = []

    for rel in releases:
        if rel.get("draft"):
            continue

        tag = rel.get("tag_name", "")
        version = tag.lstrip("v")
        if not version:
            continue

        ipa_asset = None
        for asset in rel.get("assets", []):
            if asset.get("name", "").lower().endswith(".ipa"):
                ipa_asset = asset
                break

        if not ipa_asset:
            continue

        build_ver = extract_build_version(ipa_asset.get("name", ""))
        date_str = rel.get("published_at", "")[:10]
        body = (rel.get("body") or "").strip() or APP_DESCRIPTION

        raw_download_url = ipa_asset.get("browser_download_url", "")
        # 拼接加速前缀
        download_url = f"{IPA_PROXY_PREFIX}{raw_download_url}" if IPA_PROXY_PREFIX else raw_download_url

        v_item = {
            "version": version,
            "date": date_str,
            "localizedDescription": body,
            "downloadURL": download_url,
            "size": ipa_asset.get("size", 0),
            "minOSVersion": APP_MIN_OS
        }
        if build_ver:
            v_item["buildVersion"] = build_ver
        
        versions.append(v_item)

        news.append({
            "title": f"{APP_NAME} {version}",
            "identifier": f"release-{version}",
            "caption": rel.get("name") or f"Version {version} 发布",
            "date": date_str,
            "tintColor": APP_TINT_COLOR,
            "notify": True,
            "appID": APP_BUNDLE_ID,
            "url": rel.get("html_url")
        })

    if not versions:
        print("未抓取到有效版本，跳过更新。")
        return

    versions.sort(key=lambda v: (parse_semver(v["version"]), int(v.get("buildVersion", 0))), reverse=True)
    news.sort(key=lambda n: n["date"], reverse=True)

    source_data = {
        "name": REPO_NAME,
        "identifier": REPO_IDENTIFIER,
        "subtitle": "PiliPlus 自动更新源 (国内镜像)",
        "description": "专为 SideStore 与 LiveContainer 适配的国内加速源",
        "iconURL": APP_ICON_URL,
        "website": REPO_WEBSITE,
        "tintColor": APP_TINT_COLOR,
        "apps": [
            {
                "name": APP_NAME,
                "bundleIdentifier": APP_BUNDLE_ID,
                "developerName": APP_DEVELOPER,
                "subtitle": APP_SUBTITLE,
                "localizedDescription": APP_DESCRIPTION,
                "iconURL": APP_ICON_URL,
                "screenshots": APP_SCREENSHOTS,
                "tintColor": APP_TINT_COLOR,
                "versions": versions
            }
        ],
        "news": news
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(source_data, f, indent=2, ensure_ascii=False)

    print(f"成功更新 {OUTPUT_FILE}（已注入国内镜像下载加速）")

if __name__ == "__main__":
    main()
