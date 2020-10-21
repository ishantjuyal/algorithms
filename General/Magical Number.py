"""
A positive number is magical if it is divisible by either A or B. 
Find the N-th magical number and return its modulo 10^0 + 7.
"""

print("Enter A:")
a = int(input())

print("Enter B:")
b = int(input())

print("Enter N:")
n = int(input())

num = min(a, b)
count = 0

while True:
    if num%a == 0 or num %b == 0:
        count += 1
    num += 1
    if count == n:
        num = num - 1
        break

print("N-th magical number is", num)