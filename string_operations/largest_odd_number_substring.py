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

class Solution:
  def largestOddNumber(self, num: str) -> str:
      from itertools import combinations
      
      listofnums = [int(i) for i in list(num)]
      # print(listofnums)

      if all([i%2==0 for i in listofnums]):
          return "" #Input - 1406, Output - ""

      digits_str = str(num)
      possible_numbers = [digits_str[x:y] for x, y in combinations(range(len(digits_str) + 1), r = 2)]
      possible_numbers = [int(x) for x in possible_numbers if int(x)%2 != 0]
      return str(max(possible_numbers)) #Input - 12346, Output - "123"

if __name__ == '__main__':
  Solution.largestOddNumber(1234797234)
  
        
