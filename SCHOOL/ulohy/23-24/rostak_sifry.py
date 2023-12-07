with open("homofona.txt") as subor:
    tabulka = []
    for riadok in subor:
        tabulka.append(riadok.replace(":", "").strip().split(" "))


import random

def sifruj(meno_suboru):
    sifrovane_cele = []
    with open(meno_suboru, encoding="utf8") as subor:
        for riadok in subor:
            sifrovany_riadok = []
            riadok=riadok.strip()
            for znak in riadok.upper():
                for i in tabulka:
                    je_tam = False
                    if i[0] == znak:
                        je_tam = True
                        sifrovany_riadok.append(i[random.randrange(1,len(i))])
                        break
                if je_tam == False:
                    sifrovany_riadok.append(znak)        
            sifrovane_cele.append(sifrovany_riadok)
    with open(meno_suboru, "a",encoding="utf8") as subor:
        print("\n", file=subor)
        for l in sifrovane_cele:
            print("".join(l), file=subor)

# sifruj("sifruj.txt")

def desifruj(meno_suboru):
    riadky = []
    with open(meno_suboru, encoding="utf8") as subor:
        for riadocek in subor:
            riadocek = riadocek.strip()
            riadky.append(riadocek)
    # print(riadky)
    desifrovane_cele = []
    for riadok in riadky:
        desifrovany_riadok = []
        index = 0
        while index < len(riadok):
            ciselko = riadok[index:index+2]
            je_tam = False
            for k in tabulka:
                if ciselko in k:
                    desifrovany_riadok.append(k[0])
                    index+=2
                    je_tam=True
            if je_tam==False:
                desifrovany_riadok.append(riadok[index])
                index+=1
        desifrovane_cele.append(desifrovany_riadok)
    with open(meno_suboru, "a", encoding="utf8") as subor:
        print("\n", file=subor)
        for l in desifrovane_cele:
            print("".join(l), file=subor)

desifruj("desifruj.txt")



            




