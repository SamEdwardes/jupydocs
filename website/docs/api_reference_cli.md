---
id: module_cli
title: cli module
---

# `jupydocs`

The jupydocs CLI is used to quickly generate python documentation using
jupyter notebooks and markdown.

**Usage**:

```console
$ jupydocs [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `add`: Add new .ipynb files for jupydocs to build.
* `convert`: Convert .ipynb files to .md.
* `remove`: Remove .ipynb files for jupydocs to build.

## `jupydocs add`

Add new .ipynb files for jupydocs to build.

**Usage**:

```console
$ jupydocs add [OPTIONS] FILES_TO_ADD...
```

**Arguments**:

* `FILES_TO_ADD...`: The path of each file to add to pyproject.toml  [required]

**Options**:

* `--pyproject-toml-path TEXT`: Path to alternative file if you do not want to use 'pyproject.toml'. In general this option should not be used and you should stick with the  default 'pyproject.toml'.  [default: pyproject.toml]
* `-n, --no-input`: If --no-input is used when the .ipynb files are converted to .md the code cells will not be included.  [default: False]
* `--help`: Show this message and exit.

## `jupydocs convert`

Convert .ipynb files to .md.

**Usage**:

```console
$ jupydocs convert [OPTIONS]
```

**Options**:

* `--pyproject-toml-path TEXT`: Path to alternative file if you do not want to use 'pyproject.toml'. In general this option should not be used and you should stick with the  default 'pyproject.toml'.  [default: pyproject.toml]
* `--help`: Show this message and exit.

## `jupydocs remove`

Remove .ipynb files for jupydocs to build.

**Usage**:

```console
$ jupydocs remove [OPTIONS] FILES_TO_REMOVE...
```

**Arguments**:

* `FILES_TO_REMOVE...`: The path of each file to remove from pyproject.toml  [required]

**Options**:

* `--pyproject-toml-path TEXT`: Path to alternative file if you do not want to use 'pyproject.toml'. In general this option should not be used and you should stick with the  default 'pyproject.toml'.  [default: pyproject.toml]
* `-n, --no-input`: If --no-input is used when the .ipynb files are converted to .md the code cells will not be included.  [default: False]
* `--help`: Show this message and exit.
