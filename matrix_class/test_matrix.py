from matrix import Matrix2D, Matrix2DException

import numpy as np

t1 = [[4, 5, 6],
      [1, 2, 3], 
      [7, 8, 9]]

v1 = [[1], [0], [0]]
v2 = [[1, 1, 2]]
v3 = [[1], [1], [2]]

t2 = [[1, 2, 5],
      [9, 7, 2],
      [1, 4, 6]]

t5 = [[4, 5, 6],
      [1, 2, 3], 
      [7, 8, 9],
      [10, 12, 14],
      [15, 17, 18]]

# Test 1: Confirm we get errors with mismatched matrices
# try:
#       Matrix2D(t1) @ Matrix2D(t5)
# except Matrix2DException:
#       print("Caught correct exception")

# Test 2: Mat-vec multiplication
mv = Matrix2D(t1) @ Matrix2D(v1)
mv_np = np.array(t1) @ np.array(v1)
assert Matrix2D.confirm_output(mv, mv_np) == True

# Test 3: Vec-mat multiplication
vm = Matrix2D(v2) @ Matrix2D(t1)
vm_np = np.array(v2) @ np.array(t1)
assert Matrix2D.confirm_output(vm, vm_np) == True

# Test 4: Mat-mat multiplication
mm = Matrix2D(t1) @ Matrix2D(t2)
mm_np = np.array(t1) @ np.array(t2)
assert Matrix2D.confirm_output(mm, mm_np)

# Test 5: Shape property
m_v1 = Matrix2D(v1)
assert m_v1.shape == (3, 1)

m_t2 = Matrix2D(t2)
assert m_t2.shape == (3, 3)
