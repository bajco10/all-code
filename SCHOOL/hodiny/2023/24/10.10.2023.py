#equalizer
"""
import tkinter, random
canvas = tkinter.Canvas(background='grey', width= 515, height= 420)
canvas.pack()
hz = ['32', '64', '128', '256', '512', '1k', '2k', '4k', '8k', '16k']
green_max = 150
yellow_max = 250
#hore 20 do 350
def column (x, y, height):
    canvas.create_rectangle(x + 20, y, x + 50, y - height, fill = 'green', width=0)
    if height > green_max:
        canvas.create_rectangle(x + 20, y - green_max, x + 50, y - height, fill = 'yellow', width=0)
    if height > yellow_max:
        canvas.create_rectangle(x + 20, y - yellow_max, x + 50, y - height, fill = 'red', width=0)

while True:
    for i,j in enumerate(hz):
        column(i * 50, 370, random.randrange(30, 350))
        canvas.create_text(i * 50 + 35, 390, text=j, fill='green')
    canvas.update()
    canvas.after(1)
    canvas.delete('all')
canvas.mainloop()"""

# tajnicka - dorobit!!!

import tkinter

c = tkinter.Canvas(width=600, height=600)
c.pack()

with open(r"C:\Users\tomas\Desktop\code\all-code\SCHOOL\hodiny\2023\24\tajnicka.txt", encoding="utf8") as subor:
    x = subor.readlines()
    vysledok = x[0]
    vysledok = vysledok.strip()
    riadky = []
    for i in x[1:]:
        riadky.append(i.strip().lower())
    print(vysledok, riadky)

def kresli_stvorcek(x, y, text, je_hodnota):
    if je_hodnota:
        c.create_rectangle(x, y, x+40, y+40, fill="grey", width=2)
        c.create_text(x+20, y+20, text=text, font="Arial 19")
    else:
        c.create_rectangle(x, y, x+40, y+40, fill="white", width=2)
        c.create_text(x+20, y+20, text=text, font="freemono 19")

x, y = 200, 20
# je_hodnota = False
for i in range(len(vysledok)):
    hladam = vysledok[i].lower()
    pozicia = riadky[i].index(vysledok[i].lower())
    x = 200
    x -= pozicia*40
    for j in riadky[i]:
        if riadky[i].index(j) != pozicia:
            kresli_stvorcek(x, y, j, False)
        else:
            kresli_stvorcek(x, y, j, True)
        x+=40
    y+=40


        
c.mainloop()
