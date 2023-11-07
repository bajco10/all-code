# netrvalo to moc dlho :)
with open('homofona.txt') as subor:
    riadky = []
    for riadok in subor:
        riadok = riadok.strip().replace(":", "")
        riadky.append(riadok)


tabulka = []
for i in riadky:
    tabulka.append(list(i.split(" ")))


import random
def sifruj(meno_suboru):
    riadky = []
    with open(f'{meno_suboru}') as subor:
        for riadok in subor:
            riadok = riadok.strip()
            riadky.append(riadok)
    
    sifrovane = []
    for i in riadky:
        sifrovany_riadok = []
        for j in i:
            for k in tabulka:
                if k[0] == j.upper():
                    je_v_tabulke = True
                    sifrovany_riadok.append(random.choice(k[1:]))
                    break
                je_v_tabulke = False
            if je_v_tabulke==False:
                sifrovany_riadok.append(j)
        sifrovane.append(sifrovany_riadok)

    with open(f'{meno_suboru}', 'a') as file:
        print("\n", file=file)
        for m in sifrovane:
            print("".join(m), file=file)

sifruj("sifruj.txt")

def desifruj(meno_suboru):
    riadky = []
    with open(f'{meno_suboru}') as subor:
        for riadok in subor:
            riadok = riadok.strip()
            riadky.append(riadok)
    
    desifrovane = []
    for i in riadky:
        desifrovany_riadok = []
        idx = 0
        while idx < len(i):
            je_v_tabulke = False
            for k in tabulka:
                for m in k[1:]:
                    if i[idx:idx+2] == m:
                        je_v_tabulke = True
                        desifrovany_riadok.append(k[0])
                        idx += 2
                        break
                if je_v_tabulke:
                    break
            if not je_v_tabulke:
                desifrovany_riadok.append(i[idx])
                idx += 1
        desifrovane.append(desifrovany_riadok)
    
    with open(f'{meno_suboru}', 'a') as file:
        print("\n", file=file)
        for m in desifrovane:
            print("".join(m), file=file)


desifruj('desifruj.txt')


        
