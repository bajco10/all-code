# 1
def vypis(tab, sirka=4):
    for riadok in tab:
        for prvok in riadok:
            print(f'{repr(prvok):>{sirka}}', end=' ')
        print()
#2
def vypis(tab, sirka=None):
    if sirka is None:
        sirka = 1
        for riadok in tab:
            for prvok in riadok:
                sirka = max(sirka, len(repr(prvok)))
    for riadok in tab:
        for prvok in riadok:
            print(f'{repr(prvok):>{sirka}}', end=' ')
        print()
# vypis([[1, 2], [3, 4, 5, 6], [7, 8, 9]])
#3
def zoznam_suctov(tab):
    sucty = []
    for i in tab:
        cur_sucet = 0
        if i == []:
            sucty.append(None)
        else:
            if type(i[0]) == str:
                    cur_sucet = ""
            elif type(i[0]) == tuple:
                    cur_sucet = ()
            for j in i:
                cur_sucet += j
        sucty.append(cur_sucet)
    return sucty

# print(zoznam_suctov([['1', 'x', '2'], [], [5, 6], [3.1, 4], [(5, 6), (7,)]]))

#4 - treba naformatovat na vypis cetrovany doprava
def pridaj_sucty(tab):
    for i in tab:
        cur_sucet = 0
        if i == []:
            i.append(None)
        else:
            if type(i[0]) == str:
                cur_sucet = ""
            elif type(i[0]) == tuple:
                cur_sucet = ()
            for j in i:
                cur_sucet+=j
        i.append(cur_sucet)
# t = [['1', 'x', '2'], [], [5, 6], [3.1, 4], [(5, 6), (7,)]]
# pridaj_sucty(t)
# vypis(t)

#5 - zip strasne dolezita vec!
# * v zip -> aby zip() nebral tab ako celok ale bral kazdy riadok jednotlivo
def preklop(tab):
    new_tab = list(map(list, zip(*tab)))
    return new_tab
#  p = [[1, 2], [5, 6], [3, 4]]
# vypis(preklop(p), 2)

#6
"""def ocisluj2(tab, start=0):
    max_len = max(len(row) for row in tab)
    new_tab = []
    
    for j in range(max_len):
        new_row = []
        for i, row in enumerate(tab):
            if j < len(row):
                new_row.append(start)
                start += 1
            else:
                new_row.append('')
        new_tab.append(new_row)
    
    tab[:] = list(map(list, zip(*new_tab)))"""

def ocisluj2(tab, start=0):
    poc = 0
    max_len = max(len(riadok) for riadok in tab)

    for i in range(max_len):
        for j in range(len(tab)):
            if i < len(tab[j]):
                '''ideme podla najvacsej dlzky ale pole je nesymetricke
                musime zaistit aby sme sa nedostali mimo dlzky riadku
                do ktore davame pocet
                - inak IndexError: index out of range'''
                tab[j][i] = poc
                poc += 1
"""ab = [[1, 1, 1], [], [1, 1, 1, 1], [1], [1, 1, 1, 1, 1]]
ocisluj2(ab)
for i in ab:
    print(f'{" ".join(map(str, i))}')"""

# SPRAVIT AJ POMOCOU REKURZIE
"""def pascalov_trojuholnik(n):
    if n <= 0:
        return []
    pt = [[1]]
    for i in range(1, n):
        # ak n=1 tak sa preskoci cely tento for-loop, pretoze range je (1, 1)-> range nie je inkluzivna funkcia-> i nikdy nebude 1
        minuly_riadok = pt[-1]
        novy_riadok = [1]
        for j in range(1, i):
            ne = minuly_riadok[j-1] + minuly_riadok[j]
            novy_riadok.append(ne)
        novy_riadok.append(1)
        pt.append(novy_riadok)
    return pt
def vytlac_trojuholnik(t):
    for riadok in t:
        print(" ".join(map(str, riadok)))

# t = pascalov_trojuholnik(2)
# vytlac_trojuholnik(t)"""

"""vysvetlenie n = 1
    - prva podmienka nie je pravdiva
    - vytvorim trojuholnik... prvy riadok je vzdy [[1]]
    - kedze n=1 range tohto for-loopu bude od 1 po n-1, cize od 1 po 0 -> for loop sa nepusti
    - vratim trojuholnik, ktory vyzera: [[1]]"""
"""vysvetlenie n = 2:
    - prva podmienka nie je pravdiva
    - vytvorim pascalov trojuholnik, prvy riadok je [[1]]
    - jedina hodnota ktoru bude mat i je 1, kedze range ide od 1 az po n-1
    - minuly riadok bude [1]
    - do noveho riadku si pridam prvu 1-ku (ta je v kazdom riadku)
    - druhy for loop ale preskocim, pretoze i moze byt len 1, teda je 1 a moj range ide od 1 po n-1 tj. 0, cize sa for loop nepusti
    - do noveho riadku si pridam 1-ku (ta je v kazdom riadku aj na konci)
    - do mojho trojuholnika si appendnem tento novy riadok
    - vratim trojuholnik, ktory vyzera: [[1], [1, 1]]"""
