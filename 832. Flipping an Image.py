
#? Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
#? To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
#? To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

# Example 1:
# Input: [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

class Solution:
    def flipAndInvertImage(self, A):
        for index, arr in enumerate(A):
            A[index] = self.invert(self.reverse(arr))
        return A
        
    
    def reverse(self, arr):
        beg = 0
        end = len(arr)-1
        while(beg < len(arr)//2):
            arr[beg], arr[end] = arr[end], arr[beg]
            beg += 1
            end -=1
        return arr
            
        
    def invert(self, arr):
        return [x^1 for x in arr]