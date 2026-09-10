# 示例：只删一句话

## 路由

`LOCAL_EDIT`：已有封面作为 `current_cover`，只删指定文字并修补原背景。

```yaml
reference_manifest:
  current_cover: [cover.png]
```

```text
EDIT ONLY: 删除左上角“5个月真实使用”
PRESERVE: 人物、产品、Logo、主标题、配色、构图和其余文字
REPAIR: 用相邻木墙和 UI 背景自然补齐；不得整张重绘
```
