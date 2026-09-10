# 示例：收纳小包合集

## 路由

`COMPOSITE`：收纳包、包装或本子等真实物品列为 `exact_assets`，背景和 UI 另行生成。

## reference_manifest

```yaml
reference_manifest:
  identity: [qiuqiu.jpg]
  style: [assets/qiuqiu-style-reference.png]
  exact_assets:
    - file: pouch-camera.jpg
      role: product
      preserve: exact
    - file: pouch-toiletry.jpg
      role: product
      preserve: exact
```

只放 2～3 个代表性产品；其余信息交给标题，不做七个产品的功能清单。
