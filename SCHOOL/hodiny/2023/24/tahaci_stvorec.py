import tkinter
c = tkinter.Canvas(width=800, height=800)
c.pack()
body = [(100, 50),(100, 250), (200, 50), (200, 250)]
body = {
    "D" : (300, 300),
    "A" : (300, 500),
    "C" : (500, 300),
    "B" : (500, 500)
}
def kresli_bod(sur):
    c.create_oval(sur[0]-5, sur[1]-5, sur[0]+5, sur[1]+5, fill="red")
def kresli_ciaru(a, b):
    c.create_line(a, b, fill="blue", width=4)


# kresli_ciaru(body["A"], body["B"])
# kresli_ciaru(body["B"], body["C"])
# kresli_ciaru(body["C"], body["D"])
# kresli_ciaru(body["D"], body["A"])


"""for nazov, suradnice in body.items():
    kresli_bod(suradnice)"""


c.create_polygon(body["A"], body["B"], body["C"], body["D"], width=2, fill="white", outline="black")
def tahanie(event):
    pass
def havr(event):
    c.create_text(event.x, event.y, text="*")
def klik(event):
    for meno, suradnice in 

c.bind("<Motion>", havr)
c.mainloop()