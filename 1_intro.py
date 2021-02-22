import numpy as np


a = np.array([1, 2, 3])
b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])

'''get dimension, shape, data type, size, bytes'''

print(a.ndim)
print(b.shape)
print(a.dtype)
print(a.itemsize)
print(a.nbytes)

