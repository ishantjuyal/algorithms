t = int(input())
for _ in range(t):
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))

    available_problems = sum(a)
    days = available_problems//k
    events = min(d, days)
    print(events)