'''
You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating. Beats 72%
'''

class Solution:
    def minOperations(self, s: str) -> int:
      
        #Our number will either be 010101... or it'll be 101010.... So, we evaluate the steps required for both results and take the minimum.
      
        changes_0101 = sum([1 for i, c in enumerate(s) if int(c) != i % 2]) #Total changes required to convert the number to 0101...

        # changes_1010 = sum([1 for i, c in enumerate(s) if int(c) == i % 2]) #This is double computing.
        changes_1010 = len(s) - changes_0101 #This is the elegant method. No need to double compute. #Total changes for 1010..
      
        return min(changes_0101, changes_1010)
