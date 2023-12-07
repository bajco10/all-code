n, k = map(int, input().split())
pole = list(map(int, input().split()))

max_values = [max(pole[i:i+k]) for i in range(n - k + 1)]
print(' '.join(map(str, max_values)))
