"""n = int(input())
vys = []

l = []
for i in range(n):
    sucty = []
    n_testovanych = int(input())
    l = list(map(int, input().split(" ")))
    while True:
        if len(l)==1:
            #sucty.append(l[0])
            vys.append(sum(sucty))
            break
        else:
            min1 = min(l)
            l.pop(l.index(min1))
            min2 = min(l)
            l.pop(l.index(min2))
            l.append(min1+min2)
            sucty.append(min1+min2)
    
for i in vys:
    print(i)"""

import heapq

n = int(input())
vys = []

for _ in range(n):
    n_testovanych = int(input())
    l = list(map(int, input().split()))
    heapq.heapify(l)  # Convert the list into a min-heap

    sucty = 0
    while len(l) > 1:
        min1 = heapq.heappop(l)
        min2 = heapq.heappop(l)
        l.append(min1 + min2)
        sucty += min1 + min2

    vys.append(sucty)

for i in vys:
    print(i)

