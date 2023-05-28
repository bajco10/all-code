# 2
"""def sucet(retazec):
    p = retazec.find("+")
    return int(retazec[:p]) + int(retazec[p:])
print(sucet("12+9"))"""
#3

"""def sucet(retazec):
    l = retazec.split("+")
    for i in range(len(l)): l[i] = int(l[i])
    return sum(l)
print(sucet("1+1+2+3+999+6524+5656"))"""

#4

"""def postupnost(start, koniec, krok=1):
    x = int(koniec) - int(start)
    retazec = ""
    for i in range(0, x-1, krok):
        i+=int(start)
        retazec += str(i) + " "
    retazec+=str(koniec-1)
    return retazec
print(postupnost(5, 13))
print(postupnost(13, 5, -2))"""
#5
"""def rozsekaj(text, sirka):
    for i in range(0, len(text), sirka+1):
        text = text[:i] + "\n" + text[i:]
    return text
print(rozsekaj('Anicka dusicka, kde si bola', 10))"""
#6

"""def stvorec(n, znak):
    return n*znak+"\n"+(n-2)*(znak+(n-2)*" "+znak +"\n")+n*znak

print(stvorec(5, "#"))"""

#7
"""def vyhod_duplikaty(retazec):
    res = ""
    # return res
    for i in range(len(retazec)-1):
        if retazec[i] != retazec[i+1]:
            res += retazec[i]
    res += retazec[-1]
    return res
print(vyhod_duplikaty("Braatissssllaavaaaaa"))
print(vyhod_duplikaty("Zvvvoleeeennnnnnnn"))"""
#8
"""def ozatvorkuj(retazec, podretazec):
    return retazec.replace(podretazec, f'({podretazec})')

print(ozatvorkuj('prospešné programovanie v prologu', 'pro'))"""
#9
"""def prevrat(retazec):
    res = ""
    for i in range(len(retazec)-1, -1, -1):
        res += retazec[i]
    return res
print(prevrat('tseb eht si nohtyP'))"""
#10
"""def male(retazec, i):
    retazec = retazec.replace(retazec[i], retazec[i].lower())
    return retazec
def velke(retazec, i):
    retazec = retazec.replace(retazec[i], retazec[i].upper())
    return retazec

print(male('PYTHON', 3))
print(velke('python', 5))"""
#11 - s pouzitim listu a enumerate -> nechce sa mi to robit cisto cez str :)
"""def riadky(retazec):
    riadky = retazec.split("\n")
    for i, riadok in enumerate(riadky, start=1):
        print(f"{i}. {riadok}")
(riadky('prvy riadok\n\ntreti je posledny'))
"""
#12
"""def posun_znak(znak, posun):
    abc = "abcdefghijklmnopqrstuvwxyz"
    if znak not in abc:
        return znak
    return abc[abc.find(znak)+posun]
print(posun_znak("c", 4))
print(posun_znak("g", -4))
print(posun_znak("X", 10))"""
#13
# omylom spravil aj pre velke pismena
"""def zakoduj(text, posun):
    res = ""
    abc_mal = "abcdefghijklmnopqrstuvwxyz"
    abc_vel = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in text:
        if i in abc_mal:
            if abc_mal.find(i)+posun >= len(abc_mal):
                abc_mal = 2*abc_mal
            res+=abc_mal[abc_mal.find(i)+posun]
        elif i in abc_vel:
            if abc_vel.find(i)+posun >= len(abc_vel):
                abc_vel = 2*abc_vel
            res+=abc_vel[abc_vel.find(i)+posun]
    return res"""
# spravne riesenie
"""def zakoduj(text, posun):
    res = ""
    abc = "abcdefghijklmnopqrstuvwxyz"
    for i in text:
        if i in abc:
            if abc.find(i)+posun > len(abc):
                abc = 2*abc
            res+=abc[abc.find(i)+posun]
        else:
            res+=i
    return res
print(zakoduj('pyThon', 10))"""
#14
"""def je_palindrom(retazec):
    retazec = retazec.lower()
    retazec = retazec.replace(" ", "")
    if retazec == retazec[::-1]:
        return True
    return False
print(je_palindrom("Python"))
print(je_palindrom('Jelenovi Pivo Nelej'))"""
#15
"""def pocet(retazec, podretazec):
    c = 0
    dr = len(retazec)
    dp = len(podretazec)
    for i in range(dr-dp+1):
        if retazec[i:i+dp] == podretazec:
            c+=1
    return c
print(pocet('mama ma emu a ema ma mamu', 'ma '))
print(pocet('mama ma emu a ema ma mamu', 'am'))"""
#16
"""def usporiadaj(h1, h2, h3):
    l = []
    l.append(h1)
    l.append(h2)
    l.append(h3)
    l.sort()
    return " ".join(str(i) for i in l)
print(usporiadaj(345, 123, 234))"""
#17
"""import random
def nazov(n):
    sam = "aeiouy"
    spol="bcdfghjklmnpqrstvwxz"
    x = random.choice(sam)
    y = random.choice(spol)
    return x.upper()+y*n+x
for i in range(5):
        print(nazov(2))
        print(nazov(3))"""
#18
"""import tkinter, random
c = tkinter.Canvas()
c.pack()
print(chr(0x2654))
x, y = 60, 150
for i in range(6):
    c.create_text(x, y, text=chr(0x2654+i), font="arial 50", fill=f"#{random.randrange(255**3):06x}")
    x+=50
c.mainloop()"""
#19 -> bolo na ulohu
#20
"""import tkinter
c = tkinter.Canvas(width=450)
c.pack()
def stvorce(retazec):
    x, y = 20, 200
    l = retazec.split(" ")
    print(l)
    t = True
    while t:
        for i in range(0, len(l)-1, 2):
            if x+int(l[i])>= 450:
                t=False
                break
            c.create_rectangle(x, y, x+int(l[i]), y-int(l[i]), fill=f"{l[int(i)+1]}")
            x+=int(l[i]) + 5
stvorce('40 red 20 blue 60 purple 40 red 30 gold')
c.mainloop()"""
#21
"""import tkinter

def kresli(retazec):
    x, y = 100, 100
    for znak in retazec:
        x1, y1 = x, y
        if znak == 's':
            y1 -= 10
        elif znak == 'v':
            x1 += 10
        elif znak == 'j':
            y1 += 10
        elif znak == 'z':
            x1 -= 10
        else:
            print('nerozumiem "' + znak + '"')
            return
        canvas.create_line(x, y, x1, y1)
        x, y = x1, y1

canvas = tkinter.Canvas()
canvas.pack()

kresli('ssvvjjzzjjvvssvvsszzsszzjjzzjjvv')
canvas.mainloop()"""
#22
import tkinter

c = tkinter.Canvas()
c.pack()

def kresli(retazec):
    kreslenie = True
    x, y = 100, 100
    for znak in retazec:
        x1, y1 = x, y
        if znak == "h":
            kreslenie = False
        elif znak == "d":
            kreslenie = True
        if znak in "0123456789":
            pocet = int(znak)
        if znak == "s":
            y1-=10*pocet
        elif znak == "v":
            x1+=10*pocet
        elif znak == "j":
            y1+=10*pocet
        elif znak == "z":
            x1-=10*pocet
        if kreslenie:
            c.create_line(x, y, x1, y1)
        x, y = x1, y1

kresli('4v4j4z4sh5vd'*5)
c.mainloop()

