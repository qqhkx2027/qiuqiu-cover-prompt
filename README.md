# qiuqiu-cover-prompt

秋秋封面提示词技能：从文章、Markdown 和参考图片生成可直接用于即梦、Seedream、Nano Banana 或 GPT Image 的中文封面提示词。

这是一个通用的 `SKILL.md + references/` 技能包，不绑定某一个智能体。只要你的智能体支持加载技能文件、项目指令或自定义 system prompt，就可以安装使用。

## 支持的输出

| 类型 | 画幅 | 尺寸 |
|---|---:|---:|
| 小红书图文笔记 | 3:4 竖版 | 1080×1440px |
| 微信公众号头条头图（推送列表封面） | 2.35:1 横版 | 900×383px |

如果没有指定平台，技能会先询问选择哪一种；如果两种都需要，会分别生成两套构图提示词。

## 安装到任意智能体

先下载仓库：

```bash
git clone https://github.com/qqhkx2027/qiuqiu-cover-prompt.git
cd qiuqiu-cover-prompt
```

然后把下面三部分放进目标智能体的“技能目录 / 指令目录 / 项目规则目录”：

```text
SKILL.md
agents/openai.yaml       # 可选：界面元数据，不影响核心能力
references/               # 与 SKILL.md 同级保存
```

不同智能体的目录名称可能不同：

- 支持 skills 的智能体：将整个仓库目录放入它的 skills 目录。
- 只支持项目规则的智能体：将 `SKILL.md` 作为项目指令，并把 `references/` 放在同级目录。
- 只支持 system prompt 的智能体：把 `SKILL.md` 内容加入 system prompt，按需一并提供 `references/` 文件。

不要只复制 README；`SKILL.md` 是核心入口，`references/` 是详细规则。

### Codex 示例

```bash
mkdir -p ~/.codex/skills/qiuqiu-cover-prompt
cp SKILL.md ~/.codex/skills/qiuqiu-cover-prompt/
cp -R agents references ~/.codex/skills/qiuqiu-cover-prompt/
```

### 其他智能体示例

将仓库放入该智能体文档要求的 skills 目录，例如：

```bash
cp -R qiuqiu-cover-prompt <你的智能体 skills 目录>/qiuqiu-cover-prompt
```

安装后，用自然语言触发即可，例如：

```text
根据这篇文章生成小红书 3:4 封面提示词。
```

## 主要能力

- 10 种封面构图风格
- 真人脸、旧封面、产品/UI 截图的参考图角色分配
- 长中文标题分行、安全区和错字检查
- 小红书与微信公众号尺寸预设
- 支持只生成提示词，或在用户明确要求时直接跑图
