
#? Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
#? We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

# Example 1:
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

# Example 2:
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one element.
# Note: The n belongs to [1, 10,000].


#My solution
class Solution:
    def checkPossibility(self, nums):
        counter = 0
        index = 0
        while (counter != 2 and index < (len(nums)-1)):
            if(not(nums[index] <= nums[index+1])):
                counter += 1
            index += 1
        return True if counter < 2 else False


#Correct Solution    
class Solution2:
    def checkPossibility(self, nums):
        p = None
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if p is not None:
                    return False
                p = i
        print(p)
        return (p is None or p == 0 or p == len(nums)-2 or
               nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2])
        
x = [3,4,2,3]
print(Solution().checkPossibility(x))
print(Solution2().checkPossibility(x))




