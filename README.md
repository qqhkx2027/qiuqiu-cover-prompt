# qiuqiu-cover-prompt

秋秋封面提示词技能：从文章、Markdown 和参考图片生成可直接用于即梦、Seedream、Nano Banana 或 GPT Image 的中文封面提示词。

## 支持的输出

| 类型 | 画幅 | 尺寸 |
|---|---:|---:|
| 小红书图文笔记 | 3:4 竖版 | 1080×1440px |
| 微信公众号头条头图（推送列表封面） | 2.35:1 横版 | 900×383px |

如果没有指定平台，技能会先询问选择哪一种；如果两种都需要，会分别生成两套构图提示词。

## 安装

只将技能文件复制到 Codex skills 目录（仓库 README 不必复制）：

```bash
mkdir -p ~/.codex/skills/qiuqiu-cover-prompt
cp SKILL.md ~/.codex/skills/qiuqiu-cover-prompt/
cp -R agents references ~/.codex/skills/qiuqiu-cover-prompt/
```

然后在 Codex 中调用：

```text
使用 $qiuqiu-cover-prompt，根据这篇文章生成小红书 3:4 封面提示词。
```

## 主要能力

- 10 种封面构图风格
- 真人脸、旧封面、产品/UI 截图的参考图角色分配
- 长中文标题分行、安全区和错字检查
- 小红书与微信公众号尺寸预设
- 支持只生成提示词，或在用户明确要求时直接跑图
