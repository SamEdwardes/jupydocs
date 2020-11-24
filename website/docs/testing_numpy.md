---
id: testing_numpy
title: Testing on Numpy
---

```python
from jupydocs.numpydocstring import NumpyDocString, render_class
```


```python
import numpy as np
```

## `np.sum.__doc__`


```python
print(np.sum.__doc__)
```

    
        Sum of array elements over a given axis.
    
        Parameters
        ----------
        a : array_like
            Elements to sum.
        axis : None or int or tuple of ints, optional
            Axis or axes along which a sum is performed.  The default,
            axis=None, will sum all of the elements of the input array.  If
            axis is negative it counts from the last to the first axis.
    
            .. versionadded:: 1.7.0
    
            If axis is a tuple of ints, a sum is performed on all of the axes
            specified in the tuple instead of a single axis or all the axes as
            before.
        dtype : dtype, optional
            The type of the returned array and of the accumulator in which the
            elements are summed.  The dtype of `a` is used by default unless `a`
            has an integer dtype of less precision than the default platform
            integer.  In that case, if `a` is signed then the platform integer
            is used while if `a` is unsigned then an unsigned integer of the
            same precision as the platform integer is used.
        out : ndarray, optional
            Alternative output array in which to place the result. It must have
            the same shape as the expected output, but the type of the output
            values will be cast if necessary.
        keepdims : bool, optional
            If this is set to True, the axes which are reduced are left
            in the result as dimensions with size one. With this option,
            the result will broadcast correctly against the input array.
    
            If the default value is passed, then `keepdims` will not be
            passed through to the `sum` method of sub-classes of
            `ndarray`, however any non-default value will be.  If the
            sub-class' method does not implement `keepdims` any
            exceptions will be raised.
        initial : scalar, optional
            Starting value for the sum. See `~numpy.ufunc.reduce` for details.
    
            .. versionadded:: 1.15.0
    
        where : array_like of bool, optional
            Elements to include in the sum. See `~numpy.ufunc.reduce` for details.
    
            .. versionadded:: 1.17.0
    
        Returns
        -------
        sum_along_axis : ndarray
            An array with the same shape as `a`, with the specified
            axis removed.   If `a` is a 0-d array, or if `axis` is None, a scalar
            is returned.  If an output array is specified, a reference to
            `out` is returned.
    
        See Also
        --------
        ndarray.sum : Equivalent method.
    
        add.reduce : Equivalent functionality of `add`.
    
        cumsum : Cumulative sum of array elements.
    
        trapz : Integration of array values using the composite trapezoidal rule.
    
        mean, average
    
        Notes
        -----
        Arithmetic is modular when using integer types, and no error is
        raised on overflow.
    
        The sum of an empty array is the neutral element 0:
    
        >>> np.sum([])
        0.0
    
        For floating point numbers the numerical precision of sum (and
        ``np.add.reduce``) is in general limited by directly adding each number
        individually to the result causing rounding errors in every step.
        However, often numpy will use a  numerically better approach (partial
        pairwise summation) leading to improved precision in many use-cases.
        This improved precision is always provided when no ``axis`` is given.
        When ``axis`` is given, it will depend on which axis is summed.
        Technically, to provide the best speed possible, the improved precision
        is only used when the summation is along the fast axis in memory.
        Note that the exact precision may vary depending on other parameters.
        In contrast to NumPy, Python's ``math.fsum`` function uses a slower but
        more precise approach to summation.
        Especially when summing a large number of lower precision floating point
        numbers, such as ``float32``, numerical errors can become significant.
        In such cases it can be advisable to use `dtype="float64"` to use a higher
        precision for the output.
    
        Examples
        --------
        >>> np.sum([0.5, 1.5])
        2.0
        >>> np.sum([0.5, 0.7, 0.2, 1.5], dtype=np.int32)
        1
        >>> np.sum([[0, 1], [0, 5]])
        6
        >>> np.sum([[0, 1], [0, 5]], axis=0)
        array([0, 6])
        >>> np.sum([[0, 1], [0, 5]], axis=1)
        array([1, 5])
        >>> np.sum([[0, 1], [np.nan, 5]], where=[False, True], axis=1)
        array([1., 5.])
    
        If the accumulator is too small, overflow occurs:
    
        >>> np.ones(128, dtype=np.int8).sum(dtype=np.int8)
        -128
    
        You can also start the sum with a value other than zero:
    
        >>> np.sum([10], initial=5)
        15
        



