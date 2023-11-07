# da sa to prerobit na viac suborov, nech sa tabulka nemeni zakazdym pri spusteni programu

import random

abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
cisla = [f"{x:02d}" for x in range(0, 100)]
tabulka = [[i] for i in abeceda]


for i in tabulka:
    for j in range(2):
        idx = random.randrange(0, len(cisla))
        i.append(cisla[idx])
        cisla.pop(idx)

while len(cisla) > 0:
    kam = random.randrange(len(tabulka))
    idx = random.randrange(0, len(cisla))
    tabulka[kam].append(cisla[idx])
    cisla.pop(idx)

with open('tabulka_sifier.txt', 'w') as subor:
    for i in tabulka:
        pismenko = i[0]
        # ciselka = map(int, i[1:])
        print(f"{pismenko.upper()}: {' '.join(i[1:])}", file=subor)

# takto ako zoznam tam dam tie stringy, nech to je ako keby to citam zo suboru
text = ["janko hrasko", "bryndzove halusky", "kosicky med", "dizel passat"]

# zasifrovat
sifrovane = []
for i in text:
    sifrovany_riadok = []
    for j in i:
        for k in tabulka:
            if k[0] == j:
                je_v_tabulke = True
                # print(k[0], j, random.choice(k[1:]))
                sifrovany_riadok.append(random.choice(k[1:]))
                break
            je_v_tabulke=False
        if je_v_tabulke==False:
            sifrovany_riadok.append(j)
    sifrovane.append(sifrovany_riadok)
# print(sifrovane)
for i in sifrovane:
    print("".join(i))
# desifrovat
# mozno treba dorobit pre vsetky specialne znaky, podobne ako z je_v_tabulke pri sifrovani :)
desifrovane = []
for i in sifrovane:
    desifrovany_riadok = []
    for j in i:
        if j != ' ':
            for k in tabulka:
                if j in k[1:]:
                    desifrovany_riadok.append(k[0])
        else:
            desifrovany_riadok.append(" ")
    desifrovane.append(desifrovany_riadok)
# print(desifrovane)
for i in desifrovane:
    print("".join(i))




    

