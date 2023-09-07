def vymen_slova(slova):
    stringos=""
    slovicka = slova.split(",")
    for i in slovicka[::-1]:
        stringos += i +","
    return stringos


# x= vymen_slova("blava,kosice,kezmarok,zlin,trencin,piestany,dolne_hony")
# print(x)

def rozdel_na_slova(veta):
    slova = veta.split(" ")
    for i in slova:
        print(i)

# rozdel_na_slova("isiel macek do malacek")

def rozdel_na_slova1(slovo):
    """ BEZ LISTOV -> AJ NA HLADANIE KAZDEJ POZICIE PISMENA"""
    for i in range(slovo.count(" ")):
        m1 = slovo.find(" ")
        print(slovo[:m1])
        slovo = slovo[m1+1:]
    print(slovo)

# rozdel_na_slova1("isiel macek do malacek")

def riadky(retazec):
    n = 0
    riadocky = retazec.split("\n")
    for i in riadocky:
        n+=1
        print(f"{n}. {i}")



# riadky(f"isiel\nmacek do\nmalacek")

def vypis(slovo):
    n = 0
    for i in slovo:
        print(f"{n} {i} {str(ord(i))} {chr(ord(i)+1)}")
        n += 1

# vypis("Monty Python")

def pocet(retazec, podretazec):
    pocet = 0
    for i in range(len(retazec)):
        if podretazec == retazec[i:i+len(podretazec)]:
            pocet+=1
    print(pocet)

# pocet('mama ma emu a ema ma mamu', 'ma ')

def prevrat(retazec):
    nove = ""
    for znak in retazec:
        nove = znak + nove
    return nove

"""KAZDE DRUHE PISMENO"""
def prevrat(slovo):
    nove = ""
    for i in range(len(slovo)):
        if i%2==0:
            nove = slovo[i]+nove
    return nove

print(prevrat("python"))