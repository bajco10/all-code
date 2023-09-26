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
