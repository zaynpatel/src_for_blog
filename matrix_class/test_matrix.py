# import numpy as np

# t1_np = np.array([[4, 5, 6],
#       [1, 2, 3], 
#       [7, 8, 9]])

# t2_np = np.array([[1, 2, 5],
#       [9, 7, 2],
#       [1, 4, 6]])

# Square

t1 = [[4, 5, 6],
      [1, 2, 3], 
      [7, 8, 9]]

t2 = [[1, 2, 5],
      [9, 7, 2],
      [1, 4, 6]]

# More columns, less rows
t3 = [[4, 5, 6, 4, 5],
      [1, 2, 3, 3, 2], 
      [7, 8, 9, 1, 10]]

t4 = [[1, 2, 5],
      [9, 7, 2],
      [1, 4, 6]]

# Less columns, more rows

t5 = [[4, 5, 6],
      [1, 2, 3], 
      [7, 8, 9],
      [10, 12, 14],
      [15, 17, 18]]

t6 = [[1, 2, 5],
      [9, 7, 2],
      [1, 4, 6]]

# I have a feeling this will only track rows but not column mismatches
# try:
#     for i, v in zip(t5, t6, strict=True):
#         if len(i) != len(v):  # Maybe this fixes column errors too?
#             # Because strict=True catches row mismatches and len catches column mismatches
#             raise ValueError("There is a column mismatch")
#         print(i, v)
# except ValueError:
#     raise (f"Rows mismatch")

t = []
# for m1, m2 in zip(t1, t2, strict=True):
#     for i, v in zip(m1, m2, strict=True):
#         # Ok if this works and aligns things then I need a way to sum() and save these in a matrix
#         # i, v is a tuple (num1, num2) so I need a way to access these and add
#         entry = sum((i, v))
#         t.append(entry)

# for m1, m2 in zip(t1, t2, strict=True):
#       tmp = []
#       # The nested loop does not maintain any structure of the rows so I think I need a temp store to maintain row integrity
#       for i, v in zip(m1, m2, strict=True):
#             tmp.append(i + v)
#       t.append(tmp)

# print(t)  # Ok so this nested loop structure is more correct. Nice! But it's not formatted like numpy on output. Seems like a str display thing?

# for m1, m2 in zip(t1, t2, strict=True):
#       tmp = []
#       # The nested loop does not maintain any structure of the rows so I think I need a temp store to maintain row integrity
#       for i, v in zip(m1, m2, strict=True):
#             tmp.append(i + v)
#       t.append(tmp)

# s = [[i + v for i, v in zip(m1, m2, strict=True)] for m1, m2 in zip(t1, t2, strict=True)]
# print(s)

t1 = [[4, 5, 6],
      [1, 2, 3], 
      [7, 8, 9]]

t2 = [[1, 2, 5],
      [9, 7, 2],
      [1, 4, 6]]

f = [] # The winning one
for row in t1:
      tmp = []
      for col in zip(*t2):
            tmp.append(sum(x * y for x, y in zip(row, col)))
      f.append(tmp)

print(f)


# for r in t1:
#       tmp = []
#       for c in zip(*t2):
#             tmp.append(sum((x * y for x, y in zip(row, col))))
#       f.append(tmp)
# print(f)



# import numpy as np
# print(np.array(t1) @ np.array(t2))