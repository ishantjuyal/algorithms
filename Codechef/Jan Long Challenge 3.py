# GIVING WA

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))


    if sum(a) > sum(b):
        print(0)
        continue
    else:
        a = sorted(a)
        b = sorted(b)[::-1]

        if len(a) <= len(b):
            if sum(a) + sum(b[len(a):]) > sum(b[:len(a)]):
                print(-1)
                continue
            else:
                index = 0
                while True:
                    a[index], b[index] = b[index], a[index]
                    if sum(a) > sum(b):
                        print(index +1)
                        break
                    index += 1
                    if index == len(a):
                        break
        else:
            index = 0
            while True:
                a[index], b[index] = b[index], a[index]
                if sum(a) > sum(b):
                    print(index +1)
                    break
                index += 1
                if index == len(a):
                    break
