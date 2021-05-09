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
from os.path import isfile, join
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
    jupydocs CLI
    """


def parse_pyproject_toml(path: str = 'pyproject.toml') -> dict:
    """
    A helper function to parse the pyroject.toml file.
    """
    # Check to see if a pyproject.toml exists. If one does not exist create a
    # new file with the boilerplate for jupydocs.
    if not os.path.isfile(path):
        console.print("[red]No [bold]pyproject.toml[/bold] file found. Creating a new one.[/red]")  # noqa: E501
        pyproject = {'tool': {'jupydocs': defaultdict(list)}}
    else:
        pyproject = toml.load(path)

    # Check to see if there is a `tool` section in the toml file. If not
    # create one.
    if 'tool' not in pyproject:
        console.print("[red]No [bold]\[tool.jupydocs][/bold] section found in pyproject.toml. Creating section.[/red]")  # noqa: E501
        pyproject['tool'] = {'jupydocs': defaultdict(list)}

    # Check if there is any jupydocs data in pyproject.toml. If not add the
    # jupydocs meta data.
    if 'jupydocs' not in pyproject['tool']:
        console.print("[red]No [bold]\[tool.jupydocs][/bold] section found in pyproject.toml. Creating section.[/red]")  # noqa: E501
        pyproject['tool']['jupydocs'] = defaultdict(list)

    # Parse the jupydocs meta data and turn into a deafultdict so it will be
    # easy to append more items.
    jupydocs_data = pyproject['tool']['jupydocs']
    jupydocs_data = defaultdict(list, jupydocs_data)
    pyproject['tool']['jupydocs'] = jupydocs_data

    return path, pyproject


def create_ipynb(file):
    """
    Create a blank jupyter notebook file.
    """
    ipynb_data = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {os.path.splitext(os.path.split(file)[-1])[0]}"
                ]
            }
        ],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 2
    }
    with open(os.path.normpath(file), 'w') as f:
        json.dump(ipynb_data, f)


@app.command()
def add(
    files: List[str] = typer.Argument(..., help="In progress"),
    no_input: bool = typer.Option(False, help="In progress")
):
    """
    Add new .ipynb files for jupydocs to build.

    Examples
    > python -m jupydocs add website/docs/usage_getting_started.ipynb website/docs/usage_why_use_jupydocs.ipynb
    > python -m jupydocs add website/docs/api_reference_numpy_module.ipynb --no-input
    """
    files = list(set(files))
    files.sort()
    console.print(f"[bold]Adding {len(files)} docs to build list")
    # Validate that files exist
    # for file in files:
    #     if not os.path.isfile(file):
    #         raise FileNotFoundError(f"{file} does not exist.")
    path, pyproject = parse_pyproject_toml()

    if no_input:
        key = 'no-input'
    else:
        key = 'keep-input'
    original_file_list = pyproject['tool']['jupydocs'][key].copy()
    file_list = pyproject['tool']['jupydocs'][key]
    file_list += files
    file_list = list(set(file_list))
    file_list.sort()
    pyproject['tool']['jupydocs'][key] = file_list

    console.print(f"[bold]Changes ({key}):")
    for file in file_list:
        if file in files and file not in original_file_list:
            console.print(f"[bold green]\t+ {file}")
        else:
            console.print(f"\t~ {file}")

    with open(path, 'w') as f:
        toml.dump(pyproject, f)



@app.command()
def remove(
    files: List[str] = typer.Argument(..., help="In progress"),
    no_input: bool = typer.Option(False, help="In progress")
):
    """
    Remove .ipynb files for jupydocs to build.
    """
    files = list(set(files))
    console.print(f"[bold]Attemping to remove {len(files)} docs from build list")  # noqa: E501
    path, pyproject = parse_pyproject_toml()

    if no_input:
        key = 'no-input'
    else:
        key = 'keep-input'

    files.sort()
    console.print(f"[bold]Changes ({key}):")
    for file in pyproject['tool']['jupydocs'][key]:
        console.log(file)
        if file in files:
            pyproject['tool']['jupydocs'][key].remove(file)
            console.print(f"[bold red]\t- {file}")
        else:
            console.print(f"\t~ {file}")

    # Show use the files that were not removed.
    if len(files) > 0:
        console.print("[bold]Warnings:")
    for file in files:
        console.print(f"[bold yellow]\t! {file}[/bold yellow] not in pyproject.toml")  # noqa: E501

    with open(path, 'w') as f:
        toml.dump(pyproject, f)


@app.command()
def convert():
    """
    Convert .ipynb files to .md.
    """
    # Get data from pyproject.toml
    _, pyproject = parse_pyproject_toml()
    ipynb_files_keep_input = pyproject['tool']['jupydocs']['keep-input']
    ipynb_files_no_input = pyproject['tool']['jupydocs']['no-input']

    # Only attempt to convert files that exist
    ipynb_dict = {
        'keep-input': [i for i in ipynb_files_keep_input if os.path.isfile(i)],
        'no-input': [i for i in ipynb_files_no_input if os.path.isfile(i)]
    }

    num_files = len(ipynb_dict['keep-input']) + len(ipynb_dict['no-input'])
    console.print(f"[bold]Converting {num_files} docs")

    with console.status("Converting docs from .ipynb to .md", spinner="runner"):
        for key, files in ipynb_dict.items():
            flag = '--no-input' if key == 'no-input' else ''
            for ipynb in files:
                p = os.path.normpath(ipynb)
                bash_command = f"jupyter nbconvert --to markdown --execute {p} {flag}"
                console.log(f"{p}")
                process = subprocess.run(bash_command.split(), capture_output=True)

    console.print(f"[bold green]Successfully converted {num_files} .ipynb files to .md")  # noqa: E501
