import tkinter, math
c = tkinter.Canvas(width=1000, height=400)
c.pack()
def sinusoida(rad):
    c.create_line(0, 200, 1000, 200) # x-os
    c.create_line(50, 0, 50, 400) # y-os
    x0, y0 = 50, 200
    for i in range(0, rad*100, 1):
        c.update()
        c.after(2)
        # i = i/10
        x = i + x0
        y = y0-math.sin((i/100)*math.pi)*100
        if 0.01> math.sin((i/100)) > -0.01:
            print("x-int: ", i)
        c.create_oval(x-2, y-2, x+2, y+2, fill="red", outline="")

def cosinusoida(rad):
    x0, y0 = 50, 200
    for i in range(0, rad*100, 1):
        c.update()
        c.after(2)
        x = i+x0
        y = y0-math.cos((i/100)*math.pi)*100
        c.create_oval(x-2, y-2, x+2, y+2, fill="blue", outline="")
# print(math.sin(0))
# print(math.sin(2*math.pi))
sinusoida(6)
cosinusoida(6)
c.mainloop()