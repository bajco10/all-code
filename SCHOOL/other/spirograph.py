import tkinter, math, random

c = tkinter.Canvas(width=900, height=900)
c.pack()

x, y, r_velke = 450, 450, 300
# c.create_oval(x-r_velke, y-r_velke, x+r_velke, y+r_velke)

def kruzok(x, y, r_male, r_velke, r_rucicka, uhol, n1, n2):
    r_velke -= r_male
    xm = x + r_velke * math.cos(math.radians(n1*uhol))
    ym = y + r_velke * math.sin(math.radians(n1*uhol))
    # c.create_oval(xm-r_male, ym-r_male, xm+r_male, ym+r_male, tags="c")
    
    xr = xm + r_rucicka * math.cos(math.radians(n2* -uhol))
    yr = ym + r_rucicka * math.sin(math.radians(n2* -uhol))

    # c.create_line(xm, ym, xr, yr, arrow="last", tags="c")
    return xr, yr
    #c.create_oval(xr -2, yr-2, xr+2, yr+2, fill="black", outline="")


#nahodne

r_male = random.randrange(150, 400)
r_velke = random.randrange(100, 400)
r_rucicka = random.randrange(30, 100)
n1 = round(random.uniform(1, 3), 2)
n2 = round(random.uniform(1, 3), 2)

print(f"r_male - {r_male}")
print(f"r_velke - {r_velke}")
print(f"r_rucicka - {r_rucicka}")
print(f"n1 - {n1}")
print(f"n2 - {n2}")

while True:
    uhol = 0
    while True:
        # kruzok(x, y, r_male, r_velke, r_rucicka, uhol=uhol, n1=n1, n2=n2)
        c.create_line(kruzok(x, y, r_male, r_velke, r_rucicka, uhol=uhol, n1=n1, n2=n2), kruzok(x, y, r_male, r_velke, r_rucicka, uhol=uhol-1, n1=n1, n2=n2))
        uhol-=1
        c.after(2)
        c.update()
        c.delete("c")

tkinter.mainloop()