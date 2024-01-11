# práca s csv súbormi

"""import csv

file = open("naklady.csv", encoding="utf-8-sig")
# -sig aby som sa zbavil "oznacenia" v prvom riadku suboru
subor = csv.reader(file)
mesiace = {}
for riadok in subor:
    riadok = riadok[0]
    riadok = riadok.strip()
    riadok = riadok.replace(r"\ufeff", "")
    prva = riadok.find(".")
    druha = riadok[prva+1:].find(".")
    # mesiac
    mesiac = (riadok[prva+1:druha+prva+1])
    # cislo
    datum, suma = riadok.split(" ")
    suma = suma.replace("€", "")
    if mesiac in mesiace:
        mesiace[(mesiac)] += float(suma)
    else:
        mesiace[(mesiac)] = float(suma)"""

# print(mesiace)

"""for mesiac, suma in sorted(mesiace.items(), key=lambda x:int(x[0])):
    print(f"{mesiac}. - {round(suma, 2)}")
print()
for mesiac, suma in sorted(mesiace.items(), key=lambda x:x[1], reverse=True):
    print(f"{mesiac}. - {round(suma, 2)}")"""

# zapisanie do suboru podla datumu
# dorobit!
with open("zoradene_naklady.csv", "w") as subor:
    pass

import csv

file = open("naklady.csv", encoding="utf-8-sig")
# -sig aby som sa zbavil "oznacenia" v prvom riadku suboru
subor = csv.reader(file)
zoradene_srandy = []
sumy = {}
for riadok in subor:
    riadok = riadok[0]
    riadok = riadok.strip()
    riadok = riadok.replace(r"\ufeff", "")
    datum, suma = riadok.split(" ")
    d, m, r = datum.split(".")
    cislo = int(d) + int(m) + int(r)
    # formatovany_riadok = f"{r}-{m}-{d}"
    # sumy[formatovany_riadok] = suma
    sumy[cislo] = riadok

for datum, riadok in sorted(sumy.items()):
    # print(datum)
    zoradene_srandy.append(riadok)
print(zoradene_srandy)

    