"""vysvetlenie n = 3
    - prva podmienka nie je pravdiva
    - vytvorim pt, prvy riadok je vzdy [[1]]
    - i bude mat hodnoty 1 a 2, pretoze range id od 1 az po n-1 tj. 1 po 2
    - zoberiem si minuly riadok z trojuholnika, do ktoreho ich postupne pridavam
    - novy_riadok sa zacne 1-tkou
    - j bude mat hodnoty: 1-> for loop sa nepusti (i=1), do noveho riadku pridam 1-tku, pridam riadok do trojuholnika
                          2-> for loop sa pusti pre j=1 (i=2)
                                -> novy-element(ne) sa bude rovnat cislu na indexe[j-1]->(0) tj. 1 ,plus cislu na indexe[j]->(1) tj. 1
                                    z minuleho riadku
                                -> pridam tento novy element do noveho riadku
                                -> pridam 1-ku na koniec noveho riadku, pridam tento riadok do trojuhonika
                                -> moj treti riadok v trojuholniku bude [[1,2,1]]
                                -> vratim trojuholnik, ktory vyzera: [[1], [1, 1], [1, 2, 1]]
    vzdy sa ten novy element bude rovnat dvojici cisel 'nad nim' """

# 7 LEPSIE RIESENIE
def pascalov_trojuholnik(n):
    vysl = []
    for i in range(1, n+1): # vytvara riadky trojuholnika -> tento for-loop je inkluzivny
        riadok = [1] # riadok sa vzdy zacina 1-kou
        for j in range(1, i): # vytvara zostavajuce prvky riadku -> tento for-loop nie je inkluzivny
            riadok.append(riadok[-1] * (i-j) // j) # binomial coefficient -> vzorec: C(n, k) = n! / (k! * (n - k)!) (kombinacne cisla)
            # riadok[-1] zoberie posledne cislo v riadku co sa prave vytvara, vynasobi sa (i-j) tj. (n-k) vo vzorci
        vysl.append(riadok)
    return vysl

# print(pascalov_trojuholnik(7))

# 8
def citaj(meno_suboru):
    with open(f'{meno_suboru}', encoding="utf8") as subor:
        res = []
        for riadok in subor:
            res.append(riadok.strip().split(" "))
    return res

# x = citaj("matice2023.txt")
# vypis(x)

# 9
def zapis(x, meno_suboru):
    with open(f"{meno_suboru}", "w", encoding="utf8") as subor:
        for i in x:
            print(" ".join(i), file=subor)
# zapis(x, "matice2023zapis.txt")

# 10
# na vytvorenie potrebneho suboru
'''import random
pocet_r = random.randrange(2, 5)
tab = []
for i in range(random.randrange(3, 8)):
    cur = []
    for j in range(random.randrange(1, 5)):
        cur.append(random.randrange(-1000, 1000))
    tab.append(cur)
print(tab)
with open("matice2023cisla.txt", "w") as subor:
    for i in tab:
        print(" ".join(map(str, i)), file=subor)'''

def citaj_cisla(meno_suboru):
    res = []
    with open(f"{meno_suboru}", encoding="utf8") as subor:
        for riadok in subor:
            res.append(list(map(int, riadok.strip().split(" "))))
    return res

# x = citaj_cisla("matice2023cisla.txt")
# print(x)

# kod z "prednasky" potrebny pre ulohu 11 a dalsie...
"""
import tkinter

def vyrob(pocet_riadkov, pocet_stlpcov, hodnota=0):
    '''vytvori tabulku na zaklade poctu riadkov a stlpcov'''
    vysl = []
    for i in range(pocet_riadkov):
        vysl.append([hodnota] * pocet_stlpcov)
    return vysl

def ocisluj(tab):
    '''pridavame ciselne hodnoty kazdemu elementu, po riadkoch'''
    poc = 0
    for riadok in tab:
        for j in range(len(riadok)):
            riadok[j] = poc
            poc += 1

def kresli_text(tab):
    '''vykreslime tabulku
        pouzitie enumerate aby sme dokazali upravovat x a y suradnice
        podla indexu elementu v riadku (x-suradnica)
         a indexu riadku v tabulke (y-suradnica)'''
    d = 20
    for r, riadok in enumerate(tab):
        for s, prvok in enumerate(riadok):
            canvas.create_text(s * d + 10, r * d + 10, text=prvok)

def kresli(tab, d=20, farby=('white', 'black', 'red', 'blue')):
    canvas.delete('all')
    for r, riadok in enumerate(tab):
        for s, prvok in enumerate(riadok):
            x, y = s * d + 5, r * d + 5
            farba = farby[prvok % len(farby)]
            canvas.create_rectangle(x, y, x + d, y + d,
                                    fill=farba, outline='light gray')
    canvas.update()

def zmen():
    '''funkcia pre nase tlacitko zmen, obnovi tabulku
    -> meni hodnoty '''
    for i, riadok in enumerate(t):
        for j in range(len(riadok)):
            riadok[j] += i + 1
    kresli(t)

canvas = tkinter.Canvas()
canvas.pack()

tkinter.Button(text='Zmeň', command=zmen).pack() # nebrali sme este, primitivne :)
t = vyrob(12, 12)
ocisluj(t)
# kresli_text(t)
kresli(t)

n = 11
t = vyrob(n, n)
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1: # obvod obrazka
            t[i][j] = 2
    t[i][i] = t[i][n - 1 - i] = 3 # diagonaly
kresli(t)"""

# tkinter.mainloop()

# 11 
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
def kresli(tab, d=20, farby=("black", "yellow", "orange", "blue", "red", "white")):
    for r, riadok in enumerate(tab):
        for s, prvok in enumerate(riadok):
            x, y = s * d + 5, r * d + 5
            if prvok != None:
                farba = farby[prvok]
                canvas.create_rectangle(x, y, x+d, y+d, fill=farba, outline="light gray")

panak = [
    [0, 0, 0, None, None],
    [1, 1, None, None, None],
    [1, 1, 1, None, 2],
    [3, None, None, None, 2],
    [3, 3, 2, 2, None],
    [4, 4, None, None, None],
    [4, 4, 4, None, None],
    [4, None, 4, 4, None],
    [2, None, None, 2, None],
    [2, 2, None, 2, 2]
]
# uprava panaka, nech je to symetricke pole -> doplnenie None ručne
# print(max(len(i) for i in panak))
# kresli(panak)

# 12
def zrkadlo(tab):
    res = []
    for i in tab:
        cur = []
        for j in i:
            cur.append(j)
        cur.append(None)
        for k in i[::-1]:
            cur.append(k)
        res.append(cur)
    return res

# print(zrkadlo(panak))
# kresli(zrkadlo(panak))
# kresli(zrkadlo(zrkadlo(panak)), 15)

# 13
# - lepsie riesenie, pridavam do posledne pridaneho listu cez extend
"""def zvacsi(obr):
    res = []
    for i in obr:
        res.append([])
        for j in i:
            res[-1].extend((j, j))
        res.append(res[-1])
    return res"""
# - jednoduchsie riesenie
def zvacsi(obr):
    res = []
    for i in obr:
        cur = []
        for j in i:
            cur.append(j)
            cur.append(j)
        res.append(cur)
        res.append(cur)
    return res
# kresli(zvacsi(panak), 10)
# kresli(zvacsi(zvacsi(panak)), 5)

# 14
def nahrad(obr, post):
    novy = []
    for riadok in obr:
        riadok = list(riadok)
        for i, prvok in enumerate(riadok):
            for x, y in post: # tuple!
                if prvok ==x:
                    riadok[i] = y
                    break
        novy.append(riadok)
    return novy

# kresli(nahrad(panak, ((3, 4), (4, 0), (None, 5))))
# 15 - treba ratat cez pytagorovu vetu!
t = []
for i in range(50):
    t.append([5]*50)
# print(t)
def kruh(tab, r, r1, s1, hodnota):
    """
    r -> polomer kruhu
    r1 -> riadok stredu
    s1 -> stlpec stredu
    hodnota -> index na vybratie farby z listu
    """
    n = len(tab)
    for i in range(n):
        for j in range(n):
            vzd = ((i-r1)**2 + (j-s1)**2) ** 0.5
            # obrazkove vysvetlenie
            if vzd <= r:
                tab[i][j] = hodnota
    return tab
'''kruh(t, 17, 20, 30, 4)
kruh(t, 13, 40, 25, 3)
kruh(t, 10, 15, 15, 0)
kruh(t, 8, 15, 15, 5)
kresli(t, 5)'''

# canvas.mainloop()

# 16
def do_radu(tab):
    res = []
    for i in tab:
        res.extend(i)
    return res

'''tab1 = [[1], [2, 3, 4], [5, 6], [7]]
zoz = do_radu(tab1)
print(zoz)
print(do_radu([["prvy"], [], ["druhy", "treti"]]))'''

# 17
def do_dvojrozmernej(postupnost, sirka):
    res = []
    zoz = list(postupnost)
    while zoz:
        res.append(zoz[:sirka])
        zoz = zoz[sirka:]
    return res

t1 = do_dvojrozmernej(range(10), 3)
vypis(t1)

vypis(do_dvojrozmernej('programovanie', 2))
