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

    def __add__(self, other):
        # First check dimensions
        try:
            for row_one, row_two in zip(self, other, strict=True):
                if len(row_one) != len(row_two):
                    raise ValueError(f"Number of columns are mismatched: {len(row_one)} needs to equal {len(row_two)}")
        except ValueError:
            raise Matrix2DException(f"Number of rows are mismatched {len(self)} needs to equal {len(other)} ")
        # Then do operation
        try:
            #TODO: Maybe rename these later
            # Ok so this is a generator expression. Think about this more. 
            # We return a new Matrix2D object because we do not want to modify the existing self, other (per textbook)
            return Matrix2D((col_one + col_two for col_one, col_two in zip(row_one, row_two, strict=True)) 
                            for row_one, row_two in zip(self, other, strict=True))
        except TypeError:  # TypeError will be raised because we cannot add this custom type... (obvious)
            return NotImplemented  # Make sure to mention what this means in article

    #TODO: Add __radd__

a = Matrix2D([[4, 5, 6],
            [1, 2, 3], 
            [7, 8, 9]])

b = Matrix2D([[1, 2, 5],
            [9, 7, 2],
            [1, 4, 6]])

c = a + b  # Output --> Matrix2D([[5, 7, 11], [10, 9, 5], [8, 12, 15]])
