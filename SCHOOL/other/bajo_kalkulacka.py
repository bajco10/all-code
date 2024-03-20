# spraviť konvertovanie
# z 10 -> 2✅ 
# z 2 -> 10✅
# z 10 -> 16✅
# z 16 -> 10✅
# z 2 -> 16, cez 10?
# z 16 -> 2, cez 10?

# grafika
import tkinter
c = tkinter.Canvas(width=800, height=600, bg="white")
c.pack()

# pomocné funkcie
def kruhove_tlacitko(x, y, tag, text=""):
    c.create_oval(x-30, y-30, x+30, y+30, fill="white", tags=tag)
    c.create_text(x, y, text=text, font="Arial 19")


# 3 tlačítka vľavo -> 2, 10, 16
kruhove_tlacitko(10 + 30, 70, "2_z", "2")
kruhove_tlacitko(10 + 30 + 10 + 60, 70, "10_z", "10")
kruhove_tlacitko(10 + 30 + 10 + 60 + 10 + 60, 70, "16_z", "16")
# 3 tlačítka vpravo -> 2, 10, 16
kruhove_tlacitko(800 - 10 - 30, 70, "16_do", "16")
kruhove_tlacitko(800-10-30-10-60, 70, "10_do", "10")
kruhove_tlacitko(800-10-30-10-60-10-60, 70, "2_do", "2")
# stvorec pre input -> pridať tag atď
c.create_rectangle(400-150, 70-25, 400+150, 70+25)
# stvorec pre riesenie => statické, netreba tag
c.create_rectangle(20, 130, 780, 580)
# funkcie kalkulačky
def dec_to_bin(cislo):
    bin_cislo = ""
    while cislo != 0:
        x = cislo // 2
        zv = cislo % 2
        bin_cislo+=str(zv)
        print(f"{cislo} / 2 = {x}    zv: {zv}")
        cislo = x
    # zmeniť nech to kreslí v neskoršej verzí!
    return bin_cislo[::-1]

# print(dec_to_bin(37))
# print(f"{37:b}")

def bin_to_dec(cislo):
    power = 0
    cislo = str(cislo)[::-1]
    postupy = []
    dec_cislo = 0
    for i in cislo:
        if i!="0":
            dec_cislo += 2**power
        postupy.append(f"({i} * 2^{power})")
        power+=1
    # zmeniť nech to kreslí v neskoršej verzí!
    print(" + ".join(postupy[::-1]))
    print(dec_cislo)

# bin_to_dec(1110010001000101111010110)
# print(int("110110", 2))

def dec_to_hexa(cislo):
    hex_cislo = ""
    sustava = "0123456789ABCDEF"
    while cislo != 0:
        x = cislo // 16
        # zostatok je vlastne index v stringu sústavy
        idx_zv = cislo % 16
        zv = sustava[idx_zv]
        hex_cislo+=zv
        print(f"{cislo} / 16 = {x}    zv: {zv}")
        cislo = x
    print(hex_cislo)

# dec_to_hexa(12758)


def hexa_to_dec(cislo):
    power = 0
    sustava = "0123456789ABCDEF"
    cislo = str(cislo)[::-1]
    postupy = []
    dec_cislo = 0
    for i in cislo:
        idx_i = sustava.find(i)
        if i!="0":
            dec_cislo +=(idx_i) * (16**power) 
        postupy.append(f"({idx_i} * 16^{power})")
        power+=1
    # zmeniť nech to kreslí v neskoršej verzí!
    print(" + ".join(postupy[::-1]))
    print(dec_cislo)

# hexa_to_dec("FF")

def bin_to_hexa(cislo):
    """
    -> rozdelim cislo na 4-cislia
    -> pridám 0-ly aby bola dlzka cisla % 4 = 0
    -> prve 4-cislia predstavuje 1-ky, druhe 16-tky, tretie 256-tky...
    -> vypocitam hodnotu stvorcislia
    -> prilepim hodnotu k mojmu hex cislu
    -> asi to bude fajn spravit cez polia
    => lahsie sa to bude kreslit/organizovat
    """
    hex_cislo = ""
    sustava = "0123456789ABCDEF"
    stvorcislia = []
    stvorcislia_hodnoty = []
    # doplnim cislo do nasobku 4-ky
    while len(cislo) % 4 != 0:
        cislo = "0" + cislo
    # rozdelim cislo na 4-cislia
    for i in range(len(cislo)//4):
        i = i*4
        stvorcislia.append(cislo[i:i+4])
    # vyratam kazde 4 cislie
    hodnota = 0
    for j in stvorcislia:
        idx_hodnoty = int(j[0])*8 + int(j[1])*4 + int(j[2])*2 + int(j[3])*1
        hodnota = sustava[idx_hodnoty]
        stvorcislia_hodnoty.append(hodnota)
    print(stvorcislia)
    print(stvorcislia_hodnoty)
    hex_cislo = "".join(stvorcislia_hodnoty)
    print(hex_cislo)

# bin_to_hexa("101101110")
# bin_to_hexa("100011101100011010101011110000111010101001")

def hexa_to_bin(cislo):
    """
    -> z kazdej cislice vytvorim stvorcislie v bin, ktore vysklada jej hodnotu
    -> napr. A : 1*2**3 + 0*2**2 + 0*2**1 + 1*2**0
    => tj.: 8 + 0 + 0 + 1
    """
    bin_cislo = ""
    sustava = "0123456789ABCDEF"
    stvorcislia = []
    """
    for i in cislo:
        stvorcislia.append(f"{int(i):02b}")
    print(stvorcislia)
    """
hexa_to_bin("FF")

tkinter.mainloop()