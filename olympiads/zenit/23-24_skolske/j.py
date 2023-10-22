
def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)


def count_valid_trees(n):
    if n % 2 == 1:
        return 0
    k = n // 2
    return binomial_coefficient(n - 1, k)


t = int(input())
results = []

for _ in range(t):
    n = int(input())
    results.append(count_valid_trees(n) % (10**9 + 7))


for result in results:
    print(result)