```python
NumpyDocString(np.sum).render_md()
```




## sum

Sum of array elements over a given axis.

### Parameters

| NAME     | TYPE                                   | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|:---------|:---------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| a        | array_like                             | Elements to sum.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| axis     | None or int or tuple of ints, optional | Axis or axes along which a sum is performed.  The default, axis=None, will sum all of the elements of the input array.  If axis is negative it counts from the last to the first axis. <div><br></br></div>        .. versionadded:: 1.7.0 <div><br></br></div>        If axis is a tuple of ints, a sum is performed on all of the axes specified in the tuple instead of a single axis or all the axes as before.                                                         |
| dtype    | dtype, optional                        | The type of the returned array and of the accumulator in which the elements are summed.  The dtype of `a` is used by default unless `a` has an integer dtype of less precision than the default platform integer.  In that case, if `a` is signed then the platform integer is used while if `a` is unsigned then an unsigned integer of the same precision as the platform integer is used.                                                                                |
| out      | ndarray, optional                      | Alternative output array in which to place the result. It must have the same shape as the expected output, but the type of the output values will be cast if necessary.                                                                                                                                                                                                                                                                                                     |
| keepdims | bool, optional                         | If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the input array. <div><br></br></div>        If the default value is passed, then `keepdims` will not be passed through to the `sum` method of sub-classes of `ndarray`, however any non-default value will be.  If the sub-class' method does not implement `keepdims` any exceptions will be raised. |
| initial  | scalar, optional                       | Starting value for the sum. See `~numpy.ufunc.reduce` for details. <div><br></br></div>        .. versionadded:: 1.15.0                                                                                                                                                                                                                                                                                                                                                     |
| where    | array_like of bool, optional           | Elements to include in the sum. See `~numpy.ufunc.reduce` for details. <div><br></br></div>        .. versionadded:: 1.17.0                                                                                                                                                                                                                                                                                                                                                 |

### Returns

| NAME           | TYPE    | DESCRIPTION                                                                                                                                                                                                    |
|:---------------|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| sum_along_axis | ndarray | An array with the same shape as `a`, with the specified axis removed.   If `a` is a 0-d array, or if `axis` is None, a scalar is returned.  If an output array is specified, a reference to `out` is returned. |

### See Also

ndarray.sum : Equivalent method.

add.reduce : Equivalent functionality of `add`.

cumsum : Cumulative sum of array elements.

trapz : Integration of array values using the composite trapezoidal rule.

mean, average


### Examples

```python
>>> np.sum([0.5, 1.5])
2.0
>>> np.sum([0.5, 0.7, 0.2, 1.5], dtype=np.int32)
1
>>> np.sum([[0, 1], [0, 5]])
6
>>> np.sum([[0, 1], [0, 5]], axis=0)
array([0, 6])
>>> np.sum([[0, 1], [0, 5]], axis=1)
array([1, 5])
>>> np.sum([[0, 1], [np.nan, 5]], where=[False, True], axis=1)
array([1., 5.])

```

If the accumulator is too small, overflow occurs:

```python
>>> np.ones(128, dtype=np.int8).sum(dtype=np.int8)
-128

```

You can also start the sum with a value other than zero:

```python
>>> np.sum([10], initial=5)
15
```




## `np.median.__doc__`


