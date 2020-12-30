# Build docs by rendering .ipynb to .md
# usage: poetry run bash scripts/build_docs.sh

# include input
python -m jupydocs build --no-input i \
    README.ipynb \
    website/docs/usage_getting_started.ipynb \
    website/docs/usage_why_use_jupydocs.ipynb \
    website/docs/usage_documenting_functions.ipynb \
    website/docs/usage_documenting_classes.ipynb \
    website/docs/api_reference_numpy_module.ipynb \
    website/docs/testing_numpy.ipynb \
    website/docs/testing_pandas.ipynb \
    website/docs/testing_other.ipynb

# exclude input
python -m jupydocs build --no-input n \
    website/docs/api_reference_numpy_module.ipynb

# render any other .ipynb files that were not included above
python -m jupydocs build . --walk --no-input i