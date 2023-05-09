#1 bajana
def teploty(teplota):
    teplota = teplota.upper()
    teplota = teplota.replace(" ", "")
    hodnota = ""
    for i in teplota:
            if i in ("0123456789."):
                hodnota+=i
    if "F" in teplota:
        konvertovana_hodnota = round((float(hodnota)-32)/1.8, 1)
        return f"{hodnota}F = {konvertovana_hodnota}C"
    elif "C" in teplota:
        konvertovana_hodnota = round((float(hodnota)*1.8)+32, 1)
        return f"{hodnota}C = {konvertovana_hodnota}F"
    else:
        return "Toto prekonvertovať neviem."
    
print(teploty("45F"))
print(teploty("37.6257C"))
print(teploty("2 c"))
print(teploty("157 f"))
print(teploty("157 K"))

#2 bajana
import tkinter
c = tkinter.Canvas()
c.pack()
def stvorce(vel, retazec):
    x, y = 20, 50
    farby = retazec.split(" ")
    for i in farby:
        c.create_rectangle(x, y, x+vel, y+vel, fill=f"{i}")
        x+= vel + 2
stvorce(40, 'red blue purple red gold')
c.mainloop()