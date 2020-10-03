t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    q = list(map(int, input().split()))
    sum_q = sum(q)
    day = (sum_q//k) + 1
    print(day)
