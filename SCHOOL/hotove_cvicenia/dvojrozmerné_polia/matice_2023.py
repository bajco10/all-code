# 1 lahke
#2
def vypis(tab, sirka=None):
    if sirka == None:
        max_sirka = 0
        for i in tab:
            for j in i:
                if len(str(j)) > max_sirka:
                    max_sirka = len(str(j))
        s = max_sirka
    else:
        s = sirka
    
    for i in tab:
        i = map(str, i)
        print(f"{' '*s}".join(i))
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

# print(zoznam_suctov([['1', 'x', '2'], [], [5, 6], [3.1, 4], [(5, 6), (7,)]]))

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
# pridaj_sucty(t)
# vypis(t)

#5 - zip strasne dolezita vec!
# * v zip -> aby zip nebral tab ako celok ale bral kazdy riadok jednotlivo
def preklop(tab):
    new_tab = list(map(list, zip(*tab)))
    return new_tab
#  p = [[1, 2], [5, 6], [3, 4]]
# vypis(preklop(p), 2)

#6
def ocisluj2(tab, start=0):
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
    
    tab[:] = list(map(list, zip(*new_tab)))

ab = [[1, 1, 1], [], [1, 1, 1, 1], [1], [1, 1, 1, 1, 1]]

ocisluj2(ab)
for i in ab:
    print(" ".join(map(str, i)))
