"""
Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements. 

[1, 2, 3, 4, 5, 6, 7] becomes [3, 4, 5, 6, 7, 1, 2] if we rotate by 2
"""

def rotate(arr, d):
    arr = arr[d:] + arr[:d]
    return(arr)

arr = [1,2,3,4,5,6,7]
print("Before rotation:", arr)
arr = rotate(arr, 2)
print("After rotation:", arr)