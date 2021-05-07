# Assuming all the numbers to be positive and in the range of 0 to 99

print("Enter the numbers to be sorted separated by spaces")
input_list = list(map(int, input().split()))

# Initiate an array which will keep count of the number of times a number appears in input
count_array = [0]*100

for i in input_list:
    count_array[i] += 1

sorted_list = []

for i in range(100):
    sorted_list = sorted_list + [i]*(count_array[i])

print("The sorted order of the numbers are:")
print(*sorted_list)