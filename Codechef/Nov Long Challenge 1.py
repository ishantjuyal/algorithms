t = int(input())
for _ in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    c = sorted(c)[::-1]
    l = 0
    r = 0

    for i in c:
        if l == r:
            # print("equal case")
            l += i
        elif l < r:
            # print("l < r")
            l += i
        else:
            # print("r < l")
            r += i
    # print("printing answer")
    print(max(l,r))