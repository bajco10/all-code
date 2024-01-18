# vigenerova sifra
"""
# tabulka
import random

pismena = [chr(a) for a in range(ord("A"), ord("Z")+1)]
shuff = list(pismena)
random.shuffle(shuff)

with open("vigenere.txt", "w") as subor:
    print(" ", " ".join(pismena), file=subor)
    for pismeno in pismena:
        print(pismeno, " ".join(shuff), file=subor)
        shuff = shuff[1:] + [shuff[0]] # prve pismeno dam vzdy len na koniec
"""

# tabulka pre sifrovanie/desifrovanie z textu
tabulka = []
# text: Dnes je posledý deň., heslo: heslo
abeceda = []
with open("vigenere.txt") as subor:
    pismena = subor.readline().strip().split()
    for riadok in subor:
        tabulka.append(riadok.strip().split())

def sifrovanie(veta, heslo):
    """ text je vlavo v tabulke, heslo je hore"""
    textik = ""
    heslo = heslo.upper()
    for i in veta.upper():
        if i in pismena:
            row = ord(i) - ord("A")
            col = pismena.index(heslo[0])
            heslo = heslo[1:] + heslo[0]
            textik += tabulka[row][col+1]
        else:
            textik += i
    return textik
print(sifrovanie("Dnes je posledný deň.", "heslo"))

# desifrovanie -> potrebujem toto heslo
# budem hladat pismenko zo sifrovaneho textu v stlpci podla indexu, ktory ziskam z pismena z hesla
def desifruj(sifrovane, heslo):
    textik = ""
    heslo = heslo.upper()
    for i in sifrovane:
        if i in pismena:
            idx = pismena.index(heslo[0]) + 1
            heslo = heslo[1:] + heslo[0]
            for j in tabulka:
                if j[idx] == i:
                    textik += j[0]
        else:
            textik += i 
    return textik

print(desifruj("UIYF OT GLFVTASÝ JPŇ.", "heslo"))


