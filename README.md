# 🌍 国外新闻直播源 (TVBox)

支持最新版 **TVBox / 影视仓 / FongMi 影视** 等空壳软件的国外新闻直播源，均为公开免费流，每日自动检测更新。

## 📺 频道列表（14 个，2026-09-28 验证）

### 国际新闻
| 频道 | 备注 |
|------|------|
| 🇬🇧 BBC World News | 英国广播公司 |
| 🇺🇸 CNN International | 美国有线新闻网 |
| 🇶🇦 Al Jazeera English | 半岛电视台（卡塔尔） |
| 🇬🇧 Sky News | 天空新闻（英国） |
| 🇫🇷 France 24 English | 法国 24 |
| 🇩🇪 DW English | 德国之声 |
| 🇪🇺 Euronews English | 欧洲新闻 |
| 🇸🇬 CNA International | 亚洲新闻台（新加坡） |

### 地区新闻
| 频道 | 备注 |
|------|------|
| 🇦🇪 Sky News Arabia | 天空新闻阿拉伯语（阿联酋） |
| 🇺🇸 ABC News | 美国广播公司 |
| 🇺🇸 ABC News Live | ABC 24小时流 |
| 🇯🇵 NHK World-Japan | 日本放送协会 |
| 🇹🇷 TRT World | 土耳其广播公司 |
| 🇦🇺 Sky News Australia | 天空新闻（澳洲） |

## 🔗 使用方式

### TVBox（安卓电视/手机）
1. 打开 TVBox → 设置 → 配置地址
2. 粘贴以下任一地址 → 保存

```
https://cdn.jsdelivr.net/gh/Creazy-youyou/tvbox_setfile@main/live.txt
```

或者直接用 raw 地址：

```
https://raw.githubusercontent.com/Creazy-youyou/tvbox_setfile/main/live.txt
```

### TVBox JSON 接口配置
```
https://raw.githubusercontent.com/Creazy-youyou/tvbox_setfile/main/tvbox.json
```

### 通用播放器（TiviMate / APTV / VLC）
```
https://raw.githubusercontent.com/Creazy-youyou/tvbox_setfile/main/live.m3u
```

## 🔄 自动更新

本仓库通过 GitHub Actions 每日自动检测所有直播源可用性，失效的源会被自动注解更新。也可以手动触发：

```
Actions → 检查直播源 → Run workflow
```

## ⚠️ 免责声明

- 所有直播源均来自互联网公开渠道，仅供个人学习、测试与研究使用
- 请在下载/使用后 **24 小时内删除**
- 若侵犯您的版权，请联系删除
- 源可能随时失效，请以实际播放为准
