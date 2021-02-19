"""
Write an efficient program to find the sum of contiguous subarray 
within a one-dimensional array of numbers which has the largest sum.
"""

print("Enter the array:")
a = list(map(int, input().split()))

max_so_far = 0
max_till_here = 0

for i in a:
    max_till_here += i
    if max_till_here > max_so_far:
        max_so_far = max_till_here
    if max_till_here < 0:
        max_till_here = 0

print(max_so_far)