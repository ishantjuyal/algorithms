t = int(input())
for _ in range(t):
    n, x, p, k = map(int, input().split())
    a = list(map(int, input().split()))
    if x not in a:
        print(-1)
        continue
    if sorted(a)[p-1] == x:
        print(0)
        continue
    a_sorted = sorted(a)
    index = a_sorted.index(x) + 1
    if p > index:
        if k >= p:
            print(p - index)
            continue
        else:
            print(-1)
            continue
    if p < index:
        if k <= p:
            print(index - p)
        else:
            print(-1)
            continue