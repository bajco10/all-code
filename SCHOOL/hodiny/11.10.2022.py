"""
stlpce = int(input("Zadaj pocet stlpcov: "))
riadky = int(input("Zadaj pocet riadkov: "))

print("+"+"-"*stlpce+"+")
for i in range(riadky):
    print("|"+" "*stlpce +"|")
print("+" + "-"*stlpce + "+")
"""
"""
slovo_1 = "aaa"
slovo_2 = "bbb"
slovo_3 = "ccc"

for i in slovo_1, slovo_2, slovo_3:
    for n in slovo_1, slovo_2, slovo_3:
        print(i + " " + n)

for i in slovo_1, slovo_2, slovo_3:
    for n in slovo_1, slovo_2, slovo_3:
        for j in slovo_1, slovo_2, slovo_3:
            print(i+" "+n+" "+j)
"""

"""
n = int(input("Zadaj n: "))
k = 1

for i in range(1, n+1):
    k = k*i 
print(f"{n}! = 1", end="")
for g in range(2, n+1):
    print("*"+str(g), end="")
print(" = " + str(k))
"""
k = 1
for l in range(1, 11):
    n = l
    for i in range(1, n+1):
        k = k*i 
    print(f"{n}! = 1", end="")
    for g in range(2, n+1):
        print("*"+str(g), end="")
    print(" = " + str(k))

"""
import random
for priklad in range(10):
    cislo1 = random.randrange(1, 30)
    cislo2 = random.randrange(1, 30)
    print(f"{cislo1} + {cislo2} = {cislo1 + cislo2}")
"""