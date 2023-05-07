import tkinter
canvas = tkinter.Canvas(width=600, height=300)
canvas.pack()
a = (50, 150)
b = (150, 0)
c = (250, 150)
d = (150, 300)
e = (50, 150)

m = (150, 75)
n = (150, 215)
canvas.create_line(a, b, c, d, e, width=5)
canvas.create_line(m, n, width=5)
tkinter.mainloop()