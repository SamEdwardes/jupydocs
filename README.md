![jupydocs_logo](https://github.com/SamEdwardes/jupydocs/raw/main/website/static/img/jupydocs_logo_text.png)

[![Netlify Status](https://api.netlify.com/api/v1/badges/6bc56cde-7bc0-492e-a357-7d2ca05004a3/deploy-status)](https://app.netlify.com/sites/jupydocs/deploys)

The easiest way to document your python library with jupyter and markdown.

- [GitHub](https://github.com/SamEdwardes/jupydocs)
- [docs](https://jupydocs.netlify.app/)
- [PyPi](https://pypi.org/project/jupydocs/)

```
Pleaes note jupydocs is currently under active development. 
It can be used for testing, but should not be used for deployment. 
It will change!
```


## Installation

```bash
pip install jupydocs
```

## Quickstart


```python
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
    num : Float
        A new take on the traditional sum function. x * 2 + y * 3. Not at all
        useful. But fun!
        
    Example
    -------
    >>> from examplepackage.example import custom_sum
    >>> custom_sum(2, 3)
    13    
    """
    return x * 2 + y * 3

docstring = NumpyDocString(custom_sum)
docstring.render_md()
```




## custom_sum

A new take on the class `sum` function. 

Does 1 + 1 always need to equal 2? Not anymore! Thanks to the `custom_sum` function 1 + 1 will never equal 2 again.

### Parameters

| NAME   | TYPE   | DESCRIPTION   |
|:-------|:-------|:--------------|
| x      | float  | A number.     |
| y      | float  | A number.     |

### Returns

| NAME   | TYPE   | DESCRIPTION                                                                            |
|:-------|:-------|:---------------------------------------------------------------------------------------|
| num    | Float  | A new take on the traditional sum function. x * 2 + y * 3. Not at all useful. But fun! |

### Example

```python
>>> from examplepackage.example import custom_sum
>>> custom_sum(2, 3)
13
```





```python
print(docstring.render_md(return_str=True))
```

    ## custom_sum
    
    A new take on the class `sum` function. 
    
    Does 1 + 1 always need to equal 2? Not anymore! Thanks to the `custom_sum` function 1 + 1 will never equal 2 again.
    
    ### Parameters
    
    | NAME   | TYPE   | DESCRIPTION   |
    |:-------|:-------|:--------------|
    | x      | float  | A number.     |
    | y      | float  | A number.     |
    
    ### Returns
    
    | NAME   | TYPE   | DESCRIPTION                                                                            |
    |:-------|:-------|:---------------------------------------------------------------------------------------|
    | num    | Float  | A new take on the traditional sum function. x * 2 + y * 3. Not at all useful. But fun! |
    
    ### Example
    
    ```python
    >>> from examplepackage.example import custom_sum
    >>> custom_sum(2, 3)
    13
    ```
    

