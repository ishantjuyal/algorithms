"""
Find maximum value of Sum( i*arr[i]) with only rotations on given array allowed
"""
# O(n^2) approach
def rotate(arr):
    temp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[-1] = temp

def give_val(arr):
    curr_val = 0
    for i in range(len(arr)):
        curr_val += i*arr[i]
    return(curr_val)

def max_value(arr):
    curr_val = give_val(arr)
    max_val = curr_val
    for i in range(len(arr) - 1):
        rotate(arr)
        curr_val = give_val(arr)
        max_val = max(max_val, curr_val)
    return(max_val)

arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max_value(arr))

# O(n) Approach

def find_max(arr):
    n = len(arr)
    arr_sum = sum(arr)
    curr_val = sum([i*arr[i] for i in range(len(arr))])
    max_val = curr_val
    
    for j in range(1, n):
        curr_val = curr_val + arr_sum - (n*arr[n-j])
        max_val = max(max_val, curr_val)
    return(max_val)

arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(find_max(arr))