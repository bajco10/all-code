# zdroj https://input.sk/python2020/05.html

#1
"""
def obdlznik(sirka, znak="*"):
    medzera = (sirka-2)*" "
    print(sirka*znak)
    print(f"{znak}{medzera}{znak}")
    print(sirka*znak)

obdlznik(30, znak="#")
obdlznik(6)
obdlznik(19, "O")
"""
#2
"""
sir = 40
def riadok(n, text=""):
    if text=="":
        print(n*"*")
    elif len(text)%2==0:
        z = int((n-len(text))/2 -1)
        print(z*"*", end=" ")
        print(text, end=" ")
        print(z*"*")
    else:
        z = int((n-len(text))/2)
        q = z-1
        print(z*"*", end=" ")
        print(text, end=" ")
        print(q*"*")
riadok(sir)
riadok(sir, 'Ján Botto')
riadok(sir, 'Žltá ľalija')
riadok(sir, '-')
riadok(sir, 'Stojí stojí mohyla')
riadok(sir, 'Na mohyle zlá chvíľa')
riadok(sir, 'na mohyle tŕnie chrastie')
riadok(sir, 'a v tom tŕní chrastí rastie')
riadok(sir)
"""
#3
"""
def priemer(a, b):
    return (a+b)/2
print(priemer(3.14, 31.4))
print(priemer(1, 4))
"""
#4 ???

