
#? Given an unsorted integer array, find the smallest missing positive integer.

# Example 1:
# Input: [1,2,0]
# Output: 3

# Example 2:
# Input: [3,4,-1,1]
# Output: 2

# Example 3:
# Input: [7,8,9,11,12]
# Output: 1

class Solution:
    def firstMissingPositive(self, nums):
        missing_num = 1
        nums.sort()
        for num in nums:
            if(num == missing_num):
                missing_num += 1
        return missing_num
            