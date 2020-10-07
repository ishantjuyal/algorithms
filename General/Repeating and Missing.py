""" Given an unsorted array of size n. 
Array elements are in the range from 1 to n. 
One number from set {1, 2, …n} is missing and one number occurs twice in the array. 
Find these two numbers.
"""

print("Enter the unsorted array separated by spaces")
a = list(map(int, input().split()))

n = len(a)

a_sorted = sorted(a)

count = 0
repeating = -1
missing = -1

for i in range(n):
    if a_sorted[i+1] - a_sorted[i] == 0:
        repeating = a_sorted[i+1]
        count += 1
        if count == 2:
            break
    else:
        if a_sorted[i+1] - a_sorted[i] == 2:
            missing = a_sorted[i] + 1
            count += 1
            if count == 2:
                break

print("Missing Number:", missing)
print("Repeating Number:", repeating)