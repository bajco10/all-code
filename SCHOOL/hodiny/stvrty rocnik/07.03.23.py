# najvacsi spolocny delitel - neefektivny sposob
def nsd(a, b):
    for i in range(1, b+1):
        if a%i==0 and b%i==0:
            max = i
    print(f"nsd({a}, {b})={max}")

    for i in range(b, 0, -1):
        if a%i==0 and b%i==0:
            print(f"nsd({a}, {b})={max}")
            break
    a1, b1 = a, b
    # euklidov algoritmus
    while a%b!=0:
        zvysok = a%b
        a, b = b, zvysok
    print(f"nsd({a1}, {b1})={b}")

nsd(3842890, 8434)

# pocet delitelov
def pocet_delitelov(cislo):
    pocet = 0
    for i in range(1, cislo+1):
        if cislo%i==0:
            pocet +=1
    return pocet

delit = pocet_delitelov(6)
print(delit)

# je prvocislo
def je_provcislo(cislo):
    if pocet_delitelov(cislo)==2:
        return True
    return False

print(je_provcislo(26))

# 8 - vsetky prvocisla od-do
def vsetky_prvocisla(od, do):
    for i in range(od, do+1):
        if je_provcislo(i)==True:
            print(i, end=" ")

print(vsetky_prvocisla(5, 45))

# 9 - sucet mocnin
def sucet_mocnin(n):
    sucet = 0
    for i in range(0, n):
        sucet += 2**i
        print(i, sucet)

n = 7
sucet_mocnin(n)

# 11 - kocka
from random import randrange as rr

def kocka():
    return rr(1, 6)

for i in range(20):
    if i == 0:
        cislo = kocka()
    cislo2 = kocka()
    if cislo != cislo2:
        print(cislo2, end=" ")
    else:
        print(cislo2, end="*")
    cislo = cislo2
    