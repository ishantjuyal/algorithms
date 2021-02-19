# Sort an array of 0’s 1’s 2’s without using extra space or sorting algo

print("Enter array consisting of 0s, 1s and 2s only")
a = list(map(int, input().split()))

n = len(a)
ones = 0
twos = 0

for i in a:
    if i == 1:
        ones += 1
    if i == 2:
        twos += 1

zeros = n - ones - twos

print(*[0]*zeros, end = " ")
print(*[1]*ones, end = " ")
print(*[2]*twos, end = " ")