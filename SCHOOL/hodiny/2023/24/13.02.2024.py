import tkinter, random
c = tkinter.Canvas(width=600, height=400)
c.pack()
slovo = random.choice(("koleso", "olovo", "oliva", "koza"))

stv_pis = {}

def stvorceky(slovo):
    n = len(slovo)
    x, y = 50, 50
    for i in range(len(slovo)):
        c.create_rectangle(x+50, y+50, x, y, fill="light grey", tags="stv")
        x+=60

pis_sur = {}
dlzka_slova = len(slovo)
def pismena(slovo):
    global pis_sur
    for i in slovo:
        x_s, y_s = random.randrange(50, 550), random.randrange(30, 370)
        c.create_text(x_s, y_s, text=i, font="Arial 27", tags=i)
        pis_sur[i] = (x_s, y_s)

naco = None
def klik(e):
    # print(c.find_overlapping(e.x-10, e.y-10, e.x+10, e.y+10))
    # print(c.bbox("current"))
    global naco
    naco = c.find_withtag("current")

def tahanie(e):
    global dlzka_slova
    # p = max(c.find_overlapping(e.x-5, e.y-5, e.x+5, e.y+5))
    idcko = max(naco)
    if naco and idcko > dlzka_slova:
        c.coords(str(idcko), e.x, e.y)
    
dz = []
for i in slovo:
    dz.append(i)
def kontroluj(e):
    global dz
    global dlzka_slova
    novy_zoznam = []
    x, y = 50, 50
    for i in range(dlzka_slova):
        cotam = c.find_overlapping(x+50, y+50, x, y)
        # pismeno = c.cget(max(cotam), "text")
        pismeno = c.gettags(max(cotam))[0]
        if max(cotam)>dlzka_slova:
            novy_zoznam.append(pismeno)
        else:
            novy_zoznam.append("")
        x+=60
    if dz == novy_zoznam:
        c.create_text(300, 200, text="Hotovo!", font="Arial 44", tags="hotovo")
    else:
        c.delete("hotovo")
    print(novy_zoznam)
    

stvorceky(slovo)
pismena(slovo)


c.bind("<Button-1>", klik)
c.bind("<B1-Motion>", tahanie)
c.bind("<ButtonRelease-1>", kontroluj)
c.mainloop()