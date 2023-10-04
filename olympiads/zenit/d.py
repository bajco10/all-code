n = int(input())
dni = []
zlepsovala = 0
zhorsovala = 0
vrchol = 0
for i in range(n):
    dni.append(input())

for i in range(n):
    dni[i] = int(dni[i])

for i in range(len(dni)-1):
    if dni[i] < dni[i+1]:
        zhorsovala +=1
    elif dni[i] > dni[i+1]:
        zlepsovala +=1

for i in range(len(dni)-2):
    if (dni[i] < dni[i+1]) and (dni[i+1] > dni[i+2]):
        vrchol+=1

print(zlepsovala, zhorsovala, vrchol)
