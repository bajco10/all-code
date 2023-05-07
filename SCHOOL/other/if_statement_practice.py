"""
import tkinter
import random

canvas = tkinter.Canvas(bg='white', width=300, height=300)
canvas.pack()

for i in range(1000):
    x = random.randrange(300)
    y = random.randrange(300)

    if random.randrange(50):             # t.j. random.randrange(50) != 0
        farba = 'red'
    else:
        farba = 'blue'
    canvas.create_rectangle(x-5, y-5, x+5, y+5, fill=farba, outline='')
canvas.mainloop()
"""
# program na zistovanie delitelov
"""
cislo = int(input('Zadaj číslo: '))
pocet = 0
print('delitele:', end=' ')
for delitel in range(1, cislo+1):
    if cislo % delitel == 0:        # mohli by sme zapisat aj  if not cislo % delitel:
        pocet += 1
        print(delitel, end=' ')
print()
print('počet deliteľov:', pocet)
"""
# program na zistenie prvocisla
"""
cislo = int(input("Zadaj cislo: "))
pocet = 0
for delitel in range(1, cislo+1):
    if cislo % delitel == 0:
        pocet += 1
if pocet == 2:
    print(f"{cislo} je prvocislo")
else:
    print(f"{cislo} nie je prvocislo")
"""
# program na hladanie "dokonalych" cisiel
"""
print("dokonale cislo do 10000 su ", end="")
for cislo in range(1, 10001):
    sucet = 0
    for delitel in range(1, cislo):
        if cislo % delitel == 0:
            sucet += delitel
    if sucet == cislo:
        print(cislo, end=", ")
print()
print("---viac ich uz nie je---")
"""
# vylepseny program na hladanie prvocisel
"""
cislo = int(input("Zadaj cislo: "))
pocet = 0
for delitel in range(2, cislo+1):
    if cislo % delitel == 0:
        break
if delitel == cislo:
    print(cislo, "je prvocislo")
else:
    print(cislo, "nie je prvocislo")
"""

# PODMIENENY CYKLUS - WHILE STATEMENT

""""
import tkinter

sirka = int(input('šírka plochy: '))

canvas = tkinter.Canvas(bg='white', width=sirka)
canvas.pack()

x = 5
a = 10
while x + a < sirka:
    canvas.create_rectangle(x, 200, x+a, 200-a)
    x = x + a
    a = a + 10

canvas.mainloop()
"""
# program na prvocisla s while loopom
"""
cislo = int(input("Zadaj cislo: "))
delitel = 2
while delitel < cislo and cislo % delitel !=0:
    delitel += 1

if delitel == cislo:
    print(f"{cislo} je prvocislo")
else:
    print(f"{cislo} nie je prvocislo")
"""
# zistovanie druhej odmocniny
"""
cislo = float(input("zadaj cislo:"))

x = 1
while x ** 2 < cislo:
    x = x + 0.001

print("odmocnina", cislo, "je", x)
"""
# zlepseny program na hladanie odmocnin (wtf lmao)
"""
cislo = float(input("zadaj cislo: "))

od = 1
do = cislo

x = (od + do)/2
pocet = 0
while abs(x**2 - cislo) > 0.001:
    if x**2 > cislo:
        do = x
    else:
        od = x
    x = (od + do) / 2
    pocet += 1

print("druha odmocnina", cislo, "je", x)
print("pocet prechodov while-cyklom bol", pocet)
"""


# Nekonecny cyklus


sucet = 0
while True:
    retazec = input('zadaj číslo: ')
    if retazec == '':
        break
    sucet += int(retazec)
print('súčet prečítaných čísel =', sucet)




