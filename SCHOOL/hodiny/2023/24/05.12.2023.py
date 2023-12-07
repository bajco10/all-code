'''import random, time

pole = [random.randint(2, 20) for x in range(30)]
# pole = [20, 11, 18, 11, 13, 9, 6, 10, 15, 14, 1, 18, 4, 13, 5]
# pole2 = [1, 5, 6, 12]
rozdiel = float("inf") # alebo sum(pole) -> vždy to bude menšie

start = time.time()



for i in range(1, (2**len(pole)//2)):
    """// 2 pretoze sa mi kombinacie prvkov 
    od polky zas opakuju a zacinam 
    od jedna pretoze v prvom cykle natrepem 
    vsetky prvky do jedneho zoznamu"""
    # binar = bin(i)[2:]
    # binar = "0"*(len(pole)-len(binar))+binar
    delenie = [[], []]
    binar = f"{i:0{len(pole)}b}"
    for j, znak in enumerate(binar):
        delenie[int(znak)].append(pole[j])

    if abs(sum(delenie[0]) - sum(delenie[1])) <= rozdiel:
        rozdiel = abs(sum(delenie[0]) - sum(delenie[1]))
        ake = [delenie[0], delenie[1]]
        if rozdiel == 0:
            break

print(ake[1], ake[0])
print(sum(ake[1]), sum(ake[0]))
print(time.time()-start)'''
'''import random, time

pole = [random.randint(1, 30) for x in range(10)]
# pole = [20, 11, 18, 11, 13, 9, 6, 10, 15, 14, 1, 18, 4, 13, 5]
# pole2 = [1, 5, 6, 12]
rozdiel = float("inf") # alebo sum(pole) -> vždy to bude menšie

start = time.time()

def konv_z_do(vyraz, z_sus, do_sus):
    decimal = 0
    power = 0
    result = ''
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for digit in reversed(vyraz):
        decimal += digits.index(digit.upper()) * (z_sus ** power)
        power += 1
    while decimal > 0:
        remainder = decimal % do_sus
        result = digits[remainder] + result
        decimal = decimal // do_sus
    return result


def rozdel(pole, pocet):
    rozdiel = float("inf")
    for i in range(1, (2**len(pole))):
        delenie = [[] for i in range(pocet)]
        # print(delenie)
        cislo = f"{konv_z_do(str(i), 10, pocet):0{len(pole)}}"
        # print(cislo)
        # f"{i:0{len(pole)}b}"
        for j, znak in enumerate(cislo):
            delenie[int(znak)].append(pole[j])
            je_dobry = True
            for i in range(pocet-1):
                if abs(sum(delenie[i])-sum(delenie[i+1])) > rozdiel:
                    je_dobry = False
            if je_dobry:
                temp_rozdiel = abs(sum(delenie[0]) - sum(delenie[1]))
                for i in range(pocet-1):
                    x = abs(sum(delenie[i]) - sum(delenie[i+1])) 
                    if x < temp_rozdiel:
                        temp_rozdiel = x
                rozdiel = temp_rozdiel
                ake = delenie
                """if rozdiel == 0:
                    break"""

    for i in ake:
        print(i, sum(i))
    # print(sum(ake[1]), sum(ake[0]))
    print(time.time()-start)

rozdel(pole, 3)'''

import random
import time

pole = [random.randint(1, 30) for x in range(10)]
rozdiel = float("inf")
start = time.time()

def konv_z_do(vyraz, z_sus, do_sus):
    decimal = 0
    power = 0
    result = ''
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for digit in reversed(vyraz):
        decimal += digits.index(digit.upper()) * (z_sus ** power)
        power += 1
    while decimal > 0:
        remainder = decimal % do_sus
        result = digits[remainder] + result
        decimal = decimal // do_sus
    return result

def rozdel(pole, pocet):
    global rozdiel
    for i in range(1, 2**(len(pole))):  # Changed the loop range
        delenie = [[] for _ in range(pocet)]
        cislo = f"{konv_z_do(str(i), 10, pocet):0{len(pole)}}"
        for j, znak in enumerate(cislo):
            delenie[int(znak)].append(pole[j])
        
        # Check if the division is valid
        temp_rozdiel = max(abs(sum(delenie[i]) - sum(delenie[i+1])) for i in range(pocet-1))


        if temp_rozdiel < rozdiel:
            rozdiel = temp_rozdiel
            ake = delenie
            if rozdiel == 0:
                break

    for i in ake:
        print(i, sum(i))
    print(time.time() - start)

rozdel(pole, 2)



