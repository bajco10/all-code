# zdroj prikladov: https://input.sk/python2020/06.html#specifikacia-formatu

#2
"""
def sucet(retazec):
    return int(retazec[0:(retazec.find("+"))]) + int(retazec[retazec.find("+"):len(retazec)+1])
print(sucet("987654321+99999"))
"""
#3
"""
def sucet(retazec):
    list = []
    retazec = retazec.split("+")
    for i in retazec:
        list.append(int(i))
    return sum(list)
print(sucet("12+9"))
"""
#4
"""
def postupnost(start, koniec):
    retazec = ""
    for i in range(start, koniec):
        retazec += f" {i}"
    return retazec
print(postupnost(5, 13))
"""
#5
"""
def rozsekaj(text, sirka):
    m = 1
    novy_text = ""
    for i in text:
        if m%sirka==0:
            i = i+"\n"
        novy_text+=i
        m+=1
    return novy_text
print(rozsekaj("Anicka dusicka, kde si bola", 10))
"""
#6
"""
def stvorec(n, znak):
    text = ""
    text += n*znak
    for i in range(0, int(n-2)):
        text += '\n' + znak + int(n-2)*" " + znak
    text += '\n' + n*znak
    return text
r = stvorec(5, "#")
print(r)
q = stvorec(8, "*")
print(q)
t = stvorec(12, chr(3))
print(t)
"""
#7
"""
def vyhod_duplikaty(text):
    text1 = ""
    j = ""
    for i in text:
        if i != j:
            text1+=i
        j = i
    return text1
x = vyhod_duplikaty("Braatisssllavaaaaa")
print(x)
"""
#8 ???


#9
"""
def prevrat(retazec):
    return retazec[::-1]
x = prevrat('tseb eht si nohtyP')
print(x)
"""
#10
"""
def male(retazec, i):
    text = ""
    m = 0
    for j in retazec:
        if m == i:
            text += j.lower()
        else:
            text += j
        m += 1
    return text
r = male("PYTHON", 3)
print(r)
def velke(retazec, i):
    text = ""
    m = 0
    for j in retazec:
        if m == i:
            text += j.upper()
        else:
            text += j
        m += 1
    return text
r = velke("python", 5)
print(r)
"""
#11  ?
"""
def riadky(retazec):
    for i in retazec:
        if i == "\n":
            print("hm")

print(riadky('prvy riadok\n\ntreti je posledny'))
"""




#12
"""
def posun_znak(znak, posun):
    abc = "abcdefghijklmnopqrstuvwxyz"
    m = int(abc.find(znak))
    return abc[m+int(posun)]
print(posun_znak("c", 4))
print(posun_znak("g", -4))
"""
#13 - incomplete
"""
def zakoduj(text, posun):
    text2 = ""
    abc = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    for i in text:
        m = int(abc.find(i))
        text2 += abc[m+int(posun)]
    return text2

x = zakoduj("python", 10)
print(x)
x = zakoduj(x, -10)
print(x)
x = "python"
x = zakoduj(x, 16)
print(x)
x = zakoduj(x, -16)
print(x)
"""
#14
"""
def je_palindrom(retazec):
    retazec = retazec.lower()
    retazec = retazec.replace(" ", "")
    opak = retazec[::-1]
    return opak == retazec
print(je_palindrom("python"))
print(je_palindrom("tahat"))
print(je_palindrom("Jelenovi Pivo Nelej")) 
"""
#15 ???
#16
"""
def usporiadaj(h1, h2, h3):
    list = []
    output = ""
    for i in h1, h2, h3:
        list.append(i)
    list.sort()
    for j in list:
        output += " "+ j        #?? da sa spravit elegantnejsie
    return output
x = usporiadaj("python", "pytliak", "pytagoras")
print(x)
"""
#17
"""
import random
samohlasky = "aeiouy"
spoluhlasky = "dtnlcjbmprsvzfl"
def nazov(n):
    x = random.choice(samohlasky)
    return f"{x.capitalize()}{n*random.choice(spoluhlasky)}{x}"
for i in range(5):
    print(nazov(2))
    print(nazov(3))
"""
#18
"""
import tkinter
import random
c = tkinter.Canvas()
c.pack()
x, y = 50, 150
def rgb_generator():
    return f"#{random.randint(1, 255**3):06x}"
    
for i in 0x2654, 0x2655, 0x2656, 0x2657, 0x2658, 0x2659:
    c.create_text(x, y, text=chr(i), fill=rgb_generator(), font="arial 50")
    x += 60
tkinter.mainloop()
"""
#19
"""
import tkinter
c = tkinter.Canvas()
c.pack()
def stvorce(vel, retazec):
    x, y = 50, 100
    list = retazec.split(" ")
    for i in list:
        c.create_rectangle(x-vel/2, y-vel/2, x+vel/2, y+vel/2, fill=i)
        x += vel + 3
stvorce(40, 'red blue purple red gold')
tkinter.mainloop()
"""
#20 - dorobit dako
"""
import tkinter
sirka = 450
c = tkinter.Canvas(width=sirka)
c.pack()
def stvorce(retazec):
    list = retazec.split(" ")
    velkosti = list[::2]
    for i in list:
        if i in velkosti:
            list.remove(i)
    farby = list
    x, y = 5, 200
    m = 0
    sirka2 = 0
    ano = True
    while ano:
        m = 0
        for j in velkosti:
            c.create_rectangle(x, y, x+int(j), y-int(j), fill=farby[m])
            x += int(j) + 5
            m+=1
            if sirka2 + int(j) >= sirka:
                ano = False
            sirka2 += int(j)
stvorce("40 red 20 blue 60 purple 40 red 30 gold")
tkinter.mainloop()
"""
#21
"""
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
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
kresli('ssvvjjzzvvssvvjjzzzzzzssvvjjzzvvjjssvvjjzzssssssvvjjzz')
tkinter.mainloop()
"""
#22

