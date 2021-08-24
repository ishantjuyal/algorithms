"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

nums = [-2,1,-3,4,-1,2,1,-5,4]

max_so_far = nums[0]
max_ending_here = nums[0]
for i in nums[1:]:
    max_ending_here = max(i, max_ending_here + i)
    max_so_far = max(max_so_far, max_ending_here)

print(max_so_far)