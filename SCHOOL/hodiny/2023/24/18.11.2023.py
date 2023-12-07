"""b = [[3, 1], [2,1], [1,0]]
a = [[1, 0, 2], [-1, 3, 1]]
res = []

if len(a) < len(b):
    x = a
    a = b
    b = x

for i in range(len(a)):
    res.append([]) 
    for j in range(len(b[0])):
        vysledok=0 
        for k in range(len(a[0])):
            a_cislo = a[i][k]
            b_cislo = b[k][j]
            vysledok += a_cislo*b_cislo
        res[i].append(vysledok)
print(res)
"""


mat=[[12, 6, 31, 16, 18], 
 [13, 10, 18, 32, 6], 
 [32, 21, 40, 22, 26], 
 [8, 13, 24, 41, 19]]

# hladam maximum v riadku -> pozeram ci toto maximum je minimum z cisel v stlpci jeho indexu

def hladaj_ci_max(hodnota, index, mat):
    for i in mat:
        if i[index] > hodnota:
            return False
    return True


for i in mat:
    hodnota = min(i)
    index = i.index(hodnota)
    if hladaj_ci_max(hodnota, index, mat):
        print(hodnota, f"[{index}:{mat.index(i)}]")



