# 1
zvierata = {}
with open("zoo.txt") as subor:
    for riadok in subor:
        zviera, vaha = riadok.strip().split()
        zvierata[zviera] = vaha

def najtazsie(slov):
    # ako parameter pouzijem lambda funkciu
    t =  max(slov, key=lambda x: int(slov[x]))
    return t

def tazsie_ako(zviera):
    tazsie_zvierata = []
    vaha = int(zvierata[zviera])
    for meno, kg in zvierata.items():
        if int(kg) > vaha:
            tazsie_zvierata.append(meno)
    return tazsie_zvierata

def vyber_lahsie(zviera):
    lahsie_zvierata = {}
    vaha = int(zvierata[zviera])
    for meno, kg in zvierata.items():
        if int(kg) <= vaha:
            lahsie_zvierata[meno] = kg
    return lahsie_zvierata

'''print(najtazsie(zvierata))
print(tazsie_ako("zirafa"))
lahsie = vyber_lahsie("jazvec")
print(lahsie)'''

# 2
skladatelia = {}
with open("skladatelia.txt") as subor:
    for riadok in subor:
        meno, rok = riadok.strip().split()
        rok = int(rok)
        skladatelia[meno] = rok
# print(skladatelia)
def ziskaj_meno(val):
    val = int(val)
    for key, value in skladatelia.items():
        if val == int(value):
            return key

najstarsi_rok = min(skladatelia.values())# max(skladatelia, key=lambda x : skladatelia[x])
najmladsi_rok = max(skladatelia.values())# min(skladatelia, key=lambda x : skladatelia[x])
# print(f"najstarsi: {ziskaj_meno(najstarsi_rok)} {najstarsi_rok}")
# print(f"najmladsi: {ziskaj_meno(najmladsi_rok)} {najmladsi_rok}")

def medzi(rok1, rok2):
    mena = []
    for key, value in skladatelia.items():
        if int(value) > rok1 and int(value) < rok2:
            mena.append(key)
    return mena

zoz = medzi(1820, 1830)
# print(zoz)

# 3

"""skladatelia2 = {}
for key, value in skladatelia.items():
    if value in skladatelia2:
        skladatelia.update({int(value):key})
    else:
        skladatelia2[int(value)] = key

print(skladatelia2)"""

# 4

with open("twain.txt") as subor:
    slovnik_dlzok = {}
    for riadok in subor:
        riadok = riadok.strip()
        slova = riadok.split()
        for i in slova:
            if len(i) in slovnik_dlzok:
                slovnik_dlzok[len(i)].append(i)
            else:
                slovnik_dlzok[len(i)] = [i]

zoradeny = dict(sorted(slovnik_dlzok.items(), key= lambda x:len(x[1]), reverse=True))
najcastejsie = list(zoradeny.items())[0]
# print(f"najcastejsie dlzka je {najcastejsie[0]}")
# print(f"slov dlzky {najcastejsie[0]} je {len(najcastejsie[1])}")
#...

# 5
def dvojice(meno_suboru):
    dvojice = {}
    with open(meno_suboru, encoding="utf-8") as subor:
        for riadok in subor:
            riadok = riadok.strip()
            riadok = riadok.replace(" ", "")
            for i in range(len(riadok)-1):
                dvojica = riadok[i]+riadok[i+1]
                if dvojica in dvojice:
                    dvojice[dvojica] += 1
                else:
                    dvojice[dvojica] = 1
    return dvojice

c = 0
"""for dvojica, pocet in sorted(dvojice("twain.txt").items(), key= lambda x:x[1], reverse=True):
    if c==10:
        break
    print(pocet, dvojica)
    c+=1"""

# 6
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

# 7
def fib(n):
    fibo = {}
    a, b = 0, 1
    for i in range(n+1):
        fibo[i] = a
        x = b
        b = a+b
        a = x
    return fibo

# print(fib(6))

# 8
import random

'''sifra = {}
abc = "abcdefghijklmnopqrstuvwxyz"
abc_na_sifru = list("abcdefghijklmnopqrstuvwxyz")
for i in abc:
    idx = random.randrange(0, len(abc_na_sifru))
    sifra[i] = abc_na_sifru[idx]
    abc_na_sifru.pop(idx)
print(sifra)'''

sifra = {'a': 'i', 'b': 'f', 'c': 'a', 'd': 'j', 'e': 'k', 'f': 'v', 'g': 'w', 'h': 's', 'i': 'd', 'j': 'e', 'k': 'p', 'l': 'x', 'm': 'o', 'n': 'b', 'o': 'n', 'p': 'g', 'q': 'm', 'r': 
'c', 's': 'l', 't': 'r', 'u': 'u', 'v': 'z', 'w': 'q', 'x': 't', 'y': 'h', 'z': 'y'}


def zasifruj(sifra, text):
    zasifrovany_text = ""
    for i in text:
        if i in sifra:
            zasifrovany_text+=sifra[i]
        else:
            zasifrovany_text+=i
    return zasifrovany_text

def otoc_d(slovnik):
    return {value: key for key, value in slovnik.items()}

def rozsifruj(sifra, text):
    prevratena_sifra = otoc_d(sifra)
    rozsifrovany_text = ""
    for i in text:
        if i in prevratena_sifra:
            rozsifrovany_text+=prevratena_sifra[i]
        else:
            rozsifrovany_text+=i
    return rozsifrovany_text


t = zasifruj(sifra, "jablko je super")
tt = rozsifruj(sifra, t)
# print(t)
# print(tt)

# 9 ?
# 10
# 11
import random

def rozhadz(post):
    novy_z = []
    zoz = list(post)
    while len(zoz) > 0:
        idx = random.randrange(len(zoz))
        novy_z.append(zoz.pop(idx))
    
    return novy_z

x = rozhadz("abcdefghujkl")
# print(x)
y = rozhadz(range(10, 30))
# print(y)


                    

