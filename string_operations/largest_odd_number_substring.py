"""
Level - Easy
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
Example 2:

Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".
Example 3:

Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.
"""

#Thought process - Get the odd number located at the lowest significant place (2567834 => 3), then simply take all the digits before it and form an odd number. No need of itertools

class Solution:
    def largestOddNumber(self, num: str) -> str:

        if int(num[-1])%2 != 0:
            return str(num)

        listofnums = [int(i) for i in list(num)]
        if all([i%2==0 for i in listofnums]):
            return ""

        
        pos = 1
        while True:
            digit = listofnums[-pos]
            if digit%2 != 0:
                break;
            else:
                pos = pos+1

        subnumber = num[0:-pos+1]
        return subnumber
        # return str(max(possible_numbers))

if __name__ == '__main__':
  Solution.largestOddNumber(1234797234)
  
        
