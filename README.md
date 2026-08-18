# qiuqiu-cover-prompt

秋秋封面提示词 Skill：把文章、Markdown 和参考图片整理成可直接交给生图模型的中文封面提示词。

> Qiuqiu cover prompt skill for platform-specific Chinese cover generation.

## 支持的平台

平台会自动决定基础视觉，构图模式单独选择：

| 平台 | 基础视觉 | 画幅与推荐尺寸 |
| --- | --- | --- |
| 微信公众号头条头图 | 秋秋同款星露谷像素风 | 2.35:1｜900×383px |
| 视频号 / B 站横版 | 秋秋同款抠像风格 | 16:9｜1920×1080px |
| 抖音 / 快手竖版 | 秋秋同款抠像风格 | 9:16｜1080×1920px |
| 小红书图文笔记 | 秋秋同款抠像风格 | 3:4｜1080×1440px |

## 能做什么

- 从文章提炼主题、卖点和标题候选。
- 用 10 种构图模式组织人物、产品、标题和留白关系。
- 分配人物照片、旧封面、产品截图和 Logo 的参考角色。
- 保留正式标题，处理长标题换行、安全区和中文错字风险。
- 默认只生成提示词；用户明确要求时再调用图像工具跑图。
- 适配产品主视觉、局部出镜、人物侧置和正面对视等常见封面需求。

## 安装

把下面这句话和仓库地址发给支持加载 Skill 的智能体：

```text
请安装这个技能仓库，并读取其中的 SKILL.md、references/ 和 agents/：
https://github.com/qqhkx2027/qiuqiu-cover-prompt
```

安装后可以直接说：

```text
调用 qiuqiu-cover-prompt，为这篇文章生成抖音、快手、小红书竖版封面提示词。
```

## 工作流程

1. 读取文章、平台、标题和已提供的图片。
2. 只询问尚未确定的一个关键问题。
3. 确认构图模式、人物动作和参考图用途。
4. 输出平台尺寸、视觉方案和完整中文提示词。
5. 用户明确要求时，再执行跑图并检查标题和主体边缘。

## 目录

```text
SKILL.md                         # 主流程与交互规则
agents/openai.yaml               # 智能体展示信息
references/output-presets.md     # 平台比例、尺寸与安全区
references/style-guide.md        # 星露谷像素 / 抠像视觉规范
references/style-templates.md    # 10 种构图模式
references/title-and-reference-rules.md
references/prompt-checklist.md
tools/validate_skill.py          # 无依赖的本地校验脚本
```

## 本地校验

```bash
python3 tools/validate_skill.py .
```

## 许可

MIT License。详见 [LICENSE](LICENSE)。
