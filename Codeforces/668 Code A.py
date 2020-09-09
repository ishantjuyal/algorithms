def fingerprint(p):
    n = len(p)
    f = sorted([p[i] + p[i+1] for i in range(n-2)])
    return(f)

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    print(*p[::-1])
