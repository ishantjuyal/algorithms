"""
Given a positive number N, find and return the longest distance between
two consecutive 1's in the binary representation of N.
If there aren't two consecutive 1's, return 0.
"""

print("Enter the number:")
n = int(input())

bin_n = str(bin(n))[2:]
print("Binary", bin_n)

max_val = -1
last_val = -1

for val in range(len(bin_n)):
    if last_val == -1 and bin_n[val] == '1':
        last_val = val
    else:
        if bin_n[val] == '1':
            max_val = max(max_val, val - last_val)
            last_val = val

print(max_val)