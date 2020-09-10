def clock_of_infinity(a, n, k):
    m = max(a)
    for i in range(len(a)):
        a[i] = m - a[i]
    if k % 2 == 1:
        return a
    m = max(a)
    return [m - el for el in a]


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(*clock_of_infinity(a, n, k))
