---
id: documenting_functions
title: Documenting Functions
---
jupydocs can be used to document any function that is compliant with numpy docstring standards (see [numpy docstring guide](https://numpydoc.readthedocs.io/en/latest/format.html)). 

To use jupydocs you pass your function into the `NumpyDocString` class, and then use the `render_md` function to output the markdown.


```python
from jupydocs.numpydocstring import NumpyDocString
```


```python
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
```


```python
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

| NAME   | TYPE   | DESCRIPTION   |
|:-------|:-------|:--------------|
| num    | Float  | x * 2 + y * 3 |

### Example

```python
>>> from examplepackage.example import custom_sum
>>> custom_sum(2, 3)
13

```


### See also

You should normally use the regular python `sum` function. `custom_sum` is
almost never useful!




Below is an example of using jupydocs on a function from the [pandas library](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html).


```python
import pandas as pd
df_docstring = NumpyDocString(pd.concat)
df_docstring.render_md()
```




## concat

Concatenate pandas objects along a particular axis with optional set logic along the other axes. 

Can also add a layer of hierarchical indexing on the concatenation axis, which may be useful if the labels are the same (or overlapping) on the passed axis number.

### Parameters

| NAME             | TYPE                                                 | DESCRIPTION                                                                                                                                                                                                                                                                                                                               |
|:-----------------|:-----------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| objs             | a sequence or mapping of Series or DataFrame objects | If a mapping is passed, the sorted keys will be used as the `keys` argument, unless it is passed, in which case the values will be selected (see below). Any None objects will be dropped silently unless they are all None in which case a ValueError will be raised.                                                                    |
| axis             | {0/'index', 1/'columns'}, default 0                  | The axis to concatenate along.                                                                                                                                                                                                                                                                                                            |
| join             | {'inner', 'outer'}, default 'outer'                  | How to handle indexes on other axis (or axes).                                                                                                                                                                                                                                                                                            |
| ignore_index     | bool, default False                                  | If True, do not use the index values along the concatenation axis. The resulting axis will be labeled 0, ..., n - 1. This is useful if you are concatenating objects where the concatenation axis does not have meaningful indexing information. Note the index values on the other axes are still respected in the join.                 |
| keys             | sequence, default None                               | If multiple levels passed, should contain tuples. Construct hierarchical index using the passed keys as the outermost level.                                                                                                                                                                                                              |
| levels           | list of sequences, default None                      | Specific levels (unique values) to use for constructing a MultiIndex. Otherwise they will be inferred from the keys.                                                                                                                                                                                                                      |
| names            | list, default None                                   | Names for the levels in the resulting hierarchical index.                                                                                                                                                                                                                                                                                 |
| verify_integrity | bool, default False                                  | Check whether the new concatenated axis contains duplicates. This can be very expensive relative to the actual data concatenation.                                                                                                                                                                                                        |
| sort             | bool, default False                                  | Sort non-concatenation axis if it is not already aligned when `join` is 'outer'. This has no effect when ``join='inner'``, which already preserves the order of the non-concatenation axis. <div><br></br></div>        .. versionadded:: 0.23.0 .. versionchanged:: 1.0.0 <div><br></br></div>           Changed to not sort by default. |
| copy             | bool, default True                                   | If False, do not copy data unnecessarily.                                                                                                                                                                                                                                                                                                 |

### Returns

| TYPE                 | DESCRIPTION                                                                                                                                                                                                                                       |
|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| object, type of objs | When concatenating all ``Series`` along the index (axis=0), a ``Series`` is returned. When ``objs`` contains at least one ``DataFrame``, a ``DataFrame`` is returned. When concatenating along the columns (axis=1), a ``DataFrame`` is returned. |

### See Also

Series.append : Concatenate Series.
DataFrame.append : Concatenate DataFrames.
DataFrame.join : Join DataFrames using indexes.
DataFrame.merge : Merge DataFrames by indexes or columns.


### Examples

Combine two ``Series``.

```python
>>> s1 = pd.Series(['a', 'b'])
>>> s2 = pd.Series(['c', 'd'])
>>> pd.concat([s1, s2])
0    a
1    b
0    c
1    d
dtype: object

```

Clear the existing index and reset it in the result
by setting the ``ignore_index`` option to ``True``.

```python
>>> pd.concat([s1, s2], ignore_index=True)
0    a
1    b
2    c
3    d
dtype: object

```

Add a hierarchical index at the outermost level of
the data with the ``keys`` option.

```python
>>> pd.concat([s1, s2], keys=['s1', 's2'])
s1  0    a
1    b
s2  0    c
1    d
dtype: object

```

Label the index keys you create with the ``names`` option.

```python
>>> pd.concat([s1, s2], keys=['s1', 's2'],
...           names=['Series name', 'Row ID'])
Series name  Row ID
s1           0         a
1         b
s2           0         c
1         d
dtype: object

```

Combine two ``DataFrame`` objects with identical columns.

```python
>>> df1 = pd.DataFrame([['a', 1], ['b', 2]],
...                    columns=['letter', 'number'])
>>> df1
letter  number
0      a       1
1      b       2
>>> df2 = pd.DataFrame([['c', 3], ['d', 4]],
...                    columns=['letter', 'number'])
>>> df2
letter  number
0      c       3
1      d       4
>>> pd.concat([df1, df2])
letter  number
0      a       1
1      b       2
0      c       3
1      d       4

```

Combine ``DataFrame`` objects with overlapping columns
and return everything. Columns outside the intersection will
be filled with ``NaN`` values.

```python
>>> df3 = pd.DataFrame([['c', 3, 'cat'], ['d', 4, 'dog']],
...                    columns=['letter', 'number', 'animal'])
>>> df3
letter  number animal
0      c       3    cat
1      d       4    dog
>>> pd.concat([df1, df3], sort=False)
letter  number animal
0      a       1    NaN
1      b       2    NaN
0      c       3    cat
1      d       4    dog

```

Combine ``DataFrame`` objects with overlapping columns
and return only those that are shared by passing ``inner`` to
the ``join`` keyword argument.

```python
>>> pd.concat([df1, df3], join="inner")
letter  number
0      a       1
1      b       2
0      c       3
1      d       4

```

Combine ``DataFrame`` objects horizontally along the x axis by
passing in ``axis=1``.

```python
>>> df4 = pd.DataFrame([['bird', 'polly'], ['monkey', 'george']],
...                    columns=['animal', 'name'])
>>> pd.concat([df1, df4], axis=1)
letter  number  animal    name
0      a       1    bird   polly
1      b       2  monkey  george

```

Prevent the result from including duplicate index values with the
``verify_integrity`` option.

```python
>>> df5 = pd.DataFrame([1], index=['a'])
>>> df5
0
a  1
>>> df6 = pd.DataFrame([2], index=['a'])
>>> df6
0
a  2
>>> pd.concat([df5, df6], verify_integrity=True)
Traceback (most recent call last):
...
ValueError: Indexes have overlapping values: ['a']
```



