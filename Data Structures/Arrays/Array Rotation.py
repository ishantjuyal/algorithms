"""
Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements. 

[1, 2, 3, 4, 5, 6, 7] becomes [3, 4, 5, 6, 7, 1, 2] if we rotate by 2
"""

def rotate(arr, d):
    for i in range(d):
        t = arr[0]
        for j in range(len(arr)-1):
            arr[j] = arr[j+1]
        arr[-1] = t

arr = [1,2,3,4,5,6,7]
print("Before rotation:", arr)
rotate(arr, 2)
print("After rotation:", arr)