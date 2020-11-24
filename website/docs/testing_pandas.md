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




## `pd.melt.__doc__`


```python
print(pd.melt.__doc__)
```

    
    Unpivot a DataFrame from wide to long format, optionally leaving identifiers set.
    
    This function is useful to massage a DataFrame into a format where one
    or more columns are identifier variables (`id_vars`), while all other
    columns, considered measured variables (`value_vars`), are "unpivoted" to
    the row axis, leaving just two non-identifier columns, 'variable' and
    'value'.
    
    Parameters
    ----------
    id_vars : tuple, list, or ndarray, optional
        Column(s) to use as identifier variables.
    value_vars : tuple, list, or ndarray, optional
        Column(s) to unpivot. If not specified, uses all columns that
        are not set as `id_vars`.
    var_name : scalar
        Name to use for the 'variable' column. If None it uses
        ``frame.columns.name`` or 'variable'.
    value_name : scalar, default 'value'
        Name to use for the 'value' column.
    col_level : int or str, optional
        If columns are a MultiIndex then use this level to melt.
    ignore_index : bool, default True
        If True, original index is ignored. If False, the original index is retained.
        Index labels will be repeated as necessary.
    
        .. versionadded:: 1.1.0
    
    Returns
    -------
    DataFrame
        Unpivoted DataFrame.
    
    See Also
    --------
    DataFrame.melt : Identical method.
    pivot_table : Create a spreadsheet-style pivot table as a DataFrame.
    DataFrame.pivot : Return reshaped DataFrame organized
        by given index / column values.
    DataFrame.explode : Explode a DataFrame from list-like
            columns to long format.
    
    Examples
    --------
    >>> df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
    ...                    'B': {0: 1, 1: 3, 2: 5},
    ...                    'C': {0: 2, 1: 4, 2: 6}})
    >>> df
       A  B  C
    0  a  1  2
    1  b  3  4
    2  c  5  6
    
    >>> pd.melt(df, id_vars=['A'], value_vars=['B'])
       A variable  value
    0  a        B      1
    1  b        B      3
    2  c        B      5
    
    >>> pd.melt(df, id_vars=['A'], value_vars=['B', 'C'])
       A variable  value
    0  a        B      1
    1  b        B      3
    2  c        B      5
    3  a        C      2
    4  b        C      4
    5  c        C      6
    
    The names of 'variable' and 'value' columns can be customized:
    
    >>> pd.melt(df, id_vars=['A'], value_vars=['B'],
    ...         var_name='myVarname', value_name='myValname')
       A myVarname  myValname
    0  a         B          1
    1  b         B          3
    2  c         B          5
    
    Original index values can be kept around:
    
    >>> pd.melt(df, id_vars=['A'], value_vars=['B', 'C'], ignore_index=False)
       A variable  value
    0  a        B      1
    1  b        B      3
    2  c        B      5
    0  a        C      2
    1  b        C      4
    2  c        C      6
    
    If you have multi-index columns:
    
    >>> df.columns = [list('ABC'), list('DEF')]
    >>> df
       A  B  C
       D  E  F
    0  a  1  2
    1  b  3  4
    2  c  5  6
    
    >>> pd.melt(df, col_level=0, id_vars=['A'], value_vars=['B'])
       A variable  value
    0  a        B      1
    1  b        B      3
    2  c        B      5
    
    >>> pd.melt(df, id_vars=[('A', 'D')], value_vars=[('B', 'E')])
      (A, D) variable_0 variable_1  value
    0      a          B          E      1
    1      b          B          E      3
    2      c          B          E      5
    



```python
NumpyDocString(pd.melt).render_md()
```




## melt

Unpivot a DataFrame from wide to long format, optionally leaving identifiers set. 

This function is useful to massage a DataFrame into a format where one or more columns are identifier variables (`id_vars`), while all other columns, considered measured variables (`value_vars`), are "unpivoted" to the row axis, leaving just two non-identifier columns, 'variable' and 'value'.

### Parameters

