''' 
#! DESCRIPTION
#? A self-dividing number is a number that is divisible by every digit it contains.
#? For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
#? Also, a self-dividing number is not allowed to contain the digit zero.
#? Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

'''
def is_self_dividing(number):
    for digit in str(number):
        if digit == '0' or number % int(digit) != 0: 
            return False
    return True
    
def selfDividingNumbers(left, right):
    self_divis = []
    for num in range(left, right+1):
        if is_self_dividing(num):
            self_divis.append(num)
    return self_divis

