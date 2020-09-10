def bed_war(s, n):
    counter = 0
    s = [s[i] for i in range(len(s))]
    for i in range(n):
        if s[(i - 1) % n] == 'R' and s[(i + 1) % n] == 'R' and s[i] == 'R':
            s[i] = 'L'
            counter += 1
        elif s[(i - 1) % n] == 'L' and s[(i + 1) % n] == 'L' and s[i] == 'L':
            s[i] = 'R'
            counter += 1
    return counter


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(bed_war(s, n))
