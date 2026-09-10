# 示例：旅行照片封面

## 路由

`COMPOSITE`：四张旅行照必须使用原图，像素风只用于背景、路线和相框。

## reference_manifest

```yaml
reference_manifest:
  style: [assets/qiuqiu-style-reference.png]
  exact_assets:
    - file: xinjiang-2023.jpg
      role: travel_photo
      preserve: exact
    - file: weihai-2024.jpg
      role: travel_photo
      preserve: exact
    - file: sanya-2025.jpg
      role: travel_photo
      preserve: exact
    - file: dali-2026.jpg
      role: travel_photo
      preserve: exact
```

地点、年份和路线只从文章与照片确认；不生成替代旅行照。
