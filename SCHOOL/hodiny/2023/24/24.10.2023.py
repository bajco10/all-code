'''x = 21564
# zistujeme ci je cislo prvocislo
def is_prvo(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True
#rozklad na prvocinitele
def rozloz(x):
    y = int(x)
    rozklad = []
    pocet_c = 0
    while y>1:
        for i in range(2, y+1):
            if is_prvo(i) and y%i==0:
                rozklad.append(str(i))
                pocet_c+=1
                y = y//i
                pass
        rozklad.sort()
    return ("*".join(rozklad))
def rozloz_kompakt(x):
    y = int(x)
    rozklad = []
    vysledok = []
    while y>1:
        for i in range(2, y+1):
            if is_prvo(i) and y%i==0:
                rozklad.append(str(i))
                y = y//i
                pass
        rozklad.sort()
    boli = []
    for i in rozklad:
        if i not in boli:
            if rozklad.count(i) > 1:
                vysledok.append(str(f"{i}^{rozklad.count(i)}"))
                boli.append(i)
            else:
                vysledok.append(str(i))
    return "*".join(vysledok)


cisla = []
# ziskavame cisla
with open(r"/home/tomas/Desktop/all-code/SCHOOL/hodiny/2023/24/cisla.txt", "r") as subor:
    for line in subor:
        line = line.strip()
        cisla.append(int(line))
    cisla.sort()

# piseme do noveho suboru
with open("/home/tomas/Desktop/all-code/SCHOOL/hodiny/2023/24/cisla1.txt", "w") as subor:
    for i in cisla:
        print(f"{i} = {rozloz_kompakt(i)}", file=subor)'''

#NSD viacerych cisel
# najdem najmänšie číslo v riadku, nasledne prechádzam cez range od tohto cisla po nula
# ak su vsetky cisla delitelne tymto cislom i z rangu, bude pocet rovny poctu cisel (dane cislo deli kazde z nich)
# vypisem v pozadovanom formate
'''f = open("/home/tomas/Desktop/all-code/SCHOOL/hodiny/2023/24/nsd_cisla.txt")
for riadok in f:
    cisla = [int(x) for x in riadok.strip().split()]
    minimum = min(cisla)
    for i in range(minimum, 0, -1):
        pocet = 0
        for cislo in cisla:
            if cislo%i == 0:
                pocet+=1
            else:
                break
        
        if pocet == len(cisla):
            print(f"NSD({riadok.strip().replace(' ', ',')})={i}")
            break
f.close()'''

# cez Euklidov algoritmus -> ovela rychlejsie
def nsd(a, b):
    while a%b!=0:
        a, b = b, a%b
    return b

f = open("/home/tomas/Desktop/all-code/SCHOOL/hodiny/2023/24/nsd_cisla.txt")
for riadok in f:
    cisla = [int(x) for x in riadok.strip().split()]
    minimum = min(cisla)
    while len(cisla) != 1:
        cisla = [nsd(cisla[0], cisla[1])] ; cisla[2:]

        print(f"NSD({riadok.strip().replace(' ', ',')})={cisla[0]}")
        

print(nsd(18, 93))