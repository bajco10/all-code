"""import tkinter
c = tkinter.Canvas(width=300, height=600)
c.pack()

def je_prvo(cislo):
    pocet = 0
    for i in range(1, cislo+1):
        if cislo%i==0:
            pocet +=1
    if pocet == 2:
        return True
    return False

def kresli(x, y, n, font="arial 22", fill="black"):
    c.create_text(x, y, text=n, font=font, fill=fill)

def hladaj_prvocisla(cislo, kolko, podmienka):
    podmienka_string = str(podmienka)
    mensie = []
    vacsie = []
    for i in range(cislo, 1, -1):
        if len(mensie) >= kolko:
            pass
        else:
            if je_prvo(i):
                m = str(i)
                if m[-1] != podmienka_string:
                    mensie.append(i)
    for i in range(cislo, cislo**2):
        if len(vacsie) >= kolko:
            pass
        else:
            if je_prvo(i):
                m = str(i)
                # print(m)
                if m[-1] != podmienka_string:
                    vacsie.append(i)
    
    x, y = 150, 300
    kresli(x, y, cislo, font="arial 22 bold")
    for i in mensie:
        y-=30
        kresli(x, y, i, fill="blue")
    
    y = 300

    for i in vacsie:
        y+=30
        kresli(x, y, i, fill="green")


    
    

hladaj_prvocisla(27, 5, 1)




c.mainloop()"""


import tkinter
c = tkinter.Canvas(width=300, height=600)
c.pack()

def je_prvo(cislo):
    pocet = 0
    for i in range(1, cislo+1):
        if cislo%i==0:
            pocet +=1
    if pocet == 2:
        return True
    return False

def kresli(x, y, n, font="arial 22", fill="black"):
    c.create_text(x, y, text=n, font=font, fill=fill)

def hladaj_prvocisla(cislo, kolko, podmienka):
    x, y = 150, 300
    kresli(x, y, cislo, font="arial 22 bold")
    podmienka_string = str(podmienka)
    pocet_cisel = 0
    for i in range(cislo, 1, -1):
        if pocet_cisel < kolko:
            if je_prvo(i):
                m = str(i)
                if m[-1] != podmienka_string:
                    pocet_cisel +=1
                    y-=30
                    kresli(x, y, i, fill="green")
    
    pocet_cisel, y = 0, 300

    for i in range(cislo, cislo**2):
        if pocet_cisel < kolko:
            if je_prvo(i):
                m = str(i)
                if m[-1] != podmienka_string:
                    pocet_cisel+=1
                    y+=30
                    kresli(x, y, i, fill="blue")
                    

hladaj_prvocisla(18, 5, 3)

c.mainloop()

