'''
Given a positive integer num, split it into two non-negative integers num1 and num2 such that:

The concatenation of num1 and num2 is a permutation of num.
In other words, the sum of the number of occurrences of each digit in num1 and num2 is equal to the number of occurrences of that digit in num.
num1 and num2 can contain leading zeros.
Return the minimum possible sum of num1 and num2.

Notes:

It is guaranteed that num does not contain any leading zeros.
The order of occurrence of the digits in num1 and num2 may differ from the order of occurrence of num.

Constraints:

10 <= num <= 109
'''
#First we sort the digits of the number. The approach is to distribute the digits evenly. So that the sum will be minimum. So one digit goes to num1, next goes to num2 and so on.
#Beats 99%

class Solution:
    def splitNum(self, num: int) -> int:
        numList = sorted(list(str(num)))

        pos = 0

        num1,num2 = '',''
        while pos<len(numList):
            num1 += numList[pos]
            pos += 1

            if pos<len(numList):
                num2 += numList[pos]
                pos += 1

        return int(num1)+int(num2)
