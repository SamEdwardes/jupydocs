"""CLI for jupydocs

Helpful reference material for developers:
- https://github.com/sdispater/tomlkit
- https://black.readthedocs.io/en/stable/pyproject_toml.html#configuration-format
- https://github.com/python-poetry/poetry/blob/master/pyproject.toml
"""

import json
import os
import subprocess
from collections import defaultdict
from typing import List

import toml
import typer
from rich import inspect
from rich.console import Console

app = typer.Typer()
console = Console()


@app.callback()
def callback():
    """
    The jupydocs CLI is used to quickly generate python documentation using
    jupyter notebooks and markdown.
    """


help_text_pyproject_toml_path = """Path to alternative file if you do not want
to use 'pyproject.toml'. In general this option should not be used and you
should stick with the  default 'pyproject.toml'.""".replace('\n', ' ')

help_text_no_input = """If --no-input is used when the .ipynb files are
converted to .md the code cells will not be included.""".replace('\n', ' ')

help_text_jupydocs = """The jupydocs CLI is used to quickly generate python
documentation using jupyter notebooks and markdown.""".replace('\n', ' ')


@app.command()
def add(
    files_to_add: List[str] = typer.Argument(..., help="The path of each file to add to pyproject.toml"),
    pyproject_toml_path: str = typer.Option("pyproject.toml", help=help_text_pyproject_toml_path),
    no_input: bool = typer.Option(False, "--no-input", "-n", help=help_text_no_input),
):
    """
    Add new .ipynb files for jupydocs to build.
    """
    inspect(files_to_add)
    inspect(pyproject_toml_path)
    files_to_add = list(set(files_to_add))
    files_to_add.sort()
    console.print(f"[bold]Adding {len(files_to_add)} docs to build list")

    # Validate that files exist. If it does not create a new file.
    for file in files_to_add:
        if not os.path.isfile(file):
            console.print(f"[yellow]Warning: [bold]{file}[/bold] does not exist. Creating {file}.")
            create_ipynb(file)

    path, pyproject = parse_pyproject_toml(pyproject_toml_path)
    inspect(path)

    if no_input:
        key = "no-input"
    else:
        key = "keep-input"

    original_file_list = pyproject["tool"]["jupydocs"][key].copy()
    file_list = pyproject["tool"]["jupydocs"][key]
    file_list += files_to_add
    file_list = list(set(file_list))
    file_list.sort()
    pyproject["tool"]["jupydocs"][key] = file_list

    console.print(f"[bold]Changes to \[tool.jupydocs] `{key}`:")  # noqa: W605
    for file in file_list:
        if file in files_to_add and file not in original_file_list:
            console.print(f"[bold green]+ {file}")
        else:
            console.print(f"~ {file}")

    with open(path, "w") as f:
        toml.dump(pyproject, f)


@app.command()
def remove(
    files_to_remove: List[str] = typer.Argument(..., help="The path of each file to remove from pyproject.toml"),
    pyproject_toml_path: str = typer.Option("pyproject.toml", help=help_text_pyproject_toml_path),
    no_input: bool = typer.Option(False, "--no-input", "-n", help=help_text_no_input),
):
    """
    Remove .ipynb files for jupydocs to build.
    """
    files_to_remove = list(set(files_to_remove))
    console.print(
        f"[bold]Attemping to remove {len(files_to_remove)} docs from build list"
    )

    path, pyproject = parse_pyproject_toml(pyproject_toml_path)

    if no_input:
        key = "no-input"
    else:
        key = "keep-input"

    # Validate that the files provided exist in pyproject.toml. If they do not
    # warn the user.
    files_to_remove.sort()
    for file in files_to_remove:
        if file not in pyproject["tool"]["jupydocs"][key]:
            console.print(
                f"[yellow]Warning: [bold]{file}[/bold] not in pyproject.toml"
            )

    console.print(f"[bold]Changes to \[tool.jupydocs] `{key}`:")  # noqa: W605
    files_to_keep = []
    for file in pyproject["tool"]["jupydocs"][key]:
        if file in files_to_remove:
            console.print(f"[bold red]- {file}")
        else:
            files_to_keep.append(file)
            console.print(f"~ {file}")

    pyproject["tool"]["jupydocs"][key] = files_to_keep
    with open(path, "w") as f:
        toml.dump(pyproject, f)


@app.command()
def convert():
    """
    Convert .ipynb files to .md.
    """
    # Get data from pyproject.toml
    _, pyproject = parse_pyproject_toml()
    ipynb_files_keep_input = pyproject["tool"]["jupydocs"]["keep-input"]
    ipynb_files_no_input = pyproject["tool"]["jupydocs"]["no-input"]

    # Only attempt to convert files that exist
    ipynb_dict = {
        "keep-input": [i for i in ipynb_files_keep_input if os.path.isfile(i)],
        "no-input": [i for i in ipynb_files_no_input if os.path.isfile(i)],
    }

    num_files = len(ipynb_dict["keep-input"]) + len(ipynb_dict["no-input"])
    console.print(f"[bold]Converting {num_files} docs")

    with console.status("Converting docs from .ipynb to .md", spinner="runner"):
        for key, files in ipynb_dict.items():
            flag = "--no-input" if key == "no-input" else ""
            for ipynb in files:
                p = os.path.normpath(ipynb)
                bash_command = f"jupyter nbconvert --to markdown --execute {p} {flag}"
                console.log(f"{p}")
                process = subprocess.run(bash_command.split(), capture_output=True)

    console.print(
        f"[bold green]Successfully converted {num_files} .ipynb files to .md"
    )  # noqa: E501


def parse_pyproject_toml(path: str = "pyproject.toml") -> dict:
    """
    A helper function to parse the pyroject.toml file.
    """
    # Check to see if a pyproject.toml exists. If one does not exist create a
    # new file with the boilerplate for jupydocs.
    if not os.path.isfile(path):
        console.print(
            "[yellow]Warning: no [bold]pyproject.toml[/bold] file found. Creating a new one."
        )  # noqa: E501
        pyproject = {"tool": {"jupydocs": defaultdict(list)}}
    else:
        pyproject = toml.load(path)

    # Check to see if there is a `tool` section in the toml file. If not
    # create one.
    if "tool" not in pyproject:
        console.print(
            "[yellow]Warning: no [bold]\[tool.jupydocs][/bold] section found in pyproject.toml. Creating section."  # noqa: W605
        )  # noqa: E501
        pyproject["tool"] = {"jupydocs": defaultdict(list)}

    # Check if there is any jupydocs data in pyproject.toml. If not add the
    # jupydocs meta data.
    if "jupydocs" not in pyproject["tool"]:
        console.print(
            "[yellow]Warning: no [bold]\[tool.jupydocs][/bold] section found in pyproject.toml. Creating section."  # noqa: W605
        )  # noqa: E501
        pyproject["tool"]["jupydocs"] = defaultdict(list)

    # Parse the jupydocs meta data and turn into a deafultdict so it will be
    # easy to append more items.
    jupydocs_data = pyproject["tool"]["jupydocs"]
    jupydocs_data = defaultdict(list, jupydocs_data)
    pyproject["tool"]["jupydocs"] = jupydocs_data

    return path, pyproject


def create_ipynb(file: str) -> None:
    """
    Create a blank jupyter notebook file.
    """
    ipynb_data = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [f"# {os.path.splitext(os.path.split(file)[-1])[0]}"],
            }
        ],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 2,
    }
    with open(os.path.normpath(file), "w") as f:
        json.dump(ipynb_data, f)
