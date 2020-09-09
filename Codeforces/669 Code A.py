t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if a.count(1) <= n//2:
        final = [0]*(n//2)
        print(len(final))
        print(*final)
    else:
        final = [1]*((a.count(1)//2)*2)
        print(len(final))
        print(*final)
