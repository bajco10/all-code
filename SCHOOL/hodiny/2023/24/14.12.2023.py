# diagonaly
# osemsmerovka uloha: symetricke/nesymetricke/kadejake 8-smerovky, po najdeni slov hladat podla cisel dole (za vtipom)
# pocet znakov a za ne dat medzeru
import numpy as np
m = [
    [1, 2, 3],
    [4, 5, 6],
    [3, 2, 1]
]


vedla = {}
hlavna = {}
for i in range(len(m)):
    for j in range(len(m[0])):
        if i+j in vedla:
            vedla[i+j].append(m[i][j])
        else:
            vedla[i+j] = [m[i][j]]
        
        if i-j in hlavna:
            hlavna[i-j].append(m[i][j])
        else:
            hlavna[i-j] = [m[i][j]]

print(vedla)
print(hlavna)
# print(np.diag(m, -1))