```python
print(np.median.__doc__)
```

    
        Compute the median along the specified axis.
    
        Returns the median of the array elements.
    
        Parameters
        ----------
        a : array_like
            Input array or object that can be converted to an array.
        axis : {int, sequence of int, None}, optional
            Axis or axes along which the medians are computed. The default
            is to compute the median along a flattened version of the array.
            A sequence of axes is supported since version 1.9.0.
        out : ndarray, optional
            Alternative output array in which to place the result. It must
            have the same shape and buffer length as the expected output,
            but the type (of the output) will be cast if necessary.
        overwrite_input : bool, optional
           If True, then allow use of memory of input array `a` for
           calculations. The input array will be modified by the call to
           `median`. This will save memory when you do not need to preserve
           the contents of the input array. Treat the input as undefined,
           but it will probably be fully or partially sorted. Default is
           False. If `overwrite_input` is ``True`` and `a` is not already an
           `ndarray`, an error will be raised.
        keepdims : bool, optional
            If this is set to True, the axes which are reduced are left
            in the result as dimensions with size one. With this option,
            the result will broadcast correctly against the original `arr`.
    
            .. versionadded:: 1.9.0
    
        Returns
        -------
        median : ndarray
            A new array holding the result. If the input contains integers
            or floats smaller than ``float64``, then the output data-type is
            ``np.float64``.  Otherwise, the data-type of the output is the
            same as that of the input. If `out` is specified, that array is
            returned instead.
    
        See Also
        --------
        mean, percentile
    
        Notes
        -----
        Given a vector ``V`` of length ``N``, the median of ``V`` is the
        middle value of a sorted copy of ``V``, ``V_sorted`` - i
        e., ``V_sorted[(N-1)/2]``, when ``N`` is odd, and the average of the
        two middle values of ``V_sorted`` when ``N`` is even.
    
        Examples
        --------
        >>> a = np.array([[10, 7, 4], [3, 2, 1]])
        >>> a
        array([[10,  7,  4],
               [ 3,  2,  1]])
        >>> np.median(a)
        3.5
        >>> np.median(a, axis=0)
        array([6.5, 4.5, 2.5])
        >>> np.median(a, axis=1)
        array([7.,  2.])
        >>> m = np.median(a, axis=0)
        >>> out = np.zeros_like(m)
        >>> np.median(a, axis=0, out=m)
        array([6.5,  4.5,  2.5])
        >>> m
        array([6.5,  4.5,  2.5])
        >>> b = a.copy()
        >>> np.median(b, axis=1, overwrite_input=True)
        array([7.,  2.])
        >>> assert not np.all(a==b)
        >>> b = a.copy()
        >>> np.median(b, axis=None, overwrite_input=True)
        3.5
        >>> assert not np.all(a==b)
    
        



```python
NumpyDocString(np.median).render_md()
```




## median

Compute the median along the specified axis. 

Returns the median of the array elements.

### Parameters

| NAME            | TYPE                                   | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                |
|:----------------|:---------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| a               | array_like                             | Input array or object that can be converted to an array.                                                                                                                                                                                                                                                                                                                                                                   |
| axis            | {int, sequence of int, None}, optional | Axis or axes along which the medians are computed. The default is to compute the median along a flattened version of the array. A sequence of axes is supported since version 1.9.0.                                                                                                                                                                                                                                       |
| out             | ndarray, optional                      | Alternative output array in which to place the result. It must have the same shape and buffer length as the expected output, but the type (of the output) will be cast if necessary.                                                                                                                                                                                                                                       |
| overwrite_input | bool, optional                         | If True, then allow use of memory of input array `a` for calculations. The input array will be modified by the call to `median`. This will save memory when you do not need to preserve the contents of the input array. Treat the input as undefined, but it will probably be fully or partially sorted. Default is False. If `overwrite_input` is ``True`` and `a` is not already an `ndarray`, an error will be raised. |
| keepdims        | bool, optional                         | If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the original `arr`. <div><br></br></div>        .. versionadded:: 1.9.0                                                                                                                                                                               |

### Returns

| NAME   | TYPE    | DESCRIPTION                                                                                                                                                                                                                                                                      |
|:-------|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| median | ndarray | A new array holding the result. If the input contains integers or floats smaller than ``float64``, then the output data-type is ``np.float64``.  Otherwise, the data-type of the output is the same as that of the input. If `out` is specified, that array is returned instead. |

### See Also

mean, percentile


### Examples

