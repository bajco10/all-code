
"""
import random
import tkinter

canvas = tkinter.Canvas(width=600, height=300)
canvas.pack()

# text + rectangles

canvas.create_text(190, 130, text="Python", font="arial 40")
canvas.create_text(40, 130, text="vlavo")
canvas.create_text(340, 130, text="vpravo")
canvas.create_text(190, 50, text="hore")
canvas.create_text(190, 210, text="dole")

"""
"""
canvas.create_rectangle(50, 80, 200, 160)
canvas.create_rectangle(100, 120, 250, 200, outline='red')
canvas.create_rectangle(130, 100, 280, 180, outline="blue", width=5)
canvas.create_rectangle(80, 70, 230, 150, fill="yellow")
"""
"""
x, y = 50, 50
s, v = 100, 55
farba = "red"
canvas.create_rectangle(x, y, x+s, y+v, fill=farba)
x, y = 160, 70
canvas.create_rectangle(x, y, x+s, y+v, fill=farba)
"""
"""

x, y = 10, 50
s, v = 20, 50
farba = "red"
for i in range(15):
    canvas.create_rectangle(x, y, x+s, y+v, fill=farba)
    x = x + s + 2
"""
"""
y = 10
s, v = 30, 50
farba, farba2 = "red", "blue"
for j in range(5):
    x = 10
    for i in range(15):
        canvas.create_rectangle(x, y, x+s, y+v, fill=farba)
        x = x + s + 2
    y = y + v + 2
    farba, farba2 = farba2, farba
"""
"""
x0, y0 = 10, 10
s = 30
for y in range(y0, 250, s+2):
    for x in range(x0, 550, s+2):
        r = random.randrange(256)
        g = random.randrange(256)
        b = random.randrange(256)
        farba = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_rectangle(x, y, x+s, y+s, fill=farba)
"""
# elipy (oval)
"""
x, y = 190, 130
for r in range(10, 130, 10):
    canvas.create_oval(x-r, y-r, x+r, y+r)
"""
"""
x, y = 190, 130
f1, f2 = "red", "blue"
for r in reversed(range(10, 130, 10)):
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=f1)
    f1, f2 = f2, f1
"""
"""
x0, y0 = 10, 10
s = 30
for y in range(y0, 250, s+2):
    for x in range(x0, 550, s+2):
        r = random.randrange(256)
        g = random.randrange(256)
        b = random.randrange(256)
        farba = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_oval(x, y, x+s, y+s, fill=farba)
"""
# usecky a lomene ciary
"""
a = (50, 150)
b = (150, 0)
c = (250, 150)
d = (150, 300)
e = (50, 150)

m = (150, 75)
n = (150, 215)
canvas.create_line(a, b, c, d, e)
canvas.create_line(m, n)
"""
"""
a = (100, 50)
b = (30, 150)
c = (160, 120)
d = (180, 40)
canvas.create_line(a, b, c, d)

for bod in a, b, c, d:
    x, y = bod
    canvas.create_oval(x-5, y-5, x+5, y+5, outline="red")

for x, y in a, b, c, d:
    canvas.create_oval(x-5, y-5, x+5, y+5, outline='red')
"""
# polygon
"""
a = (100, 50)
b = (30, 150)
c = (160, 120)
d = (180, 40)
canvas.create_polygon(a, b, c, d, fill='cyan')
"""
# obrazok

# civic = tkinter.PhotoImage(file=r"C:\Users\Uzivatel\Desktop\programovanie\SKOLA\other\civic_ep3.png")
# canvas.create_image(500, 100, image=civic) 
"""
text1 = "programovanie"
canvas.create_text(190, 130, text=text1,font=("Courier New", 30))
tkinter.mainloop()
"""
"""
from tkinter import Canvas, mainloop
from random import randint, randrange
from math import sin, cos, radians

canvas = Canvas()
canvas.pack()

a = 30
n = 100

for i in range(n):
    x1 = randint(a, 380 - a)
    y1 = randint(a, 260 - a)
    uhol = randint(0, 360)
    x2 = x1 + a * cos(radians(uhol))
    y2 = y1 + a * sin(radians(uhol))
    uhol = uhol - 60
    x3 = x1 + a * cos(radians(uhol))
    y3 = y1 + a * sin(radians(uhol))
    farba = f'#{randrange(256**3):06x}'
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=farba)
mainloop()            # ak treba

print(f"{(256):06x}")
"""



# 2021 tkinter
"""
import tkinter, random
c = tkinter.Canvas()
c.pack()
x, y = 10, 120

for i in range(37):
    c.create_oval(x-3, y-3, x+3, y+3, fill="red")
    x += 10
    y += random.randint(-10, 10)

tkinter.mainloop()
#
import tkinter, random
c = tkinter.Canvas()
c.pack()

x, y = 10, 120

for i in range(37):
    x1 = x+10
    y1 = y + random.randint(-10, 10)
    c.create_line(x, y, x1, y1, width=3)
    x, y = x1, y1
tkinter.mainloop()
"""


import tkinter
from math import sin, cos, radians
canvas = tkinter.Canvas(bg="white")
canvas.pack()
x0, y0 = 150, 130
r = 110
n = 7
cor = []
for uhol in range(0, 360, int((round(360/n, 0)))):
    x = x0 + r * cos(radians(uhol))
    y = y0 + r * sin(radians(uhol))
    canvas.create_line(x0, y0, x, y)
    cor.append(x)
    cor.append(y)
canvas.create_polygon(cor, fill="white", width=3, outline="black")
tkinter.mainloop()
