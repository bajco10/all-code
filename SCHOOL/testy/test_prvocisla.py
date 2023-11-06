# zistujeme ci je prvocislo
def je_prvo(n):
    pocet_d = 0
    for i in range(1, n+1):
        if n%i==0:
            pocet_d +=1
    if pocet_d == 2:
        return True
    return False
# vygenerujem si prvocisla, ktore budem pouzivat na dosadzovanie
dodatocne_prvocisla = []
for i in range(999):
    if je_prvo(i):
        dodatocne_prvocisla.append(i)
# spravim si dvojrozmerne pole z cisel v subore
with open('prvocisla.txt') as subor:
    cisla = []
    for riadok in subor:
        riadok = riadok.strip()
        cisla.append(list(map(str, riadok.split(" "))))
    print(cisla)

# dam prec duplikaty
for i in cisla:
    for j in i:
        while i.count(j) > 1:
            i.remove(j)
n = int(input())
#doplnam alebo skracujem riadky
import random
for i in cisla:
    if len(i)>n:
        while len(i) != n:
            i.pop(-1)
    elif len(i) < n:
        while len(i) != n:
            for j in range(len(dodatocne_prvocisla)):
                if dodatocne_prvocisla[j] > int(max(i)):
                    idx = j
                    break
            c = (random.choice(dodatocne_prvocisla[idx:]))
            i.append(str(c))
            dodatocne_prvocisla.remove(c)

# zapisem upravene dvojrozmerne pole do noveho suboru
with open('/home/tomas/Desktop/all-code/SCHOOL/testy/prvocisla_edit.txt', 'w') as subor:
    for i in cisla:
        i.sort(reverse=True)
        radek = list(map(str, i))
        print(" ".join(radek), file=subor)




