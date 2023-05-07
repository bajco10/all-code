#2
"""
n = int(input("zadaj cislo: "))
k = 2
print(f"{n} = ", end="")
while True:
    if n%k==0:
        n = n/k
        if n == 1:
            print(k, end="")
        else:
            print(k, end=" * ")
    else:
        k += 1
    if n ==1:
        break
"""
#9
"""
import tkinter
import random
c = tkinter.Canvas()
c.pack()
k = 21
x, y = 20, 20
hodnota = 0
m = 0
for i in range(10):
    while True:
        m = random.randint(1, 4)
        hodnota+=m
        c.create_oval(x-10, y-10, x+10, y+10, fill="white")
        c.create_text(x, y, text=m, font="arial 14")
        x+=25
        if hodnota > k:
            c.create_text(330, y, text="ŠKODA", fill="red")
            y+=25
            x = 20
            hodnota = 0
            break
        elif hodnota == k:
            c.create_text(330, y, text="HURÁ", fill="green")
            y+=25
            x = 20
            hodnota = 0
            break
tkinter.mainloop()
"""
#11
"""
import tkinter
import random
c = tkinter.Canvas()
c.pack()
n = 7
x_cor = []
y_cor = []
for i in range(n):
    x = random.randrange(60, 330)
    y = random.randrange(60, 260)
    c.create_oval(x-3, y-3, x+3, y+3, fill="red")
    x_cor.append(x)
    y_cor.append(y)
c.create_rectangle(max(x_cor), max(y_cor), min(x_cor), min(y_cor), fill="", outline="blue")

tkinter.mainloop()
"""