```python
>>> a = np.array([[10, 7, 4], [3, 2, 1]])
>>> a
array([[10,  7,  4],
[ 3,  2,  1]])
>>> np.median(a)
3.5
>>> np.median(a, axis=0)
array([6.5, 4.5, 2.5])
>>> np.median(a, axis=1)
array([7.,  2.])
>>> m = np.median(a, axis=0)
>>> out = np.zeros_like(m)
>>> np.median(a, axis=0, out=m)
array([6.5,  4.5,  2.5])
>>> m
array([6.5,  4.5,  2.5])
>>> b = a.copy()
>>> np.median(b, axis=1, overwrite_input=True)
array([7.,  2.])
>>> assert not np.all(a==b)
>>> b = a.copy()
>>> np.median(b, axis=None, overwrite_input=True)
3.5
>>> assert not np.all(a==b)

```




## `np.argmax.__doc__`


```python
print(np.argmax.__doc__)
```

    
        Returns the indices of the maximum values along an axis.
    
        Parameters
        ----------
        a : array_like
            Input array.
        axis : int, optional
            By default, the index is into the flattened array, otherwise
            along the specified axis.
        out : array, optional
            If provided, the result will be inserted into this array. It should
            be of the appropriate shape and dtype.
    
        Returns
        -------
        index_array : ndarray of ints
            Array of indices into the array. It has the same shape as `a.shape`
            with the dimension along `axis` removed.
    
        See Also
        --------
        ndarray.argmax, argmin
        amax : The maximum value along a given axis.
        unravel_index : Convert a flat index into an index tuple.
        take_along_axis : Apply ``np.expand_dims(index_array, axis)``
                          from argmax to an array as if by calling max.
    
        Notes
        -----
        In case of multiple occurrences of the maximum values, the indices
        corresponding to the first occurrence are returned.
    
        Examples
        --------
        >>> a = np.arange(6).reshape(2,3) + 10
        >>> a
        array([[10, 11, 12],
               [13, 14, 15]])
        >>> np.argmax(a)
        5
        >>> np.argmax(a, axis=0)
        array([1, 1, 1])
        >>> np.argmax(a, axis=1)
        array([2, 2])
    
        Indexes of the maximal elements of a N-dimensional array:
    
        >>> ind = np.unravel_index(np.argmax(a, axis=None), a.shape)
        >>> ind
        (1, 2)
        >>> a[ind]
        15
    
        >>> b = np.arange(6)
        >>> b[1] = 5
        >>> b
        array([0, 5, 2, 3, 4, 5])
        >>> np.argmax(b)  # Only the first occurrence is returned.
        1
    
        >>> x = np.array([[4,2,3], [1,0,3]])
        >>> index_array = np.argmax(x, axis=-1)
        >>> # Same as np.max(x, axis=-1, keepdims=True)
        >>> np.take_along_axis(x, np.expand_dims(index_array, axis=-1), axis=-1)
        array([[4],
               [3]])
        >>> # Same as np.max(x, axis=-1)
        >>> np.take_along_axis(x, np.expand_dims(index_array, axis=-1), axis=-1).squeeze(axis=-1)
        array([4, 3])
    
        



```python
NumpyDocString(np.argmax).render_md()
```




## argmax

Returns the indices of the maximum values along an axis.

### Parameters

| NAME   | TYPE            | DESCRIPTION                                                                                                |
|:-------|:----------------|:-----------------------------------------------------------------------------------------------------------|
| a      | array_like      | Input array.                                                                                               |
| axis   | int, optional   | By default, the index is into the flattened array, otherwise along the specified axis.                     |
| out    | array, optional | If provided, the result will be inserted into this array. It should be of the appropriate shape and dtype. |

### Returns

| NAME        | TYPE            | DESCRIPTION                                                                                                  |
|:------------|:----------------|:-------------------------------------------------------------------------------------------------------------|
| index_array | ndarray of ints | Array of indices into the array. It has the same shape as `a.shape` with the dimension along `axis` removed. |

### See Also

ndarray.argmax, argmin
amax : The maximum value along a given axis.
unravel_index : Convert a flat index into an index tuple.
take_along_axis : Apply ``np.expand_dims(index_array, axis)``
from argmax to an array as if by calling max.


### Examples

