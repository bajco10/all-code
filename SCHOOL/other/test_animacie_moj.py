import tkinter, math, random
c=tkinter.Canvas(width=600, height=600)
c.pack()

x, y = 300, 100
r = 200
slovo = "jablko"
n = len(slovo)
uhol = 180/n
r_male = r*math.sin(math.radians(uhol/2))
u, k = 0, 0
o = ((n-1)/2)*uhol+90

def farba():
    return f"#{random.randrange(120, 255):02x}{random.randrange(120, 255):02x}{random.randrange(120, 255):02x}"

def kruzok(u, text):
    c.create_oval(300+r_male+r*math.cos(math.radians(o-uhol*u)),
                100+r_male+r*math.sin(math.radians(o-uhol*u)),
                300-r_male+r*math.cos(math.radians(o-uhol*u)),
                100-r_male+r*math.sin(math.radians(o-uhol*u)),
                fill=farba(), tags="kruhy"
                )
    c.create_text(300+r*math.cos(math.radians(o-uhol*u)),
                100+r*math.sin(math.radians(o-uhol*u)), text=text, font="arial 20", angle=0)

while True:
    for i in range(n):
        kruzok(u, slovo[k])
        u+=1
        k+=1
    k=0
    u=0
    c.update()
    c.delete("kruhy")
    c.after(40)

    

tkinter.mainloop()