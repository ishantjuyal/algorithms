t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a == b:
        steps = 0
    elif a < b:
        diff = b-a
        steps = diff//10
        if diff%10 != 0:
            steps += 1
    else:
        diff = a-b
        steps = diff//10
        if diff%10 != 0:
            steps += 1
    print(steps)
