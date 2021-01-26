import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

print(a.shape)

# get specific element - 13 [ row, column]

print(a[1, 5])
print(a[1, -2])

# get specific row - 1
print(a[0, :])

# get specific column - 3
print(a[:, 2])

# getting fancy [start_index, stop_index, step] -
print(a[0, 1:6: 2])

# CHANGING element
a[1, 5] = 20
print(a)

# changing column
a[:, 2] = 5
print(a)
# sequence
a[:, 2] = [1, 2]
print(a)


# 3D example
b = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])
print(b)
print(b[0, 1, 1])
