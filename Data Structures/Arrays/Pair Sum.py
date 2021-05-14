"""
Given a sorted and rotated array, find if there is a pair with a given sum
"""
def look(arr, new):
    intersect = set(new).intersection(set(arr))
    return(len(intersect) > 0)

def find(arr, x):
    new = []
    n = len(arr)
    ans = False
    for i in range(n-1):
        new.append(x - arr[i])
        if look(arr[i+1:], new):
            ans = True
            break
    return(ans)

arr = [11, 15, 26, 38, 9, 10]
x = 19
print(find(arr, x))
