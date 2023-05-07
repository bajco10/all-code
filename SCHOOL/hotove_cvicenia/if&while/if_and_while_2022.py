# zdroj: https://python.input.sk/z/04.html
#1
"""
# x = input("Zadaj km pre prvy den: ")
x = 100
# y = input("Zadaj cielove km: ")
y = 121
den = 1
while x < y:
    x += x*0.1
    den += 1
print(f"Na {den}. den prebehne {round(x, 2)} km.")
"""
#2
"""
# n = int(input("zadaj cislo: "))
n = 44
while n != 1:
    if n%2==0:
        n = n/2
        if n != 1:
            print(round(n), end=", ")
        else:
            print(1)
    else:
        n = n*3 + 1
        if n != 1:
            print(round(n), end=", ")
        else:
            print(1)
"""
#3
"""
pocet = 1
m = 0
while True:
    n = float(input(f"zadaj {pocet}. cislo: "))
    if n ==0:
        break
    m += n
    pocet += 1
print(f"sucet vsetkych precitanych cisel je {m}")
"""
# 4
"""
# n = int(input("zadaj cislo: "))
n = 1001
k = 2
print(f"{n} = ", end=" ")
while True:
    if n%k==0:
        n = n/k
        if n == 1:
            print(k, end="")
        else:
            print(k, end=" * ")
    else:
        k+=1
    if n == 1:
        break
"""
#5
"""
# n = input("zadaj cislo: ")
n = "4132"
cs = 0
for i in reversed(str(n)):
    print(i)
    cs += int(i)
print(f"ciferny sucet = {cs}")
"""
#6
"""
import tkinter
c = tkinter.Canvas()
c.pack()
n = "510726"
x, y = 350, 150
for i in reversed(str(n)):
    c.create_rectangle(x-10, y-10, x+10, y+10, fill="lightblue")
    c.create_text(x, y, text=i, font="calibri 14")
    x-=22
tkinter.mainloop()
"""
#7
"""
import tkinter
c = tkinter.Canvas()
c.pack()
n = 1753
n = f"{n:o}"
x, y = 350, 150
for i in reversed(str(n)):
    c.create_rectangle(x-10, y-10, x+10, y+10, fill="lightblue")
    c.create_text(x, y, text=i, font="calibri 14")
    x-=22
tkinter.mainloop()
"""
#8
#A
"""
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
n = 13
for i in range(n):
    for j in range(n):
        x = j * 20 + 100
        y = i * 20 + 12
        if i == 6:
            farba = 'red'
        elif j == 6:
            farba = "red"
        else:
            farba = 'white'
        canvas.create_oval(x-8, y-8, x+8, y+8, fill=farba)
tkinter.mainloop()
"""
#B
"""
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
n = 13
for i in range(n):
    for j in range(n):
        x = j * 20 + 100
        y = i * 20 + 12
        if i == j:
            farba = 'red'
        elif j == n-i-1:
            farba = "red"
        else:
            farba = 'white'
        canvas.create_oval(x-8, y-8, x+8, y+8, fill=farba)
tkinter.mainloop()
"""
#9
"""
print("zadavaj vysky ziakov: ")
c_ziaka = 1
vysky_ziakov = []
while True:
    n = input(f"    vyska {c_ziaka}. ziaka: ")
    if n == "":
        break
    vysky_ziakov.append(int(n))
    c_ziaka+=1

korektne_vysky = sorted(vysky_ziakov)
if vysky_ziakov == korektne_vysky:
    print("vsetci ziaci su zoradeni spravne")
else:
    print("ziaci nie su spravne zoradeni")
"""
#10
"""
import tkinter
c = tkinter.Canvas()
c.pack()
x, y = 190, 130
r = 120
k = 6
m = 0
while r > 15:
    if m%k==0:
        farba = "grey"
    else:
        farba = "black"
    c.create_oval(x-r, y-r, x+r, y+r, outline=farba)
    m+=1
    r-=3
tkinter.mainloop()
"""
#11
"""
import tkinter
import random
c = tkinter.Canvas()
c.pack()
k = 21
x, y = 20, 20
hodnota = 0
generovane = 0

for i in range(10):
    while True:
        generovane = random.randint(1, 4)
        hodnota+=generovane
        c.create_oval(x-10, y-10, x+10, y+10, fill="white")
        c.create_text(x, y, text=generovane, font="arial 14")
        x+=25
        if hodnota > k:
            c.create_text(330, y, text="ŠKODA", fill="red")
            y+=25
            x = 20
            hodnota = 0
            break
        if hodnota == k:
            c.create_text(330, y, text="HURÁ", fill="green")
            y+=25
            x = 20
            hodnota = 0
            break
tkinter.mainloop()
"""
#12
"""
import tkinter
import random
sirka, vyska = 300, 300
c = tkinter.Canvas(width=sirka, height=vyska)
c.pack()
n = 4000
r = 5
for i in range(n):
    x = random.randint(0, sirka)
    y = random.randint(0, vyska)
    if x < 75 or x > 225:
        c.create_oval(x-r, y-r, x+r, y+r, fill="blue", width=0)
    elif y < 75 or y > 225:
        c.create_oval(x-r, y-r, x+r, y+r, fill="blue", width=0)
    else:
        c.create_oval(x-r, y-r, x+r, y+r, fill="red", width=0)
tkinter.mainloop()
"""
#14
import tkinter
import random
c = tkinter.Canvas(width=300, height=300)
c.pack()
x0, y0 = 180, 130 #stred
r = 110
for i in range(6000):
    x = random.randrange(0, 300)
    y = random.randrange(0, 300)
    l = ((x-x0)**2 + (y-y0) **2)**0.5
    if l < r:
        c.create_oval(x-6, y-6, x+6, y+6, fill="red", width=0)
    else:
        c.create_oval(x-6, y-6, x+6, y+6, fill="blue", width=0)
tkinter.mainloop()
