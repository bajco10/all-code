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
        mesiace[(mesiac)] = float(suma)

# print(mesiace)

for mesiac, suma in sorted(mesiace.items(), key=lambda x:int(x[0])):
    print(f"{mesiac}. - {round(suma, 2)}")
print()
for mesiac, suma in sorted(mesiace.items(), key=lambda x:x[1], reverse=True):
    print(f"{mesiac}. - {round(suma, 2)}")"""

# zapisanie do suboru podla datumu
# dorobit!
'''with open("zoradene_naklady.csv", "w") as subor:
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
print(zoradene_srandy)'''

import csv

file = open("naklady.csv", encoding="utf-8-sig")
subor = csv.reader(file)

slov = {i: [] for i in range(1,13)}
utried = []
date = []
for riadok in subor:
    datum, hodnota = riadok[0].split()
    d, m, r = datum.split(".")
    str_date = f'{r}-{int(m):02}-{int(d):02}'
    #ulozenie do slovnika kde klucom su mesiace
    slov[int(m)].append(float(hodnota[:-1]))
    #priprava na zapis do suboru zoredene podla datumu
    date.append([str_date, riadok])

#Vypis podla mesiacov       
for kluc, suma in slov.items():
    print(f'{kluc:2}: {sum(suma):.2f}€')
    #priprava na utriedenie podla trzieb
    utried.append([sum(suma), kluc])
print()
#vypis podla trzieb    
for prvok in sorted(utried, reverse=True):
    print(f'{prvok[1]:2}: {prvok[0]:.2f}€')
    
#ulozenie do suboru utriedene podla datumu
with open('usporiadane.csv', 'w', encoding="utf-8-sig") as f:
    writer = csv.writer(f, lineterminator='\n', delimiter=" ")
    for riadok in sorted(date):
        writer.writerow(riadok[1])
    