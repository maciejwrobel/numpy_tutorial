import numpy as np

stats = np.array([[1, 2, 3], [4, 5, 6]])

a = np.min(stats)
b = np.min(stats, axis=1)
c = np.max(stats)
d = np.sum(stats)

print(a)
print(b)
print(c)
print(d)
