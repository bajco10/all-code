""" Vo vacsine programov su hodnoty pevne danne, nech nemusime ist cez milion inputov.
    Programy kde to tak nie je, su okomentovane - aby boli nefunkcne.
    zdroj zadani: https://input.sk/python2017/04.html   # bajana
"""
#1
"""
x, y = 7, 'ab'
8 < x <= 7
x <= 3 + x // 2
y != 2 * x or 2 * y == 'abab'
x < x + 1 < 2 * x

print(x // 8 or x * y) # ababababababab
print(x or y)   # 7
print(x and y)  # ab
print(not y)    # False
print(not x%2)  # False
"""
#2
"""
import cmath

a = int(input("zadaj a: "))
b = int(input("zadaj b: "))
c = int(input("zadaj c: "))

d = (b**2) - (4*a*c) # vzorec na diskriminant

if d > 0:
    print("rovnica ma dva rozne korene")
elif d == 0:
    print("rovnica ma jeden koren")
else:
    print("rovnica nema realne korene")

# keby nahodou chceme zistit dane korene

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print(sol1, sol2)

"""
#3
"""
# 6 -> pocet cisel delitelnych 2, ktore sa nachadzaju v range() zadaneho cisla 
# alebo teda v hodnote (asi? XD)
cislo1 = 0
cislo2 = int(input("? "))
while cislo2>0:
    if cislo2%2 == 0:
        cislo2 //= 2
    else:
        cislo2 -= 1
    cislo1 += 1
print(cislo1)
"""
#4
"""
cislo = int(input("zadaj cislo: "))
while cislo:
    print(cislo%10, end=" ")
    cislo = cislo //10
"""
#5
"""
cislo = int(input("zadaj cislo: "))
sucet = 0
while cislo:
    sucet += (cislo % 10)
    cislo //= 10
print(f"ciferny sucet je {sucet}") 
"""
#6
"""
cislo = str(input("zadaj cislo: "))
cifra = str(input("zadaj cifru: "))
pocet = 0
for i in cislo:
    # print(i)
    if i == cifra:
        pocet += 1

print(f"cifra {cifra} sa vyskytla {pocet} krat")
"""
#7
"""
cislo = 655364
delitel = 2
print(cislo, "=", end=" ")
count = 0
while cislo > 1:
    if cislo % delitel == 0:
        if count != 0:
            print("*", delitel, end=" ")
        else:
            print(delitel, end=" ")
            count += 1
        cislo = cislo / delitel
    else:
        delitel += 1
"""
#8
"""
k = 1
n = 0
while k < 1000000:
    n += 1
    k = k*n
print(n-1) 
# preto n minus jedna, lebo while-loop vykona dane prikazy aj pre n = 10
# a az potom sa podmienka vyhodnoti ako neplatna (False)
"""
#9     https://en.wikipedia.org/wiki/Fibonacci_number
"""
n = 0
first_value = 0
second_value = 1
i = 0
while n < 1000000:
    if(n<1):
        n = 1
    else:
        n = first_value + second_value
        first_value = second_value
        second_value = n
    print(n)
    i += 1
print(i-1)
"""
#10
"""
import random
for i in range(10):
    while random.randrange(4):
        print(end='x')
    print()
# tymto programom dokazeme simulovat/znazornovat pravdepodobnost
# program 10 krat simuluje situaciu, kde mame sancu 3:1 uspiet 
# alebo teda 1/3 na to zlyhat, pokial sme uspesny, program ide do nekonecna 
# az kym sa nevyskytne situacia, kde dostaneme hodnotu (False) (teda random
# vyberie cislo 0) ked sa toto stane, program dokonci while-loop 
# a pokracuje az kym neprejde cely range(10)
"""
#11
"""
import tkinter
import random
vel = 500
n = 1000
vzdialenost = 0
vsetkych= 0
cervenych = 0
modrych = 0
canvas = tkinter.Canvas(width=vel, height=vel, bg="white")
canvas.pack()
while n > 0:
    x = random.randrange(0, vel)
    y = random.randrange(0, vel)
    vzdialenost = (x**2 + y**2)**0.5
    if vzdialenost < vel:
        canvas.create_oval(x, y, x + 3, y-3,fill="red")
        cervenych +=1
    else:
        canvas.create_oval(x, y, x + 3, y-3,fill="blue")
        modrych +=1
    vsetkych +=1
    n-=1
print((cervenych/vsetkych)*4)
canvas.mainloop()
# lebo nieco s kruhom...
"""