#5 ??
#6 ?
#7
"""
def vyhod_medzery(text):
    novy_text = ""
    for i in text:
        if i != " ":
            novy_text+=i
    return novy_text
"""
#8
"""
import random
def hadanie(od, do):
    print("Mýslím si cislo, uhadni ho!")
    pokus = 1
    cislo = random.randint(od, do)
    while pokus<=10:
        n = int(input("tvoj tip: "))
        if n < cislo:
            print("*** pridaj")
        elif n > cislo:
            print("*** uber")
        else:
            print(f"uhadol si na {pokus}. pokus. Gratulujem")
            pass
        pokus += 1
    print("Neuhadol si ani na 10 pokusov.")
hadanie(1, 100)
"""
#9 - dake divne
"""
import tkinter

def koleso(x, y, r=15, farba="navy"):
    y+=r/2
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=farba)

def doska(x, y, sirka=100, vyska=20, farba="red"):
    canvas.create_rectangle(x-sirka/2, y-vyska/2, x+sirka/2, y+vyska/2, fill=farba)

def vozik(x, y):
    doska(x, y)
    koleso(x-30, y)
    koleso(x+30, y)

def velky_vozik(x, y):
    doska(x, y, 150, 40, 'green')
    koleso(x-35, y, 25, 'orange')
    koleso(x+35, y, 25, 'orange')

canvas = tkinter.Canvas()
canvas.pack()

vozik(200, 100)
velky_vozik(150, 200)
vozik(300, 210)

tkinter.mainloop()
"""
#10
"""
import tkinter
import random

c = tkinter.Canvas()
c.pack()

def rgb_picker():
    return f"#{random.randrange(1, 255**3):06x}"

def kruhy(x, y):
    for i in range(50, 0, -5):
        c.create_oval(x-i, y-i, x+i, y+i, fill=rgb_picker())

for i in range(10):
    kruhy(random.randint(50, 330), random.randint(50, 210))

tkinter.mainloop()
"""
#11
"""
import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()
def karticka(x, y, text):
    canvas.create_rectangle(x-50, y-20, x+50, y+20, fill="lightgrey")
    canvas.create_text(x, y, font="arial 14", text=text)
for i in range(10):
    karticka(random.randint(50, 300), random.randint(50, 200), "Python")
tkinter.mainloop()
"""
#12
"""
import tkinter
import random
c = tkinter.Canvas()
c.pack()
def rgb():
    return f"#{random.randrange(0, 255**3):06x}"
def dom(x, y, vel1, vel2):
    c.create_rectangle(x, y, x+vel1, y-vel1, fill=rgb())
    c.create_polygon(x, y-vel1, x+vel1, y-vel1, x+vel1/2, y-vel2-vel1, fill=rgb(), outline="black")

x, y = 10, 150
while x < 330:
    v = random.randint(20, 50)
    dom(x, y, v, random.randint(v//2, v))
    x += v
tkinter.mainloop()
"""
#13 ??
"""
import tkinter
import random
import math
c = tkinter.Canvas()
c.pack()
def vzd(x1, y1, x2, y2):
    return math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)
def kresli_bodky(x, y, farba):
    c.create_oval(x-5, y-5, x+5, y+5, width=0, fill=farba)
def farebne_bodky(r, x1, y1, x2, y2, x3, y3):
    x = random.randint(10, 290)
    y = random.randint(10, 290)
"""
#14
"""
import tkinter
c = tkinter.Canvas()
c.pack()
def stv(riadok, stlpec, farba="white"):
    c.create_rectangle(stlpec*30+5, riadok*30+5, stlpec*30+35, riadok*30+35, fill=farba, width=0)
def rgb(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"
for i in range(8):
    for j in range(12):
        stv(i, j, farba=rgb(255, int(255/18)*(j+i), 0))
tkinter.mainloop()
"""
#15
"""
import tkinter
import math
import random
c = tkinter.Canvas()
c.pack()
def vektor(x, y, dlzka, uhol):
    x1 = x + dlzka*math.cos(math.radians(uhol))
    y1 = y + dlzka*math.sin(math.radians(uhol))
    c.create_line(x, y, x1, y1, arrow="last")
for i in range(10):
    vektor(random.randint(50, 300), random.randint(50, 200),
           random.randint(10, 80), random.randint(0, 359))
tkinter.mainloop()
"""
#16
"""
import tkinter
import math
c = tkinter.Canvas()
c.pack()
def slnko(n, x, y):
    uhol = 360/n
    for i in range(1, n+1):
        x1 = x + 70*math.cos(math.radians(uhol))
        y1 = y + 70*math.sin(math.radians(uhol))
        c.create_line(x, y, x1, y1, fill="yellow", width=15)
        uhol += 360/n
    c.create_oval(x-50, y-50, x+50, y+50, fill="yellow", outline="")
slnko(10, 100, 80)
slnko(20, 180, 120)
tkinter.mainloop()
"""
#17 dako mi nesedia uhly !dorobit!
"""
import tkinter
import math
c = tkinter.Canvas()
c.pack()
def vybodkuj_usecku(x1, y1, x2, y2, n):
    x_rozdiel = (x1-x2)
    y_rozdiel = (y1-y2)
    diel = ((x1-x2) ** 2 + (y1-y2) ** 2)**0.5 / n
    # diel = round(diel, 2)
    if n == 2:
        c.create_oval(x1-1, y1-1, x1+1, y1+1, fill="black")
        c.create_oval(x2-1, y2-1, x2+1, y2+1, fill="black")
    else:
        for i in range(0, n+1):
            roc = (y_rozdiel/x_rozdiel)
            # roc = round(roc, 2)
            xb = x1 + (i*diel)*math.cos(math.tan(roc))
            yb = y1 + (i*diel)*math.sin(math.tan(roc))
            c.create_oval(xb-1, yb-1, xb+1, yb+1, fill="black")
            print(xb, yb)

c.create_line(100, 80, 180, 120, fill='light gray')
vybodkuj_usecku(100, 80, 180, 120, 5)
tkinter.mainloop()
"""
# 18
"""
import tkinter
from math import *
c = tkinter.Canvas()
c.pack()
def n_uholnik(n, x0, y0, r):
    body = []
    uhol = 360/n
    for i in range(n):
        x = x0 + r * cos(radians(uhol))
        y = y0 + r * sin(radians(uhol))
        body.append(x)
        body.append(y)
        uhol += 360/n
    c.create_polygon(body, fill="", outline="black", width=1)

n_uholnik(3, 50, 50, 45)
n_uholnik(4, 150, 50, 45)
n_uholnik(5, 250, 50, 45)

n_uholnik(6, 50, 150, 45)
n_uholnik(7, 150, 150, 45)
n_uholnik(8, 250, 150, 45)
tkinter.mainloop()
"""
#19
"""
import tkinter
from math import *
c = tkinter.Canvas()
c.pack()

def n_hviezda(n, x0, y0, r, k=2):
    uhol = 360/n
    for i in range(0, n+1):
        x1 = x0 + r * cos(radians(uhol))
        y1 = y0 + r * sin(radians(uhol))
        x2 = x0 + r * cos(radians(uhol+(360/n*k)))
        y2 = y0 + r * sin(radians(uhol+(360/n)*k))
        c.create_line(x1, y1, x2, y2)
        uhol += 360/n

n_hviezda(5, 50, 50, 45)
n_hviezda(7, 150, 50, 45)
n_hviezda(7, 250, 50, 45, 3)
n_hviezda(9, 50, 150, 45)
n_hviezda(9, 150, 150, 45, 4)
n_hviezda(11, 250, 150, 45, 4)
tkinter.mainloop()
"""
#20
"""
import tkinter
from math import *
c = tkinter.Canvas()
c.pack()
def n_spirala(n, x0, y0, r):
    uhol = 360/n
    polomer = 5
    while polomer < r:
        x1 = x0 + polomer * cos(radians(uhol))
        y1 = y0 + polomer * sin(radians(uhol))
        x2 = x0 + polomer * cos(radians(uhol+360/n))
        y2 = y0 + polomer * sin(radians(uhol+360/n))
        c.create_line(x1, y1, x2, y2)
        uhol += 360/n
        polomer += 2

n_spirala(3, 50, 50, 45)
n_spirala(4, 150, 50, 45)
n_spirala(5, 250, 50, 45)
n_spirala(6, 50, 150, 45)
n_spirala(7, 150, 150, 45)
n_spirala(8, 250, 150, 45)
tkinter.mainloop()
"""
#21
"""
import tkinter as tk
from math import *
c = tk.Canvas()
c.pack()
def horna(x0, y0, r):
    uhol = 180
    while uhol <= 360:
        x1 = x0 + r * cos(radians(uhol))
        y1 = y0 + r * sin(radians(uhol))
        x2 = x0 + r * cos(radians(uhol+(360/36)))
        y2 = y0 + r * sin(radians(uhol+(360/36)))
        c.create_line(x1, y1, x2, y2)
        uhol += 360/36
def dolna(x0, y0, r):
    uhol = 0
    while uhol <= 180:
        x1 = x0 + r * cos(radians(uhol))
        y1 = y0 + r * sin(radians(uhol))
        x2 = x0 + r * cos(radians(uhol+(360/36)))
        y2 = y0 + r * sin(radians(uhol+(360/36)))
        c.create_line(x1, y1, x2, y2)
        uhol += 360/36
horna(30, 100, 30)
dolna(90, 100, 30)
horna(150, 100, 30)
dolna(210, 100, 30)
horna(270, 100, 30)
dolna(330, 100, 30)
for i in range(6):
    horna(30+60*i, 200, 30)
tk.mainloop()
"""
#22
import tkinter
from math import *
import time
c = tkinter.Canvas()
c.pack()
def rucicka(uhol, dlzka, hrubka, farba):
    x,y = 190, 130
    x1 = x + dlzka*cos(radians(uhol))
    y1 = y + dlzka*sin(radians(uhol))
    c.create_line(x, y, x1, y1, width=hrubka, fill=farba)

def hodinky(h, m, s):
    c.create_oval(90, 30, 290, 230, fill="white", outline="black", width=2)
    uhol_h = 270 + (30*h+ 0.5*m)
    uhol_m = 270 + 6*m
    uhol_s = 270 + 6*s
    rucicka(uhol_h, 60, 10, "gray")
    rucicka(uhol_m, 70, 6, "black")
    rucicka(uhol_s, 80, 2, "red")

while True:
    c.delete('all')
    h, m, s = time.localtime()[3:6]
    hodinky(h, m, s)
    c.update()
    c.after(1000)

# hodinky(8, 55, 10)
tkinter.mainloop()