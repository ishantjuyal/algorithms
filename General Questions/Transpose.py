"""
Find transpose of a matrix
"""

print("Enter the numbers of rows:")
r = int(input())

a = []
print("Enter the elements of a square matrix:")
for i in range(r):
    arr = list(map(int, input().split()))
    a.append(arr)

for i in range(r):
    for j in range(i,r):
        a[i][j], a[j][i] = a[j][i], a[i][j]

print("Resultant matrix:")
for i in a:
    print(*i)