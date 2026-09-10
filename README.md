# qiuqiu-cover-prompt

为公众号「秋秋」生成统一品牌风格的 2.35:1 文章封面。
在固定的「暖木色复古像素游戏工作台 + 真人秋秋 + 真实主体素材」视觉体系中，按每篇文章真实主题替换标题与素材，不再每次重新发明封面。

## 定位

- 固定比例：2.35:1（公众号头条封面）
- 固定风格：暖木像素工作台、紫 / 粉 / 奶油黄强调、像素 UI
- 先读文章 -> 提炼钩子 -> 控制文字 20~35 字 -> 再生成
- 真实优先：有真人照就用真人；有产品 / Logo / 旅行照就原位使用，不重绘
- 不虚构：无参考时不生成替身人物，不编造 Logo

## 目录

    SKILL.md                         # 主流程与规则
    agents/openai.yaml              # 智能体展示信息
    references/style-guide.md       # 公众号 2.35:1 风格指南
    references/prompt-template.md   # 标准跑图 Prompt 模板
    tools/validate_skill.py         # 本地校验
    examples/                       # 封面示例（按需添加）

## 安装

把下面这行和仓库地址发给支持加载 Skill 的智能体：

请安装这个技能仓库，并读取其中的 SKILL.md 与 references/：
https://github.com/qqhkx2027/qiuqiu-cover-prompt

安装后可说：调用 qiuqiu-wechat-cover，为这篇文章生成公众号封面。

## 本地校验

python3 tools/validate_skill.py .

## 许可

MIT License。

