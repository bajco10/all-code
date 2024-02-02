"""
- spracujem údaje do vnorených slovníkov
- zistím rok z inputu
- ak input=="all", pozriem údaje zo všetkých rokov
- inak pre špecifikovaný rok
- vyfiltrujem, spravim nový slovník fakturantov
- pozor na trvalé príkazy atď. -> vyhodím zo slovníku
- funkcia na vyratanie odchylky od hodnot
- 10 s najv. odchylom vypíšem
- grafy?
"""
import json

subor = json.load(open("faktury_BB.json", encoding="utf-8"))
firmy = {}
for i in range(len(subor)):
    meno = subor[i]["Dodávateľ"]
    cena = subor[i]["Celková_cena"]
    cena = cena.strip().replace("-","").replace(" ","")
    cifra = cena[0]
    ico = subor[i]["IČO"].strip()
    datum = subor[i]["Dátum_vystavenia"]
    rok = int((datum.split("."))[2])
    if (ico not in firmy):
        # print("nova firma")
        firmy[ico] = {
            "meno":meno,
            "data":{
                rok:{
                    "cifry":[cifra],
                    "sumy":[cena]
                }
            }
        }
    elif rok not in firmy[ico]["data"]:
        # print("rok nie je ale firma hej")
        firmy[ico]["data"][rok] = {"cifry":[cifra],
                                   "sumy":[cena]}
    else:
        # print("vsetko je, pridavam")
        firmy[ico]["data"][rok]["cifry"].append(cifra)
        firmy[ico]["data"][rok]["sumy"].append(cena)

fakturanti = {}
def vyhod_trvale(rok=None):
    global fakturanti
    
    if rok:
        ico_von = []
        for ico, udaje in fakturanti.items():
            platby = udaje["sumy"]
            for platba in platby:
                if platby.count(platba) >= len(platby)//2:
                    ico_von.append(ico)
                    print("vymazana firma: " + ico)
                    break
        for icko in ico_von:
            del fakturanti[icko]

def rataj_benf(fakturanti):
    benf = [0.301, 0.176, 0.123, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]

def vyfiltruj(rok):
    global firmy
    global fakturanti
    if rok!="all":
        for ico, udaje in firmy.items():
            if int(rok) in firmy[ico]["data"]:
                fakturanti[ico] = firmy[ico]["data"][int(rok)]
    # print(fakturanti)
    elif rok=="all":
        for ico, udaje in firmy.items():
            fakturanti[ico] = firmy[ico]["data"]
    else:
        print("Neplatný vstup")
    if rok=="all":
        vyhod_trvale()
    else:
        vyhod_trvale(rok)

vyfiltruj(2013)

# print(firmy["44889780"])
print(firmy["36634654"])  
# vypisat top 10 spolocnosti, ktore sa vymykaju Benfordovho zakonu
# -> pomery maju velku odchylku od grafu
# ak je pocet vyskytu cislice dlhsi ako zoznam(cislic tejto firmy) treba firmu vylucit
# => nieco ako stale prikazy -> skresluje to benf. krivku
benf = [0.301, 0.176, 0.123, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]