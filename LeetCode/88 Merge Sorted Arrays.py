"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should 
be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# A function to add an element and shift all the elements on the right by one
def rotate(nums, i, val):
    if i == len(nums) - 1:
        nums[i] = val
        return
    # shifting index i+1 to len(nums)-1 one step right 
    for j in range(len(nums)-1, i, -1):
        nums[j] = nums[j-1]
    # Inserting the element at index i
    nums[i] = val

i = 0
j = 0
        
while j < n:
    if i < m+j:
        if nums1[i] <= nums2[j]:
            i += 1
        else:
            rotate(nums1, i, nums2[j])
            i += 1
            j += 1
    else:
        nums1[i] = nums2[j]
        i +=1
        j += 1

print(nums1)