import tkinter, random, math

c = tkinter.Canvas(width=600, height=600)
c.pack()

n_start = 12
uhol = 360/n_start
p_start = 0
priratavanie = 5
aktiv = True
n = n_start
x0, y0, r0 = 300, 300, 100


def kruhas(i, farba="klasik"):
    r = r0*math.sin(math.radians(uhol/2))
    x = x0 + r0*math.cos(math.radians(uhol*i))
    y = y0 + r0*math.sin(math.radians(uhol*i))
    if farba == "klasik":
        c.create_oval(x-r, y-r, x+r, y+r, fill="white", outline="")
    elif farba == "tmavy":
        c.create_oval(x-r, y-r, x+r, y+r, fill="#999999", tags="farebny", outline="")
    elif farba == "tmavsi":
        c.create_oval(x-r, y-r, x+r, y+r, fill="#666666", tags="farebny", outline="")
    elif farba == "najtmavsi":
        c.create_oval(x-r, y-r, x+r, y+r, fill="#444444", tags="farebny", outline="")


def percenta(percento):
    c.create_text(x0, y0+200, text=f"{percento:02d}%", font="timesnewroman 39", tags="prsent")


for i in range(n_start):
    kruhas(i)

while aktiv:
    for i in range(100):
        if p_start < 100:
            percenta(p_start)
            if i%5==0:
                p_start += priratavanie
        else:
            break
        kruhas(i-1, farba="najtmavsi")
        kruhas(i-2, farba="tmavsi")
        kruhas(i-3, farba="tmavy")
        c.update()
        c.after(80)
        c.delete("farebny", "prsent")
    #percenta(100)
    # c.update()
    # c.after(100)
    c.delete("all")
    aktiv = False
    c.create_text(300, 300, text="JEBO", font="arial 110")

tkinter.mainloop()