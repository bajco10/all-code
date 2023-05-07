"""
import tkinter
import random
c = tkinter.Canvas(width=600, height=600)
c.pack()
n = 9
x, y = 50, 50
sucet = 0
m = ""

def rgb():
    return f"#{random.randrange(255**3):06x"

for i in range(1, n+1):
    for j in range(1, i+1):
        n = random.choice("123456789")
        # n = random.randrange(0, 10)
        farba = f"#{random.randrange(1, 255**3):06x}"
        c.create_rectangle(x, y, x+50, y+50, fill="yellow")
        if n in "2468":
            c.create_text(x+25, y+25, font="arial 20", text=n)
            m+=n
        else:
            c.create_text(x+25, y+25, fill=farba, text=n, font="arial 20")
            m+=n
        sucet+=int(m)
        x+=52
        
    x=50
    y+=52
    m=""
c.create_text(500, 200, text=sucet, font="arial 20")
tkinter.mainloop()
"""
"""
import tkinter
import random
c = tkinter.Canvas(width=700, height=700)
c.pack()
def rgb():
    return f"#{random.randrange(255**3):06x}"

parne, neparne = 0, 0
def stvorec(x, y):
    c.create_rectangle(x-20, y-20, x+20, y+20, fill="yellow")
    bude = random.randrange(2)
    if bude:
        parny_abo_neparny = random.randrange(4)
        if parny_abo_neparny:
            n = random.choice("2468")
            c.create_text(x, y, text=n, fill=rgb(), font="arial 20")
        else:
            n = random.choice("13579")
            c.create_text(x, y, text=n, font="arial 20" )
            

y = 50
for i in range(10):
    x = 50
    for i in range(10):
        stvorec(x, y)
        x+=45
    y += 45

tkinter.mainloop()
"""
"""
import tkinter
import random

canvas = tkinter.Canvas(height=800,width=800)
canvas.pack()

n = 10
x,y = 50, 50
for i in range(1,n+1):
    for j in range(1,n+1):
        canvas.create_rectangle(x,y,x+50,y+50, fill='yellow')
        m = random.choice('1 2 3 4 5 6 7 8 9 ')
        if m in '2468':
            canvas.create_text(x+25,y+25, text=m, font='Arial 20', fill ='blue')
        else:
            canvas.create_text(x+25,y+25, text=m, font='Arial 20', fill ='red')
        x = x+55
    x = 50
    y = y+55 
        
canvas.mainloop()

"""
"""
import tkinter, random

c = tkinter.Canvas(width = 800, height = 800)
c.pack()

n = 10
x, y = 100, 100
a = 40
u = 0
par = 0
nepar = 0
for i in range(n):
    for z in range(n):
        r = random.randrange(2)
        cis = random.randrange(1,10)
        c.create_rectangle(x, y,x+a, y+a, fill = 'yellow')
        if r==0:
            if cis%2==0 and u<3:
                c.create_text(x+a/2, y+a/2, text = str(cis), font = 'arial 40')
                u += 1
                par += 1
            elif cis%2==1 and u<3:
                cis -= 1
                c.create_text(x+a/2, y+a/2, text = str(cis), font = 'arial 40')
                u += 1
                par += 1
            elif cis%2==1 and u==3:
                c.create_text(x+a/2, y+a/2, text = str(cis), font = 'arial 40', fill = f'#{random.randrange(256):02x}{random.randrange(256):02x}{random.randrange(256):02x}')
                u = 0
                nepar += 1
            elif cis%2==0 and u==3:
                cis += 1
                c.create_text(x+a/2, y+a/2, text = str(cis), font = 'arial 40', fill = f'#{random.randrange(256):02x}{random.randrange(256):02x}{random.randrange(256):02x}')
                u = 0
                nepar += 1
        x += 43
    x = 100
    y += 43
print(par, nepar)

c.mainloop()
"""
"""
import tkinter
import random
c = tkinter.Canvas(width=600, height=600)
c.pack()
n = 5
sucet=0
m=""
x, y = 50, 50
for i in reversed(range(n)):
    for j in range(i):
        n = random.choice("123456789")
        farba = f"#{random.randrange(1, 255**3):06x}"
        c.create_rectangle(x, y, x+50, y+50, fill="yellow")
        if n in "2468":
            c.create_text(x+25, y+25, font="arial 20", text=n)
            m+=n
        else:
            c.create_text(x+25, y+25, fill=farba, text=n, font="arial 20")
            m+=n
        sucet+=int(m)
        x+=52
    x=50
    y+=52
    m=""
c.create_text(500, 200, text=sucet, font="arial 20")
tkinter.mainloop()
"""
"""
import tkinter
import random
import math

c = tkinter.Canvas(width=600, height=600)
c.pack()
x, y = 20, 20
x_start = 20
n = 5
cislo = 0
cisla = []
for i in reversed(range(n+1)):
    for j in range(i):
        cislo = random.randint(-99, 99)
        cisla.append(cislo)
        c.create_polygon(x,y, x+30, y+60, x+60, y, fill="red")
        c.create_text(x+30, y+30, font="arial 10", text=cislo)
        x+=60
    x-=60
    for m in range(i-1):
        c.create_polygon(x-30, y+60, x, y, x+30, y+60, fill="blue")
        x-=(60)
    y+=60
    x_start+=30
    x = x_start



modre_cislo=0
cisla_sucty = []
prve = 0
druhe = 1
tretie = n 
bla=len(cisla) - (n)
for i in range(1, bla+1):
    modre_cislo=cisla[prve]+cisla[druhe]+cisla[tretie]
    cisla_sucty.append(modre_cislo)
    prve += 1
    druhe += 1
    tretie += 1

print(cisla)
print(cisla_sucty)
tkinter.mainloop()
"""
"""
import tkinter
c = tkinter.Canvas(width=500, height=500)
c.pack()
x, y = 50, 50
n = 7
m = 1
sucet = 0
for i in range(n):
    for j in range(n):
        c.create_polygon(x-30, y+30, x, y, x+30, y+30, x, y+60, fill="lightblue", width=2, outline="black")
        c.create_text(x, y+30, text=m, font="arial 12")
        sucet = m + (m+1) + (m+n) + (m+1+n)
        if (i != n-1) and (m%n != 0):
            c.create_text(x+30, y+60, text=sucet, font="arial 12")
        m+=1
        x+=60
    x=50
    y+=60
tkinter.mainloop()
"""
"""
#pyramida so suctami cisel
import tkinter
c = tkinter.Canvas(width=1000, height=1000)
c.pack()
x, y = 50, 50
x_start = 50
n = 18
m = 0
sucet = 0
for i in range(n+1):
    for j in range(i):
        m += 1
for i in reversed(range(n+1)):
    for j in range(i):
        c.create_polygon(x, y, x+60, y, x+30, y+60, fill="black")
        c.create_text(x+30, y+25, text=m, font="arial 14", fill="white")
        # c.create_polygon(x+60, y, x+30, y+60, x+90, y+60, fill="orange")
        sucet = m + (m-1) + (m-i)
        if j!=i-1:  
            c.create_text(x+60, y+40, text=sucet, font="arial 14", tags="t")
        m -= 1
        x+=60
    x-=60
    for j in range(i-1):
        x-=60
        if j==0 or (j==i-2) or (i==n):   
            c.create_polygon(x+60, y, x+30, y+60, x+90, y+60, fill="orange")
        else:
            c.create_polygon(x+60, y, x+30, y+60, x+90, y+60, fill="blue")
    c.tag_raise("t")
        
    x_start += 30
    x = x_start
    y+=60
tkinter.mainloop() 
"""
"""
import tkinter
c = tkinter.Canvas(width=800, height=400, bg="black")
c.pack()
s = 40
x, y, v = 50, 350, 300
m = 1
def obdlznik(x, y, v, tag):
    c.create_rectangle(x, y, x+s, y-v, outline="", fill="white", tags=tag)


for i in range(16):
    tag = f"{m}"
    obdlznik(x, y, v, tag)
    x+=s+5
    m+=1

for i in range(16):
    c.itemconfig(i, v)
    c.after(10)
    c.update()

"""
"""while True:
    c.delete("rect")
    obdlznik(x, y, v)
    c.after(20)
    c.update()
    if v < 200:
        v+=20
    elif v > 200:
        while v > 20:
            c.delete("rect")
            obdlznik(x, y, v)
            c.after(20)
            c.update()
            v-=20"""


"""
def animacia(x, y, v):
    while True:
        c.delete("rect")
        obdlznik(x, y, v)
        c.after(2)
        c.update()
        if v < 200:
            v+=20
        elif v > 200:
            while v > 20:
                c.delete("rect")
                obdlznik(x, y, v)
                c.after(2)
                c.update()
                v-=20


animacia(x, y, v)
"""



