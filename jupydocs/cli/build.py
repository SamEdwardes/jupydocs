"""
A command line interface (CLI) for quickly converting ipynb files to markdown.
"""
import os
import subprocess

import plac


@plac.annotations(
    directories=plac.Annotation(
        help="The directory to search for .ipynb files. The relative path to a\
            .ipynb file can also be provided, in which case only that single\
            file will be converted. By default '.' (current working directory).",
        kind="positional",
        abbrev=None,
        type=str,
        choices=None,
        metavar=None,
    ),
    walk=plac.Annotation(
        help="If flag is included `build` will search the provided directory\
             and all subdirectories for .ipynb files.",
        kind="flag",
        abbrev="w",
        type=bool,
        choices=None,
        metavar=None,
    ),
    old=plac.Annotation(
        help="If flag is included `build` will render all found .ipynb files\
            even if no changes have occurred since the last build.",
        kind="flag",
        abbrev="o",
        type=bool,
        choices=None,
        metavar=None,
    ),
    noinput=plac.Annotation(
        help="If flag is included `build` will render all found .ipynb files\
            with no input, meaning that only the output from the code blocks\
            will be rendered to markdown.",
        kind="flag",
        abbrev="n",
        type=bool,
        choices=None,
        metavar=None,
    ),
)
def build(*directories, walk=False, old=False, noinput=False):
    """Convert .ipynb files to .md

    Converts .ipynb file to markdown. Only .ipynb files that have been changed
    since the last build will be converted unless otherwise specified.
    """
    # find all of the ipynb and md files
    if directory.endswith(".ipynb"):
        files = [directory]
    elif walk:
        files = [os.path.join(r, file) for r, d, f in os.walk(directory) for file in f]
    else:
        files = os.listdir(directory)
        files = [directory + '/' + f for f in files]
    ipynb = [f for f in files if f.endswith(".ipynb")]
    ipynb = [f for f in ipynb if ".ipynb_checkpoints/" not in f]
    md = [f for f in files if f.endswith(".md")]

    # capture the time stamp the last time the file was run
    build_log = {}
    for ipynb_name in ipynb:
        doc_name = ipynb_name[0:-6]
        md_name = doc_name + ".md"
        build_log[doc_name] = {
            ipynb_name: os.path.getmtime(ipynb_name),
            md_name: get_timestamp(md_name),
        }

    # build docs for docs that have been updated
    updated_docs = []
    not_updated_docs = []
    for doc_name, doc_file in build_log.items():
        ipynb_time = doc_file[doc_name + ".ipynb"]
        md_time = doc_file[doc_name + ".md"]
        if md_time < ipynb_time or old:
            print("/" * 64)
            print(f"Converting {doc_name}.ipynb to markdown.")
            print("/" * 64)
            bash_command = (
                f"jupyter nbconvert --to markdown --execute {doc_name}.ipynb"
            )
            if noinput:
                bash_command += ' --no-input'
            process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            updated_docs.append(f"\t - {doc_name}.ipynb")
        else:
            not_updated_docs.append(f"\t - {doc_name}.ipynb")

    # results
    print("=" * 64, "\n", "Summary of results\n", "=" * 64, sep="")
    print(
        f"{len(updated_docs)} of {len(updated_docs) + len(not_updated_docs)} docs were built"
    )
    print("UPDATED:")
    for i in updated_docs:
        print(i)
    print("NOT UPDATED:")
    for i in not_updated_docs:
        print(i)


def get_timestamp(x):
    """A helper function to get the timestamp from a file.

    Parameters
    ----------
    x : str
        The path of a file (for example 'README.ipynb')

    Returns
    -------
    float
        The timestamp of the files last modified date
    """
    try:
        return os.path.getmtime(x)
    except FileNotFoundError:
        return 0.0


if __name__ == "__main__":
    plac.call(build)
