'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = []
        left = 0
        str_len = len(s)
        max_len = 0
        for right in range(str_len):

            new_str = s[right]

            if new_str not in substring: #If a char is absent, it can be added
                substring.append(new_str)
                # max_len += 1 This is not right, as insertion will deletion will ruin it
                max_len = max(max_len, right-left+1)

            else: #If not, we will repeatedly cut down left chars until all chars are unique and then add the new char
                while new_str in substring:
                    substring.remove(s[left])
                    left += 1
                substring.append(new_str)

        return max_len
