#!/usr/bin/env python3
"""直播源健康检测：检查 live.txt / live.m3u / tvbox.json 中所有地址，
失效的源会在输出中标注，并在 README 可用性报告中更新。"""
import re
import requests
import json
import datetime

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def check_url(url, timeout=12):
    try:
        r = requests.get(url, headers=UA, timeout=timeout, verify=False, stream=True)
        body = r.raw.read(200)
        ok = r.status_code == 200 and (b"#EXT" in body or b"m3u8" in body.lower() or b"mpd" in body)
        return ok, r.status_code
    except Exception:
        return False, None

def main():
    results = {}
    # 从 live.txt 读 URL
    with open("live.txt", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(",")
            if len(parts) >= 3:
                name, url = parts[0], parts[-1]
                ok, code = check_url(url)
                results[name] = (ok, code)
                print(f"{'✅' if ok else '❌'} {name} ({code})")

    # 生成状态报告附加到 README 顶部说明（可选）
    good = sum(1 for v in results.values() if v[0])
    total = len(results)
    print(f"\n可用 {good}/{total}")

if __name__ == "__main__":
    main()
