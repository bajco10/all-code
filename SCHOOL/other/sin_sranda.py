import tkinter, math
c = tkinter.Canvas(width=1200, height=700)
c.pack()
uhol = 0
x, y = 0, 250

c.create_line(0, 350, 1200, 350, width=2, fill="black")
for i in range(360):
    c.create_oval(x-3, y-3, x+3, y+3, fill="red", outline="")
    y+= (math.sin(math.radians(uhol)))*20
    uhol += 10
    x+=10

tkinter.mainloop()