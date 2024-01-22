# heslo -> "covid"
def decoding(text, password):
    sifra_tabulka, abc = ziskaj_tabulku("tabulka.txt")
    novy_text = ""
    idx_hesla = 0
    idx_textu = 0
    while True:
        if len(novy_text) == len(text):
            break
        if idx_hesla > len(password)-1:
            idx_hesla = 0
        znak = text[idx_textu].upper()
        if znak in abc:
            kluc = password[idx_hesla].upper()
            idx_v_abc = sifra_tabulka[kluc].index(znak)
            print(znak, kluc, idx_v_abc, abc[idx_v_abc])
            """for key, value in sifra_tabulka.items():
                if key == kluc:
                    idx_v_abc = value.index(znak)"""
            novy_text += abc[idx_v_abc]
            idx_textu += 1
            idx_hesla += 1
        else:
            novy_text += text[idx_textu]
            idx_textu += 1
            idx_hesla += 1
    print(novy_text)



def ziskaj_tabulku(meno_suboru):
    # abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sifra_tabulka = {}
    with open(meno_suboru, encoding="utf8") as subor:
        prvy = True
        for riadok in subor:
            if prvy:
                riadok = riadok.strip()
                abc = riadok.split(" ")
                prvy = False
            else:
                riadok = riadok.strip()
                riadok = riadok.split(" ")
                kluc = riadok[0]
                sifra_tabulka[kluc] = riadok[1:]
                print(kluc, sifra_tabulka[kluc])
    return sifra_tabulka, abc
    """for key, value in sifra_tabulka.items():
        print(key, "-", value)"""
       
def ziskaj_text(meno_suboru):
    text = ""
    with open(meno_suboru, encoding="utf8") as subor:
        for riadok in subor:
            text+=riadok
    return text

decoding(ziskaj_text("text.txt"), "covid")
# ziskaj_text("text.txt")
# print(len("covid"))
# ziskaj_tabulku("tabulka.txt")