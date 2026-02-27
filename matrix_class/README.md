## Background
This directory contains supporting code for my blog post (coming soon) on operator overloading and Python's generator/sequence protocol. I thought it would be interesting to implement two objects: `Vector` and `Matrix2D` and understand how Python handles custom methods especially when the object types differ. You can find a deeper discussion in the blog post.

In this README I include a table of the computations that you can perform; some of these differ from `numpy`. I also provide more detail about the classes and their properties and methods. 

### Valid operations
| Operation | How-to | Return type
| -------- | ------- | ------- |
| Vector addition $^{1}$  | `Vector()` + `Vector()`| `Vector` |
| Vector subtraction $^{2}$ | `Vector()` - `Vector()` | `Vector` |
| Scalar multiplication $^{3}$ | `int` * `Vector()` or `Vector()` * `int` | `Vector` |
| Inner product $^{4}$ | `Vector()` @ `Vector()` | `Vector` |
| Row-vector @ matrix multiplication | `Vector()` @ `Matrix2D()` | `Vector` |
| Dot product | `Vector.dot_product(Vector, Vector)` | `int` |
| Matrix addition | `Matrix2D()` + `Matrix2D()` | `Matrix2D` |
| Matrix subtraction | `Matrix2D()` - `Matrix2D()` | `Matrix2D` |
| Scalar multiplication (w/matrix) | `int` * `Matrix2D()` or `Matrix2D()` * `int` | `Matrix2D` |
| Matrix multiplication | `Matrix2D()` @ `Matrix2D()` | `Matrix2D` |
| Matrix @ column-vector multiplication $^{5}$ | `Matrix2D()` @ `Vector()` | `Matrix2D` |
| Outer product $^{6}$ | `Vector()` @ `Vector()` | `Matrix2D` |

Some examples can be found in the [test matrix file](/matrix_class/test_matrix.py).

#### Footnote discussion
**Footnote 1, 2, and 3:** These concern the lack of support for these operations using column vectors. Right now these operations are only supported using row vectors. Of course row or column vectors are valid for these operations and I may get to support for column vectors at a different time.

**Footnote 4:** The `Vector` class has aimed to support computation between a row vector and column vector just as one would compute an inner product in a linear algebra class. You can explicitly access the shapes of these with the `.shape` property. In the the `.shape` output of two `Vector` objects which you want to take the inner product of, you will see `(1, n) @ (n, 1)` which is different from a numpy inner product `(n,) @ (n, 1)`.

**Footnote 5:** This output should intuitively be a `Vector` instead of a `Matrix2D` object since matrix @ column-vector multiplication returns a column vector. More information about this implementation detail is in the blog post. This return type is subject to change and will be `Vector` in the future.

**Footnote 6:** An outer product is an operation between a column vector and a row vector. In numpy an example would be: `np.array([[3], [2], [1]]) @ np.array([[1, 2, 3]])` whereas in the `Vector` class this is `Vector([[3], [2], [1]]) @ Vector([1, 2, 3])`. They both produce the same output just like in Footnote 4's dot product example, but the `Vector` class treats `Vector([1, 2, 3])`, the "one dimensional array", as a row vector. The way numpy treats 2D arrays is part of the reason for this discrepancy can be seen in the [`np.dot()` documentation](https://numpy.org/doc/stable/reference/generated/numpy.dot.html). In numpy 2D arrays are solved with the matmul operator. I could also define `Matrix2D[[3], [2], [1]] @ Matrix2D[[1, 2, 3]]` and receive a valid output but this would break my convention of allowing column vector @ row vector operations with row vectors defined as 1D arrays.

### More things to point out
- The `Vector` and `Matrix2D` objects are mutable and have a `__setitem__` method so values can be changed in-place. This follows [numpy's array conventions](https://numpy.org/doc/stable/user/absolute_beginners.html).
- The `Matrix2D` object has a `confirm_output` method which confirms that its output is the same as numpy's. This is currently being used in place of the `all()` property.
- Both `Vector` and `Matrix2D` objects have a `.shape` property that returns a tuple of the number of rows and columns.