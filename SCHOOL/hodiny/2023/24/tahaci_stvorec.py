# zobrazit nazvy bodov, len ked hover a ked taham?
# spravit hover!
import tkinter

c = tkinter.Canvas(width=800, height=800)
c.pack()

body = {
    "D": (300, 300),
    "A": (300, 500),
    "C": (500, 300),
    "B": (500, 500)
}

# globalna premenna na bod, ktory prave taham
tahany_bod = None

def zaciatok_tahania(event):
    global tahany_bod
    for name, coord in body.items():
        if coord[0]-20 < event.x < coord[0]+20 and coord[1]-20 < event.y < coord[1]+20: # zistim, ci som klikol zacal tahat v okoli nejakeho bodu
            tahany_bod = name
            update_kruhu(name, event.x, event.y)

def tahanie(event):
    global tahany_bod # body, kt. taham
    if tahany_bod is not None:
        body[tahany_bod] = (event.x, event.y) # menim suradnice "tahaneho" bodu na tie kurzoru
        novy_uholnik()
        update_bodu(tahany_bod, (event.x, event.y))
        update_kruhu(tahany_bod, event.x, event.y)

def koniec_tahania(event):
    global tahany_bod
    tahany_bod = None # uz netaham ziadny bod

"""def hover(event):
    for name, coord in body.items():
        if coord[0]-20 < event.x < coord[0]+20 and coord[1]-20 < event.y < coord[1]+20: # zistim, ci som je hover v okoli bodu
            c.create_oval(coord[0]-20, coord[1]-20, coord[0]+20, coord[1]+20, fill=f'rgba(20, 255, 20, {100})', outline="black", width=2)
     """   

def novy_uholnik():
    # updatnem polygon s upravenym bodom
    c.coords("uholnik", *body["A"], *body["B"], *body["C"], *body["D"])
# def kruh_na_hover():
def update_bodu(meno, suradnice):
    c.coords(meno, suradnice)
def update_kruhu(tag, x, y):
    c.coords(tag, x-20, y-20, x+20, y+20)
c.bind("<Button-1>", zaciatok_tahania)
c.bind("<B1-Motion>", tahanie)
c.bind("<ButtonRelease-1>", koniec_tahania)
# c.bind("<B1-Motion>", hover)

# stvorec, s ktorym zacinam na ploche
# *body["A"] -> rozbali values pre tento kluc napr. (suradnica_x, suradnica_y) -> (300, 300) => tuple
c.create_polygon(*body["A"], *body["B"], *body["C"], *body["D"], width=2, fill="white", outline="black", tags="uholnik")
# mena bodov
for meno, suradnice in body.items():
    c.create_text(suradnice, text=meno, font="Arial 15", tags=f"{meno}")
# kruhy
for name, coord in body.items():
    c.create_oval(coord[0]-20, coord[1]-20, coord[0]+20, coord[1]+20, fill="light green", outline="black", width=2, tags=name)

c.mainloop()
