from itertools import combinations

suma1, suma2 = 5341.88, 12019.56
test_suma = 6573.00+7369.24-132.75

cisla_faktur, faktury, cisla_dobropisov, dobropisy = [], [], [], []
uz_dobropisy = False

with open(r"vacsie_projekty\hladanie_faktur\faktury.txt", encoding="utf8") as subor:
    for riadok in subor:
        riadok = riadok.strip()
        if riadok == "":
            uz_dobropisy=True
        if uz_dobropisy==False and riadok!="":
            cislo, suma = riadok.split(" ")
            cisla_faktur.append(cislo)
            faktury.append(float(suma))
        elif uz_dobropisy==True and riadok!="":
            cislo,suma = riadok.split(" ")
            cisla_dobropisov.append(cislo)
            dobropisy.append(float(suma))
            
# print(cisla_dobropisov, dobropisy)

for r in range(1, len(faktury)+1):
    for combo in combinations(faktury, r):
        if sum(combo) == test_suma:
            print(combo)
            break
        for j in dobropisy:
            if sum(combo) - j== test_suma:
                print(combo)

        
