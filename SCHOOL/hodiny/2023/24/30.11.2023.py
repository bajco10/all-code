# 5
mena = ["Igor","Filip", "Jojo", "Cyril", "Adam", "Anna", "Jamal", "Frederika", "Margita"]
import random
vysky = {}
for i in mena:
    vysky[i] = random.randrange(140, 202)
# 6
for kluc, hodnota in sorted(vysky.items()):
    print(kluc, hodnota)
# print()
# 7
'''for kluc, hodnota in sorted(vysky.items(), key=lambda x:x[1], reverse=True):
    print(kluc, hodnota)'''

# 8
def priemer(vysky):
    return sum(vysky.values())/len(vysky)

# print(priemer(vysky))

#9
'''for meno, vyska in vysky.items():
    if vyska < priemer(vysky):
        print(meno, vyska, "podpriemer")
    elif vyska == priemer(vysky):
        print(meno, vyska, "priemer")
    else:
        print(meno, vyska, "nadpriemer")'''

# 10
def len_od_do(vysky, od, do):
    nove_vysky = {}
    for meno, vyska in vysky.items():
        if od < vyska and do > vyska:
            nove_vysky[meno] = vyska
    return nove_vysky

# print(len_od_do(vysky, 150, 180))
        


