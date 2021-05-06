"""
A command line interface (CLI) for quickly converting ipynb files to markdown.
"""
import os
import subprocess
import textwrap

import plac


@plac.annotations(
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
    no_input=plac.Annotation(
        help="Specify if the markdown files should be rendered with or without\
            the input code cells. Use 'i' to include the input or 'n' to not\
            include the input. If multiple files are provided you can provide\
            multiple characters matching the order of the file to convert. For\
            example if you pass two .ipynb files to be converted you could\
            include input for the first and not the second by passing 'in'.",
        kind="option",
        abbrev="n",
        type=str,
        choices=None,
        metavar=None,
    ),
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
)
def build(walk=False, old=False, no_input='i', *directories):
    """ Converts `.ipynb` file to markdown. Only `.ipynb` files that have been
    changed since the last build will be converted unless otherwise specified.
    
    Examples
    --------
    python -m jupydocs build .
    python -m jupydocs build . --walk
    python -m jupydocs build . --walk --old
    python -m jupydocs build README.ipynb website/docs/usage_getting_started.ipynb --no-input ni
    """
    # objects to hold results
    dirs = list(directories)
    updated_docs = []
    not_updated_docs = []
    ipynb = []
    
    # find all of the ipynb
    for directory in dirs:
        if directory.endswith(".ipynb"):
            files = [directory]
        elif walk:
            files = [os.path.join(r, file) for r, d, f in os.walk(directory) for file in f]
        else:
            files = os.listdir(directory)
            files = [directory + '/' + f for f in files]
        for f in files:
            if f.endswith(".ipynb") and ".ipynb_checkpoints/" not in f:
                ipynb.append(f)
                
    # print start
    print("\n", ">" * 64, sep="")
    print(f"Conversion starting! {len(ipynb)} .ipynb files detected.")
    print(">" * 64)
    
    # validate that the arguments provided are correct.
    # there are three possible outcomes:
    # (1) only one input mapping was provided, so apply it to all files
    # (2) the number of arguments provided to --no-input does not match the
    #     number of .ipynb files
    # (3) the number of arguments provided to --no-input does match the number
    #     of .ipynb files
    input_mapping = list(no_input)
    if len(input_mapping) == 1:
        input_mapping = input_mapping * len(ipynb)
    elif len(input_mapping) != len(ipynb):
        error_msg = (
            f"The number of files provided ({len(ipynb)}) does not match the "
            f"number of arguments provided to --no-input ({len(input_mapping)})."
        )
        raise ValueError(error_msg)
    else:
        pass

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
    for idx, (doc_name, doc_file) in enumerate(build_log.items()):
        ipynb_time = doc_file[doc_name + ".ipynb"]
        md_time = doc_file[doc_name + ".md"]
        if md_time < ipynb_time or old:
            print("\n", "/" * 32, sep='')
            print(f"Converting {doc_name}.ipynb to markdown.")
            bash_command = (
                f"jupyter nbconvert --to markdown --execute {doc_name}.ipynb"
            )
            if input_mapping[idx] == 'n':
                bash_command += ' --no-input'
            process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            updated_docs.append(f"\t - {doc_name}.ipynb")
        else:
            not_updated_docs.append(f"\t - {doc_name}.ipynb")

    # results
    print("\n", "=" * 32, "\n", "Summary of results\n", "=" * 32, sep="")
    print(
        f"{len(updated_docs)} of {len(updated_docs) + len(not_updated_docs)} docs were built"
    )
    print("UPDATED:")
    for i in updated_docs:
        print(i)
    print("NOT UPDATED:")
    for i in not_updated_docs:
        print(i)
        
    # print end
    print("\n", "<" * 64, sep="")
    print(f"Conversion complete! {len(updated_docs)} of {len(updated_docs) + len(not_updated_docs)} docs were built.")
    print("<" * 64)


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
