'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Using a simple recursion takes too much time, while using cache does the trick.
Beats 85% users.
'''

class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        elif n==1:
            return x
        elif n == -1:
            return 1/x
        return self.myPow(x,n//2)*self.myPow(x,n//2)*self.myPow(x,n%2)
        
