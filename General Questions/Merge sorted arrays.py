"""
Merge two sorted arrays without using
extra space
"""

print("Enter first sorted array")
a = list(map(int, input().split()))

print("Enter second sorted array")
b = list(map(int, input().split()))

i = 0
j = 0

while True:
    # print("i", i)
    # print("j", j)
    if a[i] >= b[j]:
        a = a[:i] + [b[j]] + a[i:]
        i += 1
        j += 1
        
    else:
        if a[i] < b[j]:
            # print("i", i)
            # print("j", j)
            # print("a[i]", a[i])
            # print("b[j]", b[j])
            if i == len(a) -1:
                a.append(b[j])
                j += 1
            elif b[j] <= a[i+1]:
                a = a[:i+1] + [b[j]] + a[i+1:]
                i += 1
                j += 1
            else:
                i += 1
    # print("Sample")
    # print(a)
    # print("i", i)
    # print("j", j)
    if j >= len(b):
        break

print("\nThe merged array is:")
print(*a)