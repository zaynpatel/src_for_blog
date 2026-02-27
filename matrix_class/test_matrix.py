from matrix import Matrix2D, Matrix2DException
from vector import Vector

import numpy as np

t1 = [[4, 5, 6],
      [1, 2, 3], 
      [7, 8, 9]]

v1 = [[1], [0], [2]]
v100 = [[5], [0], [2]]
v1_np = [1, 0, 2]
v100_np = [5, 0, 2]

vv3 = [[1], [1], [2]]

t2 = [[1, 2, 5],
      [9, 7, 2],
      [1, 4, 6]]

t5 = [[4, 5, 6],
      [1, 2, 3], 
      [7, 8, 9],
      [10, 12, 14],
      [15, 17, 18]]

# Test 1: Confirm we get errors with mismatched matrices
try:
      Matrix2D(t1) @ Matrix2D(t5)
except Matrix2DException:
      print("Caught correct exception")

# Test 2: Mat-vec multiplication
mv = Matrix2D(t1) @ Vector(v1)
mv_np = np.array(t1) @ np.array(v1)
assert Matrix2D.confirm_output(mv, mv_np) == True
assert isinstance(mv, Matrix2D)

# Test 3: Vec-mat multiplication
v2 = Vector([1, 1, 2])
t2 = Matrix2D([[1, 2, 5],
      [9, 7, 2],
      [1, 4, 6]])

v3 = v2 @ t2
assert v3.shape == (v2.shape[0], t2.shape[1])
assert isinstance(v3, Vector)

# Test 4: Mat-mat multiplication
mm = Matrix2D(t1) @ Matrix2D(t2)
mm_np = np.array(t1) @ np.array(t2)
assert Matrix2D.confirm_output(mm, mm_np)

# Test 5: Shape property
m_v1 = Matrix2D(v1)
assert m_v1.shape == (3, 1)
v_v1 = Vector([[3], [0]])
assert v_v1.shape == (2, 1)

# Test 6: Outer product -> matrix
# Subject to change. Numpy doesn't do outer products with 1D arrays, needs 2D for the row vector since their shapes are defined differently
# For now I am allowing defining vectors and then doing a shape check, returning a Matrix2D but I could just as well state that the operation only
# works for Matrix2D objects multiplying together since that is the output. Keeping this partly because the inner product is row vector @ col vector
# so maybe we should allow more of these constructions (e.g. outer product)
v = Vector([[3], [4], [5]])
rv = Vector([1, 2, 3])

v_np = np.array([[3], [4], [5]])
rv_np = np.array([[1, 2, 3]])

v_rv = v @ rv
v_rv_np = v_np @ rv_np
assert isinstance(v_rv, Matrix2D)
assert Matrix2D.confirm_output(v_rv, v_rv_np)

# Test 7: Dot product
column_vector = Vector(v1)
column_vector_two = Vector(v100)
assert Vector.dot_product(Vector(v1), Vector(v100))  == np.dot(v1_np, v100_np)
print("All tests passed!")
