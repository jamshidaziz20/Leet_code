
#? Given an integer, write a function to determine if it is a power of three.

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while(n%3 == 0 and n>1):
            n = n/3  
        return n==1