import tkinter
c = tkinter.Canvas(width=300, height=800)
c.pack()

def je_prvo(cislo):
    pocet = 0
    for i in range(1, cislo+1):
        if cislo%i==0:
            pocet +=1
    if pocet == 2:
        return True
    return False

def kresli(x, y, n, font="arial 14"):
    c.create_text(x,y, text=n, font=font)

def cisla(cislo, n_range):
    mensie = []
    vacsie = []
    
    for i in (range(cislo, 1, -1)):
        if len(mensie) >= n_range:
            pass
        else:
            if je_prvo(i):
                mensie.append(i)
    
    for i in range(cislo, cislo**2):
        if len(vacsie) >= n_range:
            pass
        else:
            if je_prvo(i):
                vacsie.append(i)
    
    x, y= 150, 400
    kresli(x, y, cislo, font="arial 14 bold")
    for i in mensie:
        y-=20
        kresli(x, y, i)
    
    y = 400
    for i in vacsie:
        y+=20
        kresli(x, y, i)
        
cisla(2654, 18)
c.mainloop()