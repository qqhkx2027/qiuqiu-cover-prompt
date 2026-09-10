# 秋秋微信公众号封面提示词模板

先选择模式并填好 `reference_manifest`。当存在 `preserve: exact` 素材或用户要求局部修改时，不使用全画面重绘。

## GENERATE / COMPOSITE：画面阶段

```text
Create a 2.35:1 horizontal WeChat Official Account article cover for creator QIUQIU, recommended canvas 1880x800.

MODE: [GENERATE or COMPOSITE]
ARTICLE: [用一句话说明正文主题和点击理由]
REFERENCE MANIFEST: [粘贴已确认的 manifest，并说明每个文件用途]

STYLE: warm wooden study/workspace, retro pixel-game UI, bright cream window light, purple/pink/cream-yellow accents, cozy and lively, realistic person and real objects integrated with pixel atmosphere.
LAYOUT: headline-safe blank title area on the left 55-65%; QIUQIU or clean space on the right 30-40%; real subject/product/route along the bottom.
TEXT AREA: leave clean title plaques or empty space; do not render Chinese copy in the image.
CONSTRAINTS: preserve every exact asset as supplied, keep people and products unobstructed, add no unauthorized people/products/logos, keep the image bright and warm, keep 2.35:1.
NEGATIVE: no invented logos/products, no unrelated laptop/electronics unless the article requires them, no cartoon or doll-like face, no full pixel person, no dark cyber-tech mood, no unrelated decorations, no aspect-ratio change.
```

如果图像工具无法可靠留出无字区域，可以先生成背景，再在 COMPOSITE 阶段排版真实素材；不要用“Chinese characters exact”代替后期压字。

## 文字后期阶段

用 `scripts/render_cover_text.py` 在确认后的底图上压字：

```json
{
  "hook": "均价10块！",
  "title": "7款超可爱收纳小包",
  "subtitle": "日常好用，出门更轻松"
}
```

脚本会使用本机可用的中文字体、奶油黄/粉紫标题、深紫描边和游戏式投影；字体文件不需要放入 Skill 仓库。输出文件必须放到项目目录之外。

## LOCAL_EDIT

```text
MODE: LOCAL_EDIT
CURRENT COVER: [已有封面路径]
EDIT ONLY: [用户点名要改的区域]
PRESERVE: [其余必须保持不变的区域]
REPAIR: use surrounding original background to fill the edited region; do not redraw the full image.
```

## 多产品与旅行

多产品把真实 Logo 或文字名牌放在标题下方横排，空间不足时先删标签。旅行照作为路线节点或 Polaroid 组图，地点、年份和路线只能使用文章或图片已确认的信息。
