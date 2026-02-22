from typing import List

# TODO: Need to build vector class for vector, matrix operations

class Matrix2DException(Exception):
    pass

class Matrix2D:
    def __init__(self, components: List[List]):
        # TODO: Add a check to make sure we get a nested list passed in
        self.components = [[r for r in row] for row in components]  # [[thing inner loop] outer loop]
        assert id(self.components) != id(components)  # Confirm a copy has been made

    def __iter__(self):
        return iter(self.components)  # Does this iter implement __next__?

    def __repr__(self):
        return f"Matrix2D({self.components})"

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
            #TODO: Maybe rename these later
            # Ok so this is a generator expression. Think about this more. 
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
