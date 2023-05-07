# zdroj: https://input.sk/python2021/z/04.html
# 1
"""
x = int(input("zadaj km pre prvý deň: "))
y = int(input("zadaj cieľové km: "))
dni = 1
while y > x:
    dni += 1
    x = x+x*0.1
print(f"na {dni}. deň prebehne {round(x, 2)} km")
"""
# 2
"""
n = int(input("zadaj cislo: "))
print(n, end=", ")
while n != 1:
    if n%2==0:
        if n/2==1:
            print(1, end="")
            break
        else:
            n = n/2
            print(int(n), end=", ")
    else:
        if n*3+1==1:
            print(int(n), end="")
        else:
            n = n*3 + 1
            print(int(n), end=", ")
"""
# 3
"""
sucet = 0
while True:
    n = float(input("zadaj cislo: "))
    if n == 0:
        break
    else:
        sucet += n
print(f"sucet vsetkych precitanych cisel je {round(sucet, 2)}")
"""
# 4
"""
n = int(input("zadaj cislo: "))
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
# 5
"""
n = str(input("zadaj cislo: "))
cs = 0
while len(n) > 0:
    k = n[-1]
    cs += int(k)
    n = n[:-1]
    print(k)
print(f"ciferny sucet = {cs}")
"""
# 6
"""
import tkinter
c = tkinter.Canvas()
c.pack()
n = str(input("zadaj cislo: "))
cs = 0
x, y, a = 250, 100, 10
while len(n) > 0:
    k = n[-1]
    cs += int(k)
    n = n[:-1]
    # print(k)
    c.create_rectangle(x-a, y-a, x+a, y+a, fill="lightblue")
    c.create_text(x, y, text=k, font="arial 10")
    x -= 20 + 2
print(f"ciferny sucet = {cs}")
c.mainloop()
"""
# 7
"""
import tkinter
c = tkinter.Canvas()
c.pack()
n = int(input("zadaj cislo: "))
cs = 0
x, y, a = 250, 100, 10
n = int(f"{n:o}") 
# n = int(f"{n:b}") # <-- na konvertovanie do binarnej
n = str(n)
while len(n) > 0:
    k = n[-1]
    cs += int(k)
    n = n[:-1]
    # print(k)
    c.create_rectangle(x-a, y-a, x+a, y+a, fill="lightblue")
    c.create_text(x, y, text=k, font="arial 10")
    x -= 20 + 2
