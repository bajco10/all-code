n_ved = int(input())
v = list(map(int, input().split()))

max_value = v[-1]
vys = [n_ved]

for i in range(n_ved - 2, -1, -1):
    if v[i] > max_value:
        vys.append(i + 1)
        max_value = v[i]

vys = vys[::-1]

for i in vys:
    print(i, end=" ")




        


