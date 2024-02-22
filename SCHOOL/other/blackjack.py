# split a double!
# na zacitok len farba+hodnota, neskôr celé karty??

# keď sa vyberie bet spawnúť žetón, po konci kola ho zmazať
# ak má hráč BJ pozrieť, či aj díler nemá, ak áno tak PUSH
# pridať scenar kde hráč/díler dostane dve A -> buď 12 alebo 2
# diler prve A za 11 (ak to neznamená bust), každé ďalšie za 1
import tkinter, random
c = tkinter.Canvas(width=800, height=600, bg="light grey")
c.pack()


"""veci co sa vzdy zobrazujú!"""
# stol
x1, x2, y1, y2, r = 20, 780, 40, 560, 60
points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, 
          x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, 
          x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
c.create_polygon(points, fill="dark green", smooth=True)
# podlozka pod zeton
c.create_oval(360, 520, 440, 550, fill="green", outline="")
# tlacitko hit
hit_x, hit_y = 500, 525
c.create_oval(hit_x-20, hit_y-20, hit_x+20, hit_y+20, fill="light grey", outline="", tags="hit")
c.create_text(hit_x, hit_y, text="+", font="Arial 32", fill="green", tags="hit")
# tlacitko stand
stand_x, stand_y = 550, 525
c.create_oval(stand_x-20, stand_y-20, stand_x+20, stand_y+20, fill="light grey", outline="", tags="stand")
c.create_text(stand_x, stand_y, text="+", font="Arial 32", fill="red", angle=45, tags="stand")
# minus_tlacidko
minus_x, minus_y =70, 530
c.create_rectangle(minus_x-20, minus_y-20, minus_x+20, minus_y+20, fill="light grey", outline="", tags="minus")
c.create_text(minus_x, minus_y-4, text="-", font="Arial 32", tags="minus") # -4 nech je to vycentrované na x-osi :)
# hodnota_displej
hod_x, hod_y = 130, 530
c.create_rectangle(hod_x-40, hod_y-20, hod_x+40, hod_y+20, fill="light grey", outline="")
# !!! hodnota sa bude meniť na základe tlačidiel
stavka = 50
c.create_text(hod_x, hod_y, text=stavka, font="Arial 16", tags="hodnota")
# plus_tlacitko
plus_x, plus_y = 190, 530
c.create_rectangle(plus_x-20, plus_y-20, plus_x+20, plus_y+20, fill="light grey", outline="", tags="plus")
c.create_text(plus_x, plus_y, text="+", font="Arial 32", tags="plus")
# tlačítko Štart
start_x, start_y = 260, 530
c.create_rectangle(start_x-40, start_y-20, start_x+40, start_y+20, fill="light grey", outline="", tags="start")
c.create_text(start_x, start_y, text="Štart", font="Arial 16", tags="start")

# súčet kariet hráč
hrac_x, hrac_y = 400, 580
c.create_text(hrac_x, hrac_y, text="0", font="Arial 16", tags="hrac_sucet")

# súčet kariet díler
dil_x, dil_y = 400, 20
c.create_text(dil_x, dil_y, text="0", font="Arial 16", tags="diler_sucet")


deck = []
for i in range(6):
    """
    funkcia, kt. vytvorí balíček kariet 6-krát (štandard pri bj)
    """
    for suit in "HSCD":
        for value in ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]:
            card = suit + str(value)
            deck.append(card)

# inicializácia premenných
karta_x, karta_y = 400, 500 # pociatocne hodnoty pre moje karty
d_karta_x, d_karta_y = 400, 100 # pociatocne hodnoty pre dilerove karty
moje_karty = []
diler_karty = []
kolo = False
hrac_celkovo, diler_celkovo = 0, 0

zaciatocny_balance = 100
def vykresli_current_skore(skore):
    c.delete("current_skore")
    c.create_text(100, 20, text=f"balance: {skore}$", font="arial 16", tags="current_skore")

def vykresli_high_skore(skore):
    c.delete("high_skore")
    c.create_text(700, 20, text=f"high-score: {skore}$", font="arial 16", tags="high_skore")

def kresli_zeton():
    farba = f"#{random.randrange(255**3):06x}"
    c.create_oval(370, 522, 430, 548, fill=farba, outline="")
def zisti_diler_bj():
    global diler_karty, diler_celkovo
    for karta in diler_karty:
        if "A" in karta:
            zober_kartu(diler_karty)
            s1, s2 = sucet_kariet(diler_karty)
            diler_logika(s1, s2)
            if diler_celkovo==21:
                return True
    return False

