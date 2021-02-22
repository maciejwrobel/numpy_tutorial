import numpy as np

'''You can index with a list in numpy'''
c = np.array([1,2,3,4,5,6,7,8,9])
d = c[[1,2,8]]
# print(d)


'''loading / generating data from file. Delimiter - separator'''

filedata = np.genfromtxt('data.txt', delimiter=',')
filedata = filedata.astype('int32')

'''Boolean Masking and Advanced Indexing'''

a = filedata > 50
# print(a)
'''zwróci tabelę z wartościami True/False'''

b = filedata[filedata > 50]
# print(b)
'''zwróci tabelę z wartościami filedata > 50'''

e = np.any(filedata > 50, axis=0)
f = np.all(filedata > 50, axis=1)
# print(e)
# print(f)
'''zwróci tabelę z True/False, jeżeli którakolwiek (ANY) / wszystkie (ALL)
wartości w KOLUMNIE (axis=0) / RZĘDZIE (axis=1) > 50'''

g = ((filedata > 50) & (filedata < 70))
print(g)
h = (~((filedata > 50) & (filedata < 70)))
print(h)
# REVERSED



