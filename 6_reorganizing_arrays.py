import numpy as np

before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

after = before.reshape((8, 1))
print(after)

# new shape HAVE TO have same amount of values !


# VERTICALLY STACKING
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

np.vstack([v1, v2])

# HORIZONTAL STACK

np.hstack([v1, v2])

# 47:33