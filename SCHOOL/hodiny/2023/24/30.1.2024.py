import csv
import matplotlib.pyplot as ppt
subor = open("populacia.csv", encoding="utf-8-sig")
# subor = csv.reader(file)

# print(subor)
krajiny_obyvatelia = {}
for riadok in subor:
    riadok = riadok.strip()
    # print(riadok)
    krajinka, obyvatelia, rozloha = riadok.split(";")
    krajiny_obyvatelia[krajinka] = obyvatelia

# print(krajiny_obyvatelia)
pocty_cislic = {}
for hodnota in krajiny_obyvatelia.values():
    x = hodnota[0]
    if x in "123456789":
        if x in pocty_cislic:
            pocty_cislic[x] +=1
        else:
            pocty_cislic[x] = 1
cislice, pocty = [], []
for cislica, pocet in sorted(pocty_cislic.items(), key = lambda x:x[1], reverse=True):
    cislice.append(cislica)
    pocty.append(int(pocet))

ppt.bar(cislice, pocty)
#ppt.bar(pocty, cislice)
ppt.show()
print(pocty_cislic)
    
import json

subor = json.load(open("faktury_BB.json"))
firmy_sumy = {}
firmy_ico = {}
for i in range(len(subor)):
    firma = subor[i]["Dodávateľ"]
    cena = subor[i]["Celková_cena"]
    ico = subor[i]["IČO"]
    if firma in firmy_sumy:
        firmy_sumy[firma] += float(cena.strip().replace(",", ".").replace(" ", ""))
    else:
        firmy_sumy[firma] = float(cena.strip().replace(",", ".").replace(" ", ""))
    
    firmy_ico[firma] = ico
# print(firmy_ico)
# print(firmy_sumy)
c = 0
for firma, suma in sorted(firmy_sumy.items(), key = lambda x:x[1], reverse=True):
    if c == 3:
        break
    ico = firmy_ico[firma]
    suma = round(suma, 2)
    print(firma, suma, ico)
    c+=1

# sumy po rokoch - podla inputu
# vypisat top 10 spolocnosti, ktore sa vymykaju Benfordovho zakonu
# -> pomery maju velku odchylku od grafu
# ak je pocet vyskytu cislice dlhsi ako zoznam(cislic tejto firmy) treba firmu vylucit
# => nieco ako stale prikazy -> skresluje to benf. krivku
benf = [0.301, 0.176, 0.123, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]

"""
slov = {"ICO":{"meno":"string",
                "rok":{"2012":[list],
                        "2013":[list]
                        }
                }
        }
"""
