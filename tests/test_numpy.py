from IPython.display import Markdown
from jupydocs.numpydocstring import NumpyDocString


def custom_sum(x, y):
    """A new take on the class `sum` function.
    
    Does 1 + 1 always need to equal 2? Not anymore! Thanks to the `custom_sum`
    function 1 + 1 will never equal 2 again.

    Parameters
    ----------
    x : float
        A number.
    y : float
        A number.

    Returns
    -------
    num :Float
        x * 2 + y * 3
        
    Example
    -------
    >>> from examplepackage.example import custom_sum
    >>> custom_sum(2, 3)
    13
    
    See also
    --------
    You should normally use the regular python `sum` function. `custom_sum` is
    almost never useful!
    
    """
    return x * 2 + y * 3

def test_numpy():
    docstring = NumpyDocString(custom_sum)
    assert type(docstring.render_md(True)) is str
    assert type(docstring.render_md()) is Markdown
