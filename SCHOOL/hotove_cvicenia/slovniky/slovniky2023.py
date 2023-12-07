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

skladatelia2 = {}
for key, value in skladatelia.items():
    if value in skladatelia2:
        skladatelia.update({int(value):key})
    else:
        skladatelia2[int(value)] = key

print(skladatelia2)



