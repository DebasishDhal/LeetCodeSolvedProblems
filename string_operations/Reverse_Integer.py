'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
'''

class Solution:
    def reverse(self, x: int) -> int:

        digits = list(str(x))[::-1]
        negative = True if '-' in digits else False
        if negative:
            digits.remove('-')
        number = ''.join(digits)
        number = int(number)

        if number > 2**31-1 or number < -2**31:
            return 0
            
        if negative:
            number = -1*number
        return number
