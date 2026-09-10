# qiuqiu-cover-prompt

为公众号「秋秋」生成统一品牌风格的 2.35:1 文章封面。
在固定的「暖木色复古像素游戏工作台 + 真人秋秋 + 真实主体素材」视觉体系中，按每篇文章真实主题替换标题与素材，不再每次重新发明封面。

## 定位

- 固定比例：2.35:1（公众号头条封面）
- 固定风格：暖木像素工作台、紫 / 粉 / 奶油黄强调、像素 UI
- 先读文章 -> 提炼钩子 -> 控制文字 20~35 字 -> 再生成
- 真实优先：有真人照就用真人；有产品 / Logo / 旅行照就原位使用，不重绘
- 不虚构：无参考时不生成替身人物，不编造 Logo

## 调用时会发生什么

调用技能后，它会按顺序处理：

1. 没有文章时，先请你粘贴公众号正文或提供 Markdown 路径。
2. 当前对话的图 1 作为秋秋真人参考，图 2 作为整体风格参考。
3. 根据文章主题，只询问必要的产品图、Logo、截图或旅行照；新增素材从图 3 开始编号。
4. 文章和素材齐备后，先给出主题判断、3 个封面钩子和推荐构图。
5. 你确认文案并明确说“生成/跑图”后，才生成 2.35:1 封面。

图 1 只负责人物身份，图 2 只负责风格；两张图都不会被原样复制。

## 目录

    SKILL.md                         # 主流程与规则
    agents/openai.yaml              # 智能体展示信息
    references/style-guide.md       # 公众号 2.35:1 风格指南
    references/prompt-template.md   # 标准跑图 Prompt 模板
    references/assets/qiuqiu-face-reference.jpg  # 默认图 1：真人身份
    references/assets/qiuqiu-style-reference.png # 默认图 2：整体风格
    tools/validate_skill.py         # 本地校验
    examples/                       # 封面示例（按需添加）

## 安装

把下面这行和仓库地址发给支持加载 Skill 的智能体：

请安装这个技能仓库，并读取其中的 SKILL.md 与 references/：
https://github.com/qqhkx2027/qiuqiu-cover-prompt

安装后可说：调用 qiuqiu-wechat-cover，为这篇文章生成公众号封面。

项目已内置图 1 和图 2。调用时如果附带新图，新图优先；新增产品、Logo、截图或旅行照从图 3 开始编号。

## 本地校验

python3 tools/validate_skill.py .

## 许可

MIT License。
