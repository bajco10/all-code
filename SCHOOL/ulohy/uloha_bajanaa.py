# 16
n = int(input("n: "))
for i in reversed(range(1, n + 1)):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print()
# 17
n = int(input("n: "))

for i in range(n+1, 1, -1):
    print(" "*(n-i+1), end="")
    for j in range(1, i):
        print(j, end=" ")
    print("")