# qiuqiu-cover-prompt

「秋秋」微信公众号封面 Skill。它把一篇真实文章转换成统一的 2.35:1 横版封面：先读正文、提炼钩子、确认素材和文案，再生成或编辑图片。

Skill 的规范名称是 `$qiuqiu-wechat-cover`；`qiuqiu-cover-prompt` 是仓库名称。

## 能做什么

- 好物分享、AI 工具测评、旅行、学习效率、数码体验和桌面改造封面
- 固定暖木色复古像素工作台风格，保留真人秋秋和真实产品的辨识度
- 新封面与已有封面局部编辑
- 生成前提炼 3 个钩子，生成后检查比例、文字和素材一致性

它不替代正文策划，也不会在缺少文章、真人照、产品图或 Logo 时自行编造事实。

## 使用方式

把本仓库交给支持加载 Skill 的智能体，然后这样调用：

> 使用 `$qiuqiu-wechat-cover`，为这篇公众号文章生成封面：`/path/to/article.md`

调用时：

1. 提供完整正文、Markdown 内容或可读取的本地路径。
2. 默认图 1 是真人身份参考，默认图 2 是整体风格参考；对话中附带的新图优先。
3. 按文章需要补充产品、Logo、截图、旅行照或旧封面，不需要的素材不用提供。
4. 先查看主题判断、3 个钩子和构图建议，确认文案后再明确说“生成/跑图”。

详细输入、阶段输出和失败处理见 [references/workflow.md](references/workflow.md)。

## 目录

```text
SKILL.md                         入口规则与硬约束
agents/openai.yaml              UI 展示和默认调用提示
references/workflow.md          输入角色、阶段协议、编辑边界
references/style-guide.md       2.35:1 视觉系统
references/prompt-template.md   可复制的生成提示词结构
references/prompt-checklist.md  生成前后验收清单
references/assets/              默认图 1、图 2
examples/                       已完成的示例
tools/validate_skill.py         本地和 CI 校验
outputs/                        已生成的封面样例
```

## 本地校验

```bash
python3 tools/validate_skill.py .
```

GitHub Actions 会在提交时运行同一校验。校验只检查结构、链接和必需资产，不替代生成后的视觉验收。

## 安装

仓库地址：<https://github.com/qqhkx2027/qiuqiu-cover-prompt>

安装后请读取 `SKILL.md`，按需读取 `references/`；项目已内置默认图 1 和图 2。

## 许可

MIT License
