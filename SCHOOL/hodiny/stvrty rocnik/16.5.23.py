"""def over(priklad):
    vysledok = priklad[(priklad.find("="))+1:]
    zadanie = priklad[:(priklad.find("="))]
    stringy = zadanie.split("+")
    cisla = []
    for i in stringy:
        j = int(i)
        cisla.append(j)
    print(cisla)
    if sum(cisla) == int(vysledok):
        return True
    return False
print(over("1+1=2"))
print(over("1+1+12+22+22333=2"))
print(over("1=2"))"""

# dost dolezity program na test!!!
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


print(konv_z_do("63", 16, 10))
print(konv_z_do("01100011", 2, 10))
print(konv_z_do("01100011", 2, 16))
print(konv_z_do("01100011", 2, 30))
# print(int("01100011", 36))



