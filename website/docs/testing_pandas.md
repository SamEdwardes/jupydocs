---
id: testing_pandas
title: Testing on Pandas
---

```python
from jupydocs.numpydocstring import NumpyDocString
```


```python
import pandas as pd
```

## `pd.DataFrame.__doc__`


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
NumpyDocString(pd.DataFrame).render_md()
```




## DataFrame

Two-dimensional, size-mutable, potentially heterogeneous tabular data. 

Data structure also contains labeled axes (rows and columns). Arithmetic operations align on both row and column labels. Can be thought of as a dict-like container for Series objects. The primary pandas data structure.

### Parameters

| NAME    | TYPE                                                              | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                  |
|:--------|:------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| data    | ndarray (structured or homogeneous), Iterable, dict, or DataFrame | Dict can contain Series, arrays, constants, or list-like objects. <div><br></br></div>        .. versionchanged:: 0.23.0 If data is a dict, column order follows insertion-order for Python 3.6 and later. <div><br></br></div>        .. versionchanged:: 0.25.0 If data is a list of dicts, column order follows insertion-order for Python 3.6 and later. |
| index   | Index or array-like                                               | Index to use for resulting frame. Will default to RangeIndex if no indexing information part of input data and no index provided.                                                                                                                                                                                                                            |
| columns | Index or array-like                                               | Column labels to use for resulting frame. Will default to RangeIndex (0, 1, 2, ..., n) if no column labels are provided.                                                                                                                                                                                                                                     |
| dtype   | dtype, default None                                               | Data type to force. Only a single dtype is allowed. If None, infer.                                                                                                                                                                                                                                                                                          |
| copy    | bool, default False                                               | Copy data from inputs. Only affects DataFrame / 2d ndarray input.                                                                                                                                                                                                                                                                                            |

### See Also

DataFrame.from_records : Constructor from tuples, also record arrays.
DataFrame.from_dict : From dicts of Series, arrays, or dicts.
read_csv : Read a comma-separated values (csv) file into DataFrame.
read_table : Read general delimited file into DataFrame.
read_clipboard : Read text from clipboard into DataFrame.


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




## `pd.concat.__doc__`


```python
print(pd.concat.__doc__)
```

    
        Concatenate pandas objects along a particular axis with optional set logic
        along the other axes.
    
        Can also add a layer of hierarchical indexing on the concatenation axis,
        which may be useful if the labels are the same (or overlapping) on
        the passed axis number.
    
        Parameters
        ----------
        objs : a sequence or mapping of Series or DataFrame objects
            If a mapping is passed, the sorted keys will be used as the `keys`
            argument, unless it is passed, in which case the values will be
            selected (see below). Any None objects will be dropped silently unless
            they are all None in which case a ValueError will be raised.
        axis : {0/'index', 1/'columns'}, default 0
            The axis to concatenate along.
        join : {'inner', 'outer'}, default 'outer'
            How to handle indexes on other axis (or axes).
        ignore_index : bool, default False
            If True, do not use the index values along the concatenation axis. The
            resulting axis will be labeled 0, ..., n - 1. This is useful if you are
            concatenating objects where the concatenation axis does not have
            meaningful indexing information. Note the index values on the other
            axes are still respected in the join.
        keys : sequence, default None
            If multiple levels passed, should contain tuples. Construct
            hierarchical index using the passed keys as the outermost level.
        levels : list of sequences, default None
            Specific levels (unique values) to use for constructing a
            MultiIndex. Otherwise they will be inferred from the keys.
        names : list, default None
            Names for the levels in the resulting hierarchical index.
        verify_integrity : bool, default False
            Check whether the new concatenated axis contains duplicates. This can
            be very expensive relative to the actual data concatenation.
        sort : bool, default False
            Sort non-concatenation axis if it is not already aligned when `join`
            is 'outer'.
            This has no effect when ``join='inner'``, which already preserves
            the order of the non-concatenation axis.
    
            .. versionadded:: 0.23.0
            .. versionchanged:: 1.0.0
    
               Changed to not sort by default.
    
        copy : bool, default True
            If False, do not copy data unnecessarily.
    
        Returns
        -------
        object, type of objs
            When concatenating all ``Series`` along the index (axis=0), a
            ``Series`` is returned. When ``objs`` contains at least one
            ``DataFrame``, a ``DataFrame`` is returned. When concatenating along
            the columns (axis=1), a ``DataFrame`` is returned.
    
        See Also
        --------
        Series.append : Concatenate Series.
        DataFrame.append : Concatenate DataFrames.
        DataFrame.join : Join DataFrames using indexes.
        DataFrame.merge : Merge DataFrames by indexes or columns.
    
        Notes
        -----
        The keys, levels, and names arguments are all optional.
    
        A walkthrough of how this method fits in with other tools for combining
        pandas objects can be found `here
        <https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html>`__.
    
        Examples
        --------
        Combine two ``Series``.
    
        >>> s1 = pd.Series(['a', 'b'])
        >>> s2 = pd.Series(['c', 'd'])
        >>> pd.concat([s1, s2])
        0    a
        1    b
        0    c
        1    d
        dtype: object
    
        Clear the existing index and reset it in the result
        by setting the ``ignore_index`` option to ``True``.
    
        >>> pd.concat([s1, s2], ignore_index=True)
        0    a
        1    b
        2    c
        3    d
        dtype: object
    
        Add a hierarchical index at the outermost level of
        the data with the ``keys`` option.
    
        >>> pd.concat([s1, s2], keys=['s1', 's2'])
        s1  0    a
            1    b
        s2  0    c
            1    d
        dtype: object
    
        Label the index keys you create with the ``names`` option.
    
        >>> pd.concat([s1, s2], keys=['s1', 's2'],
        ...           names=['Series name', 'Row ID'])
        Series name  Row ID
        s1           0         a
                     1         b
        s2           0         c
                     1         d
        dtype: object
    
        Combine two ``DataFrame`` objects with identical columns.
    
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
    
        Combine ``DataFrame`` objects with overlapping columns
        and return everything. Columns outside the intersection will
        be filled with ``NaN`` values.
    
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
    
        Combine ``DataFrame`` objects with overlapping columns
        and return only those that are shared by passing ``inner`` to
        the ``join`` keyword argument.
    
        >>> pd.concat([df1, df3], join="inner")
          letter  number
        0      a       1
        1      b       2
        0      c       3
        1      d       4
    
        Combine ``DataFrame`` objects horizontally along the x axis by
        passing in ``axis=1``.
    
        >>> df4 = pd.DataFrame([['bird', 'polly'], ['monkey', 'george']],
        ...                    columns=['animal', 'name'])
        >>> pd.concat([df1, df4], axis=1)
          letter  number  animal    name
        0      a       1    bird   polly
        1      b       2  monkey  george
    
        Prevent the result from including duplicate index values with the
        ``verify_integrity`` option.
    
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
        



```python
NumpyDocString(pd.concat).render_md()
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



