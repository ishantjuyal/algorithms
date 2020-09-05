print("Enter elements of array:")
a = list(map(int, input().split()))
n = len(a)
for j in range(1, n):
    key = a[j]
    i = j-1
    while i>=0 and a[i] > key:
        a[i], a[i+1] = a[i+1], a[i]
        i = i - 1

print(a)