| NAME         | TYPE                              | DESCRIPTION                                                                                                                                                               |
|:-------------|:----------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_vars      | tuple, list, or ndarray, optional | Column(s) to use as identifier variables.                                                                                                                                 |
| value_vars   | tuple, list, or ndarray, optional | Column(s) to unpivot. If not specified, uses all columns that are not set as `id_vars`.                                                                                   |
| var_name     | scalar                            | Name to use for the 'variable' column. If None it uses ``frame.columns.name`` or 'variable'.                                                                              |
| value_name   | scalar, default 'value'           | Name to use for the 'value' column.                                                                                                                                       |
| col_level    | int or str, optional              | If columns are a MultiIndex then use this level to melt.                                                                                                                  |
| ignore_index | bool, default True                | If True, original index is ignored. If False, the original index is retained. Index labels will be repeated as necessary. <div><br></br></div>    .. versionadded:: 1.1.0 |

### Returns

| TYPE      | DESCRIPTION          |
|:----------|:---------------------|
| DataFrame | Unpivoted DataFrame. |

### See Also

DataFrame.melt : Identical method.
pivot_table : Create a spreadsheet-style pivot table as a DataFrame.
DataFrame.pivot : Return reshaped DataFrame organized
by given index / column values.
DataFrame.explode : Explode a DataFrame from list-like
columns to long format.


### Examples

```python
>>> df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
...                    'B': {0: 1, 1: 3, 2: 5},
...                    'C': {0: 2, 1: 4, 2: 6}})
>>> df
A  B  C
0  a  1  2
1  b  3  4
2  c  5  6

```

```python
>>> pd.melt(df, id_vars=['A'], value_vars=['B'])
A variable  value
0  a        B      1
1  b        B      3
2  c        B      5

```

```python
>>> pd.melt(df, id_vars=['A'], value_vars=['B', 'C'])
A variable  value
0  a        B      1
1  b        B      3
2  c        B      5
3  a        C      2
4  b        C      4
5  c        C      6

```

The names of 'variable' and 'value' columns can be customized:

```python
>>> pd.melt(df, id_vars=['A'], value_vars=['B'],
...         var_name='myVarname', value_name='myValname')
A myVarname  myValname
0  a         B          1
1  b         B          3
2  c         B          5

```

Original index values can be kept around:

```python
>>> pd.melt(df, id_vars=['A'], value_vars=['B', 'C'], ignore_index=False)
A variable  value
0  a        B      1
1  b        B      3
2  c        B      5
0  a        C      2
1  b        C      4
2  c        C      6

```

If you have multi-index columns:

```python
>>> df.columns = [list('ABC'), list('DEF')]
>>> df
A  B  C
D  E  F
0  a  1  2
1  b  3  4
2  c  5  6

```

```python
>>> pd.melt(df, col_level=0, id_vars=['A'], value_vars=['B'])
A variable  value
0  a        B      1
1  b        B      3
2  c        B      5

```

```python
>>> pd.melt(df, id_vars=[('A', 'D')], value_vars=[('B', 'E')])
(A, D) variable_0 variable_1  value
0      a          B          E      1
1      b          B          E      3
2      c          B          E      5
```




## `pd.isna.__doc__`


```python
print(pd.isna.__doc__)
```

    
        Detect missing values for an array-like object.
    
        This function takes a scalar or array-like object and indicates
        whether values are missing (``NaN`` in numeric arrays, ``None`` or ``NaN``
        in object arrays, ``NaT`` in datetimelike).
    
        Parameters
        ----------
        obj : scalar or array-like
            Object to check for null or missing values.
    
        Returns
        -------
        bool or array-like of bool
            For scalar input, returns a scalar boolean.
            For array input, returns an array of boolean indicating whether each
            corresponding element is missing.
    
        See Also
        --------
        notna : Boolean inverse of pandas.isna.
        Series.isna : Detect missing values in a Series.
        DataFrame.isna : Detect missing values in a DataFrame.
        Index.isna : Detect missing values in an Index.
    
        Examples
        --------
        Scalar arguments (including strings) result in a scalar boolean.
    
        >>> pd.isna('dog')
        False
    
        >>> pd.isna(pd.NA)
        True
    
        >>> pd.isna(np.nan)
        True
    
        ndarrays result in an ndarray of booleans.
    
        >>> array = np.array([[1, np.nan, 3], [4, 5, np.nan]])
        >>> array
        array([[ 1., nan,  3.],
               [ 4.,  5., nan]])
        >>> pd.isna(array)
        array([[False,  True, False],
               [False, False,  True]])
    
        For indexes, an ndarray of booleans is returned.
    
        >>> index = pd.DatetimeIndex(["2017-07-05", "2017-07-06", None,
        ...                           "2017-07-08"])
        >>> index
        DatetimeIndex(['2017-07-05', '2017-07-06', 'NaT', '2017-07-08'],
                      dtype='datetime64[ns]', freq=None)
        >>> pd.isna(index)
        array([False, False,  True, False])
    
        For Series and DataFrame, the same type is returned, containing booleans.
    
        >>> df = pd.DataFrame([['ant', 'bee', 'cat'], ['dog', None, 'fly']])
        >>> df
             0     1    2
        0  ant   bee  cat
        1  dog  None  fly
        >>> pd.isna(df)
               0      1      2
        0  False  False  False
        1  False   True  False
    
        >>> pd.isna(df[1])
        0    False
        1     True
        Name: 1, dtype: bool
        



