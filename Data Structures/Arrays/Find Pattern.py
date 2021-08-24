"""
we have a python list
A = [3,4,5,6,1,1,3,4,5,6,4,4,3,4,5,6]
So I want to count the total number of times, the sequence 3,4,5,6 appears in this?
"""
a = [3,4,5,6,1,1,3,4,5,6,4,3,4,5,6,4,3,4,5,6]

n = len(a)
i = 0
count = 0

while i <= (n-4):
    if a[i] == 3 and a[i:i+4] == [3, 4, 5, 6]:
        count += 1
        i += 4
    else:
        i += 1
print(count)