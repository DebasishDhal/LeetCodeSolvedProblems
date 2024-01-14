'''
Two strings are close if one string can be converted into another string by applying the following operations as suitable: - 
1 - Swap any two characters with each other. 'abc' -> 'acb'
2- Swap entire collection of one character with entire collection of another. 'aaabc' -> 'bbbac'
'''

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        m,n = len(word1),len(word2)
        if m!=n:
            return False
        
        chars1, chars2 = set(word1), set(word2)
        if chars1 != chars2:
            return False

        freq1 = []
        freq2 = []
        for char in chars1:
            freq1.append(word1.count(char))
            freq2.append(word2.count(char))
        
        return sorted(freq1) == sorted(freq2)
