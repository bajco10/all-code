""" Vo vacsine programov su hodnoty pevne danne, nech nemusime ist cez milion inputov.
    Programy kde to tak nie je, su okomentovane - aby boli nefunkcne.
    zdroj zadani: https://input.sk/python2017/02.html
"""
# 1
slovo = "Python"
n = 5

for i in range(n):
    n -=1
    print(n * "."+slovo)

# 2
slovo = "slon"
n = 4
for i in range(n + 1):
    print(i*(slovo+" "))

# 3
od = 5
do = 11
for n in range(od, do + 1):
    print(f"{n} {n**2} {n**3}")

# 4
x = -2
y = 3

for i in range(x, y+1):
    print(i, i**2, i**3)

# 5
zadaj_cislo = 1267650600228229401496703205376 # alebo 53124
sucet = 0
for i in str(zadaj_cislo):
    sucet += int(i)
print(f"pocet cifier: {len(str(zadaj_cislo))}")
print(f"ciferny sucet: {sucet}")

print("--------")
# 6
cislo = 31841624
for cifra in str(cislo):
    zvysok = cislo % 10
    cislo = cislo // 10
    print(cislo, zvysok)
print("----------")
# 7
slovo = "python"
n = -1
for i in slovo:
    n += 1
    print(str(n) + i, end="")

print() # <- nepodstatny print, len na "zkraslenie" outputu (nesuvisi s ulohou 7 ani 8)
# 8
n = 18 # alebo:  n = int(input("Zadaj cislo: "))
for i in range(n):
    print(i%7, end=" ")

# 9
n = 5
f1 = "modra"
f2 = "cervena"
for i in range(n + 1):
    print(f1)
    f1, f2 = f2, f1

# 10
"""
pocet = int(input("Zadaj pocet: "))
sucet = 0
for i in range(pocet):
    cislo = float(input(f"zadaj {i+1}. cislo: "))
    sucet += cislo
priemer = sucet/pocet
print(f"sucet: {sucet}")
print(f"priemer: {priemer}")
"""
# 11
"""
stlpce = int(input("Zadaj pocet stlpcov: "))
riadky = int(input("Zadaj pocet riadkov: "))

print("+"+"-"*stlpce+"+")
for i in range(riadky):
    print("|"+" "*stlpce +"|")
print("+" + "-"*stlpce + "+")
"""
# 12
slovo_1 = "aaa"
slovo_2 = "bbb"
slovo_3 = "ccc"

for i in slovo_1, slovo_2, slovo_3:
    for n in slovo_1, slovo_2, slovo_3:
        print(i + " " + n)
# experiment
"""
for i in slovo_1, slovo_2, slovo_3:
    for n in slovo_1, slovo_2, slovo_3:
        for j in slovo_1, slovo_2, slovo_3:
            print(i+" "+n+" "+j)
"""

# 13
n = 5 # alebo: n = int(input("zadaj n: "))
k = 1

for i in range(1, n+1):
        k = k*i 
print(f"{n}! = 1", end="")
for g in range(2, n+1):
        print("*"+str(g), end="")
print(" = " + str(k))

# 14
k = 1
for l in range(1, 11):
    n = l
    for i in range(1, n+1):
        k = k*i 
    print(f"{n}! = 1", end="")
    for g in range(2, n+1):
        print("*"+str(g), end="")
    print(" = " + str(k))

# 15
n = 6

for i in range(1, n+1):
    for j in range(n):
        print(i+j*n,"",end="")
    print()
# 16
n = 5
for i in reversed(range(1, n + 1)):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print()
# 17
n = 5

for i in range(n+1, 1, -1):
    print(" "*(n-i+1), end="")
    for j in range(1, i):
        print(j, end=" ")
    print("")



