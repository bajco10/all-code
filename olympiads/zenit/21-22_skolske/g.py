n = int(input())

dates = []
# ['1.1.1.0 00:00', '3.1.2000 17:35', '19.10.2021 09:00']
for i in range(n):
    dates.append(input())

def ich(date):
    # listocky.vetvicky.konare.stromy hh:mm
    # strom 5 konarov, ak je delitelny 47 -> 4 konare
    # kazdy konar -> 7 vetviciek
    # vetvicka 4 listocky ak parna, 5 ak neparna
    # kazdy listocek trva 3 hodiny

    # skontrolovat strom a vetvicku

    # prekonvertovat cele na minuty

    dokopy = 0
    
    ostatok, hm = date.split(" ")
    hod, min = hm.split(":")
    dokopy += int(hod)*60 + int(min)

    listy, vetvy, konare, stromy = ostatok.split(".")
    if (stromy!=0) or (stromy%47==0):
        # 4 konare
        if vetvy!=2==0:
            # 4 listocky
            dokopy += (60*3)*listy + 4*(60*3*listy) + 7*() 


for i in dates:
    if i.count(".")==3:
        # ich
        pass
    elif i.count(".")==2:
        # nas
        pass
