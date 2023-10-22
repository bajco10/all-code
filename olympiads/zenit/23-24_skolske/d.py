hodnoty = []
pocet = input()
for i in range(int(pocet)):
    x = input()
    obr_b = f'{int(x):032b}'[::-1]
    hodnoty.append(int(obr_b, base=2))
    
for i in hodnoty:
    print(i)