def hrac_logika(sucet, sucet_2):
    global kolo, hrac_celkovo, diler_celkovo
    if sucet == 21 or sucet_2 == 21:
        if zisti_diler_bj():
            c.itemconfigure("hrac_sucet", text=str(max(sucet_kariet(moje_karty))))
            vyhodnotenie_hry("Push!")
        else:
            c.itemconfigure("hrac_sucet", text=str(max(sucet_kariet(moje_karty))))
            vyhodnotenie_hry("Blackjack!")
        kolo = False
            # napisat ze hrac automaticky vyhral, vyplatit 3:1?
    elif sucet > 21:
        c.itemconfigure("hrac_sucet", text=str(max(sucet_kariet(moje_karty))))
        vyhodnotenie_hry("Díler vyhral.")
        kolo = False
            # napisat ze hrac automaticky prehral
    elif sucet == sucet_2:
        c.itemconfigure("hrac_sucet", text=str(sucet))
        hrac_celkovo = sucet
    elif sucet != sucet_2 and sucet_2 < 22:
        c.itemconfigure("hrac_sucet", text=f"{str(sucet)}/{str(sucet_2)}")
        hrac_celkovo = sucet_2
    else:
        c.itemconfigure("hrac_sucet", text=str(sucet))
        hrac_celkovo = sucet

def diler_logika(sucet, sucet_2):
    global kolo, hrac_celkovo, diler_celkovo
    if sucet == sucet_2:
        c.itemconfigure("diler_sucet", text=str(sucet))
        diler_celkovo = sucet
    elif sucet != sucet_2 and sucet_2 < 22:
        c.itemconfigure("diler_sucet", text=f"{str(sucet)}/{str(sucet_2)}")
        diler_celkovo = sucet_2
    else:
        c.itemconfigure("diler_sucet", text=str(sucet))
        diler_celkovo = sucet



def zober_kartu(komu):
    """
    funkcia, kt. zoberie kartu jednej z partií
    """
    global karta_x, karta_y, d_karta_x, d_karta_y
    if komu == moje_karty:
        k = random.choice(deck)
        karta(karta_x, karta_y, k)
        # deck.pop(deck.index(k))
        moje_karty.append(k)
        karta_x += 25
        karta_y -= 50
    elif komu == diler_karty:
        k = random.choice(deck)
        karta(d_karta_x, d_karta_y, k)
        # deck.pop(deck.index(k))
        diler_karty.append(k)
        d_karta_x -= 25
        d_karta_y += 50

def sucet_kariet(karty):
    """
    funkcia, kt. sčíta z listu hodnoty kariet, kritická pre logiku oboch strán
    """
    global kolo, hrac_celkovo, diler_celkovo
    sucet = 0
    sucet_2 = 0
    for i in karty:
        i = i.replace("H", "").replace("D","").replace("S", "").replace("C", "")
        if i in "TJQK":
            sucet+=10
            sucet_2+=10
        elif i == "A":
            sucet += 1
            sucet_2 += 11
        else:
            sucet += int(i)
            sucet_2 += int(i)
    return sucet, sucet_2
        
def karta(x, y, value):
    """
    funkcia, kt. vytvára kartu na základe jej farby a znaku (hodnoty)
    + dorobiť aj symboly
    """
    x1 = x-20
    x2 = x+20
    y1 = y-35
    y2 = y+35
    r=20
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, 
          x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, 
          x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    if "H" in value or "D" in value:
        # hearts & diamonds
        # c.create_rectangle(x-20, y-35, x+20, y+35, fill="white", tags="karta")
        c.create_polygon(points, fill="white", tags="karta", smooth=True, outline="black")
        c.create_text(x, y, text=value[-1], font="Arial 30", fill="red", tags="karta")
    else:
        # spades & clubs
        # c.create_rectangle(x-20, y-35, x+20, y+35, fill="white", tags="karta")
        c.create_polygon(points, fill="white", tags="karta", smooth=True, outline="black")
        c.create_text(x, y, text=value[-1], font="Arial 30", fill="black", tags="karta")

def klik(e):
    naco = c.find_withtag("current") # ziskam id toho naco som klikol
    co = (c.gettags(naco[0]))[0]
    global stavka, zaciatocny_balance
    if co == "start":
        if kolo == False and zaciatocny_balance>0:
            c.delete("karta")
            c.delete("stav")
            c.itemconfigure("diler_sucet", text="0")
            c.itemconfigure("hrac_sucet", text="0")
            zaciatocny_balance -= stavka
            start_hry()
    elif co == "hit":
        if kolo == True:
            hit_karty()
    elif co == "stand":
        if kolo == True:
            diler_tahy()
            # kolo == False
    elif co == "plus":
        if kolo == False:
            if (stavka) < zaciatocny_balance:
                stavka += 5
                c.itemconfigure("hodnota", text=str(stavka))
    elif co == "minus":
        if kolo == False:
            if stavka > 5:
                stavka -= 5
                c.itemconfigure("hodnota", text=str(stavka))
def updejt(e):
    global stavka, zaciatocny_balance
    # print("updejt sa spravil")
    vykresli_current_skore(zaciatocny_balance)
    hs = precitaj_skore()
    if int(zaciatocny_balance) > hs:
        prepis_skore(zaciatocny_balance)
        vykresli_high_skore(zaciatocny_balance)
                   
