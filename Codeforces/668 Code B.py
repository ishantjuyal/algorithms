t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    

    for i in range(n):
        if a[i] > 0:
            fin = i
            for j in range(i+1, n):
                if a[i] == 0:
                    break
                if a[j] < 0:
                    sub = abs(a[j])
                    if a[i]>=sub:
                        a[i] = a[i] - sub
                        a[j] = a[j] + sub
                    else:
                        sub = a[i]
                        a[i] = a[i] - sub
                        a[j] = a[j] + sub

    count = 0
    for i in a:
        if i > 0:
            count += i
    print(count)
