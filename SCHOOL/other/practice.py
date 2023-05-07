
"""
# pocet_riadkov = int(input("zadaj n: "))
pocet_riadkov = 5
for cislo_riadku in (range(1, pocet_riadkov + 1)):
    print(" "* (pocet_riadkov-cislo_riadku), end="")
    for cislo in (range(1, cislo_riadku+1)):
        print(cislo, end="")
    for cislo in reversed(range(1, cislo_riadku)):
        print(cislo, end="")
    print()


pocet_riadkov = 5
for cislo_riadku in (range(1, pocet_riadkov + 1)):
    print(" "* (pocet_riadkov-cislo_riadku), end="")
"""
"""
n = 5
for i in range(1,n+1):              # 1, 2, 3, 4, 5
    print(' '*(n-i), end='')        # 4, 3, 2, 1, 0
    for j in range(1, i+1):         # 1; 1, 2; 1, 2, 3; 1, 2, 3, 4; 1, 2, 3, 4, 5
        print(j+n-i, end='')        # 1+5 - 1; 2+5-1; 3+5-1
    for k in range(1, i):
        print(n-k, end='')
    print()


# pocet_riadkov = int(input("zadaj n: "))
pocet_riadkov = 5
for cislo_riadku in (range(1, pocet_riadkov + 1)):
    print(" "* (pocet_riadkov-cislo_riadku), end="")
    for cislo in (range(1, cislo_riadku+1)):
        print(cislo+pocet_riadkov-cislo_riadku, end="")
    for cislo in reversed(range(1, cislo_riadku)):
        print(pocet_riadkov - cislo, end="")
    print()
"""


"""
n = 9

for i in range(1, n+1):
    print(i, end="")
for j in reversed(range(1, n)):
    print(j, end="")
print()
for i in reversed(range(1, n)):
    for j in range(1, i+1):
        print(j, end="")
    print(" " * ((n-i)*2-1), end="")
    for i in reversed(range(1, i+1)):
        print(i, end="")
    print()
"""



"""
n = 9
for i in range(1, n+1):
    print(i, end='')
for i in range(8, 0, -1):
    print(i, end='')
print()
n -= 1
for i in reversed(range(1, n)):
    for j in range(1, i+2):
        print(j, end="")
    print(" " * ((n-i)*2-1), end="")
    for i in reversed(range(1, i+2)):
        print(i, end="")
    print()
"""
"""n = 8
for i in range(1,n+1):
    print(' '*(n-i), end='')        
    for j in range(1, i+1):       
        print(j+n-i, end='')        
    for k in range(1, i):
        print(n-k, end='')
    print()"""


#tkinter+if/while test skupina 1
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
            c.create_text(x, y, text=n, font="arial 20")
            

y = 50
for i in range(10):
    x = 50
    for i in range(10):
        stvorec(x, y)
        x+=45
    y += 45

tkinter.mainloop()


n = "242424240482"
print(n[-4:])






