# 失败护栏：常见翻车与修复

这些案例用于选择模式和复核结果，不是新的硬性文案模板。

| 翻车 | 修复 |
| --- | --- |
| Logo 与产品名对调 | 用 `reference_manifest` 明确 `role: logo`，走 `COMPOSITE` |
| 删除文字后留下透明洞 | 走 `LOCAL_EDIT`，用周围原背景修补 |
| 只说“修脸”却整张重绘 | 走 `LOCAL_EDIT`，只改脸部区域 |
| 用户给了真实本子，模型重新画了一批 | 将本子列为 `exact_assets`，走 `COMPOSITE` |
| 标题出现重复字、漏字或英文 | 生成无字底图，使用 `scripts/render_cover_text.py` 后期压字 |

复核时，先问“模式是否选错”，再调整提示词细节。
