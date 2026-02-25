class VectorException(Exception):
    pass

class Vector:
    def __init__(self, components):
        self.components = [val for val in components]
        assert id(self.components) != id(components)

    def __iter__(self):
        return iter(self.components)
    
    def __repr__(self):
        return f"Vector({self.components})"
    
    def __getitem__(self, index):
        return self.components[index]

    def __setitem__(self, idx, value):
        self.components[idx] = value

    def __eq__(self, other):
        return (len(self) == len(other) and 
                all(self_num == other_num for self_num, other_num in zip(self, other)))

    def __len__(self):
        return len(self.components)

    def __add__(self, other):
        # One thought is that this passes a generator expression and the list iterates through this and gives just a list of the components
        try:
            return Vector(self_num + other_num for self_num, other_num in zip(self, other, strict=True))
        except TypeError:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __neg__(self):
        return Vector(-num for num in self)

    def __sub__(self, other):
        try:
            return Vector(self_num - other_num for self_num, other_num in zip(self, other, strict=True))
        except TypeError:
            return NotImplemented
    
    def __rsub__(self, other):
        return self - other

    def __mul__(self, scalar):
        try:
            return Vector(scalar * self_num for self_num in self)
        except TypeError:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __matmul__(self, other):
        try:
            return sum(self_num * other_num for self_num, other_num in zip(self, other, strict=True))
        except TypeError:
            return NotImplemented
    
    def __rmatmul__(self, other):
        return self @ other

    @staticmethod
    def is_nested(obj):
      #TODO: Find a way to use this. I don't like the TypeError raised for addition between nested/unnested list
      # It should be more helpful
      """Check if the input object is nested or not"""
      return any(isinstance(i, list) for i in obj)

    @property
    def shape(vector):
      """
      Computes the shape of an input vector

      Background: `len()` providees the number of rows in a vector. In any Vector object we calculate the columns
      based on the length of the inner list
      
      :param matrix: Input matrix (or vector) object
      """
      if Vector.is_nested(vector):
        num_rows = len(vector)
        get_col_num = [len(row) for row in vector]
        check_cols = all(x == get_col_num[0] for x in get_col_num)
        if not check_cols:
            raise VectorException("The vector is improperly structured; one vector entry has more than one number in it")
        num_cols = get_col_num[0]
        if num_rows != 1 and num_cols != 1:
            raise VectorException("Object other than a vector was passed in")
      else:
          num_rows = 1
          num_cols = len(vector)

      return (num_rows, num_cols)
