'''
There are two strings s and t of the same length, consisting of smallcase letters only. At a time, we can replace one string of t with any other string. What's the minimal number of 
operations needed to convert t into an anagram of s (Two words are anagrams if they've the same count for every character)
'''
class Solution:
    # from collections import Counter
    def minSteps(self, s: str, t: str) -> int:
        dict_s = {item:0 for item in 'abcdefghijklmnopqrstuvwxyz'}
        dict_t = dict_s.copy()

        for i in range(len(s)):
            dict_s[s[i]] += 1
            dict_t[t[i]] += 1

        res = {}
        for item in dict_s.keys():
            res[item] = abs(dict_s[item] - dict_t[item])
        return int(sum(res.values())/2)