def precitaj_skore():
    with open("bj_skore.txt") as subor:
        s = subor.readlines()
    s = s[0].strip()
    return int(s)

def prepis_skore(hodnota):
    with open("bj_skore.txt", "w") as subor:
        print(str(hodnota), file=subor)

def start_hry():
    global karta_x, karta_y, kolo, d_karta_x, d_karta_y, moje_karty, diler_karty, hrac_celkovo, diler_celkovo
    # resetujem na default hodnoty, kedže ide nové kolo
    karta_x, karta_y = 400, 500
    d_karta_x, d_karta_y = 400, 100
    moje_karty, diler_karty = [], []
    hrac_celkovo, diler_celkovo = 0, 0
    kolo = True
        # 2-karty mne
    for i in range(2):
        zober_kartu(moje_karty)
        s1, s2 = sucet_kariet(moje_karty)
        hrac_logika(s1, s2)
        c.update()
        c.after(300)
    c.after(300)
    for i in range(1):
        zober_kartu(diler_karty)
        s1, s2 = sucet_kariet(diler_karty)
        diler_logika(s1, s2)
        

def hit_karty():
    global moje_karty
    zober_kartu(moje_karty)
    s1, s2 = sucet_kariet(moje_karty)
    hrac_logika(s1, s2)

def vyhodnotenie_hry(stav):
    global zaciatocny_balance, stavka
    stav_x, stav_y = 400, 300
    x1, x2 = stav_x-100, stav_x+100
    y1, y2 = stav_y-50, stav_y+50
    r = 50
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, 
          x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, 
          x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    # c.create_rectangle(stav_x-100, stav_y-50, stav_x+100, stav_y+50, fill="light grey", outline="", tags="stav")
    c.create_polygon(points, fill="light grey", outline="black", tags="stav", smooth=True)
    c.create_text(stav_x, stav_y, text=stav, font="Arial 22", tags="stav")
    if stav=="Hráč vyhral.":
        vykresli_current_skore(zaciatocny_balance+(2*stavka))
        zaciatocny_balance += 2*stavka
    elif stav=="Push!":
        vykresli_current_skore(zaciatocny_balance+(stavka))
        zaciatocny_balance += stavka
    elif stav=="Blackjack!":
        """Pays 2:1 :)"""
        # x = stavka//2
        vykresli_current_skore(zaciatocny_balance+(3*stavka)) # 3* pretože pri štarte stahujem bet z balance, nech to viem vykrelsiť
        zaciatocny_balance += 3*stavka

def diler_tahy():
    """
    funkcia, kt. 'simuluje' kolo dílera, stojí na 17-tich, ak menej tak hit, ak viac stand
    """
    global karta_x, karta_y, kolo, d_karta_x, d_karta_y, diler_celkovo, hrac_celkovo
    # s1, s2 = sucet_kariet(diler_karty)
    # diler_logika(s1, s2, True)
    while kolo:
        s1, s2 = sucet_kariet(diler_karty)
        diler_logika(s1, s2)
        if 17 <= diler_celkovo < 21 and diler_celkovo > hrac_celkovo:
            kolo=False
            c.itemconfigure("diler_sucet", text=diler_celkovo)
            vyhodnotenie_hry("Díler vyhral.")
        elif 17 < diler_celkovo < 21 and diler_celkovo < hrac_celkovo:
            kolo = False
            c.itemconfigure("diler_sucet", text=diler_celkovo)
            vyhodnotenie_hry("Hráč vyhral.")
        elif diler_celkovo == 17 and diler_celkovo < hrac_celkovo:
            kolo = False
            c.itemconfigure("diler_sucet", text=diler_celkovo)
            vyhodnotenie_hry("Hráč vyhral.")
        elif diler_celkovo == 17 and hrac_celkovo == 17:
            kolo = False
            c.itemconfigure("diler_sucet", text=diler_celkovo)
            vyhodnotenie_hry("Push!")
        elif diler_celkovo == 21:
            kolo = False
            c.itemconfigure("diler_sucet", text=diler_celkovo)
            vyhodnotenie_hry("Díler vyhral.")
        elif diler_celkovo > 21:
            kolo = False
            c.itemconfigure("diler_sucet", text=diler_celkovo)
            vyhodnotenie_hry("Hráč vyhral.")
        elif diler_celkovo > 17 and diler_celkovo == hrac_celkovo:
            kolo = False
            c.itemconfigure("diler_sucet", text=diler_celkovo)
            vyhodnotenie_hry("Push!")
        elif diler_celkovo <17:
            c.itemconfigure("diler_sucet", text=diler_celkovo)
            c.update()
            c.after(300)
            zober_kartu(diler_karty)
    # print(f"Hráč: {hrac_celkovo} - Díler: {diler_celkovo}")

c.bind("<Button-1>", klik)
c.bind("<ButtonRelease-1>", updejt)
print(precitaj_skore())
vykresli_high_skore(precitaj_skore())
vykresli_current_skore(zaciatocny_balance)
c.mainloop()