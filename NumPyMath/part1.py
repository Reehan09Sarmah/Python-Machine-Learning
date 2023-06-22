# Linear Algebra --> Column of 1st matrix = Rows of 2nd
import numpy as np

a = np.full((2, 3), 5)
b = np.full((3, 2), 3)
print(f'a:\n {a}')
print(f'b:\n {b}')
# matrix multiplication
c = np.matmul(a, b)
print(f'c = a * b :\n {c}')

d = np.identity(3)
print(np.linalg.det(d))  # determinant of an identity matrix

# Visit: https://numpy.org/doc/stable/reference/routines.linalg.html for more linear algebra functions