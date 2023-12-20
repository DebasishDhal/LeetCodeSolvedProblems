'''
You are given an integer array prices representing the prices of various chocolates in a store. You are also given a single integer money, which represents your initial amount of money.

You must buy exactly two chocolates in such a way that you still have some non-negative leftover money. You would like to minimize the sum of the prices of the two chocolates you buy.

Return the amount of money you will have leftover after buying the two chocolates. If there is no way for you to buy two chocolates without ending up in debt, return money. Note that the leftover must be non-negative.
Constraints:

2 <= prices.length <= 50
1 <= prices[i] <= 100
1 <= money <= 100
'''

#Unoptimized solution, involving sorting, still beats 85% of users.
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices = sorted(prices)
        print(prices)
        if prices[0]+prices[1] > money:
            return money

        else:
            return money - prices[0] - prices[1]
        return prices[0]

#Optimized solution, without any sorting. Somehow it's only 35% in performance.
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first_price = float('inf')
        second_choice = float('inf') #Will be smaller

        for item in prices:
            if item < second_choice:
                first_choice, second_choice = second_choice, item
            elif item < first_choice: #Stays somewhere between first choice and second choice. We don't want values greater than first choice anyway.
                first_choice = item

            
        if first_choice+second_choice>money:
            return money
        else:
            return money-first_choice-second_choice
