---
id: jupydocs_work_flow
title: jupydocs Work Flow
---

There are three main components to using jupydocs to document your library:

1. Writing your docstrings in a [NumPy compliant style](https://numpydoc.readthedocs.io/en/latest/format.html).
2. Organizing your documentation in one or many jupyter notebooks.
3. Use a static site generator to share your docs with the world.

To use jupydocs effectvely and effeciently you can build a simple workflow.

## Workflow step 1 - Write your docstrings

As you are authoring or your python library write your docstrings as you normally would. Nothing fancy happening here.

## Workflow step 2 - Organize your documentation in a jupyter notebook

There is not right way to organize your docs. As a general starting point it would probably make sense to have a separate jupyter notebook for each module. You can order the functions in what ever way that makes the most sense (alphabetical, logical, etc.). Each function that you wish to document you need to specifically call out in the jupyter notebook. Your notebook will probably look something like this:

```python
# docs/mypackage_api_reference.ipynb
from jupydocs.numpydocstring import NumpyDocString

from mypackage.mypackage import my_function_1, my_function_2

NumpyDocString(my_function_1).render_md()

NumpyDocString(my_function_2).render_md()
```

As you have new functions, or new modules you will need to add them to a notebook as well.

## Workflow step 3 - Convertying `.ipynb` to `.md`

Now that you have your jupyter notebooks set up you need to convert them to markdown so they can be used by a static site generator. Jupyter provides a handy tool called [nbconvert](https://github.com/jupyter/nbconvert) that can help us. If you have pip installed jupydocs you should already have nbconvert as well.

You can execute and convert the notebook you just created using:

```bash
jupyter nbconvert --to markdown --execute docs/mypackage_api_reference.ipynb --no-input
```

Notice that `--no-input` flag at the end of the command. This will hide the code cells and only show the output in your rendered markdown file. Sometimes you may not want to include this flag if you are generating documentation where you do not want to hide the code (e.g. README, an vignette, etc.).

If you have several or many .ipynb files to convert I recommend using a script to automate the process. For example:

```bash
# scripts/build_docs.sh
# usage: bash scripts/build_docs.sh

echo "-----------------------------------"
echo "Convert .ipynb to markdown"
echo "-----------------------------------"
jupyter nbconvert --to markdown --execute docs/mypackage_api_reference.ipynb --no-input
```

Now every time you update a docstring you only need to call `bash scripts/build_docs.sh` and your markdown files will be updated. Check out the [build_docs.sh](https://github.com/SamEdwardes/jupydocs/blob/main/scripts/build_docs.sh) for jupydocs if you need inspiration.

## Workflow step 4 - Publish using a static site generator

Now that you have your rendered markdown files you can use any static site generator to render your docs. A few popular options include:

- [Docusaurus](https://v2.docusaurus.io/) (jupydocs website is built with Docusaurus)
- [Hugo](https://gohugo.io/)
- [GitHub Pages](https://pages.github.com/)

You could even using a static site generator and keep your markdown files in your git repo, linking to them in the README. But I would recommend using a static site generator. It is a little bit of extra effort but your package much more professional looking.
