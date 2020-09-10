def water_gorka(a):
    counter = 0
    for i in range(len(a) - 2, -1, -1):
        if a[i] > a[i + 1]:
            counter += a[i] - a[i + 1]
    return counter


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(water_gorka(a))
