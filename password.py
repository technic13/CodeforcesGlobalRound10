def password(a):
    if max(a) == min(a):
        return len(a)
    else:
        return 1


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(password(a))
