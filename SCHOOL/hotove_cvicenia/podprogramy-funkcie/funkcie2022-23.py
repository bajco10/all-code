# zdroj prikladov: https://python.input.sk/z/05.html#

#1
def obdlznik(sirka, znak="*"):
    medzera = (sirka-2)*" "
    print(sirka*znak)
    print(f"{znak}{medzera}{znak}")
    print(sirka*znak)

#2
# moje riesenie
def riadok(n, text=""):
    if text == "":
        print(n*"*")
    else:
        filler = int((n-2-len(text))//2) * "*"
        print(f"{filler} {text} {filler}")

# spravne riesenie
def riadok(n, text=''):
    if text != '':
        text = ' ' + text + ' '
    pol1 = (n - len(text)) // 2
    pol2 = n - len(text) - pol1
    print('*' * pol1 + text + '*' * pol2)

#3
def priemer(a, b):
    return (a+b)/2

#4
def nsn(a, b):
    sucin = a*b
    while b != 0:
        a, b = b, a%b
    return sucin // a   # Súčin najmenšieho spoločného 
                        # násobku a najväčšieho spoločného deliteľa 
                        # čísel m a n je ich súčin.

#5
# moje riesenie
def fibonacci_medzi(od, do):
    a, b = 0, 1
    n = 100
    while n:
        a, b = b, a+b
        n -= 1
        if a > od and a < do:
            print(a, end=" ")
    print()
# lepsie riesenie
def fibonacci_medzi(od, do):
    a, b = 0, 1
    while a <= do:
        if a >= od:
            print(a, end=' ')
        a, b = b, a+b
    print()

#6 ??

#7
def vyhod_medzery(text):
    text2 = ""
    for i in text:
        if i != " ":
            text2 +=i
    return text2

#8
from random import randrange as rr
def hadanie(od, do):
    cislo = rr(od, do)
    print("Myslím si číslo, uhádni ho!")
    i=0
    while True:
        tip = int(input("tvoj tip: "))
        i+=1
        if tip < cislo:
            print("*** pridaj")
        elif tip > cislo:
            print("*** uber")
        elif tip == cislo:
            print(f"Uhádol si na {i}. pokus. Gratulujem.")
            break
        elif i >= 10:
            print(f"Neuhádol si ani na 10 pokusov. \n Myslel som si číslo {cislo}.")
            break

#9
"""import tkinter

def koleso(x, y, r=15, farba="blue"):
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=farba)

def doska(x, y, inc1=100, inc2=20, farba="red"):
    canvas.create_rectangle(x-inc1/2, y+inc2/8, x+inc1/2, y-inc2, fill=farba)
    # celkom odveci pomery -> +- to sedi
def maly_vozik(x, y):
    doska(x, y)
    koleso(x-30, y)
    koleso(x+30, y)

def velky_vozik(x, y):
    doska(x, y, 150, 40, 'green')
    koleso(x-35, y, 25, 'orange')
    koleso(x+35, y, 25, 'orange')

canvas = tkinter.Canvas()
canvas.pack()
"""
"""maly_vozik(200, 100)
velky_vozik(150, 200)
maly_vozik(300, 210)"""

#tkinter.mainloop()



#10
"""
import tkinter
from random import randrange as rr
import random
def kruhy(x, y):
    r = 50
    for i in range(10):
        canvas.create_oval(x-r, y-r, x+r, y+r, fill=f"#{rr(255**3):06x}")
        r-=5

canvas = tkinter.Canvas()
canvas.pack()
for i in range(10):
    kruhy(random.randint(50, 330), random.randint(50, 210))

tkinter.mainloop()
"""

#11
"""
import tkinter, random

def karticka(x, y, text):
    canvas.create_rectangle(x-50, y-20, x+50, y+20, fill="lightgrey")
    canvas.create_text(x, y, text=text, font="arial 14")

canvas = tkinter.Canvas()
canvas.pack()
for i in range(10):
    karticka(random.randint(50, 300), random.randint(50, 200), 'Python')
tkinter.mainloop()
"""
#12
"""
import tkinter, random
from random import randrange as rr
def dom(x, y, vel1, vel2):
    canvas.create_rectangle(x,y, x+vel1, y-vel1, fill=f"#{rr(255**3):06x}")
    canvas.create_polygon(x, y-vel1, x+vel1/2, y-vel2-vel1, x+vel1, y-vel1, fill=f"#{rr(255**3):06x}", width=1, outline="black")

canvas = tkinter.Canvas()
canvas.pack()

x, y = 10, 150
while x < 330:
    v = random.randint(20, 50)
    dom(x, y, v, random.randint(v//2, v))
    x += v

tkinter.mainloop()
"""
#13 - ???
"""
import tkinter, random, math

def vzd(x1, y1, x2, y2):
    return math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)

def kresli_bodku(x, y, farba):
        c.create_oval(x-4, y-4, x+4, y+4, fill=farba, width=0)

def farebne_bodky(r, x1, y1, x2, y2, x3, y3):
    
    for i in range(20000):
        x = random.randint(5, 380)
        y = random.randint(5, 260)
        v1 = vzd(x, y, x1, y1) < r
        v2 = vzd(x, y, x2, y2) < r
        v3 = vzd(x, y, x3, y3) < r
        if (v1 + v2 + v3) % 2 == 0:
            farba = 'navy'
        else:
            farba = 'yellow'
        c.create_oval(x-2, y-2, x+2, y+2, fill=farba, width=0)

c = tkinter.Canvas(width=400, height=400)
c.pack()

farebne_bodky(80, 120, 120, 180, 110, 160, 170)

tkinter.mainloop()
"""
#14a
"""import tkinter, random

c = tkinter.Canvas()
c.pack()
def nahodna_farba():
    return f"#{random.randrange(255**3):06x}"
def stv(riadok, stlpec, farba="white"):
    c.create_rectangle(30*stlpec, 30*riadok, 30*stlpec+30, 30*riadok+30, fill=farba, outline="")

for i in range(8):
    for j in range(12):
        if i == j:
            stv(i, j)
        else:
            stv(i, j, nahodna_farba())

tkinter.mainloop()"""

#14b
"""
import tkinter

c = tkinter.Canvas()
c.pack()

def rgb(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def stv(riadok, stlpec, farba="white"):
    c.create_rectangle(30*stlpec, 30*riadok, 30*stlpec+30, 30*riadok+30, fill=farba, outline="")

posun = 255//18
for i in range(8):
    for j in range(12):
        stv(i, j, farba=rgb(255, posun*i+posun*j, 0))

tkinter.mainloop()
"""

#15
"""
import tkinter, math, random

c=tkinter.Canvas()
c.pack()

def vektor(x, y, dlzka, uhol):
    xv = x + dlzka*math.cos(math.radians(uhol))
    yv = y + dlzka*math.sin(math.radians(uhol))
    c.create_line(x, y, xv, yv, arrow="last")

for i in range(10):
    vektor(random.randint(50, 300), random.randint(50, 200),
           random.randint(10, 80), random.randint(0, 359))
    
c.mainloop()
"""

#16

import tkinter, math

c = tkinter.Canvas()
c.pack()

def slnko(n, x, y):
    c.create_oval(x-40, y-40, x+40, y+40, fill="yellow", outline="")
    skok = 360//n
    for i in range(0, 360, skok):
        c.create_line(x, y,
                      x+70*math.cos(math.radians(i)),
                      y+70*math.sin(math.radians(i)),
                      width=6, fill="yellow")

slnko(10, 100, 80)
slnko(20, 250, 120)

c.mainloop()

#17
"""
import tkinter

def vybodkuj_usecku(x1, y1, x2, y2, n):
    dx = (x2 - x1) / (n-1)
    dy = (y2 - y1) / (n-1)
    for i in range(n):
        x = x1 + i*dx
        y = y1 + i*dy
        canvas.create_oval(x-3, y-3, x+3, y+3, width=0, fill='blue')

canvas = tkinter.Canvas(bg='white')
canvas.pack()

canvas.create_line(100, 80, 280, 120, fill='lightgray', width=11)
vybodkuj_usecku(100, 80, 280, 120, 20)
canvas.create_line(280, 120, 150, 200, fill='lightgray', width=11)
vybodkuj_usecku(280, 120, 150, 200, 10)
canvas.create_line(150, 200, 100, 80, fill='lightgray', width=11)
vybodkuj_usecku(150, 200, 100, 80, 8)

tkinter.mainloop()
"""
#18
"""
import tkinter, math
c = tkinter.Canvas()
c.pack()

def n_uholnik(n, x0, y0, r):
    m = int(360/n)
    for i in range(0, 360, m):
        x = x0 + r * math.cos(math.radians(i))
        y = y0 + r * math.sin(math.radians(i))

        x1 = x0 + r * math.cos(math.radians(i+m))
        y1 = y0 + r * math.sin(math.radians(i+m))
        c.create_line(x, y, x1, y1)

n_uholnik(3, 50, 50, 45)
n_uholnik(4, 150, 50, 45)
n_uholnik(5, 250, 50, 45)

n_uholnik(6, 50, 150, 45)
n_uholnik(7, 150, 150, 45)
n_uholnik(8, 250, 150, 45)
c.mainloop()
"""
#19
"""
import tkinter
from math import sin, cos, radians

x0, y0 = 190, 130

def n_hviezda(n, x0, y0, r, k=2):
    x1, y1 = x0 + r, y0
    for i in range(1, n+1):
        uhol = k*360/n * i
        x2 = x0 + r * cos(radians(uhol))
        y2 = y0 + r * sin(radians(uhol))
        canvas.create_line(x1, y1, x2, y2)
        x1, y1 = x2, y2

canvas = tkinter.Canvas()
canvas.pack()

n_hviezda(5, 50, 50, 45)
n_hviezda(7, 150, 50, 45)
n_hviezda(7, 250, 50, 45, 3)

n_hviezda(9, 50, 150, 45)
n_hviezda(9, 150, 150, 45, 4)
n_hviezda(11, 250, 150, 45, 4)

tkinter.mainloop()
"""
# 20
"""
import tkinter, math

c=tkinter.Canvas()
c.pack()
def n_spirala(n, x0, y0, r):
    r1 = 5
    uhol = 1
    posun = 360/n
    while r1<r:
       x1 = x0 + r1*math.cos(math.radians(uhol)) 
       y1 = y0 + r1*math.sin(math.radians(uhol))

       x2 = x0 + (r1+2) *math.cos(math.radians(uhol+posun)) 
       y2 = y0 + (r1+2) *math.sin(math.radians(uhol+posun))

       c.create_line(x1, y1, x2, y2)
       uhol+=posun
       r1+=2

n_spirala(3, 50, 50, 45)
n_spirala(4, 150, 50, 45)
n_spirala(5, 250, 50, 45)

n_spirala(6, 50, 150, 45)
n_spirala(7, 150, 150, 45)
n_spirala(8, 250, 150, 45)
c.mainloop()
"""
#21
"""
import tkinter, math

c = tkinter.Canvas()
c.pack()

def horna(x0, y0, r):
    for i in range(180, 360, 10):
        x1 = x0 + r*math.cos(math.radians(i))
        y1 = y0 + r*math.sin(math.radians(i))
        
        x2 = x0 + r*math.cos(math.radians(i+10))
        y2 = y0 + r*math.sin(math.radians(i+10))

        c.create_line(x1, y1, x2, y2)

def dolna(x0, y0, r):
    for i in range(0, 180, 10):
        x1 = x0 + r*math.cos(math.radians(i))
        y1 = y0 + r*math.sin(math.radians(i))
        
        x2 = x0 + r*math.cos(math.radians(i+10))
        y2 = y0 + r*math.sin(math.radians(i+10))
        
        c.create_line(x1, y1, x2, y2)

horna(30, 100, 30)
dolna(90, 100, 30)
horna(150, 100, 30)
dolna(210, 100, 30)
horna(270, 100, 30)
dolna(330, 100, 30)
for i in range(6):
    horna(30+60*i, 200, 30)
c.mainloop()
"""
#22
"""
import tkinter, math, time

def rucicka(uhol, dlzka, hrubka, farba):
    x = 190 + dlzka*math.cos(math.radians(uhol))
    y = 130 + dlzka*math.sin(math.radians(uhol))
    c.create_line(190, 130, x, y, width=hrubka, fill=farba, arrow="last")

def hodinky(hod, min, sek):
    u_hod = 360/12
    u_min = 360/60
    u_sek = 360/60
    c.create_oval(90, 30, 290, 230, fill="white")
    rucicka(-90 + hod*u_hod, 60, 10, "gray")
    rucicka(-90 + min*u_min, 70, 6, "black")
    rucicka(-90 + sek*u_sek, 80, 2, "red")
c = tkinter.Canvas()
c.pack()
hodinky(12, 35, 30)


while True:
    c.delete('all')
    h, m, s = time.localtime()[3:6]
    hodinky(h, m, s)
    c.update()
    c.after(1000)

"""
# c.mainloop()
