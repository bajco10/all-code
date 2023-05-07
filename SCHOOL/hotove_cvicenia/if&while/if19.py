# zdroj: https://input.sk/python2019/04.html

#1 - zbytocne
#2
"""
n = int(input("zadaj číslo: "))
print(f"{n} = ", end="")
while n > 1:
    for i in range(2, 100):
        while n%i==0:
            if n == i:
                print(i, end="")
                n = n//i
            else:
                print(i, end=" * ")
                n = n//i
"""
#3
"""
n = 4132
cs = 0
while n > 0:
    print(n%10)
    cs += n%10
    n = n//10
print(f"ciferný súčet = {cs}")
"""
#4
"""
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
n = 510726
x, y = 330, 150
while n>0:
    canvas.create_rectangle(x-10, y-10, x+10, y+10, fill="lightblue")
    canvas.create_text(x, y, text=f"{n%10}")
    n = n//10
    x -= 22
tkinter.mainloop()
"""
#5
"""
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
n = 1753
n = int(f"{n:o}")
# n = int(f"{n:b}")
x, y = 330, 150
while n>0:
    canvas.create_rectangle(x-10, y-10, x+10, y+10, fill="lightblue")
    canvas.create_text(x, y, text=f"{n%10}")
    n = n//10
    x -= 22
tkinter.mainloop()
"""
#6a
"""import tkinter
canvas = tkinter.Canvas()
canvas.pack()
n = 13
for i in range(n):
    for j in range(n):
        x = j * 20 + 100
        y = i * 20 + 10
        if i == 6:
            farba = 'red'
        elif j == 6:
            farba = "red"
        else:
            farba = 'white'
        canvas.create_oval(x-8, y-8, x+8, y+8, fill=farba)
tkinter.mainloop()"""
#6b
"""
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
n = 13
for i in range(n):
    for j in range(n):
        x = j * 20 + 100
        y = i * 20 + 10
        if i ==j:
            farba = 'red'
        elif j == n-i-1:
            farba = "red"
        else:
            farba = 'white'
        canvas.create_oval(x-8, y-8, x+8, y+8, fill=farba)
tkinter.mainloop()
"""
#7
"""
print("zadavaj vysky ziakov")
i = 1
n = 0
vysky = []
while True:
    n = (input(f"vyska {i} ziaka: "))
    if n =="":
        break
    vysky.append(n)
    i+=1
druhy = vysky[:]
druhy.sort()
if vysky == druhy:
    print("ziaci su zoradeni spravne")
else:
    print("ziaci nie su spravne zoradeni")
"""
#8
"""
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
x, y = 190, 130
r = 120
k = 6
n = 0
while r > 20:
    if n%6==0:
        canvas.create_oval(x-r, y-r, x+r, y+r, outline="grey")
    else:
        canvas.create_oval(x-r, y-r, x+r, y+r)
    r -= 3
    n += 1
tkinter.mainloop() 
"""
#9
"""
import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()
k = 21
sucet = 0
x, y = 20, 20
yt = 20
r = 10
t = True
for i in range(10):
    while t:
        m = random.randint(1, 4)
        canvas.create_oval(x-r, y-r, x+r, y+r, fill="white")
        canvas.create_text(x, y, text=m, font="arial 14")
        x+=2*r+3
        sucet += m
        if sucet == k:
            canvas.create_text(350, y, text="HURA", fill="green")
            x = 20
            t = False
            sucet = 0
        elif sucet > k:
            canvas.create_text(350, y, text="SKODA", fill="red")
            x = 20
            t = False
            sucet = 0
    y+=20 +3
    t = True
tkinter.mainloop()
"""
#10 
"""
import tkinter
import random
from math import sqrt
c = tkinter.Canvas()
c.pack()
x0, y0 = 190, 130
r = 90
def vzd(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)
for i in range(0, 2000):
    x = random.randint(1, 350)
    y = random.randint(1, 250)
    if vzd(x0, y0, x, y) < r:
        c.create_oval(x-5, y-5, x+5, y+5, width=0, fill="red")
    else:
        c.create_oval(x-5, y-5, x+5, y+5, width=0, fill="yellow")
tkinter.mainloop()
"""
#11
"""
import tkinter
import random
c = tkinter.Canvas()
c.pack()
n = 7
xcor = []
ycor = []
for i in range(7):
    x = random.randint(50, 300)
    y = random.randint(50, 250)
    c.create_oval(x-3, y-3, x+3, y+3, fill="red")
    xcor.append(x)
    ycor.append(y)
c.create_rectangle(max(xcor), max(ycor), min(xcor), min(ycor),width=1, outline="blue")
tkinter.mainloop()
"""
# 16
"""
import tkinter
import random
sirka = 400
c = tkinter.Canvas(width=sirka)
c.pack()
x0, y0 = 10, 200
def rgb():
    return(f"#{random.randint(0, 255**3):06x}")
while True:
    w = random.randint(10, 70)
    h = random.randint(10, 70)
    if w >= sirka:
        break
    if w>h:                 # tento 
        w, h = h, w         # a tento riadok su upravou
    c.create_rectangle(x0, y0, x0+w, y0-h, fill=rgb())
    sirka -= w
    x0+=w
tkinter.mainloop()
"""
#17
"""
import tkinter
import random
c = tkinter.Canvas()
c.pack()
def r_generator():
    return random.randint(10, 50)
r1 = r_generator()
r2 = r_generator()
r3 = r_generator()
x, y = 190, 20
polomery = [r1, r2, r3]
polomery.sort()
for i in polomery:
    y+=i
    c.create_oval(x-i, y-i, x+i, y+i, fill="white")
    y+=i
tkinter.mainloop()
"""
#18
"""
import tkinter
import math
c = tkinter.Canvas()
c.pack()
x0, y0 = 190, 130
r = 100
farba1, farba2 = "red", "yellow"
n, k = 35, 7
uhol = 360/n
print(uhol)
obvod = 2*math.pi*r
strana = obvod/(2*n)
for i in range(1, n+1):
    x = x0 + r*math.cos(math.radians(uhol))
    y = y0 + r*math.sin(math.radians(uhol))
    if i%k==0:
        c.create_oval(x-strana, y-strana, x+strana, y+strana, fill="yellow")
    else:
        c.create_oval(x-strana, y-strana, x+strana, y+strana, fill="red")
    
    uhol+= (360/n)
    print(i)
tkinter.mainloop()
"""














