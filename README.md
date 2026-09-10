# qiuqiu-cover-prompt

「秋秋」微信公众号封面 Skill。它把一篇真实文章转换成统一的 2.35:1 横版封面：先读正文、提炼钩子、确认素材和文案，再生成或编辑图片。

Skill 的规范名称是 `$qiuqiu-wechat-cover`；`qiuqiu-cover-prompt` 是仓库名称。

## 能做什么

- 好物分享、AI 工具测评、旅行、学习效率、数码体验和桌面改造封面
- 固定暖木色复古像素工作台风格，保留真人秋秋和真实产品的辨识度
- 新封面、真实素材合成与已有封面局部编辑
- 角色清单驱动的参考图管理，避免依赖“图 1 / 图 2”顺序
- 用本机字体把确认后的中文确定性地压到无字底图上
- 生成前提炼 3 个钩子，生成后检查比例、文字和素材一致性

它不替代正文策划，也不会在缺少文章、真人照、产品图或 Logo 时自行编造事实。

## 使用方式

把本仓库交给支持加载 Skill 的智能体，然后这样调用：

> 使用 `$qiuqiu-wechat-cover`，为这篇公众号文章生成封面：`/path/to/article.md`

调用时：

1. 提供完整正文、Markdown 内容或可读取的本地路径。
2. 用 `reference_manifest` 声明图片角色；对话中附带的新图按角色覆盖默认资产，不依赖序号。
3. 按文章需要补充产品、Logo、截图、旅行照或旧封面，不需要的素材不用提供。
4. 说“先规划/先想标题”时先看方案；说“生成封面/做一张封面/跑图”时可直接执行；已给文案则原样使用。
5. 有必须原样保留的真实素材时走 `COMPOSITE`，只改已有封面局部时走 `LOCAL_EDIT`。

详细输入、阶段输出和失败处理见 [references/workflow.md](references/workflow.md)。

## 目录

```text
SKILL.md                         入口规则与硬约束
agents/openai.yaml              UI 展示和默认调用提示
references/workflow.md          输入角色、阶段协议、编辑边界
references/style-guide.md       2.35:1 视觉系统
references/prompt-template.md   可复制的生成提示词结构
references/prompt-checklist.md  生成前后验收清单
assets/                         默认真人和风格参考图
examples/                       已完成的示例
scripts/validate_skill.py      本地和 CI 校验
scripts/render_cover_text.py   用本机字体确定性压字
```

生成的 PNG/JPG/WebP 默认保存到项目目录之外。调用时请提供保存目录；仓库不接收生成图片。

## 本地校验

```bash
python3 scripts/validate_skill.py .
```

GitHub Actions 会在提交时运行同一校验。压字脚本需要 Pillow；校验器本身只检查结构、链接和必需资产，不替代生成后的视觉验收。

## 安装

仓库地址：<https://github.com/qqhkx2027/qiuqiu-cover-prompt>

安装后请读取 `SKILL.md`，按需读取 `references/`；项目已内置 `assets/` 下的默认身份和风格参考图。生成图片请保存到项目目录之外。

当前仓库包含默认真人身份参考图。若不希望公开分发，请移除 `assets/qiuqiu-face-reference.jpg`，并在调用时提供 `identity` 图片。

## 许可

MIT License