```python
>>> a = np.arange(6).reshape(2,3) + 10
>>> a
array([[10, 11, 12],
[13, 14, 15]])
>>> np.argmax(a)
5
>>> np.argmax(a, axis=0)
array([1, 1, 1])
>>> np.argmax(a, axis=1)
array([2, 2])

```

Indexes of the maximal elements of a N-dimensional array:

```python
>>> ind = np.unravel_index(np.argmax(a, axis=None), a.shape)
>>> ind
(1, 2)
>>> a[ind]
15

```

```python
>>> b = np.arange(6)
>>> b[1] = 5
>>> b
array([0, 5, 2, 3, 4, 5])
>>> np.argmax(b)  # Only the first occurrence is returned.
1

```

```python
>>> x = np.array([[4,2,3], [1,0,3]])
>>> index_array = np.argmax(x, axis=-1)
>>> # Same as np.max(x, axis=-1, keepdims=True)
>>> np.take_along_axis(x, np.expand_dims(index_array, axis=-1), axis=-1)
array([[4],
[3]])
>>> # Same as np.max(x, axis=-1)
>>> np.take_along_axis(x, np.expand_dims(index_array, axis=-1), axis=-1).squeeze(axis=-1)
array([4, 3])

```




## `np.array.__doc__`


```python
print(np.array.__doc__)
```

    array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0)
    
        Create an array.
    
        Parameters
        ----------
        object : array_like
            An array, any object exposing the array interface, an object whose
            __array__ method returns an array, or any (nested) sequence.
        dtype : data-type, optional
            The desired data-type for the array.  If not given, then the type will
            be determined as the minimum type required to hold the objects in the
            sequence.
        copy : bool, optional
            If true (default), then the object is copied.  Otherwise, a copy will
            only be made if __array__ returns a copy, if obj is a nested sequence,
            or if a copy is needed to satisfy any of the other requirements
            (`dtype`, `order`, etc.).
        order : {'K', 'A', 'C', 'F'}, optional
            Specify the memory layout of the array. If object is not an array, the
            newly created array will be in C order (row major) unless 'F' is
            specified, in which case it will be in Fortran order (column major).
            If object is an array the following holds.
    
            ===== ========= ===================================================
            order  no copy                     copy=True
            ===== ========= ===================================================
            'K'   unchanged F & C order preserved, otherwise most similar order
            'A'   unchanged F order if input is F and not C, otherwise C order
            'C'   C order   C order
            'F'   F order   F order
            ===== ========= ===================================================
    
            When ``copy=False`` and a copy is made for other reasons, the result is
            the same as if ``copy=True``, with some exceptions for `A`, see the
            Notes section. The default order is 'K'.
        subok : bool, optional
            If True, then sub-classes will be passed-through, otherwise
            the returned array will be forced to be a base-class array (default).
        ndmin : int, optional
            Specifies the minimum number of dimensions that the resulting
            array should have.  Ones will be pre-pended to the shape as
            needed to meet this requirement.
    
        Returns
        -------
        out : ndarray
            An array object satisfying the specified requirements.
    
        See Also
        --------
        empty_like : Return an empty array with shape and type of input.
        ones_like : Return an array of ones with shape and type of input.
        zeros_like : Return an array of zeros with shape and type of input.
        full_like : Return a new array with shape of input filled with value.
        empty : Return a new uninitialized array.
        ones : Return a new array setting values to one.
        zeros : Return a new array setting values to zero.
        full : Return a new array of given shape filled with value.
    
    
        Notes
        -----
        When order is 'A' and `object` is an array in neither 'C' nor 'F' order,
        and a copy is forced by a change in dtype, then the order of the result is
        not necessarily 'C' as expected. This is likely a bug.
    
        Examples
        --------
        >>> np.array([1, 2, 3])
        array([1, 2, 3])
    
        Upcasting:
    
        >>> np.array([1, 2, 3.0])
        array([ 1.,  2.,  3.])
    
        More than one dimension:
    
        >>> np.array([[1, 2], [3, 4]])
        array([[1, 2],
               [3, 4]])
    
        Minimum dimensions 2:
    
        >>> np.array([1, 2, 3], ndmin=2)
        array([[1, 2, 3]])
    
        Type provided:
    
        >>> np.array([1, 2, 3], dtype=complex)
        array([ 1.+0.j,  2.+0.j,  3.+0.j])
    
        Data-type consisting of more than one element:
    
        >>> x = np.array([(1,2),(3,4)],dtype=[('a','<i4'),('b','<i4')])
        >>> x['a']
        array([1, 3])
    
        Creating an array from sub-classes:
    
        >>> np.array(np.mat('1 2; 3 4'))
        array([[1, 2],
               [3, 4]])
    
        >>> np.array(np.mat('1 2; 3 4'), subok=True)
        matrix([[1, 2],
                [3, 4]])



