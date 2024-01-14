# slovníky začínajú č. 4

# 4
import random
vysky = {}
mena = ["Igor", "Majo", "Peter", "Filip", "Jojo", "Martin"]
for i in mena:
    vysky[i] = random.randrange(160, 202)

"""for meno, vyska in vysky.items():
    print(meno, vyska)"""

# 5
"""for meno, vyska in sorted(vysky.items()):
    print(meno, vyska)"""

# 6
"""for meno, vyska in sorted(vysky.items(), key=lambda x:x[1]):
    print(meno, vyska)"""

# 7
def priemer(slovnik):
    sucet = 0
    pocet = len(slovnik)
    for vyska in slovnik.values():
        sucet += int(vyska)
    return round(sucet/pocet, 2)
# print(priemer(vysky))

# 8
def vypis2(slovnik, priemer):
    for meno, vyska in slovnik.items():
        if vyska > priemer:
            print(meno, vyska, "nadpriemer")
        else:
            print(meno, vyska, "podpriemer")
# vypis2(vysky, priemer(vysky))
# print(priemer(vysky))

# 9
def len_od_do(slovnik, od, do):
    novy_slovnik = {}
    for meno, vyska in slovnik.items():
        if od < vyska < do:
            novy_slovnik[meno] = vyska
    return novy_slovnik
# print(len_od_do(vysky, 180, 200))

# 10
def prevrat(slovnik):
    novy_slovnik = {}
    for meno, vyska in slovnik.items():
        if vyska in novy_slovnik:
            novy_slovnik[vyska].append(meno)
        else:
            novy_slovnik[vyska] = [meno]
    return novy_slovnik

# print(prevrat(vysky))

# 11
def dve_kocky(n):
    hody = {}
    for i in range(n):
        c1 = random.randrange(1, 7)
        c2 = random.randrange(1, 7)
        sucet = c1+c2
        if sucet in hody:
            hody[sucet] += 1
        else:
            hody[sucet] = 1
    return hody

# 12
def delitele(od, do):
    delitele = {}
    for i in range(od, do+1):
        for j in range(1, i+1):
            if i%j==0:
                if i in delitele:
                    delitele[i].append(j)
                else:
                    delitele[i] = [j]
    return delitele
# print(delitele(1, 12))

# 13 - pass

# 14
def opakuju(meno_suboru):
    tabulka = {}
    with open(meno_suboru) as subor:
        for riadok in subor:
            riadok = riadok.strip()
            if riadok in tabulka:
                tabulka[riadok] += 1
            else:
                tabulka[riadok] = 1
    return tabulka

# print(opakuju("opakuju.txt"))

# 15
# rovnaké ako 2017

# 16 ?
