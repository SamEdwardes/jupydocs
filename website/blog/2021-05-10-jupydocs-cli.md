---
slug: jupydocs-in-development
title: jupydocs is in Development!
author: Sam Edwardes
author_url: https://github.com/SamEdwardes
author_image_url: https://avatars0.githubusercontent.com/u/18248949?s=400&u=78ed90a2387c7f44831687d50fbc467b802b6e39&v=4
tags: [update]
---
The latest release of jupydocs now comes bundled with a CLI and pyproject.toml configuration to help you better manage your docs. You can use the commands:

- `jupydocs add` to add a new .ipynb to your documentation
- `jupydocs remove` to remove a .ipynb from documentation
- `jupydocs convert` to convert all .ipynb docs to markdown

### `jupydocs add`

```bash
❯ jupydocs add website/docs/test.ipynb
Adding 1 docs to build list
Warning: website/docs/test.ipynb does not exist. 
Creating website/docs/test.ipynb.
Changes to [tool.jupydocs] `keep-input`:
~ README.ipynb
~ website/blog/2021-05-10-jupydocs-cli.ipynb
+ website/docs/test.ipynb
~ website/docs/usage_documenting_classes.ipynb
~ website/docs/usage_documenting_functions.ipynb
~ website/docs/usage_getting_started.ipynb
~ website/docs/usage_why_use_jupydocs.ipynb
```

### `jupydocs remove`

```bash
❯ jupydocs remove website/docs/test.ipynb 
Attemping to remove 1 docs from build list
Changes to [tool.jupydocs] `keep-input`:
~ README.ipynb
~ website/blog/2021-05-10-jupydocs-cli.ipynb
- website/docs/test.ipynb
~ website/docs/usage_documenting_classes.ipynb
~ website/docs/usage_documenting_functions.ipynb
~ website/docs/usage_getting_started.ipynb
~ website/docs/usage_why_use_jupydocs.ipynb
```

### `jupydocs convert`




```python

```
