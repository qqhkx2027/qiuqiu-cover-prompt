# 示例：MacBook 好物测评

## 路由

`COMPOSITE`：电脑照片和真人身份需要保持真实，背景和像素 UI 可以生成。

## reference_manifest

```yaml
reference_manifest:
  identity: [qiuqiu.jpg]
  style: [assets/qiuqiu-style-reference.png]
  exact_assets:
    - file: macbook.jpg
      role: product
      preserve: exact
```

## 文案

- 小钩子：3K 多拿下！
- 主标题：值不值得买？
- 补充：5 个月真实使用体验

画面阶段留出左侧标题牌，中文由后期脚本压字。