```python
NumpyDocString(np.array).render_md()
```




## array

array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0) 

Create an array.

### Parameters

| NAME   | TYPE                           | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:-------|:-------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| object | array_like                     | An array, any object exposing the array interface, an object whose __array__ method returns an array, or any (nested) sequence.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| dtype  | data-type, optional            | The desired data-type for the array.  If not given, then the type will be determined as the minimum type required to hold the objects in the sequence.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| copy   | bool, optional                 | If true (default), then the object is copied.  Otherwise, a copy will only be made if __array__ returns a copy, if obj is a nested sequence, or if a copy is needed to satisfy any of the other requirements (`dtype`, `order`, etc.).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| order  | {'K', 'A', 'C', 'F'}, optional | Specify the memory layout of the array. If object is not an array, the newly created array will be in C order (row major) unless 'F' is specified, in which case it will be in Fortran order (column major). If object is an array the following holds. <div><br></br></div>        ===== ========= =================================================== order  no copy                     copy=True ===== ========= =================================================== 'K'   unchanged F & C order preserved, otherwise most similar order 'A'   unchanged F order if input is F and not C, otherwise C order 'C'   C order   C order 'F'   F order   F order ===== ========= =================================================== <div><br></br></div>        When ``copy=False`` and a copy is made for other reasons, the result is the same as if ``copy=True``, with some exceptions for `A`, see the Notes section. The default order is 'K'. |
| subok  | bool, optional                 | If True, then sub-classes will be passed-through, otherwise the returned array will be forced to be a base-class array (default).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ndmin  | int, optional                  | Specifies the minimum number of dimensions that the resulting array should have.  Ones will be pre-pended to the shape as needed to meet this requirement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

### Returns

| NAME   | TYPE    | DESCRIPTION                                            |
|:-------|:--------|:-------------------------------------------------------|
| out    | ndarray | An array object satisfying the specified requirements. |

### See Also

empty_like : Return an empty array with shape and type of input.
ones_like : Return an array of ones with shape and type of input.
zeros_like : Return an array of zeros with shape and type of input.
full_like : Return a new array with shape of input filled with value.
empty : Return a new uninitialized array.
ones : Return a new array setting values to one.
zeros : Return a new array setting values to zero.
full : Return a new array of given shape filled with value.



### Examples

```python
>>> np.array([1, 2, 3])
array([1, 2, 3])

```

Upcasting:

```python
>>> np.array([1, 2, 3.0])
array([ 1.,  2.,  3.])

```

More than one dimension:

```python
>>> np.array([[1, 2], [3, 4]])
array([[1, 2],
[3, 4]])

```

Minimum dimensions 2:

```python
>>> np.array([1, 2, 3], ndmin=2)
array([[1, 2, 3]])

```

Type provided:

```python
>>> np.array([1, 2, 3], dtype=complex)
array([ 1.+0.j,  2.+0.j,  3.+0.j])

```

Data-type consisting of more than one element:

```python
>>> x = np.array([(1,2),(3,4)],dtype=[('a','<i4'),('b','<i4')])
>>> x['a']
array([1, 3])

```

Creating an array from sub-classes:

```python
>>> np.array(np.mat('1 2; 3 4'))
array([[1, 2],
[3, 4]])

```

```python
>>> np.array(np.mat('1 2; 3 4'), subok=True)
matrix([[1, 2],
```



