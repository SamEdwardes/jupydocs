# inspired by https://github.com/pytorch/botorch/blob/master/scripts/build_docs.sh
# usage: poetry run bash scripts/build_docs.sh
echo "-----------------------------------"
echo "Convert .ipynb to markdown"
echo "-----------------------------------"

# GITHUB
echo "-------------"
jupyter nbconvert --to markdown --execute README.ipynb

# DOCS

#   GETTING STARTED
echo "-------------"
jupyter nbconvert --to markdown --execute website/docs/usage_getting_started.ipynb
echo "-------------"
jupyter nbconvert --to markdown --execute website/docs/usage_why_use_jupydocs.ipynb
echo "-------------"
jupyter nbconvert --to markdown --execute website/docs/usage_documenting_functions.ipynb
echo "-------------"
jupyter nbconvert --to markdown --execute website/docs/usage_documenting_classes.ipynb
echo "-------------"
jupyter nbconvert --to markdown --execute website/docs/usage_jupydocs_work_flow.ipynb

#   API REFERENCE
echo "-------------"
jupyter nbconvert --to markdown --execute website/docs/api_reference_numpy_module.ipynb --no-input

#   TESTING
echo "-------------"
jupyter nbconvert --to markdown --execute website/docs/testing_numpy.ipynb
echo "-------------"
jupyter nbconvert --to markdown --execute website/docs/testing_pandas.ipynb
echo "-------------"
jupyter nbconvert --to markdown --execute website/docs/testing_other.ipynb