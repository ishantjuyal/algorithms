"""
Given a set of time intervals in any order, merge all 
overlapping intervals into one and output the result 
which should have only mutually exclusive intervals.
"""

print("Enter the time intervals:")
print("Enter (1,2) (3,4) as 1 2 3 4")
a = list(map(int, input().split()))
n = len(a) # Should always be even

# Convert time intervals in tuples
b = [(a[i], a[i+1]) for i in range(0, n, 2)]

# Sort the array of time intervals with respect to the initial time
b.sort(key= lambda x: x[0])

# Go through the whole array and merge the intervals
i = 0
while True:
    if b[i][1] >= b[i+1][0]:
        b[i] = (b[i][0], max(b[i][1], b[i+1][1]))
        b.remove(b[i+1])
    else:
        i += 1
    
    if i == len(b)-1:
        break

print(*b)