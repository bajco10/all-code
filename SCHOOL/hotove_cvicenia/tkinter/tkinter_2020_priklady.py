# rgb do hexadecimalnej!!!!
# f"#{r:02x}{g:02x}{b:02x}"
# najlepsi color generator
# color = "%06x" % random.randint(0, 0xFFFFFF)
# 1
"""
import tkinter 
canvas = tkinter.Canvas(width=800, height=600, bg="white")
canvas.pack()
x1, y1 = 100, 300
x2, y2 = 210, 300
canvas.create_rectangle(x1, y1, x1+100, y1-100, fill="red")
canvas.create_text(x1+50, y1-50, font="arial 20", fill="yellow", text="červený")
canvas.create_rectangle(x2, y2, x2+100, y2-100, fill="blue")
canvas.create_text(x2+50, y2-50, font="arial 20", fill="yellow", text="modrý")
canvas.mainloop()
"""
# 2
"""
import tkinter as tk
import random
canvas = tk.Canvas(width=800, height=600, bg="navy")
canvas.pack()
n = 2000
for i in range(n):
    velkost_fontu = random.randint(11, 20)
    x = random.randrange(0, 800)
    y = random.randrange(0, 600)
    canvas.create_text(x, y, font=f"arial {velkost_fontu}", text="*", fill="yellow")
canvas.mainloop()
"""
# 3
"""
import tkinter as tk
import random
canvas = tk.Canvas(width=800, height=600, bg="white")
canvas.pack()
x, y = 50, 50
a1, a2 = 180, 100
r_s = a1 - a2
canvas.create_rectangle(x, y, x+a1, y+a1, fill="indian red")
canvas.create_rectangle(x+(r_s/2), y+(r_s/2),x+(r_s/2)+a2,y+(r_s/2)+a2, fill="light blue")
canvas.create_text(x-5, y-5, text="A")
canvas.create_text(x+a1+5,y-5, text="B")
canvas.create_text(x+a1+5, y+a1+5, text="C")
canvas.create_text(x-5, y+a1+5, text="D")
canvas.create_text(x+a1+10, y+(a1/2), text=a1) # vonkajsi text
canvas.create_text(x+(a1/2), y+a1-8-r_s/2, text=a2) # vnutorny text
canvas.mainloop()
"""
# 4
"""
import tkinter as tk
canvas = tk.Canvas(width=800, height=600, bg="white")
canvas.pack()
farba1, farba2, farba3 = "red", "blue", "yellow"
n = 20
x = 200
y = 200
for i in range(n*10, 0, -10):
    canvas.create_rectangle(x+(i/2), y-(i/2), x-(i/2), y+(i/2), fill=farba1)
    temp_var = farba1
    farba1 = farba2
    farba2 = farba3
    farba3 = temp_var
canvas.mainloop()
"""
# 5
"""
import tkinter as tk
canvas = tk.Canvas(width=800, height=600, bg="white")
canvas.pack()
strana1 = 135
strana2 = 90
# nemecko
canvas.create_rectangle(10, 10, 10+(strana1), 10+(strana2/3), fill="black")
canvas.create_rectangle(10, 10+(strana2/3), 10+strana1, 10+2*(strana2/3), fill="red")
canvas.create_rectangle(10, 10+2*(strana2/3), 10+strana1, 10+strana2, fill="yellow")
# rusko
canvas.create_rectangle(200, 140, 200+(strana1), 140+(strana2/3), fill="white")
canvas.create_rectangle(200, 140+(strana2/3), 200+strana1, 140+2*(strana2/3), fill="blue")
canvas.create_rectangle(200, 140+2*(strana2/3), 200+strana1, 140+strana2, fill="red")
# francuzko
canvas.create_rectangle(10, 140, 10+(strana1/3), 140+strana2, fill="blue")
canvas.create_rectangle(10+(strana1/3), 140, 10+2*(strana1/3), 140+strana2, fill="white")
canvas.create_rectangle(10+2*(strana1/3), 140, 10+strana1, 140+strana2,fill="red")
# taliansko
canvas.create_rectangle(200, 10, 200+(strana1/3), 10+strana2, fill="green")
canvas.create_rectangle(200+(strana1/3), 10, 200+2*(strana1/3), 10+strana2, fill="white")
canvas.create_rectangle(200+2*(strana1/3), 10, 200+strana1, 10+strana2, fill="red")
canvas.mainloop()
"""
# 6
"""
import tkinter as tk
canvas = tk.Canvas(width=800, height=600, background="white")
canvas.pack()
zelene = ["lime", "darkgreen", "green", "greenyellow"]
x, y = 180, 250
k=0
for i in range(200, 0, -50):
    canvas.create_rectangle(x-(i/2), y, x+(i/2), y-50, fill=zelene[k] )
    y-=50
    k +=1
canvas.mainloop()
"""
# 7
"""
import tkinter
c = tkinter.Canvas()
c.pack()
x, y = 10, 100
y1 = 100
y2 = 120
d = 20
n = 16
for i in range(0, n):
    c.create_line(x+i*d, y1, x+d+i*d, y2, width=5, fill="blue")
    y1, y2 = y2, y1
c.mainloop()
"""
# 8
"""
import tkinter
c = tkinter.Canvas(width=800, height=600, bg="white")
c.pack()
x, y = 70, 100
r = 50
dx, dy = 120, 60
x2,y2 = 70+(dx/2), 100+(dy)
c.create_oval(x-r, y-r, x+r, y+r, width=15, outline="blue")
c.create_oval(x2-r, y2-r, x2+r, y2+r, width=15, outline="yellow")
c.create_oval((x+dx)-r, y-r, (x+dx)+r, y+r, width=15, outline="black")
c.create_oval(dx+x2-r, y2-r, x2+dx+r, y2+r, width=15, outline="green")
c.create_oval((x+2*dx)-r, y-r, (x+2*dx)+r, y+r, width=15, outline="red")
c.mainloop()
"""
# 9
"""
import tkinter
import random
c = tkinter.Canvas()
c.pack()
n = 10
x, y = 50, 15
spolu = 0
for i in range(0, n+1):
    hodnota = random.choice((1, 2, 5, 10, 20, 50))
    c.create_rectangle(x, y, x+50, y+20, fill="white")
    c.create_text(x+25, y+10, text=f"{hodnota} €")
    y+=20
    spolu += hodnota
c.create_text(200, 40, text=f"spolu = {spolu} €", font="timesnewroman 16")
c.mainloop()
"""
# 10
"""
import tkinter
import random
c = tkinter.Canvas(width=800, height=600, bg="white")
c.pack()
n = 30
r = 20
x, y = 0, 0
for i in range(0, n+1):
    color = "%06x" % random.randint(0, 0xFFFFFF) 
    x = random.randrange(20, 780)
    y = random.randrange(20, 580)
    cislo = random.randrange(0, 10)
    c.create_oval(x-r, y-r, x+r, y+r, fill=f"#{color}")
    c.create_text(x, y, font="arial 30", text=cislo)
c.mainloop()
"""
# 11
"""
import tkinter
import random
c = tkinter.Canvas(width=800, height=600, bg="white")
c.pack()
a = 30
x, y = 10, 150
# n = input("slovo/a: ")
n = "lubim python"
n = n.upper() # zmeni kazdy input na vsetky velke pismena (pozri string methods)
for i in n:
    color = "%06x" % random.randint(0, 0xFFFFFF)
    color2 = "%06x" % random.randint(0, 0xFFFFFF)
    c.create_rectangle(x, y, x+a, y+a, fill=f"#{color}")
    c.create_text(x+a/2, y+a/2, fill=f"#{color2}", font="arial 26", text=i)
    x+=a
c.mainloop()
"""
# 12
"""
import tkinter
import random
c = tkinter.Canvas()
c.pack()
n = 7
a = (370-(n*5)) // n
x, y = 10, 100
for i in range(0, n):
    color = "%06x" % random.randint(0, 0xFFFFFF)
    c.create_rectangle(x, y, x+a, y+a, fill=f"#{color}")
    x+=(a+5)
c.mainloop()
"""
# 13
"""
import tkinter
c = tkinter.Canvas(width=800, height=600)
c.pack()
x, y = 50, 250
a = 280
v = (((3**0.5)*a)/2)
print("v = ", v)
c.create_polygon(x, y, x+a, y, x+a/2, y-v, fill="blue")
c.mainloop()
"""
# 14
"""
import tkinter
import random
c = tkinter.Canvas(width=800, height=600, bg="white")
c.pack()
n = 20
for i in range(n):
    x = random.randrange(20, 780)
    y = random.randrange(20, 580)
    color = "%06x" % random.randint(0, 0xFFFFFF)
    color2 = "%06x" % random.randint(0, 0xFFFFFF)
    a = random.randrange(10, 50)
    v = (((3**0.5)*a)/2)
    c.create_rectangle(x, y, x+a, y+a, fill=f"#{color}", outline="")
    c.create_polygon(x, y, x+a, y, x+a/2, y-v, fill=f"#{color2}")
c.mainloop()
"""
# 15
"""
import tkinter
c = tkinter.Canvas(width=800, height=600, bg="white")
c.pack()
sirka, vyska = 300, 200
v = (((3**0.5)*200)/2)
x, y = 20, 10
c.create_rectangle(x, y, x+sirka, y+(vyska/2), fill="white")
c.create_rectangle(x, y+(vyska/2), x+sirka, y + vyska, fill="red")
c.create_polygon(x, y, x, y+vyska, x+(sirka/2), y+(vyska/2), fill="blue")
c.mainloop()
"""
# 16
"""
import tkinter
c = tkinter.Canvas()
c.pack()
vel = 30
farba1, farba2 = "maroon", "gold"
riadky = 6
stlpce = 10
x, y = 10, 10
for i in range(0, riadky):
    for i in range(0, stlpce):
        c.create_rectangle(x, y, x+vel, y+vel, fill=farba1)
        x+=(vel+3)
        farba1, farba2 = farba2, farba1
    farba1, farba2 = farba2, farba1
    x = 10
    y += (vel+3)
c.mainloop()
"""
# 17
"""
import tkinter
c = tkinter.Canvas(width=800, height=600, bg="white")
c.pack()
r = 255
g = 0
b = 0
x, y = 5, 5
sirka, dlzka = 15, 250
for i in range(25):
    c.create_rectangle(x, y, x+sirka, y+dlzka, outline="", fill=f"#{r:02x}{g:02x}{b:02x}")
    r-=10
    b+=10
    x+=sirka
c.mainloop()
"""
# 18 
"""import tkinter
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
tkinter.mainloop()"""
# 19
"""
import tkinter
from math import sin, cos, radians
canvas = tkinter.Canvas(width = 1000, height= 1000, bg="white")
canvas.pack()
x0, y0, r = 180 + 250, 130 + 250, 300
n = 19
cor = []
for uhol in range(0, 360, int((round(360/n, 0)))):
    x = x0 + r * cos(radians(uhol))
    y = y0 + r * sin(radians(uhol))
    cor.append(x)
    cor.append(y)
canvas.create_polygon(cor, fill="", width=1, outline="black")
xcor = []
ycor = []
for i in range(0, 2*n, 2):
    xcor.append(cor[i])
    ycor.append(cor[i+1])
points = []
for i in range(0, n):
    point = (xcor[i], ycor[i])
    points.append(point)
for i in range(0, n):
    for j in range(0, n-1):
        canvas.create_line(points[i], points[j], width= .3)
tkinter.mainloop()
"""
#20   ???
"""
import tkinter
import math
import random
c = tkinter.Canvas(width=800, height=500)
c.pack()
x0, y0 = 400, 250
n = 13
uhol = -60
r1 = 130
r2 = 95
krok = int(round(360/n, 0))
krok = 360//n
obvod = n*40
alfa = 0.00968

# vonkajsia kruznica
for uhol in range(0, 360, krok):
    x_von = x0 + r2*math.cos(math.radians(uhol))
    y_von = y0 + r2*math.sin(math.radians(uhol))
    x_vnu = x0 + r1*math.cos(math.radians(uhol))
    y_vnu = y0 + r1*math.sin(math.radians(uhol))
    c.create_oval(x_von, y_von, x_vnu, y_vnu, fill="red

for i in range(0, 360, krok):
    x = x0 + r2*math.cos(math.radians(i))
tkinter.mainloop()
"""
# 21
"""
import tkinter
c = tkinter.Canvas()
c.pack()
x, y = 30, 30
sir, vys = 325, 216
modra, cervena = '#0b4ea2', '#ee1c25'
img = tkinter.PhotoImage(file="sk.png")
c.create_rectangle(x, y, x+sir, y+(vys/3), fill="white")
c.create_rectangle(x, y+(vys/3), x+sir, y+2*(vys/3), fill=modra)
c.create_rectangle(x, y+2*(vys/3), x+sir, y+vys, fill=cervena)
c.create_image(x+100, y+108, image = img)
c.mainloop()
"""