```python
NumpyDocString(pd.isna).render_md()
```




## isna

Detect missing values for an array-like object. 

This function takes a scalar or array-like object and indicates whether values are missing (``NaN`` in numeric arrays, ``None`` or ``NaN`` in object arrays, ``NaT`` in datetimelike).

### Parameters

| NAME   | TYPE                 | DESCRIPTION                                 |
|:-------|:---------------------|:--------------------------------------------|
| obj    | scalar or array-like | Object to check for null or missing values. |

### Returns

| TYPE                       | DESCRIPTION                                                                                                                                        |
|:---------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| bool or array-like of bool | For scalar input, returns a scalar boolean. For array input, returns an array of boolean indicating whether each corresponding element is missing. |

### See Also

notna : Boolean inverse of pandas.isna.
Series.isna : Detect missing values in a Series.
DataFrame.isna : Detect missing values in a DataFrame.
Index.isna : Detect missing values in an Index.


### Examples

Scalar arguments (including strings) result in a scalar boolean.

```python
>>> pd.isna('dog')
False

```

```python
>>> pd.isna(pd.NA)
True

```

```python
>>> pd.isna(np.nan)
True

```

ndarrays result in an ndarray of booleans.

```python
>>> array = np.array([[1, np.nan, 3], [4, 5, np.nan]])
>>> array
array([[ 1., nan,  3.],
[ 4.,  5., nan]])
>>> pd.isna(array)
array([[False,  True, False],
[False, False,  True]])

```

For indexes, an ndarray of booleans is returned.

```python
>>> index = pd.DatetimeIndex(["2017-07-05", "2017-07-06", None,
...                           "2017-07-08"])
>>> index
DatetimeIndex(['2017-07-05', '2017-07-06', 'NaT', '2017-07-08'],
dtype='datetime64[ns]', freq=None)
>>> pd.isna(index)
array([False, False,  True, False])

```

For Series and DataFrame, the same type is returned, containing booleans.

```python
>>> df = pd.DataFrame([['ant', 'bee', 'cat'], ['dog', None, 'fly']])
>>> df
0     1    2
0  ant   bee  cat
1  dog  None  fly
>>> pd.isna(df)
0      1      2
0  False  False  False
1  False   True  False

```

```python
>>> pd.isna(df[1])
0    False
1     True
Name: 1, dtype: bool
```




## `pd.to_datetime.__doc__`


