"""
An array is monotonic if it is either monotone increasing
or monotone decreasing. Given an array, return whether it is
monotonic or not.
"""

print("Enter the array:")
a = list(map(int, input().split()))

diff = [a[i+1] - a[i] for i in range(len(a) - 1)]

if max(diff) == 0:
    ans = True
elif max(diff) < 0 and min(diff) <= 0:
    ans = True
else:
    if max(diff) > 0:
        if min(diff) >= 0:
            ans = True
        if min(diff) < 0:
            ans = False

if ans == True:
    print("\nArray is monotonic")
else:
    print("\nArray is not monotonic")