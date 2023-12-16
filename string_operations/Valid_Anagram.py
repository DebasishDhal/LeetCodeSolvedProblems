'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Beats 76% of users.
The point is not to lose time in making new lists, their copies, always try not to make full loops if you reach a result early enough.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        counter = {}

        for char in s:
            counter[char] = counter.get(char,0)+1

        print(counter)

        for char in t:
            if char not in counter or counter[char] == 0:
                return False

            counter[char] -= 1

        return True
