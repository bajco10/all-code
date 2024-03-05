import tkinter
from random import choice as rc
c = tkinter.Canvas(width=500, height=400)
c.pack()
slova = ["jablko", "programovanie", "koleso", "uloha", "riesenia"]
pis = ""
slovo = ""
text = []
ids = None
bezi_hra = False

def start_hry(e):
    global bezi_hra, text, ids, slova, bezi_hra, pis, slovo
    if not bezi_hra:
        bezi_hra = True
        if len(slova) > 0:
            c.delete("vysledok")
            pis = " "
            slovo = rc(slova)
            slova.remove(slovo)
            text = ["*" for i in range(len(slovo))] # spravím si list s dĺžkou slova
            ids = c.create_text(250, 30, text="".join(text), font="Calibri 22")
            
def klavesa(e):
    global pis, slovo
    pis = e.char

def casovac():
    global pis, text, ids, slovo, bezi_hra, slova
    if bezi_hra:
        if pis in slovo:
            vyskyt = [index for index, char in enumerate(slovo) if char==pis]
            for i in vyskyt:
                text[i] = pis
            c.itemconfig(ids, text = "".join(text), font="Calibri 22")
        if "".join(text) != slovo:
            c.move(ids, 0, 0.4) # 0 na x-osi, +0.4 na y-osi
            zisti_prehru() # poslem si do funkcie y-suradnicu padajuceho slova
        else:
            c.delete(ids)
            if len(slova) > 0:
                pis = ""
                slovo = rc(slova)
                slova.remove(slovo)
                text = ["*" for i in range(len(slovo))] # spravím si list s dĺžkou slova
                ids = c.create_text(250, 30, text="".join(text))
            else:
                    # vypisat, ze som vyhral
                c.create_text(250, 200, text="Vyhral si!", fill="green", font="Arial 30", tags="vysledok")
                slova = ["jablko", "programovanie", "koleso", "uloha", "riesenia"]
                bezi_hra = False
    c.after(10, casovac) # dolezite mat maly "after", nech sa to často obnovuje kvoli vstupu

def zisti_prehru():
    # zistim, ci je text pod spodnou hranicou obrazovky -> prehral som
    global bezi_hra, ids, slova
    suradnice = c.coords(ids)
    y_spodok = 400
    if suradnice:
        y_textu = suradnice[1]
        if y_textu >= y_spodok:
            bezi_hra = False
            c.delete(ids)
            c.create_text(250, 200, text="Prehral si!", fill="red", font="Arial 30", tags="vysledok")
            slova = ["jablko", "programovanie", "koleso", "uloha", "riesenia"]

casovac()

c.bind_all("<Key>", klavesa)
c.bind("<1>", start_hry)
c.mainloop()