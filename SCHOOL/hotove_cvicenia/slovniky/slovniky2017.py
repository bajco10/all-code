# 5
mena = ["Igor","Filip", "Jojo", "Cyril", "Adam", "Anna", "Jamal", "Frederika", "Margita"]
"""import random
vysky = {}
for i in mena:
    vysky[i] = random.randrange(140, 202)"""
vysky = {"Igor" : 152,
         "Filip" : 160,
         "Jojo" : 148,
         "Cyril" : 201,
         "Adam" : 152,
         "Anna" : 150,
         "Jamal" : 189,
         "Frederika" : 144,
         "Margita" : 196}
# 6
# vypise podla abecedy
"""for kluc, hodnota in sorted(vysky.items()):
    print(kluc, hodnota)
print()"""
# 7
# vypise od najvyssich po najnizsich
"""for kluc, hodnota in sorted(vysky.items(), key=lambda x:x[1], reverse=True):
    print(kluc, hodnota)"""

# 8
def priemer(vysky):
    return sum(vysky.values())/len(vysky)

# print(priemer(vysky))

#9
'''for meno, vyska in vysky.items():
    if vyska < priemer(vysky):
        print(meno, vyska, "podpriemer")
    elif vyska == priemer(vysky):
        print(meno, vyska, "priemer")
    else:
        print(meno, vyska, "nadpriemer")'''

# 10
def len_od_do(vysky, od, do):
    nove_vysky = {}
    for meno, vyska in vysky.items():
        if od < vyska and do > vyska:
            nove_vysky[meno] = vyska
    return nove_vysky

# print(len_od_do(vysky, 150, 180))

# 11

vysky = {"Igor" : 152,
         "Filip" : 160,
         "Jojo" : 148,
         "Cyril" : 201,
         "Adam" : 152,
         "Anna" : 150,
         "Jamal" : 189,
         "Frederika" : 144,
         "Margita" : 196}

def prevrat(vysky):
    novy = {}
    for key, value in vysky.items():
        if value in novy:
            novy[value].append(key)
        else:
            novy[value] = [key]
    return novy
# x = prevrat(vysky)
# print(x)

# 12
import random

def dve_kocky(n):
    tabulka_suctov = {}
    for i in range(n):
        k1, k2 = random.randint(1, 6), random.randint(1, 6)
        sucet = k1 + k2
        if sucet in tabulka_suctov:
            tabulka_suctov[sucet] += 1
        else:
            tabulka_suctov[sucet] = 1
    return tabulka_suctov
'''x = dve_kocky(1200)
for kluc, hodnota in sorted(x.items()):
    print(f"sucet: {kluc} padol {hodnota}-krat")'''

# 13 -> neviem, ci sa toto da povazovat za riesenie bez if
def farba(retazec):
    try:
        farby = {
            "biela" : "white",
            "cierna" : "black",
            "cervena" : "red",
            "modra" : "blue",
            "zlta" : "yellow",
            "zelena" : "green"
        }
        return farby[retazec]
    except:
        return "pink"

# print(farba("cierna"))

# 14 - ??
def pretypuj(nazov, hodnota):
    pass

# 15
# kod na vytvorenie suboru s nahodnym poctom riadkov, dlzky riadku a nahodnymi znakmi
'''with open("opakuju.txt", "w") as subor:
    for i in range(random.randrange(30, 100)):
        pocet = random.randrange(1, 4)
        r = ""
        for i in range(pocet):
            r += random.choice("abcdefghijkl")
        print(r, file=subor)'''

def opakuju(meno_suboru):
    tabulka = {}
    with open(meno_suboru) as subor:
        for riadok in subor:
            riadok = riadok.strip()
            if riadok in tabulka:
                tabulka[riadok] += 1
            else:
                tabulka[riadok] = 1
    for r, p in tabulka.items():
        if p >= 3:
            print(r)

# opakuju("opakuju.txt")

# 16
def dvojice(meno_suboru):
    tabulka = {}
    with open(meno_suboru) as subor:
        for riadok in subor:
            riadok = riadok.strip().replace(" ", "")
            for i in range(len(riadok)-1):
                dvojica = riadok[i]+riadok[i+1]
                if dvojica in tabulka:
                    tabulka[dvojica] += 1
                else:
                    tabulka[dvojica] = 1

    m = 0 # strasne divny sposob vypisovania ale funguje
    for kluc, hodnota in sorted(tabulka.items(), key=lambda x:x[1], reverse=True)[:10]:
            """if m > 10:
                break"""
            print(kluc, hodnota)
            m+=1
            

"""dvojice("twain.txt")
print()
dvojice("dobs.txt")"""

# 17
