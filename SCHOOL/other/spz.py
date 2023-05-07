#uloha 1
import random

spz_dk = 'DK'
spz_mt = 'MT'
spz_za = 'ZA'
county = [spz_dk, spz_mt, spz_za]

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'

for i in county:
    for j in range(3):
        for k in range(5):
            x = ''
            n = ''
            for l in range(3):
                x = x + str(random.choice(numbers))
            for m in range(2):
                n = n + str(random.choice(letters))    
            print(f'{i}-{x}{n} ', end='')
        print('')
    print('')
#uloha 2
n = int(input('Zadaj cislo n: '))

for i in range (n+1, 1, -1):
    print(' '*(n-i+1), end = '')
    for j in range(1,i):
        print (j, end =' ')
    print('')


# riesenie 2
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
    