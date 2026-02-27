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
            return NotImplemented

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
        self_cols = self.shape[1]
        other_rows = other.shape[0]
        if self_cols != other_rows:
            raise Matrix2DException(f"Matrix multiplication must have rows: {other_rows} equal to columns: {self_cols}")
        try:
            return Matrix2D((sum(x * y for x, y in zip(row, col)) for col in zip(*other)) for row in self)
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
    
    @staticmethod
    def confirm_output(matrix2d_output, numpy_output):
        """
        Confirm the output of two matrices (one from Matrix2D class and another from numpy)
        
        :param matrix2d_output: Output from a Matrix2D matmul
        :param numpy_output: Output from a numpy matmul

        This is implemented because `Matrix2D` does not have an `.all()` method and I am not implementing one now
        """
        for row_one, row_two in zip(matrix2d_output, numpy_output):
            for r1, r2 in zip(row_one, row_two):
                if r1 != r2:
                    raise Matrix2DException(f"There is a mismatch between output values: {r1, r2}")
        return True

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
