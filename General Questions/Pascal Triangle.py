"""
Pascal’s triangle is a triangular array of the binomial 
coefficients. Write a function that takes an integer value 
n as input and prints first n lines of the Pascal’s triangle.
"""

print("Enter value of n:")
n = int(input())

print("Pascal's triangle for n = " + str(n) + " is:")

for line in range(1, n+1):
    C = 1
    for i in range(1, line + 1):
        print(C, end = ' ')
        C = int(C*(line - i)/i)
    print("")

