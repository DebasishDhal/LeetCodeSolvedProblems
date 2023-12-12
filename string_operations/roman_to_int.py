'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
'''

#Beats 60% in speed, 5% in memory. Easy level
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'CM':900, 'XC':90, 'IV':4, 'IX':9, 'XL':40, 'CD':400, 'I':1, 'L':50,
        'C':100, 'D':500, 'M':1000, 'V': 5}

        res = 0
        for element in dic.items():
            if element[0] in s:
                res += element[1]
                s = s.replace(element[0],'q', 1)

        res += s.count('M')*1000
        res += s.count('D')*500
        res += s.count('L')*50
        res += s.count('I')
        res += s.count('X')*10
        res += s.count('C')*100

        return res
