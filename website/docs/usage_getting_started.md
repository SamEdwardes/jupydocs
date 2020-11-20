---
id: getting_started
title: Getting Started
slug: /
---
## Installation

jupycdocs can be downloaded from [PyPi](https://pypi.org/project/jupydocs/).

```bash
pip install jupydocs
```

## Quick Start


```python
from jupydocs.numpydocstring import NumpyDocString
```


```python
def silly_function(name):
    """
    Parameters
    ----------
    name : str
        The name of a person
        
        
    Returns
    -------
    str
        Let the person know they are silly!
    """
    return(f'Hey {name}, you are silly!')
```


```python
NumpyDocString(silly_function).render_md()
```




## silly_function



### Parameters

| NAME   | TYPE   | DESCRIPTION                    |
|:-------|:-------|:-------------------------------|
| name   | str    | The name of a person <br></br> |

### Returns

| TYPE   | DESCRIPTION                         |
|:-------|:------------------------------------|
| str    | Let the person know they are silly! |


