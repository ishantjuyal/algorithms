# Find duplicates in an array of N integers

print("Enter the N numbers:")
a = list(map(int, input().split()))

a_dict = {}

for i in a:
    if i in a_dict:
        a_dict[i] += 1
    else:
        a_dict[i] = 1

s = []

for k, v in a_dict.items():
    if v >= 2:
        s = s + [k]*v
s = sorted(s)

print("The duplicates present in the Array are:")
print(*s)