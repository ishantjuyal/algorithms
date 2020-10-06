# Covid Run

t = int(input())
for _ in range(t):
    n, k, x, y = map(int, input().split())
    f = x
    while True:
        x = (x+k)%n
        if x == y:
            print("YES")
            break
        if x == f:
            print("NO")
            break
