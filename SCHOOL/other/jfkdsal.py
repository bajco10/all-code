"""

n = int(input(("zadaj n: ")))
k = 1
for i in reversed(range(1, n+1)):
    k = k*i
print(f"{n}! = {n}", end="")
for g in reversed(range(1, n)):
    print("*"+str(g), end="")
    print(" = ", str(k))

 
n = int(input(('zadaj cislo:')))
y= 0
for j in range(n):
    for i in range(n-j):
        y+=1
for j in range(n):
    print()
    for i in range(n-j):
        y-=1
        print(y+1, end=' ')
"""
"""
n = 5
for i in reversed(range(1, n+1)):
    for j in range(1, i+1):
        print(j, end=" ")
    for k in reversed(range(1, i)):
        print(k, end=" ")
    
    print()
"""
"""
pocet_riadkov = int(input('Zadaj pocet riadkov: '))

for riadok in range(pocet_riadkov+1):
    print(' '*(pocet_riadkov-riadok), end='')
    for poradie_znaku in range((riadok*2)-1):
        if poradie_znaku < (riadok*2-poradie_znaku):
            print(poradie_znaku+1, end='')
        else:
            print(riadok*2-poradie_znaku-1, end='')
    print()

n = int(input("pocet riadkov"))

for i in range(n+1):
    print(" "*(n-i), end="")
    for j in range((i*2)-1):
        if j < (i*2-j):
            print(j+1, end="")
        else:
            print(i*2 - j - 1, end="")
    print()



n = int(input(('zadaj cislo:')))
y= 0
for j in range(n):
    for i in range(n-j):
        y+=1
for j in range(n):
    print()
    for i in range(n-j):
        y-=1
        print(y+1, end=' ')
"""


"""
n = int(input("Zadaj pocet riadkov: "))
for i in (range(1, n+1)):
    print(" "*(n-i), end="")
    for j in range(1, i+1):
        print(j, end="")
    for k in reversed(range(1, i)):
        print(k, end="")
    print()


n = int(input(('zadaj cislo:')))
y= 0
for j in range(n):
    for i in range(n-j):
        y+=1
for j in range(n):
    print()
    for i in range(n-j):
        y-=1
        print(y+1, end=' ')
"""




"""
rows=int(input('zadaj n: '))
number=1
for i in reversed(range(1,rows+1)):
    for j in (range(1, i+1)):
        print(number, end=' ')
        number+=1
    print()
"""