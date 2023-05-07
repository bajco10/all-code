'''
def odvesna(a, b, c=None):
    c = (a**2 + b**2)**(1/2)
    print(f"Trojuholník so stranami: {a}, {b} je: {c}")

while True:
    a = input("Zadaj stranu a: ")
    if a == "q":
        break
    else:
        a = float(a)
    b = input("Zadaj stranu b: ")
    if b == "q":
        break
    else:
        b = float(b)
    odvesna(a, b)
'''
'''
a = float(input("Zadaj stranu a: "))
b = float(input("Zadaj stranu b: "))
c = (a**2 + b**2)**(1/2)

print(f"Trojuholník so stranami: {a}, {b} je: {c}")
'''
'''
pocet_rokov = 10
stav_uctu = 100
print(stav_uctu*((1+0.04)**pocet_rokov))



sirka = float(input("sirka: "))
dlzka = float(input("dlzka: "))
cena_za_meter = (8.40 / 14)
treba_plechoviek = (sirka * dlzka) // 14
if treba_plechoviek % 1 < 0.5:
    treba_plechoviek += 1
print((sirka*dlzka)/14)
print(treba_plechoviek)
print(f"Finálna suma: {treba_plechoviek * 8.40} €")
'''

# akvarium
# hustota skla = 2500kg / m**3
# hustota vody = 998 kg**m3
dlzka = 1
sirka = 0.3
vyska = 0.5

objem_vody = (dlzka-0.02) * (sirka-0.02) * (vyska-0.02)
objem = dlzka * sirka * vyska
blok_skla_vaha = 2500 * (dlzka * sirka * vyska)
vyrez_zo_skla_vaha = 2500 * ((dlzka-0.02) * (sirka-0.02) * (vyska-0.02))
akvarium_vaha = (blok_skla_vaha - vyrez_zo_skla_vaha) + (998 * ((dlzka-0.02) * (sirka-0.02) * (vyska-0.02)))
print(f"Vaha plne naplneneho akvaria je {akvarium_vaha}kg.")


meranie1 = 5.333*10**4
meranie2 = 5.25*10**4
# print((meranie1 - meranie2) / 5)
# 166 rotations inbetween measures
# v = s/t , v = s/830
# s = rotacie * 360°
s = 166 * 360
t = 830
v = s/t
print(f"Rychlost, ktorou sa lietadlo priblizuje k radaru je {v}m/s.")


cislo = 31841624

for cifra in str(cislo):
    zvysok = cislo % 10
    cislo = cislo // 10
    print(cislo, zvysok)



for i in range(5):
    for j in range(i, 5**2):
        print(j, end=' ')
    print()





