""" Vo vacsine programov su hodnoty pevne danne, nech nemusime ist cez milion inputov.
    Programy kde to tak nie je, su okomentovane - aby boli nefunkcne.
    zdroj zadani: https://input.sk/python2017/03.html   # bajana
"""
# import random
from cmath import sqrt
import tkinter
import math
import random


canvas = tkinter.Canvas(width=800, height=600,bg="navy") #bg="navy") # pri cviceniach kde je iny canvas treba toto cele vykomentovat!
canvas.pack()                                   # aj toto! inak budu 2 alebo viac platna na sebe
                                # pre ulohu č.13 pouzijeme bg="navy"
# 1
"""
text1 = "programovanie"
canvas.create_text(190, 130, text=text1,font=("Courier New", 30))
canvas.create_text(200, 230, text=text1,font=("Comic Sans", 20))
canvas.create_text(100, 295, text=text1,font=("Arial Black", 30))
canvas.create_text(90, 110, text=text1,font=("Times New Roman", 10))
"""
# 2
# jednoduche riesenie
"""
canvas.create_rectangle(100, 250, 200, 230, fill="cyan")
canvas.create_rectangle(120, 230, 180, 210, fill="red")
canvas.create_rectangle(140, 210, 160, 190, fill="lime")
"""
# forloop riesenie
"""
x1 = 100
y1 = 250
x2 = 200
y2 = 230

for i in range(3):
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    farba = f"#{r:02x}{g:02x}{b:02x}"
    canvas.create_rectangle(x1, y1, x2, y2, fill=farba)
    x1+=20
    y1-=20
    x2-=20
    y2-=20
"""
# 3 
"""
x1 = 100
y1 = 250
x2 = 300
y2 = 240
for i in range(10):
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    farba = f"#{r:02x}{g:02x}{b:02x}"
    canvas.create_rectangle(x1, y1, x2, y2, fill=farba)
    x1+=10
    y1-=10
    x2-=10
    y2-=10
"""
# 4
"""
import tkinter

c = tkinter.Canvas(width=600, height=400)
c.pack()
r1 = 20
r2 = 30
n = 10
x, y = 50, 50
f1 = "#ffad00"
f2 = "#2dad00"
f3 = "#bc63eb"
for i in range(n):
    c.create_oval(x, y-r1, x+2*r1, y+r1, fill=f1, width=0)
    x += 2*r1
    r1, r2 = r2, r1
    f1, f2 = f2, f1
    f2, f3 = f3, f2
c.mainloop()
"""
# 5
"""
r = int(input("Zadaj polomer: "))
# r = 60
stred_x = 600/2
stred_y = 300/2
a = r / 1.41421356237 # sqrt(2) = cca 1.41421356237
canvas.create_oval(stred_x -r, stred_y + r, stred_x + r, stred_y - r)
canvas.create_rectangle(stred_x -a, stred_y + a, stred_x + a, stred_y - a, outline="red")
"""
# 6
"""
r1, r2, r3 = 60, 40, 20
canvas = tkinter.Canvas(width=600, height=300, background="light blue")
canvas.pack()

canvas.create_oval(270, 250, 270+r1, 250-r1, fill="#b4b4b4")
canvas.create_oval(260+r1, 250-r1, 260+r1-r2, 250-r1-r2, fill="#c8c8c8")
canvas.create_oval(270+r2, 250-r1-r2, 270+r2-r3, 250-r1-r2-r3, fill="#dcdcdc")
"""
# 7
"""
x = 100
y = 295
a = int(input("Zadaj stranu: "))
v = int(input("Zadaj vysku: "))
canvas.create_polygon(x,y, x+a,y, x+(a/2),y-v, fill="salmon")
"""
# 8
"""
# vyska rovnostranneho trojuholnika je: v = (a*sqrt(3))/2
x, y = 50, 120
z, a = 100, 80

prevysok_strechy = z - a
v = (z*1.732050807568877) / 2
canvas.create_polygon(x-(prevysok_strechy/2),y, x+z-(prevysok_strechy/2),y, 
                        x+(z/2)-(prevysok_strechy/2),y-v, fill="red")
canvas.create_rectangle(x, y, x+a, y+a, fill="blue")
"""
# 9
"""
n = 30
r = 20
for i in range(n):
    x = random.randrange(50, 550)
    y = random.randrange(50, 250)
    canvas.create_oval(x, y, x+r, y+r, fill="yellow")
    canvas.create_text(x+r/2, y+r/2, text=str(i))
"""
# 10
"""
# a - b, b - c, c - d, d - e, e - c, c - a, a - d, d - b
a = (300, 250)
b = (400, 250)
c = (400, 150)
d = (300, 150)
e = (350, 50)
canvas.create_line(a, b, c, d, e, c, a, d, b)
"""
# 11
"""
a = (300, 250)
b = (400, 250)
c = (400, 150)
d = (300, 150)
e = (350, 50)
f = (350, 200)  # stred uhlopriecky stvorca
canvas.create_polygon(a, b, f, fill="orange", outline="black", width=2)
canvas.create_polygon(b, c, f, fill = "yellow", outline="black", width=2)
canvas.create_polygon(c, d, f, fill="red", outline="black", width=2)
canvas.create_polygon(d, a, f, fill="lime", outline="black", width=2)
canvas.create_polygon(d, c, e, fill="blue", outline="black", width=2)
"""
# 12
"""
x0, y0 = 300, 200
r = 100
krok = 20
for uhol in range(0, 360, krok):
    x = x0 + r * math.cos(math.radians(uhol))
    y = y0 + r * math.sin(math.radians(uhol))
    x1 = x0 + r * math.cos(math.radians(uhol+krok))
    y1 = y0 + r * math.sin(math.radians(uhol+krok))
    
    canvas.create_line(x, y, x1, y1)
"""
# 13

x0, y0 = 200, 170
pocet_lucov = 30
dlzka_lucov = 150 # polomer vacsiej kruznice
velkost_slnka = 80 # polomer mensej kruznice
farba_pozadia = "navy"

krok = 360 // pocet_lucov

for uhol in range(0, 360, krok):
    x = x0 + dlzka_lucov * math.cos(math.radians(uhol))
    y = y0 + dlzka_lucov * math.sin(math.radians(uhol))
    canvas.create_line(x, y, x0, y0, width=5, fill="yellow")

canvas.create_oval(x0-velkost_slnka, y0-velkost_slnka, 
                    x0+velkost_slnka, y0+velkost_slnka, 
                    fill="yellow", outline="yellow")

# 14
"""
meno_suboru = "python-logo.png"
python_logo = tkinter.PhotoImage(file=meno_suboru)
for i in range(10):
    canvas.create_image(random.randrange(0, 800), 
    random.randrange(0, 600), image=python_logo)
"""

tkinter.mainloop() # <- toto tu musi vzdy ostat! inak sa nic nezobrazi