#12
"""
# vzdialenost = ( (x2 - x1)**2 + (y2 - y1)**2 ) **0.5
import tkinter
import random
canvas = tkinter.Canvas(width=300, height=200, bg="white")
canvas.pack()
n = 1000            # bod1 = 100, 100
vzdialenost = 0     # bod2 = 180, 100
x1, y1 = 100, 100
x2, y2 = 180, 100
while n > 0:
    x = random.randrange(0, 300)
    y = random.randrange(0, 200)
    vzdialenost = (x**2 + y**2)**0.5
    if (((x1 - x)**2 + (y1 - y)**2) ** 0.5) < 80:
        canvas.create_oval(x, y, x+3, y-3, fill="red")
    elif (((x2 - x)**2 + (y2 - y)**2) ** 0.5) < 90:
        canvas.create_oval(x, y, x+3, y-3, fill="blue")
    else:
        canvas.create_oval(x, y, x+3, y-3, fill="black")
    n-=1
canvas.mainloop()
"""
#13
"""
import tkinter
canvas = tkinter.Canvas(width=250, height=250, bg="white")
canvas.pack()
farba1 = "salmon"
farba2 = "black"
x = 5
y = 5
for i in range(8):
    for i in range(8):
        canvas.create_rectangle(x, y, x+30, y+30, fill=farba1)
        farba1, farba2 = farba2, farba1
        x += 30
    y += 30
    x = x - 8*30
    farba1, farba2 = farba2, farba1
canvas.mainloop()
"""
#14
"""
import tkinter

sirka, vyska = 200, 150     # 800, 600
canvas = tkinter.Canvas(width=sirka, height=vyska, bg="white")
canvas.pack()
farba1 = "salmon"
farba2 = "black"
x, y = 5, 5
pocet_stvorcov_x = (sirka-10) // 30
pocet_stvorcov_y = (vyska-10) // 30

while pocet_stvorcov_y > 0:
    while pocet_stvorcov_x > 0:
        canvas.create_rectangle(x, y, x+30, y+30, fill=farba1)
        farba1, farba2 = farba2, farba1
        x += 30
        pocet_stvorcov_x -= 1
    pocet_stvorcov_x = sirka//30    # "resetujeme" pocet stvorcov, nech sa while
                                    # loop pusti znova
    pocet_stvorcov_y -= 1
    y += 30
    x = x - pocet_stvorcov_x*30
    farba1, farba2 = farba2, farba1
canvas.mainloop()
"""
# 1. domáce zadanie
"""
n = int(input("n: "))
znak1 = input("znak1: ")
znak2 = input("znak2: ")

i = 1
while(i <= n):
    j = 1
    while(j <= n):
        if(i == 1 or i == n or j == 1 or j == n
           or i == j or j == (n - i) + 1):
            print(znak1, end = '')
        else:
            print(znak2, end = '')
        j += 1
    print()
    i += 1
"""
# i a j predstavuju y a x suradnicu
# i==1 -> prvy stlpec
# i==n -> posledny stlpec
# j==1 -> prvy riadok
# j==n -> posledny riadok
# i==j -> stred stvorca
# j==(n-i)+1 -> ked x suradnica sa rovna y (i sa vo while loope pripocitava)
                # +1 -> lebo prvy riadok je cely plny (nerata sa)

# dalsi sposob, akym sa da spravit dane zadanie
"""
n = int(input("n: "))
znak1 = input("znak1: ")
znak2 = input("znak2: ")

i = n
while(i > 0):
    j = n
    while(j > 0):
        if(i == 1 or i == n or j == 1 or j == n
           or i == j or j == (n - i) + 1):
            print(znak1, end = '')
        else:
            print(znak2, end = '')
        j -= 1
    print()
    i -= 1
"""



