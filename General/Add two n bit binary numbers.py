print("Enter first binary number:")
a = list(map(int, input().split()))
print("Enter second binary number:")
b = list(map(int, input().split()))

a = a[::-1]
b = b[::-1]

n = len(a)
c = [0]*(n+1)

for i in range(n):
    val = a[i] + b[i]
    if val == 2:
        c[i] = 0
        c[i+1] = 1
    else:
        c[i] = val
c = c[::-1]
print(*c)

