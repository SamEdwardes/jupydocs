import tomlkit

from jupydocs.cli import parse_pyproject_toml


def test_no_parse_pyproject_toml():
    """
    When no pyproject.toml exists a new one with the jupydocs meta data should
    be created.
    """
    _, pyproject = parse_pyproject_toml("tests/data/does_not_exist.toml")
    assert isinstance(pyproject['tool']['jupydocs'], tomlkit.items.Table)


def test_empty_parse_pyproject_toml():
    """
    When there is an empty pyproject.toml file check that the jupydocs meta
    data is added.
    """
    _, pyproject = parse_pyproject_toml("tests/data/pyproject_empty.toml")
    assert isinstance(pyproject['tool']['jupydocs'], tomlkit.items.Table)


def test_jupydocs_parse_pyproject_toml():
    """
    Test that when pyroject.toml already contains some jupydocs meta data that
    it is not overwritten.
    """
    _, pyproject = parse_pyproject_toml("tests/data/pyproject_jupydocs.toml")
    assert isinstance(pyproject['tool']['jupydocs'], tomlkit.items.Table)
    assert pyproject['tool']['jupydocs']['docs']['test.ipynb'] == {"output-style": "keep-input", "output-directory": "test.ipynb"}


def test_tool_parse_pyproject_toml():
    """
    Check that when there is an existing `tool` section in pyproject.toml
    that it is not overwritten.
    """
    _, pyproject = parse_pyproject_toml("tests/data/pyproject_tool.toml")
    assert isinstance(pyproject['tool']['jupydocs'], tomlkit.items.Table)
    assert 'poetry' in pyproject['tool']
    assert pyproject['tool']['poetry']['dependencies']['python'] == "^3.7"
    assert 'jupydocs' in pyproject['tool']
    assert 'build-system' in pyproject


def test_no_tool_parse_pyproject_toml():
    """
    Check that when there is no `tool` section in an existing pyproject.toml
    that it is added correctly.
    """
    _, pyproject = parse_pyproject_toml("tests/data/pyproject_no_tool.toml")
    assert isinstance(pyproject['tool']['jupydocs'], tomlkit.items.Table)
