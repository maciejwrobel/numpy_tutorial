import numpy as np

# basic
c = np.array([1, 2, 3, 4])
# print(c+2)

d = np.array([1, 0, 1, 0])

# print(c+d)

np.cos(c)

# linear algebra

a = np.full((2, 3), 1)
b = np.full((3, 2), 2)
# print(a)
# print(b)

# NOPE
# print(a*b)

# MATRIX MULTIPLICATION
np.matmul(a, b)

# FIND DETERMINANT
c = np.identity(3)
print(c)
# linear algebra determinant
d = np.linalg.det(c)
print(d)


# REFERENCE DOCS
# https://numpy.org/doc/stable/reference/index.html
# https://docs.scipy.org/doc/