print(f"ciferny sucet = {cs}")
c.mainloop()
"""
# 8A
"""import tkinter
canvas = tkinter.Canvas()
canvas.pack()
n = 13
for i in range(n):
    for j in range(n):
        x = j * 20 + 100
        y = i * 20 + 12
        if i == (n//2):
            farba = 'red'
        elif j == (n//2):
            farba = "red"
        else:
            farba = 'white'
        canvas.create_oval(x-8, y-8, x+8, y+8, fill=farba)
tkinter.mainloop()"""
# 8B
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
        elif j == i:
            farba = "red"
        elif j == n-i-1:
            farba = "red"
        else:
            farba = 'white'
        canvas.create_oval(x-8, y-8, x+8, y+8, fill=farba)
tkinter.mainloop()
"""
# 9
"""
n = 0
k = 1
vysky = []
print("zadávaj výšky žiakov")
while n!="":
    n = (input(f"výška {k}. žiaka "))
    k+=1
    if n !="":
        vysky.append(int(n))
    vysky_copy = vysky[:]               #listA[:] -> to create a copy
    vysky_copy.sort()
if (vysky==vysky_copy):
        print("spravne zoradenie")
else:
    print("zle zoradenie")   
"""
# 10
"""
import tkinter
c=tkinter.Canvas()
c.pack()
x, y = 190, 130
r = 120
k = 6
m = 0
while r >= 15:
    m+=1
    if m%6==0:
        c.create_oval(x-r, y-r, x+r, y+r, outline="grey")
    else:
        c.create_oval(x-r, y-r, x+r, y+r, fill="")
    r-=3
c.mainloop()
"""
# 11
"""
import random
import tkinter
c = tkinter.Canvas()
c.pack()
k = 21
sucet = 0
x, y = 20, 20
yt = 20
r = 10
t = True
for i in range(10):
    # m = random.randint(1,4)
    #c.create_oval(x-r, y-r, x+r, y+r, fill="white")
    while t:
        m = random.randint(1, 4)
        c.create_oval(x-r, y-r, x+r, y+r, fill="white")
        c.create_text(x, y, text=m, font="arial 14")
        x+=2*r + 3
        sucet += m
        if sucet == k:
            c.create_text(350, y, text="HURÁ", fill="green")
            x = 20  
            t = False
            sucet = 0
        elif sucet > k:
            c.create_text(350, y, text="ŠKODA", fill="red")
            x = 20  
            t = False
            sucet = 0    
    y+=20 + 3
    t = True
tkinter.mainloop()
"""
# 12
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
# 13
"""
import tkinter
import random
sirka, vyska = 300, 300
c = tkinter.Canvas(width=sirka, height=vyska)
c.pack()
n = 40000
r = 5
for i in range(n):
    x = random.randint(0, sirka)
    y = random.randint(0, vyska)
    if (x < 150 and y < x) or (x > 150 and y < 300-x):
        c.create_oval(x-r, y-r, x+r, y+r, fill="blue", width=0)
    elif (x < 150 and y>300-x) or (x>150 and y > x):
        c.create_oval(x-r, y-r, x+r, y+r, fill="green", width=0)
    elif (x < 150 and y > x):
        c.create_oval(x-r, y-r, x+r, y+r, fill="red", width=0)
    elif (x>150 and y<x):
        c.create_oval(x-r, y-r, x+r, y+r, fill="yellow", width=0)
tkinter.mainloop()
"""
# 14
"""
import tkinter
import random
c = tkinter.Canvas(width=300, height=300)
c.pack()
x0, y0 = 180, 130
r = 110
v = 0
for i in range(2000):
    x = random.randrange(0, 300)
    y = random.randrange(0, 300)
    l = ((x-x0)**2 + (y-y0) **2)**0.5
    if l < r:
        c.create_oval(x-6, y-6, x+6, y+6, fill="red", width=0)
    else:
        c.create_oval(x-6, y-6, x+6, y+6, fill="blue", width=0)
tkinter.mainloop()
"""
# 15
"""
import tkinter
import random
c = tkinter.Canvas(width=300, height=300)
c.pack()
cervene = 0
for i in range(0, 10000):
    x = random.randint(0, 300)
    y = random.randint(0, 300)
    if x*x+y*y <= 300*300:
        c.create_oval(x-2, y-2, x+2, y+2, fill="red", width=0)
        cervene += 1
    else:
        c.create_oval(x-2, y-2, x+2, y+2, fill="blue", width=0)
print((cervene/10000)*4)
tkinter.mainloop()
"""
#16
"""
import tkinter
import random
c = tkinter.Canvas()
c.pack()
n = 7
smallest_x=1000
greatest_x=0
smallest_y=1000
greatest_y=0
for i in range(n):
    x = random.randrange(350)
    y = random.randrange(250)
    c.create_oval(x-2, y-2, x+2, y+2, fill="red")
    if x > greatest_x:
        greatest_x = x
    if x < smallest_x:
        smallest_x = x
    if y > greatest_y:
        greatest_y = y
    if y < smallest_y:
        smallest_y = y
c.create_rectangle(smallest_x, smallest_y, greatest_x, greatest_y, outline="blue")
# print(smallest_x, smallest_y, greatest_x, greatest_y)
tkinter.mainloop()
"""
#17
"""
import tkinter
import random
c = tkinter.Canvas()
c.pack()
for i in range(10000):
    x = random.randrange(10, 350)
    y = random.randrange(10, 250)
    if y < 90:
        c.create_oval(x-3, y-3, x+3, y+3, width=0, fill="black")
    elif y < 170:
        c.create_oval(x-3, y-3, x+3, y+3, width=0, fill="red")
    else:
        c.create_oval(x-3, y-3, x+3, y+3, width=0, fill="gold")
tkinter.mainloop()
"""
#18
"""
import tkinter
import random
c = tkinter.Canvas()
c.pack()
for i in range(10000):
    x = random.randrange(10, 350)
    y = random.randrange(10, 250)
    if x <= 130 and y <= 130 and x < y:
        c.create_oval(x-3, y-3, x+3, y+3, fill="blue", width=0)
    elif x <= 130 and y >= 130 and 260 - y>x:
        c.create_oval(x-3, y-3, x+3, y+3, fill="blue", width=0)
    elif y < 130:
        c.create_oval(x-3, y-3, x+3, y+3, fill="white", width=0)
    elif y > 130:
        c.create_oval(x-3, y-3, x+3, y+3, fill="red", width=0)
tkinter.mainloop()
"""
#19
"""
import random
nums = []
eur = 20
print(f"začínam so sumou: {eur}\nštart ", end="")
for i in range(1000):
    for i in range(3):
        cislo = random.randint(1, 20)
        nums.append(cislo)
    if nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
        print("+5", end="")
        eur+=5
    if nums[0] == nums[1] == nums[2]:
        print("+100", end="")
        eur+=100
    else:
        print("-1", end="")
        eur-=1
    nums.clear()
    if eur <=0:
        break
print(f"\nzostalo mi {eur} euro")
"""
#20 - netusim ako to spravit bez listu
"""
n = int(input("zadaj cislo: "))
bankovky = [100, 50, 20, 10, 5, 2, 1]
for i in bankovky:
    if n >= i:
        print(f"{n//i} krat hodnota {i}")
        n = n%i
"""
#21 ??????????
# 22
"""
import tkinter
import random
a = 10, 100
b = 250, 10
c = 300, 250
m = [0, 0]
canvas = tkinter.Canvas()
canvas.pack()
flag=True
while flag:
    farba = random.randint(1, 255**3)
    canvas.create_polygon(a, b, c, fill=f"#{farba:06x}")
    m = a # m, pretoze hodnota a[0] a a[1] sa uz raz zmeni, takze 
          # c[0], c[1] by bolo nekorektne vypocitane
    a = [abs(a[0]+b[0])/2, abs(a[1]+b[1])/2] 
    b = [abs(b[0]+c[0])/2, abs(b[1]+c[1])/2]
    c = [abs(c[0]+m[0])/2, abs(c[1]+m[1])/2]
    print(a, b, c)
    # pytagorova veta pre vypocet dlzky strany, pouzivam (delta x) a (delta y)
    h = ((abs(a[0]-b[0]))**2  + abs(a[1]-b[1])**2)**0.5
    if h<30:
        flag = False
tkinter.mainloop()
"""
# 2. tyzdenny projekt
"""
import tkinter
import math
canvas = tkinter.Canvas()
canvas.pack()
start_length = 20# int(input("Zadej štartovou délku: "))
increment = 3# int(input("Zadej inkrement: "))
sum_lengths = 1950# int(input("Zadej součet délek: "))
x = 175
y = 150
angle = 180
length = start_length
while sum_lengths > 0:
    end_x = x + length * math.cos(angle)
    end_y = y + length * math.sin(angle)
    canvas.create_line(x, y, end_x, end_y)
    x = end_x
    y = end_y
    angle -= math.pi / 2
    length += increment
    sum_lengths -= length
tkinter.mainloop()
"""