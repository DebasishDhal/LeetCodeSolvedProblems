'''
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.
A substring is a contiguous sequence of characters within a string
Example 1:
Input: s = "aa" Output: 0, Explanation: The optimal substring here is an empty substring between the two 'a's.
'''

#Brute force. Beats 5%

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # left, right = 0, len(s)-1

        maxWords = 0
        equal = False
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if s[i] == s[j]:
                    print(s[i],s[j])
                    equal = True
                    temp = len(s[i+1:j])
                    maxWords = max(temp,maxWords)

        if maxWords == 0 and equal == False:
            return -1
        elif maxWords == 0 and equal == True:
            return 0
        else:
            return maxWords        

#More optimized solution Beats 16%
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        occurence = {}

        for i in range(len(s)):
            if s[i] not in occurence:
                occurence[s[i]] = [i]
            else:
                occurence[s[i]].append(i)
        maxLen = 0
        # print(occurence)
        repeat = False
        for item in occurence.values():
            
            if len(item) <2:
                continue
            else:
                repeat = True

            largestStrech = item[-1]-item[0]-1
            maxLen = max(maxLen,largestStrech)

        if repeat:
            return maxLen
        else:
            return -1

#Best optimized solution Beats 100%.Not mine
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        length = -1
        myhash= {}
        
        for i in range(len(s)):
            
            if s[i] not in myhash:
                myhash[s[i]] = i
            else:
                length = max(length , i- myhash.get(s[i]) -1)
                
        return length