```python
print(pd.to_datetime.__doc__)
```

    
        Convert argument to datetime.
    
        Parameters
        ----------
        arg : int, float, str, datetime, list, tuple, 1-d array, Series, DataFrame/dict-like
            The object to convert to a datetime.
        errors : {'ignore', 'raise', 'coerce'}, default 'raise'
            - If 'raise', then invalid parsing will raise an exception.
            - If 'coerce', then invalid parsing will be set as NaT.
            - If 'ignore', then invalid parsing will return the input.
        dayfirst : bool, default False
            Specify a date parse order if `arg` is str or its list-likes.
            If True, parses dates with the day first, eg 10/11/12 is parsed as
            2012-11-10.
            Warning: dayfirst=True is not strict, but will prefer to parse
            with day first (this is a known bug, based on dateutil behavior).
        yearfirst : bool, default False
            Specify a date parse order if `arg` is str or its list-likes.
    
            - If True parses dates with the year first, eg 10/11/12 is parsed as
              2010-11-12.
            - If both dayfirst and yearfirst are True, yearfirst is preceded (same
              as dateutil).
    
            Warning: yearfirst=True is not strict, but will prefer to parse
            with year first (this is a known bug, based on dateutil behavior).
        utc : bool, default None
            Return UTC DatetimeIndex if True (converting any tz-aware
            datetime.datetime objects as well).
        format : str, default None
            The strftime to parse time, eg "%d/%m/%Y", note that "%f" will parse
            all the way up to nanoseconds.
            See strftime documentation for more information on choices:
            https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior.
        exact : bool, True by default
            Behaves as:
            - If True, require an exact format match.
            - If False, allow the format to match anywhere in the target string.
    
        unit : str, default 'ns'
            The unit of the arg (D,s,ms,us,ns) denote the unit, which is an
            integer or float number. This will be based off the origin.
            Example, with unit='ms' and origin='unix' (the default), this
            would calculate the number of milliseconds to the unix epoch start.
        infer_datetime_format : bool, default False
            If True and no `format` is given, attempt to infer the format of the
            datetime strings based on the first non-NaN element,
            and if it can be inferred, switch to a faster method of parsing them.
            In some cases this can increase the parsing speed by ~5-10x.
        origin : scalar, default 'unix'
            Define the reference date. The numeric values would be parsed as number
            of units (defined by `unit`) since this reference date.
    
            - If 'unix' (or POSIX) time; origin is set to 1970-01-01.
            - If 'julian', unit must be 'D', and origin is set to beginning of
              Julian Calendar. Julian day number 0 is assigned to the day starting
              at noon on January 1, 4713 BC.
            - If Timestamp convertible, origin is set to Timestamp identified by
              origin.
        cache : bool, default True
            If True, use a cache of unique, converted dates to apply the datetime
            conversion. May produce significant speed-up when parsing duplicate
            date strings, especially ones with timezone offsets. The cache is only
            used when there are at least 50 values. The presence of out-of-bounds
            values will render the cache unusable and may slow down parsing.
    
            .. versionadded:: 0.23.0
    
            .. versionchanged:: 0.25.0
                - changed default value from False to True.
    
        Returns
        -------
        datetime
            If parsing succeeded.
            Return type depends on input:
    
            - list-like: DatetimeIndex
            - Series: Series of datetime64 dtype
            - scalar: Timestamp
    
            In case when it is not possible to return designated types (e.g. when
            any element of input is before Timestamp.min or after Timestamp.max)
            return will have datetime.datetime type (or corresponding
            array/Series).
    
        See Also
        --------
        DataFrame.astype : Cast argument to a specified dtype.
        to_timedelta : Convert argument to timedelta.
        convert_dtypes : Convert dtypes.
    
        Examples
        --------
        Assembling a datetime from multiple columns of a DataFrame. The keys can be
        common abbreviations like ['year', 'month', 'day', 'minute', 'second',
        'ms', 'us', 'ns']) or plurals of the same
    
        >>> df = pd.DataFrame({'year': [2015, 2016],
        ...                    'month': [2, 3],
        ...                    'day': [4, 5]})
        >>> pd.to_datetime(df)
        0   2015-02-04
        1   2016-03-05
        dtype: datetime64[ns]
    
        If a date does not meet the `timestamp limitations
        <https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html
        #timeseries-timestamp-limits>`_, passing errors='ignore'
        will return the original input instead of raising any exception.
    
        Passing errors='coerce' will force an out-of-bounds date to NaT,
        in addition to forcing non-dates (or non-parseable dates) to NaT.
    
        >>> pd.to_datetime('13000101', format='%Y%m%d', errors='ignore')
        datetime.datetime(1300, 1, 1, 0, 0)
        >>> pd.to_datetime('13000101', format='%Y%m%d', errors='coerce')
        NaT
    
        Passing infer_datetime_format=True can often-times speedup a parsing
        if its not an ISO8601 format exactly, but in a regular format.
    
        >>> s = pd.Series(['3/11/2000', '3/12/2000', '3/13/2000'] * 1000)
        >>> s.head()
        0    3/11/2000
        1    3/12/2000
        2    3/13/2000
        3    3/11/2000
        4    3/12/2000
        dtype: object
    
        >>> %timeit pd.to_datetime(s, infer_datetime_format=True)  # doctest: +SKIP
        100 loops, best of 3: 10.4 ms per loop
    
        >>> %timeit pd.to_datetime(s, infer_datetime_format=False)  # doctest: +SKIP
        1 loop, best of 3: 471 ms per loop
    
        Using a unix epoch time
    
        >>> pd.to_datetime(1490195805, unit='s')
        Timestamp('2017-03-22 15:16:45')
        >>> pd.to_datetime(1490195805433502912, unit='ns')
        Timestamp('2017-03-22 15:16:45.433502912')
    
        .. warning:: For float arg, precision rounding might happen. To prevent
            unexpected behavior use a fixed-width exact type.
    
        Using a non-unix epoch origin
    
        >>> pd.to_datetime([1, 2, 3], unit='D',
        ...                origin=pd.Timestamp('1960-01-01'))
        DatetimeIndex(['1960-01-02', '1960-01-03', '1960-01-04'], dtype='datetime64[ns]', freq=None)
        



