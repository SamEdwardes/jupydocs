---
id: usage
title: Usage
---

```python
from jupydocs.numpydocstring import NumpyDocString
```

Imagine you have a simple python package.


```python
!tree examplepackage
```

    [01;34mexamplepackage[00m
    ├── README.md
    └── [01;34mexamplepackage[00m
        ├── __init__.py
        ├── [01;34m__pycache__[00m
        │   ├── __init__.cpython-36.pyc
        │   ├── __init__.cpython-37.pyc
        │   ├── example.cpython-36.pyc
        │   └── example.cpython-37.pyc
        └── example.py
    
    2 directories, 7 files



```python
from examplepackage.examplepackage.example import custom_sum
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

    num : Float
        x * 2 + y * 3

### Examples

```python
>>> from examplepackage.example import custom_sum
>>> custom_sum(2, 3)
13
```





```python
import pandas as pd
df_docstring = NumpyDocString(pd.DataFrame)
df_docstring.render_md()
```




## DataFrame

Two-dimensional, size-mutable, potentially heterogeneous tabular data. 

Data structure also contains labeled axes (rows and columns). Arithmetic operations align on both row and column labels. Can be thought of as a dict-like container for Series objects. The primary pandas data structure.

### Parameters

| NAME    | TYPE                                                              | DESCRIPTION                                                                                                                                                                                                                                                                                                                     |
|:--------|:------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| data    | ndarray (structured or homogeneous), Iterable, dict, or DataFrame | Dict can contain Series, arrays, constants, or list-like objects. <br></br> .. versionchanged:: 0.23.0 If data is a dict, column order follows insertion-order for Python 3.6 and later. <br></br> .. versionchanged:: 0.25.0 If data is a list of dicts, column order follows insertion-order for Python 3.6 and later. <br></br> |
| index   | Index or array-like                                               | Index to use for resulting frame. Will default to RangeIndex if no indexing information part of input data and no index provided.                                                                                                                                                                                               |
| columns | Index or array-like                                               | Column labels to use for resulting frame. Will default to RangeIndex (0, 1, 2, ..., n) if no column labels are provided.                                                                                                                                                                                                        |
| dtype   | dtype, default None                                               | Data type to force. Only a single dtype is allowed. If None, infer.                                                                                                                                                                                                                                                             |
| copy    | bool, default False                                               | Copy data from inputs. Only affects DataFrame / 2d ndarray input.                                                                                                                                                                                                                                                               |

### Examples

Constructing DataFrame from a dictionary.

```python
>>> d = {'col1': [1, 2], 'col2': [3, 4]}
>>> df = pd.DataFrame(data=d)
>>> df
col1  col2
0     1     3
1     2     4

```

Notice that the inferred dtype is int64.

```python
>>> df.dtypes
col1    int64
col2    int64
dtype: object

```

To enforce a single dtype:

```python
>>> df = pd.DataFrame(data=d, dtype=np.int8)
>>> df.dtypes
col1    int8
col2    int8
dtype: object

```

Constructing DataFrame from numpy ndarray:

```python
>>> df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
...                    columns=['a', 'b', 'c'])
>>> df2
a  b  c
0  1  2  3
1  4  5  6
2  7  8  9

```





```python
print(pd.DataFrame.__doc__)
```

    
        Two-dimensional, size-mutable, potentially heterogeneous tabular data.
    
        Data structure also contains labeled axes (rows and columns).
        Arithmetic operations align on both row and column labels. Can be
        thought of as a dict-like container for Series objects. The primary
        pandas data structure.
    
        Parameters
        ----------
        data : ndarray (structured or homogeneous), Iterable, dict, or DataFrame
            Dict can contain Series, arrays, constants, or list-like objects.
    
            .. versionchanged:: 0.23.0
               If data is a dict, column order follows insertion-order for
               Python 3.6 and later.
    
            .. versionchanged:: 0.25.0
               If data is a list of dicts, column order follows insertion-order
               for Python 3.6 and later.
    
        index : Index or array-like
            Index to use for resulting frame. Will default to RangeIndex if
            no indexing information part of input data and no index provided.
        columns : Index or array-like
            Column labels to use for resulting frame. Will default to
            RangeIndex (0, 1, 2, ..., n) if no column labels are provided.
        dtype : dtype, default None
            Data type to force. Only a single dtype is allowed. If None, infer.
        copy : bool, default False
            Copy data from inputs. Only affects DataFrame / 2d ndarray input.
    
        See Also
        --------
        DataFrame.from_records : Constructor from tuples, also record arrays.
        DataFrame.from_dict : From dicts of Series, arrays, or dicts.
        read_csv : Read a comma-separated values (csv) file into DataFrame.
        read_table : Read general delimited file into DataFrame.
        read_clipboard : Read text from clipboard into DataFrame.
    
        Examples
        --------
        Constructing DataFrame from a dictionary.
    
        >>> d = {'col1': [1, 2], 'col2': [3, 4]}
        >>> df = pd.DataFrame(data=d)
        >>> df
           col1  col2
        0     1     3
        1     2     4
    
        Notice that the inferred dtype is int64.
    
        >>> df.dtypes
        col1    int64
        col2    int64
        dtype: object
    
        To enforce a single dtype:
    
        >>> df = pd.DataFrame(data=d, dtype=np.int8)
        >>> df.dtypes
        col1    int8
        col2    int8
        dtype: object
    
        Constructing DataFrame from numpy ndarray:
    
        >>> df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        ...                    columns=['a', 'b', 'c'])
        >>> df2
           a  b  c
        0  1  2  3
        1  4  5  6
        2  7  8  9
        



```python

```
