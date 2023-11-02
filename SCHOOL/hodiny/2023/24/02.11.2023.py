# cvicenia na inpute
# 1
matica = [[1, 2, 3], [4], [5, 6]]

def sucty(l):
    vys = []
    for i in l:
        vys.append(str(sum(i)))
    return " ".join(vys)

# print(sucty(matica))

# 2
matica = [[1, 2, 3], [4], [5, 6]]

def suc(l):
    vys = []
    for i in l:
        vys.append(sum(i))
    return vys

# print(suc(matica))

# 3
matica = [[1, 2, 3], [4], [5, 6]]

def pridaj_sucty(tab):
    for i in range(len(tab)):
        tab[i].append(sum(tab[i]))
    return tab

# print(pridaj_sucty(matica))

# 4
p = [[1, 2], [5, 6], [3, 4]]

def oto(m):
    for prvok in m:
        for cislo in prvok:
            print(cislo,end=" ")
        print()

def otoc(m):
    nova = []
    for i in range(len(m[0])):
        pom = []
        for j in range(len(m)):
            pom.append(m[j][i])
        nova.append(pom)
    oto(nova)
"""oto(p)
print()
otoc(p)"""

# 5
# bez toho return je to take divne, pozitie global etc.
def preklop(zoz):
    global m
    nova = []
    for i in range(len(zoz[0])):
        pom = []
        for j in range(len(zoz)):
            pom.append(zoz[j][i])
        nova.append(pom)
    m = nova.copy()

"""m = [[1, 2], [5, 6], [3, 4]]
preklop(m)
print(m)"""

# 6
p = [[1, 2], [3, 4], [5, 6]]

def zisti_dlzky(m):
    pom = len(m[0])
    for prvok in m:
        if len(prvok) != pom:
            return None
    return pom
"""print(zisti_dlzky(p))
print(zisti_dlzky([[1, 2, 3]]))
print(zisti_dlzky([[], [1, 2, 3]]))"""

# 7
a = [[5, 6], [1, 2, 3], [4]]

def dopln(m):
    dlzka = -1
    for i in m:
        if len(m) > dlzka:
            dlzka = len(m)
    # na zistenie najdlhsieho prvku
    naj = max(len(prvok) for prvok in m)
    # na zistenie najdlhsieho prvku
    for i in range(len(m)):
        while len(m[i]) < dlzka:
            m[i].append(None)
    return m

# print(dopln(a))

# 9
a = [[5, 6], [1, 2, 3], [4]]
b = [[0, 0], [0, 0, 0], [0]]
b2 = [[0, 0], [0, 0, 0]]
b3 = [[0, 0], [0, 0], [0]]
def zisti(tab1, tab2):
    if len(tab1) == len(tab2):
        for i in range(len(tab1)):
            if len(tab1[i]) != len(tab2[i]):
                return False
        return True
    return False

print(zisti(a, b))
print(zisti(a, b2))
print(zisti(a, b3))

# 10
# dorobit!
"""def sucet(tab1, tab2):
    vys = []
    for i in range(len(tab1)):
        pom = []
        for j in range(len())"""

