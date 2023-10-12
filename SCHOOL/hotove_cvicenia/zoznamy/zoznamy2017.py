#1
"""def sucin(zoznam):
    x = 1
    if zoznam=="":
        return 1
    else:
        for i in zoznam:
            x*=i
        return x
print(sucin([2,3,3]))"""
#2
"""def mocniny(n):
    l = []
    for i in range(n+1):
        l.append(i**2)
    return l
print(mocniny(7))"""
#3
"""def len_parne(zoznam):
    l = []
    for i in zoznam:
        if i%2==0:
            l.append(i)
    return l
print(len_parne([2, 5, 7, 10, 13]))"""
#4
"""def spoj(zoznam):
    veta=""
    for i in range(len(zoznam)):
        if i!=zoznam[-1]:
            veta += f"{zoznam[i]} "
        else:
            veta+= i
    return veta
print(spoj(["nepi", "jano", "nepi", "vodu"]))"""
#5
"""def zisti(zoznam):
    c = 0
    for i in zoznam:
        if type(i)== int and i%7==0:
            c+=1
    return c
print(zisti([4, 7.0, 14, "7", 0]))"""
#6
"""def zoznam2(n, hodn1, hodn2):
    l = []
    for i in range(n//2):
        l.append(hodn1)
        l.append(hodn2)
    return l
print(zoznam2(10, 7, "w"))"""
#7
"""def na_parnych(zoznam):
    l = []
    for i in range(0, len(zoznam), 2):
        l.append(zoznam[i])
    return l
print(na_parnych(list("programovanie")))"""
#8
"""def zostupne(zoznam):
    l = zoznam[::]
    l.sort()
    if zoznam == l:
        return True
    return False
print(zostupne([1,5,3]))"""
#9
"""def vyrob1(zoznam):
    l = []
    for i in zoznam:
        if i%2!=0:
            l.append(i)
        else:
            l.append(i+1)
    return l
print(vyrob1([3, 5, 6, 8, 9, 10, 11, 13]))"""
#10
"""def vyrob2(zoznam):
    l = []
    for i in zoznam:
        if type(i)== str:
            l.append(i)
    return l
print(vyrob2([1, 2.2, ['a', 'b'], 'tri', 4, '']))"""
#11
"""def zoznam_cifier(cislo):
    x = list(str(cislo))
    for i in range(len(x)):
        x[i] = int(x[i])
    return x
print(zoznam_cifier(123789))"""
#12
"""def gener(a, b, c=1):
    l = []
    while a!=b:
        l.append(a)
        a+=c
    return l
print(gener(5, 20, 3))
print(gener(4, 0, -1))"""
#13
"""def cele(zoznam):
    return [int(x) for x in zoznam]
print(cele([3.14, -7.0, 0.99]))"""
#14
"""def vymen(zoznam):
    x, y = zoznam[0], zoznam[1]
    return [y, x]
print(vymen(["ahoj", 123]))"""
#15
"""def vymen2(zoznam):
    a = zoznam[0]
    zoznam[0]=zoznam[1]
    zoznam[1]=a
dvojica = ["ahoj", 123]
vymen2(dvojica)
print(dvojica)"""
#16
"""def vyhod(zoznam, hodnota):
    l = []
    for i in zoznam:
        if i != hodnota:
            l.append(i)
    return l
zoz = zoz = [37, 'hello', -7, 3.14, 'hello', 2]
novy = vyhod(zoz, "hello")
print(novy)
print(zoz)"""
#17 -> nevyhadzujeme prvky cez for cykly!
"""def vyhod2(zoz, co):
    while co in zoz:
        zoz.remove(co)
zoz = [37, "hello", "hello", -7, -7, -7, "hello"]
vyhod2(zoz, -7)
print(zoz)"""
#18
"""def zo_suboru(meno_suboru):
    subor = open("/home/tomas/Desktop/all-code/SCHOOL/hotove_cv math problems
icenia/zoznamy/subor.txt") math problems

    l = []
    for riadok in subor:
        riadok=riadok.strip()
        if " " in riadok:
            l.append(riadok.split(" "))
        else:
            l.append(riadok)
    subor.close()
    return l
print(zo_suboru("subor.txt"))"""
#19
"""def do_suboru(meno_suboru, zoznam):
    subor=open("/home/tomas/Desktop/all-code/SCHOOL/hotove_cvicenia/zoznamy/subor1.txt", "w")
    for i in zoznam:
        print(i, file=subor)
    subor.close()
    with open("/home/tomas/Desktop/all-code/SCHOOL/hotove_cvicenia/zoznamy/subor1.txt", "r") as subor:
        lines = subor.readlines()
    return [line.strip() for line in lines]
xy = [[100, 200], 300, 400, [500, 600]]
print(do_suboru("subor1.txt", xy))"""
#20
"""def krat2(zoznam):
    for i in range(len(zoznam)):
        zoznam[i] = zoznam[i]*2
z = [5, 3.14, [1, 2], -4, 'ab']
krat2(z)
print(z)"""
#21
"""def zdvoj(zoznam):
    i = 0
    dlzka = len(zoznam)
    while i < dlzka:
        x = zoznam[i]
        zoznam.insert(i+1, x)
        dlzka = len(zoznam)
        i+=2
        
tab = [1, "Python", 2, "Java", 3, "C#"]
zdvoj(tab)
print(tab)"""
#22 - neviem ci mozem pouzit sort() - asi hej, aby sa predstavili mozne argumenty pre sort()
"""def uprac(zoznam):
    zoznam.sort(reverse=True)
f = [0, 1, 2, 0, 0, 2]
uprac(f)
print(f)"""
#23
"""from random import choice 
def nahodny_zoznam(n, vyber):
    l = []
    for i in range(n+1):
        l.append(choice(vyber))
    return l
print(nahodny_zoznam(8, [7, 'red', None]))
print(nahodny_zoznam(13, [2, 3]))"""
        