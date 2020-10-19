"""
Given an m x n matrix. If an element is 0,
set its entire row and column to 0.
"""

print("Enter number of rows")
m = int(input())
print("Enter number of columns")
n = int(input())

print("Enter the matrix")

a = []
for i in range(m):
    arr = list(map(int, input().split()))
    a.append(arr)
    col = len(arr)
    if col != n:
        print("Wrong number of columns")
        exit()

zero_row = []
zero_col = []

for i in range(m):
    for j in range(n):
        if a[i][j] == 0:
            zero_col.append(j)
            zero_row.append(i)

for i in range(m):
    for j in zero_col:
        a[i][j] = 0

for i in zero_row:
    a[i] = [0]*n

print("Matrix after transformation:")
for i in a:
    print(*i)