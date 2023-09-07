n = 5

for i in reversed(range(n+1, 1, -1)):
    print(" "*(n-i+1), end="")
    for j in range(1, i):
        print(j, end=" ")
    print("")
