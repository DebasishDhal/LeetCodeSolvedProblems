Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
#Beats 76% of users
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #Instead of comparing every str with another. We first sort the list, then trap all the words between the first and last word. Our problem now gets reduced to just two words. 
        res = ""

        strs = sorted(strs)
        first, last = strs[0], strs[-1]

        for i in range( min(len(first),len(last) ) ):
            if first[i] != last[i]:
                return res

            else:
                res += first[i]

        return res
