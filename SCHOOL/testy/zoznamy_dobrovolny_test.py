def nsd(a, b):
    if(b==0):
        return a
    else:
        return nsd(b, a%b)

def nsn(cisla):
    nsn = 1
    for cislo in cisla:
        nsn = nsn*cislo // nsd(nsn, cislo)
    return nsn

def scitaj_zlomky(a, b):
    a_citatel, a_menovatel = map(int, a.split("/"))
    b_citatel, b_menovatel = map(int, b.split("/"))
    menovatel = nsn([a_menovatel, b_menovatel])
    citatel = a_citatel*(menovatel//a_menovatel) + b_citatel*(menovatel//b_menovatel)
    nsd_cit_men = nsd(citatel, menovatel)
    if nsd_cit_men != 1:
        citatel = citatel // nsd_cit_men
        menovatel = menovatel // nsd_cit_men

    return f"{citatel}/{menovatel}"
vysledky = []
with open("zlomky.txt") as subor:
    for riadok in subor:
        zlomky = riadok.strip().replace("=", "").replace(" ", "").split("+")
        while True:
            if len(zlomky) == 1:
                vysledky.append(zlomky[0])
                break
            else:
                a, b = zlomky.pop(), zlomky.pop()
                x = scitaj_zlomky(a, b)
                zlomky.append(x)
                print(a, b, x, len(zlomky))

for i in range(len(vysledky)):
    a, b = vysledky[i].strip().split("/")
    if b == "1":
        vysledky[i] = str(a)
with open("zlomky.txt") as subor:
    priklady = subor.readlines()

with open("zlomky_riesenie.txt", "w") as subor:
    idx = 0
    for riadok in priklady:
        riadok = riadok.strip()
        print(f"{riadok}{vysledky[idx]}", file=subor)
        idx+=1

