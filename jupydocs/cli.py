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

import typer
from rich import inspect
from rich.console import Console
import tomlkit


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
    files_to_add = list(set(files_to_add))
    files_to_add.sort()
    console.print(f"[bold]Adding {len(files_to_add)} docs to build list")

    # Validate that files exist. If it does not create a new file.
    for file in files_to_add:
        if not os.path.isfile(file):
            console.print(f"[yellow]Warning: [bold]{file}[/bold] does not exist. Creating {file}.")
            create_ipynb(file)

    path, pyproject = parse_pyproject_toml(pyproject_toml_path)

    original_file_list = list(pyproject["tool"]["jupydocs"]["docs"].keys())
    all_files = original_file_list + files_to_add
    all_files = list(set(all_files))
    all_files.sort()

    if no_input:
        output_style = "no-input"
    else:
        output_style = "keep-input"

    console.print("[bold]Changes to \[tool.jupydocs.docs]:")  # noqa: W605
    for file in all_files:
        if file in original_file_list:
            console.print(f"  ~ {file}")
        else:
            console.print(f"  [bold green]+ {file}")
            file_table = tomlkit.inline_table()
            file_table["output-style"] = output_style
            file_table["output-directory"] = file
            pyproject["tool"]["jupydocs"]["docs"][file] = file_table

    with open(path, "w") as f:
        f.write(tomlkit.dumps(pyproject))


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

    original_files = list(pyproject["tool"]["jupydocs"]["docs"].keys())
    all_files = list(set(original_files + files_to_remove))
    all_files.sort()

    # Validate that the files provided exist in pyproject.toml. If they do not
    # warn the user.
    files_to_remove.sort()
    for file in files_to_remove:
        if file not in original_files:
            console.print(f"[yellow]Warning: [bold]{file}[/bold] not in pyproject.toml")

    console.print("[bold]Changes to \[tool.jupydocs.docs]:")  # noqa: W605

    for file in all_files:
        if file in files_to_remove and file in original_files:
            console.print(f"  [bold red]- {file}")
            del pyproject["tool"]["jupydocs"]["docs"][file]
        elif file in original_files:
            console.print(f"  ~ {file}")

    with open(path, "w") as f:
        f.write(tomlkit.dumps(pyproject))


@app.command()
def convert(
    pyproject_toml_path: str = typer.Option("pyproject.toml", help=help_text_pyproject_toml_path)
):
    """
    Convert .ipynb files to .md.
    """
    # Get data from pyproject.toml
    _, pyproject = parse_pyproject_toml(pyproject_toml_path)
    
    with console.status("Converting docs from .ipynb to .md", spinner="runner"):
        for file, data in pyproject["tool"]["jupydocs"]["docs"].items():
            if not os.path.isfile:
                console.print(f"[yellow]Warning: [bold]{file}[/bold] does not exist.")
            else:
                flag = "--no-input" if data["output-style"] == "no-input" else ""
                p = os.path.normpath(file)
                bash_command = f"jupyter nbconvert --to markdown --execute {p} {flag}"
                console.log(f"{p}")
                process = subprocess.run(bash_command.split(), capture_output=True)
                if process.returncode == 1:
                    console.print(f"[red]Error: {p} failed to convert.")

    console.print(f"[bold green]Complete!")
    

@app.command()
def show(
    pyproject_toml_path: str = typer.Option("pyproject.toml", help=help_text_pyproject_toml_path)
):
    """
    Show currenty jupydocs settings.
    """
    _, pyproject = parse_pyproject_toml(pyproject_toml_path)
    console.print(dict(pyproject["tool"]["jupydocs"]["docs"]))


@app.command()
def clear(
    pyproject_toml_path: str = typer.Option("pyproject.toml", help=help_text_pyproject_toml_path),
    do_not_prompt: bool = typer.Option(False, help="Skip the user prompt?")
):
    """
    Show currenty jupydocs settings.
    """
    console.print("[yellow]Warning: `clear` will delete all contents in \[tool.jupydocs.docs].")
    
    if do_not_prompt:
        run_clear = "yes"
    else:
        run_clear = typer.prompt("Are you sure you want to continue?[yes/no]")
    
    if run_clear.lower()[0] == "y":
        path, pyproject = parse_pyproject_toml(pyproject_toml_path)
    
        pyproject["tool"]["jupydocs"]["docs"] = tomlkit.table()
        
        with open(path, "w") as f:
            f.write(tomlkit.dumps(pyproject))


def parse_pyproject_toml(path: str = "pyproject.toml") -> dict:
    """
    A helper function to parse the pyroject.toml file.
    """
    # Check to see if a pyproject.toml exists. If one does not exist create a
    # new file with the boilerplate for jupydocs.
    if not os.path.isfile(path):
        console.print("[yellow]Warning: no [bold]pyproject.toml[/bold] file found. Creating a new one.")  # noqa: E501 # fmt: off
        pyproject = tomlkit.document()
    else:
        with open(path, 'r') as f:
            pyproject = tomlkit.parse(f.read())

    # Check to see if the [tool] table exists.
    if "tool" not in pyproject:
        pyproject["tool"] = tomlkit.table()

    # Check to see if [tool.jupydocs] table exists.
    if "jupydocs" not in pyproject["tool"]:
        pyproject["tool"]["jupydocs"] = tomlkit.table()

    warning_text = "[yellow]Warning: creating [bold]\[tool.jupydocs.docs][/bold] in pyproject.toml."  # noqa: E501 W605
    # Check to see if [tool.jupydocs.docs] table exists
    if "docs" not in pyproject["tool"]["jupydocs"]:
        console.print(warning_text)
        pyproject["tool"]["jupydocs"]["docs"] = tomlkit.table()

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
