# 工作流与输出协议

这份文档处理输入角色、模式路由和阶段输出。视觉参数请读 [style-guide.md](style-guide.md)，跑图结构请读 [prompt-template.md](prompt-template.md)。

## Reference manifest

不要依赖图片序号猜角色。先建立一份简短清单：

```yaml
reference_manifest:
  style:
    - current_cover.png
  identity:
    - qiuqiu.jpg
  exact_assets:
    - file: workbuddy-logo.png
      role: logo
      preserve: exact
    - file: sanya-2025.jpg
      role: travel_photo
      preserve: exact
```

角色优先级：用户明确说明的角色 ＞ 当前轮图片内容判断 ＞ 项目默认资产 ＞ 历史序号约定。项目默认资产是 `assets/qiuqiu-face-reference.jpg`（`identity`）和 `assets/qiuqiu-style-reference.png`（`style`）。新增图片可使用 `current_cover`、`identity`、`style`、`product`、`logo`、`travel_photo`、`screenshot` 等角色，并明确 `preserve: exact` 是否适用。

## 模式路由

| 模式 | 允许做什么 | 适用情形 |
| --- | --- | --- |
| `GENERATE` | 重构背景、构图、像素 UI，可生成无真实素材的装饰 | 从零做新封面，主体可由模型生成 |
| `COMPOSITE` | 生成背景，真实素材后期抠图/裁切/排版，素材保持原样 | 产品、Logo、包装、截图、旅行照必须准确 |
| `LOCAL_EDIT` | 只改点名区域，用周围原背景修补 | 改字、换 Logo、修脸、删元素 |

出现“真实的、原图、保持不变、不要生造、只修改、换成这个 Logo”时，至少使用 `COMPOSITE`；已有封面局部修改使用 `LOCAL_EDIT`。

## 输入清单

| 项目 | 必需性 | 处理方式 |
| --- | --- | --- |
| 完整文章 | 必需 | 粘贴正文、提供 Markdown 内容或可读取路径；只有标题时标记「待确认」 |
| 真人参考图 | 可选 | 用 manifest 的 `identity`；无图就不画真人 |
| 真实主体图 | 按文章需要 | 产品、Logo、截图、旅行照等；只索取确实需要的图 |
| 当前封面 | `LOCAL_EDIT` 必需 | 用 manifest 的 `current_cover`，先确认要改的对象和保留项 |

## 阶段与触发

1. **收集**：缺文章只问文章，缺必要图片只问图片。
2. **分析**：记录一句话主题、点击理由、一个核心数字/结果/冲突、必须真实的对象和可删信息；每项都要有正文依据。
3. **提案**：用户说“先规划/先想标题”时输出 3 个钩子和 1 个构图并等待确认。用户说“生成封面/做一张封面/跑图”时，内部生成并选择最佳钩子后直接执行。用户已给文案时原样使用。
4. **制作**：GENERATE 或 COMPOSITE 先生成无字或少字画面，再用 `scripts/render_cover_text.py` 把确认后的中文压字；LOCAL_EDIT 只执行点名修改。
5. **验收**：检查实际尺寸和 2.35:1、正文一致性、中文逐字、人物身份、真实素材、Logo、明度、遮挡和改动范围。

## 停止条件

- 路径不可读、正文不完整或关键事实缺失：停止并写「待确认」。
- 必要真实素材缺失：说明缺哪张，并给出文字名/留白替代方案。
- 生成失败、尺寸不符或文字不可读：不声称成功，只保留已确认文案和失败项。
- 图片输出必须在项目目录之外；用户未指定目录时先询问。

## 建议的最终回报

```text
模式：COMPOSITE
已生成：/absolute/path/outside/project/cover.png
尺寸：1880×800（2.35:1）
文案：...
reference_manifest：...
文字后期：已压字 / 未执行（原因）
已检查：...
待确认：...
```
