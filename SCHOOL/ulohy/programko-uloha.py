slovo = "janko"
n = 0
for i in slovo:
    n +=1
    print(str(n) + i, end="")


n = int(input("Zadaj cislo: "))
for i in range(n):
    print(i%7, end=" ")

