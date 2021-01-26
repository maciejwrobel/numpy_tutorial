import numpy as np

# all 0s matrix
a = np.zeros((5, 5))


# all 1s matrix
np.ones((4, 2, 2), dtype='int32')

# any other number (shape, value)
np.full((2, 2), 99)

# any other number (full_like method) (shape_like, value)
np.full_like(a, 4)

# random decimal numbers

np.random.rand(4, 2)
np.random.random_sample(a.shape)

# random integer values (low (0), high, size)
np.random.randint(2, 7, size=(3, 3))

# square matrix
np.identity(5)

# repeat an array
arr = np.array([[1, 2, 3]])
r1 = np.repeat(arr, 3, axis=0)

# excercise

out = np.ones((5,5))
middle = np.zeros((3,3))
middle[1, 1] = 9
out[1:-1, 1:4] = middle
print(out)

# be careful when copying arrays !!!!!!!!!!!!!!!!!!!!!

a = np.array([1,2,3])
# b = a
# b[0] = 100
# print(b)
# print(a)
# !!!!!!!!!!!!!
b = a.copy()