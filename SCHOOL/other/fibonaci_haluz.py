import tkinter
c = tkinter.Canvas(width=300, height=600)
c.pack()
def fibonacci(n):
    if n < 2:
        return n
    f1, f2 = 0, 1
    for i in range(n-1):
        f1, f2 = f2, f1+f2
    return f2

def kresli(x, y, n, font="arial 17"):
    c.create_text(x, y, text = n, font=font)

def fibonacci_ciselka(cislo, pocet):
    mensie, vacsie = [], []

    """for i in range(cislo, cislo+pocet):
        vacsie.append(fibonacci(i))
        
    for i in range(cislo, cislo-pocet):
        mensie.append(fibonacci(i))"""
    
    x, y = 150, 300
    kresli(x, y, fibonacci(cislo), font="arial 17 bold")

    kresli(x, y, 122)
    for i in range(cislo, cislo+pocet):
        y+=20
        kresli(x, y, i)

print(fibonacci(12))

c.mainloop()