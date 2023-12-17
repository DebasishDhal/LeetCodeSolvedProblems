'''
Beats 69% of users in runtime.
This thing doesn't work in Python 2. If you print this dictionary in Python 2, the ordering of items would be different. Hence, it won't work.
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {1000:'M',900:'CM',500:'D',400:'CD',100:'C', 90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
        dic = {item:value for item,value in dic.items() if item<=num} #This decreased the runtime to a big extent
        roman = ''
        for number,symbol in dic.items():
            if num<number:
                continue
            quotient = num // number
            roman += symbol*quotient
            num -= quotient*number

        return roman
