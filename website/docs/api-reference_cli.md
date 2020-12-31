---
id: cli
title: Command line interface
---
jupydocs comes with a command line interface (CLI) to help quickly build and render your `.ipynb` files into `.md` files. The CLI was inpired by the [spaCy](https://spacy.io/api/cli) CLI tool.

## Build

### Arguments

| Argument           | Type       | Description                                                  |
| ------------------ | ---------- | ------------------------------------------------------------ |
| `directories`      | positional | The directory to search for .ipynb files. The relative path to .ipynb file can also be provided, in which case only that single  file will be converted. By default '.' (current working directory). |
| `--walk`, `w`      | flag       | If flag is included `build` will search the provided directory and all subdirectories for .ipynb files. |
| `--old`, `-o`      | flag       | If flag is included `build` will render all found .ipynb files even if no changes have occurred since the last build. |
| `--no-input`, `-n` | option     | Specify if the markdown files should be rendered with or without the input code cells. Use 'i' to include the input or 'n' to not include the input. If multiple files are provided you can provide multiple characters matching the order of the file to convert. For example if you pass two .ipynb files to be converted you could include input for the first and not the second by passing 'in'. |


### Examples

(1) run on all changed .ipynb files in current working directory.
```bash
python -m jupydocs build .
```

(2) run on all changed .ipynb files in current working directory and
child directories.
```bash
python -m jupydocs build . --walk
```

(3) run on all .ipynb files in current working directory and child
directories including files that have not been changed since the last build.
```bash
python -m jupydocs build . --walk --old
```

(4) run on two specified files and do not include any input code.
```bash
python -m jupydocs build --no-input n \
    README.ipynb \
    website/docs/usage_getting_started.ipynb
```

(5) run on two specified files and do not include any input code for the
first file but do include for the second file
```bash
python -m jupydocs build --no-input ni \
    README.ipynb \
    website/docs/usage_getting_started.ipynb
```

(6) run on all .ipynb files in the current working directory including
files that have not been changed since the last build
```bash
python -m jupydocs build . --old
```
