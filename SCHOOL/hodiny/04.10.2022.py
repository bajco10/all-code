

slovo = "janko"
n = 0
for i in slovo:
    n +=1
    print(str(n) + i, end="")


n = int(input("Zadaj cislo: "))
for i in range(n):
    print(i%7, end=" ")

# riesenie z hodiny
n = 6
f1 = "modra"
f2 = "cervena"
for i in range(n):
    print(f1)
    f1, f2 = f2, f1
# riesenie s if-statements
for i in range(n):
    if i%2:
        print("1modra")
    else:
        print("2cervena")

# riesenie na hodine
pocet = int(input("Zadaj pocet: "))
sucet = 0
for i in range(pocet):
    cislo = float(input(f"zadaj {i+1}. cislo: "))
    sucet += cislo
priemer = sucet/pocet
print(f"sucet: {sucet}")
print(f"priemer: {priemer}")

