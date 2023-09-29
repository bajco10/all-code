z, k = [int(x) for x in input().split(" ")]
p=int(input())
mys_poschodia = [int(x) for x in input().split(" ")]
spolu = mys_poschodia + [z, k]
spolu.sort()
# prejdem = mys_poschodia[0]-1 - z
prejdem = 0

for i in range(len(spolu)-1):
    if spolu[i+1] in mys_poschodia and spolu[i] in mys_poschodia and p>0:
        odpocet = 1
    elif p>0:
        odpocet=0
    else:
        odpocet = -1
    rozdiel = spolu[i+1] - spolu[i]-odpocet
    if rozdiel > prejdem:
        prejdem = rozdiel

print(prejdem)