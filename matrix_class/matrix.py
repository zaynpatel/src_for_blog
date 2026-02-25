from typing import List

class Matrix2DException(Exception):
    pass

class Matrix2D:
    def __init__(self, components: List[List]):
        self.components = [[r for r in row] for row in components]  # [[thing inner loop] outer loop]
        assert id(self.components) != id(components)  # Confirm a copy has been made

    def __iter__(self):
        return iter(self.components)  # Does this iter implement __next__?

    def __repr__(self):
        return f"Matrix2D({self.components})"
    
    def __getitem__(self, index):
        return self.components[index]

    def __setitem__(self, idx, value):
        self.components[idx] = value

    def __eq__(self, other):
        # This works but maybe come back to later to see if non-generator design on first loop is ok
        self.check_dimensions(self, other)
        for row_one, row_two in zip(self, other, strict=True):
            if all(col_one == col_two for col_one, col_two in zip(row_one, row_two, strict=True)):
                return True
            else:
                return False

    def __len__(self):
        return len(self.components)

    def __add__(self, other):
        self.check_dimensions(self, other)
        try:
            # We return a new Matrix2D object because we do not want to modify the existing self, other (per textbook)
            return Matrix2D((col_one + col_two for col_one, col_two in zip(row_one, row_two, strict=True)) 
                            for row_one, row_two in zip(self, other, strict=True))
        except TypeError:
            return NotImplemented  # Make sure to mention what this means in article

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        self.check_dimensions(self, other)
        try:
            return Matrix2D((col_one - col_two for col_one, col_two in zip(row_one, row_two, strict=True)) 
                            for row_one, row_two in zip(self, other, strict=True))
        except TypeError:
            return NotImplemented
    
    def __rsub__(self, other):
        return self - other

    def __mul__(self, scalar):
        try:
            return Matrix2D((scalar * num for num in arr) for arr in self)
        except TypeError:
            return NotImplemented

    def __rmul__(self, scalar):
        return self * scalar
    
    def __matmul__(self, other):
        try:
            final = []
            for row_idx, row in enumerate(self):
                tmp = []
                for col_idx, col in enumerate(other):
                        row_col_mult = []
                        for num_idx, num in enumerate(row):
                            row_col_mult.append(num * other[num_idx][col_idx])
                        tmp.append(sum(row_col_mult))
                final.append(tmp)
            return final
        except TypeError:
            return NotImplemented
    
    def __rmatmul__(self, other):
        return self @ other

    @staticmethod
    def check_dimensions(self, other):
        """
        Confirm dimensions of input matrix before performing addition and subtraction
        
        :param self: Instance of Matrix2D
        :type self: Matrix2D
        :param other: Object to be added/subtracted to Matrix2D instance
        :type other: Any
        """
        try:
            for row_one, row_two in zip(self, other, strict=True):
                if len(row_one) != len(row_two):
                    raise ValueError(f"Number of columns are mismatched: {len(row_one)} needs to equal {len(row_two)}")
        except ValueError:
            raise Matrix2DException(f"Number of rows are mismatched {len(self)} needs to equal {len(other)} ")

    @property
    def shape(matrix):
      """
      Computes the shape of an input matrix

      Background: `len()` providees the number of rows in a matrix. In any Matrix2D object we calculate the columns
      based on the length of the inner list
      
      :param matrix: Input matrix (or vector) object
      """
      num_rows = len(matrix)
      get_col_num = [len(row) for row in matrix]
      check_cols = all(x == get_col_num[0] for x in get_col_num)
      if not check_cols:
            raise Matrix2DException("The matrix is improperly structured; one row has more columns than the others")
      num_cols = get_col_num[0] 

      return (num_rows, num_cols)

a = Matrix2D([[4, 5, 6],
            [1, 2, 3], 
            [7, 8, 9]])

a2 = Matrix2D([[4, 12, 6],
            [1, 2, 3], 
            [7, 8, 9]])

b = Matrix2D([[1, 2, 5, 4],
            [9, 7, 2, 5],
            [1, 4, 6, 9]])

#c = a - b  # Output --> Matrix2D([[5, 7, 11], [10, 9, 5], [8, 12, 15]])

# Test 1: See what happens without __radd__ (comment it out)
# t1 = [[0, 0, 1], [0, 1, 0], [1, 0, 0]] + a
# print(t1) --> Output: TypeError: can only concatenate list (not "Matrix2D") to list. This is expected!

# Test 2: Uncomment __radd__ and check
# print(t1) # --> Output: Matrix2D([[4, 5, 7], [1, 3, 3], [8, 8, 9]]). This is also expected!