```python
NumpyDocString(pd.to_datetime).render_md()
```




## to_datetime

Convert argument to datetime.

### Parameters

| NAME                                                                   | TYPE                                                                           | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|:-----------------------------------------------------------------------|:-------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| arg                                                                    | int, float, str, datetime, list, tuple, 1-d array, Series, DataFrame/dict-like | The object to convert to a datetime.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| errors                                                                 | {'ignore', 'raise', 'coerce'}, default 'raise'                                 | - If 'raise', then invalid parsing will raise an exception. - If 'coerce', then invalid parsing will be set as NaT. - If 'ignore', then invalid parsing will return the input.                                                                                                                                                                                                                                                                                                                                  |
| dayfirst                                                               | bool, default False                                                            | Specify a date parse order if `arg` is str or its list-likes. If True, parses dates with the day first, eg 10/11/12 is parsed as 2012-11-10. Warning: dayfirst=True is not strict, but will prefer to parse with day first (this is a known bug, based on dateutil behavior).                                                                                                                                                                                                                                   |
| yearfirst                                                              | bool, default False                                                            | Specify a date parse order if `arg` is str or its list-likes. <div><br></br></div>        - If True parses dates with the year first, eg 10/11/12 is parsed as 2010-11-12.                                                                                                                                                                                                                                                                                                                                      |
| - If both dayfirst and yearfirst are True, yearfirst is preceded (same |                                                                                | as dateutil). <div><br></br></div>        Warning: yearfirst=True is not strict, but will prefer to parse with year first (this is a known bug, based on dateutil behavior).                                                                                                                                                                                                                                                                                                                                    |
| utc                                                                    | bool, default None                                                             | Return UTC DatetimeIndex if True (converting any tz-aware datetime.datetime objects as well).                                                                                                                                                                                                                                                                                                                                                                                                                   |
| format                                                                 | str, default None                                                              | The strftime to parse time, eg "%d/%m/%Y", note that "%f" will parse all the way up to nanoseconds. See strftime documentation for more information on choices: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior.                                                                                                                                                                                                                                                                 |
| exact                                                                  | bool, True by default                                                          | Behaves as: - If True, require an exact format match. - If False, allow the format to match anywhere in the target string.                                                                                                                                                                                                                                                                                                                                                                                      |
| unit                                                                   | str, default 'ns'                                                              | The unit of the arg (D,s,ms,us,ns) denote the unit, which is an integer or float number. This will be based off the origin. Example, with unit='ms' and origin='unix' (the default), this would calculate the number of milliseconds to the unix epoch start.                                                                                                                                                                                                                                                   |
| infer_datetime_format                                                  | bool, default False                                                            | If True and no `format` is given, attempt to infer the format of the datetime strings based on the first non-NaN element, and if it can be inferred, switch to a faster method of parsing them. In some cases this can increase the parsing speed by ~5-10x.                                                                                                                                                                                                                                                    |
| origin                                                                 | scalar, default 'unix'                                                         | Define the reference date. The numeric values would be parsed as number of units (defined by `unit`) since this reference date. <div><br></br></div>        - If 'unix' (or POSIX) time; origin is set to 1970-01-01. - If 'julian', unit must be 'D', and origin is set to beginning of Julian Calendar. Julian day number 0 is assigned to the day starting at noon on January 1, 4713 BC.                                                                                                                    |
| - If Timestamp convertible, origin is set to Timestamp identified by   |                                                                                | origin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| cache                                                                  | bool, default True                                                             | If True, use a cache of unique, converted dates to apply the datetime conversion. May produce significant speed-up when parsing duplicate date strings, especially ones with timezone offsets. The cache is only used when there are at least 50 values. The presence of out-of-bounds values will render the cache unusable and may slow down parsing. <div><br></br></div>        .. versionadded:: 0.23.0 <div><br></br></div>        .. versionchanged:: 0.25.0 - changed default value from False to True. |

