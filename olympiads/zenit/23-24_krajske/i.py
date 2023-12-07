from itertools import combinations

n = int(input())
menus = [list(map(int, input().strip().split())) for _ in range(n)]

maximum = max(
    sum(abs(menus[i][k] - menus[j][k]) for k in range(4))
    for i, j in combinations(range(n), 2)
)

print(maximum)
