"""
Find the factorial of a given number in most optimal way
"""

n = int(input("Enter the number N: "))

fact_dict = {1:1}

def factorial(n):
    if n in fact_dict:
        return(fact_dict[n])
    else:
        fact_dict[n] = n*factorial(n-1)
        return(fact_dict[n])
    

print("Factorial of", n, "is", factorial(n))