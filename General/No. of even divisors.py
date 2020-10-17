"""
Find the number of even divisors of a number n
fot t test cases
"""

t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if n%i == 0 and i%2 == 0:
            count += 1
    print(count)