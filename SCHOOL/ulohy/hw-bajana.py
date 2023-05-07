import random
import string

spz_dk = "DK"
spz_mt = "MT"
spz_za = "ZA"

for i in range(3):
    for n in range(5):
        letters_on_end = string.ascii_uppercase
        cislo = random.randrange(100, 999)
        x = random.choice(letters_on_end)
        y = random.choice(letters_on_end)
        print(f"{spz_dk}-{cislo}{x}{y}", end=" ")
    print()
print()
for i in range(3):  
    for n in range(5):
        letters_on_end = string.ascii_uppercase
        cislo = random.randrange(100, 999)
        x = random.choice(letters_on_end)
        y = random.choice(letters_on_end)
        print(f"{spz_mt}-{cislo}{x}{y}", end=" ")
    print()
print()
for i in range(3):
    for n in range(5):
        letters_on_end = string.ascii_uppercase
        cislo = random.randrange(100, 999)
        x = random.choice(letters_on_end)
        y = random.choice(letters_on_end)
        print(f"{spz_za}-{cislo}{x}{y}", end=" ")
    print()
    