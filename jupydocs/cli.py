"""CLI for jupydocs

Helpful reference material for developers:
- https://github.com/sdispater/tomlkit
- https://black.readthedocs.io/en/stable/pyproject_toml.html#configuration-format
- https://github.com/python-poetry/poetry/blob/master/pyproject.toml
"""

import os
from os.path import isfile, join
import subprocess

from collections import defaultdict

from typing import List

import typer
from rich.console import Console

import toml


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
    # Check to see if a pyproject.toml exists
    if not os.path.isfile(path):
        console.print("[red]No [bold]pyproject.toml[/bold] file found. Creating a new one.[/red]")
        pyproject = {
            'tool': {
                'jupydocs': defaultdict(list)
            }
        }
    else:
        pyproject = toml.load(path)
        
    # Check if there is any jupydocs data in pyproject.toml.
    try:
        jupydocs_data = pyproject['tool']['jupydocs']
        jupydocs_data = defaultdict(list, jupydocs_data)
        pyproject['tool']['jupydocs'] = jupydocs_data
    except KeyError:
        console.print("Adding tool.jupydocs to pyproject.toml")
        pyproject['tool']['jupydocs'] = defaultdict(list)
    
    return path, pyproject
    

@app.command()
def add(
    files: List[str]=typer.Argument(..., help="In progress"), 
    no_input: bool=typer.Option(False, help="In progress")
):
    """
    Add new .ipynb files for jupydocs to build.
    
    Examples
    > python -m jupydocs add website/docs/usage_getting_started.ipynb website/docs/usage_why_use_jupydocs.ipynb
    > python -m jupydocs add website/docs/api_reference_numpy_module.ipynb --no-input
    """
    # Validate that files exist
    # for file in files:
    #     if not os.path.isfile(file):
    #         raise FileNotFoundError(f"{file} does not exist.")
    path, pyproject = parse_pyproject_toml()
    
    if no_input:
        key = 'no-input'
    else:
        key = 'keep-input'
    file_list =  pyproject['tool']['jupydocs'][key]
    file_list += files
    file_list = list(set(file_list))
    pyproject['tool']['jupydocs'][key] = file_list
    
    with open(path, 'w') as f:
         toml.dump(pyproject, f)
         

@app.command()
def remove(
    files: List[str]=typer.Argument(..., help="In progress"), 
    no_input: bool=typer.Option(False, help="In progress")
):
    """
    Remove .ipynb files for jupydocs to build.
    """
    path, pyproject = parse_pyproject_toml()
    
    if no_input:
        key = 'no-input'
    else:
        key = 'keep-input'
        
    for file in files:
        pyproject['tool']['jupydocs'][key].remove(file)
    
    with open(path, 'w') as f:
         toml.dump(pyproject, f)
        

@app.command()
def build():
    """
    Build the docs
    """
    path, pyproject = parse_pyproject_toml()
    
    ipynb_files_keep_input = pyproject['tool']['jupydocs']['keep-input']
    ipynb_files_no_input = pyproject['tool']['jupydocs']['no-input']
    num_files = len(ipynb_files_keep_input) + len(ipynb_files_no_input)
    console.print(f"[bold]Building {num_files} docs")
    
    
    console.print("Files keeping input")
    for ipynb in ipynb_files_keep_input:
        p = os.path.normpath(ipynb)
        console.rule(p)
        bash_command = f"jupyter nbconvert --to markdown --execute {p}"
        process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
    
    console.print("Files dropping input")
    for ipynb in ipynb_files_no_input:
        p = os.path.normpath(ipynb)
        console.rule(p)
        bash_command = f"jupyter nbconvert --to markdown --execute {p} --no-input"
        process = subprocess.Popen((bash_command).split(), stdout=subprocess.PIPE)
        output, error = process.communicate()