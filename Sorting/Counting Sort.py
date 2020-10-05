# Assuming all the numbers to be positive and in the range of 0 to 99
print("Enter the numbers to be sorted separated by spaces")
a = list(map(int, input().split()))

count_array = [0]*100

for i in a:
    count_array[i] += 1

s = []

for i in range(100):
    s = s + [i]*(count_array[i])

print("The sorted order of the numbers are:")
print(*s)