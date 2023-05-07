#zdroj uhol = https://python.input.sk/z/06.html

#2
"""
def sucet(retazec):
    diel = retazec.find("+")
    a = int(retazec[:diel])
    b = int(retazec[diel:])
    return a+b
x = sucet("12437892+4897239842")
print(x)
"""
#3
"""
def sucet(retazec):
    m=0
    cisla = retazec.split("+")
    for i in cisla:
        m += int(i)
    return m
x = sucet("1+2+3+4")
print(x)
"""
#4
"""
def postupnost(start, koniec, krok=1):
    m = ""
    for i in range(start, koniec, krok):
        m+=str(i) + " "
    return m
p = postupnost(13, 5, -2)
print(p)
"""
#5



ret = 'Anicka dusicka, kde si bola'
print(ret)
novy = ret[:10] + "\n" + ret[10:20] + "\n" + ret[20:]
print(novy)