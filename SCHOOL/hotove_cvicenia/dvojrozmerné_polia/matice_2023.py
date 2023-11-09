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

# 6 LEPSIE RIESENIE
def pascalov_trojuholnik(n):
    vysl = []
    for i in range(1, n+1): # vytvara riadky trojuholnika -> tento for-loop je inkluzivny
        riadok = [1] # riadok sa vzdy zacina 1-kou
        for j in range(1, i): # vytvara zostavajuce prvky riadku -> tento for-loop nie je inkluzivny
            riadok.append(riadok[-1] * (i-j) // j) # binomial coefficient -> vzorec: C(n, k) = n! / (k! * (n - k)!) (kombinacne cisla)
            # riadok[-1] zoberie posledne cislo v riadku co sa prave vytvara, vynasobi sa (i-j) tj. (n-k) vo vzorci
        vysl.append(riadok)
    return vysl

print(pascalov_trojuholnik(7))

