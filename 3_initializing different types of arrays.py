import numpy as np

'''all 0s matrix'''
a = np.zeros((5, 5))
# print(a)

'''all 1s matrix'''
b = np.ones((4, 2, 2), dtype='int32')
# print(b)

'''any other number (shape, value)'''
c = np.full((7, 7), 99)
# print(c)

'''any other number (full_like method) -> (shape_like, value)'''
d = np.full_like(a, 4)
# print(d)

'''random decimal numbers'''

e = np.random.rand(4, 2)
f = np.random.random_sample(a.shape)
# print(e)
# print(f)

'''random integer values (low (0), high, size)'''
g = np.random.randint(2, 7, size=(3, 3))
# print(g)

'''square matrix - > jedynki po przekątnej'''
h = np.identity(7)
# print(h)

'''repeat an array'''
arr = np.array([[1, 2, 3]])
r1 = np.repeat(arr, 3, axis=0)
# print(r1)

'''excercise'''

out = np.ones((5,5))
middle = np.zeros((3,3))
middle[1, 1] = 9
out[1:-1, 1:4] = middle
print(out)

'''be careful when copying arrays !!!!!!!!!!!!!!!!!!!!!'''

a = np.array([1,2,3])
# b = a
# b[0] = 100
# print(b)
# print(a)
# !!!!!!!!!!!!!
b = a.copy()