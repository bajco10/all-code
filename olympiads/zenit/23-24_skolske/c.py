n = int(input())
l = list(map(int,(input().split())))
m = sum(l)
for i in range(n):
    print(m-l[i])