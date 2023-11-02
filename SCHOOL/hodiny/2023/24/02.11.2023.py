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

# print(zisti(a, b))
# print(zisti(a, b2))
# print(zisti(a, b3))

# 10
def sucet(tab1, tab2):
    vys = []
    for i in range(len(tab1)):
        pom = []
        for j in range(len(tab1[i])):
            pom.append(tab1[i][j]+tab2[i][j])
        vys.append(pom)
    return vys

a = [[5, 6], [1, 2, 3], [4]]
b = [[-1, -3], [-2, 0, 1], [2]]
# print(sucet(a, b))

# 11

def citaj(meno_suboru):
    m = []
    with open(fr"/home/tomas/Desktop/all-code/SCHOOL/hodiny/2023/24/{meno_suboru}") as subor:
        for line in subor:
            line = line.strip()
            m.append(line.split(" "))
    citac(m)

def citac(mat):
    for i in mat:
        print(" ".join(i))

# (citaj("matice_uloha11.txt"))

# 12

def zapis(m, meno_suboru):
    with open(fr"/home/tomas/Desktop/all-code/SCHOOL/hodiny/2023/24/{meno_suboru}", "w") as subor:
        for i in m:
            riad = ""
            for j in i:
                riad += str(j) + " "
            print(riad, file=subor)

# s = [['anicka', 'dusicka'], ['kde', 'si', 'bola'], ['ked', 'si', 'si', 'cizmicky'], ['zarosila']]
# zapis(s, "anicka_text.txt")
# zapis([[1, 11, 21], [345], [-5, 10]], 'cisla.txt')
# 13

def citaj_cisla(meno_suboru):
    m = []
    with open(fr"/home/tomas/Desktop/all-code/SCHOOL/hodiny/2023/24/{meno_suboru}") as subor:
        for riadok in subor:
            riadok = riadok.strip()
            vys = riadok.split(" ")
            vys = [int(s) for s in vys]
            m.append(vys)
    return m

# print(citaj_cisla("cisla.txt"))

# 14

def prvky(tab):
    vys = []
    for i in tab:
        for j in i:
            vys.append(j)
    return vys

a = [[5, 6], [1, 2, 3], [4]]
# b = prvky(a)
# print(b)

# 15
def vyrob(pr, ps, hodnoty):
    m = []
    for i in range(pr):
        m.append([])
    idx = 0
    for i in range(len(m)):
        for _ in range(ps):
            if idx+1>len(hodnoty):
                idx = 0
            m[i].append(hodnoty[idx])
            idx +=1
    return m
# print(vyrob(3, 2, [3, 5, 7]))
# print(vyrob(3, 3, list(range(1, 20, 2))))

# 16
'''import tkinter
c = tkinter.Canvas()
c.pack()
def kruhy(meno_suboru):
    kruhy_m = []
    with open(fr"/home/tomas/Desktop/all-code/SCHOOL/hodiny/2023/24/{meno_suboru}") as subor:
        for riadok in subor:
            riadok = riadok.strip()
            kruhy_m.append(riadok.split(" "))
    # print(kruhy_m)
    x, y = 40, 40
    for i in kruhy_m:
        for j in i:
            c.create_oval(x, y, x+40, y+40, fill=j)
            x+=40
        y+=40
        x=40

kruhy("kruhy.txt")
c.mainloop()'''

#17

import tkinter
c = tkinter.Canvas()
c.pack()
def kruhy(meno_suboru):
    kruhy_m = []
    with open(fr"C:\Users\tomas\Desktop\code\all-code\SCHOOL\hodiny\2023\24\{meno_suboru}") as subor:
        for riadok in subor:
            riadok = riadok.strip()
            kruhy_m.append(riadok.split(" "))
    # print(kruhy_m)
    x, y = 40, 40
    for i in kruhy_m:
        for j in i:
            if j!="None":
                c.create_oval(x, y, x+40, y+40, fill=j)
            x+=40
        y+=40
        x=40

# kruhy("kruhy2.txt")
# c.mainloop

#18

def precitaj(meno_suboru):
    with open(fr"C:\Users\tomas\Desktop\code\all-code\SCHOOL\hodiny\2023\24\{meno_suboru}") as subor:
        l = []
        for riadok in subor:
            riadok = riadok.strip()
            l.append(riadok)
        pr, ps = map(int, l[0].split(" "))
        m = []
        for i in range(pr):
            m.append([0]*ps)
        l.pop(0)
        for i in l:
            # m[int(i[0])][int(i[1])] = int(i[2])
            y, x, val = map(int, i.split(" "))
            m[y][x] = val
        print(m)

# precitaj("matice_uloha18.txt")