import tkinter

c = tkinter.Canvas(width=600, height=400)
c.pack()
r1 = 20
r2 = 30
n = 10
x, y = 50, 50
f1 = "#ffad00"
f2 = "#2dad00"
f3 = "#bc63eb"
for i in range(n):
    c.create_oval(x, y-r1, x+2*r1, y+r1, fill=f1, width=0)
    x += 2*r1
    r1, r2 = r2, r1
    f1, f2 = f2, f1
    f2, f3 = f3, f2
c.mainloop()