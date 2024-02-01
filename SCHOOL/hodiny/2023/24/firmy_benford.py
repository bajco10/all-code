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

subor = json.load(open("faktury_BB.json"))
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
        """firmy[ico] = {
            "meno":meno,
            "data":{
                rok["cifry"].append(cifra),
                rok["sumy"].append(cena)
            }
        }"""
        firmy[ico]["data"][rok]["cifry"].append(cifra)
        firmy[ico]["data"][rok]["sumy"].append(cena)

"""for ico, x in firmy.items():
    if ico == "44553625":
        print(ico, x)"""

fakturanti = {}
def vyfiltruj(rok):
    global firmy
    global fakturanti
    for ico, udaje in firmy.items():
        if str(rok) in firmy[ico]["data"]:
            fakturanti[ico] = udaje

for i in fakturanti.values():
    print(i)
    