### Returns

| TYPE     | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                     |
|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| datetime | If parsing succeeded. Return type depends on input: <br></br> - list-like: DatetimeIndex - Series: Series of datetime64 dtype - scalar: Timestamp <br></br> In case when it is not possible to return designated types (e.g. when any element of input is before Timestamp.min or after Timestamp.max) return will have datetime.datetime type (or corresponding array/Series). |

### See Also

DataFrame.astype : Cast argument to a specified dtype.
to_timedelta : Convert argument to timedelta.
convert_dtypes : Convert dtypes.


### Examples

Assembling a datetime from multiple columns of a DataFrame. The keys can be
common abbreviations like ['year', 'month', 'day', 'minute', 'second',
'ms', 'us', 'ns']) or plurals of the same

```python
>>> df = pd.DataFrame({'year': [2015, 2016],
...                    'month': [2, 3],
...                    'day': [4, 5]})
>>> pd.to_datetime(df)
0   2015-02-04
1   2016-03-05
dtype: datetime64[ns]

```

If a date does not meet the `timestamp limitations
<https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html
#timeseries-timestamp-limits>`_, passing errors='ignore'
will return the original input instead of raising any exception.

Passing errors='coerce' will force an out-of-bounds date to NaT,
in addition to forcing non-dates (or non-parseable dates) to NaT.

```python
>>> pd.to_datetime('13000101', format='%Y%m%d', errors='ignore')
datetime.datetime(1300, 1, 1, 0, 0)
>>> pd.to_datetime('13000101', format='%Y%m%d', errors='coerce')
NaT

```

Passing infer_datetime_format=True can often-times speedup a parsing
if its not an ISO8601 format exactly, but in a regular format.

```python
>>> s = pd.Series(['3/11/2000', '3/12/2000', '3/13/2000'] * 1000)
>>> s.head()
0    3/11/2000
1    3/12/2000
2    3/13/2000
3    3/11/2000
4    3/12/2000
dtype: object

```

```python
>>> %timeit pd.to_datetime(s, infer_datetime_format=True)  # doctest: +SKIP
100 loops, best of 3: 10.4 ms per loop

```

```python
>>> %timeit pd.to_datetime(s, infer_datetime_format=False)  # doctest: +SKIP
1 loop, best of 3: 471 ms per loop

```

Using a unix epoch time

```python
>>> pd.to_datetime(1490195805, unit='s')
Timestamp('2017-03-22 15:16:45')
>>> pd.to_datetime(1490195805433502912, unit='ns')
Timestamp('2017-03-22 15:16:45.433502912')

```

.. warning:: For float arg, precision rounding might happen. To prevent
unexpected behavior use a fixed-width exact type.

Using a non-unix epoch origin

```python
>>> pd.to_datetime([1, 2, 3], unit='D',
...                origin=pd.Timestamp('1960-01-01'))
DatetimeIndex(['1960-01-02', '1960-01-03', '1960-01-04'], dtype='datetime64[ns]', freq=None)
```



