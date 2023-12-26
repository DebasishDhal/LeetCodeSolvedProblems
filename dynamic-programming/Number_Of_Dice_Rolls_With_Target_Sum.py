'''
You have n dice, and each die has k faces numbered from 1 to k. Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.
Example 1: 
Input: n = 1, k = 6, target = 3, Output: 1, Explanation: You throw one die with 6 faces. There is only one way to get a sum of 3.
Example 2:
Input: n = 2, k = 6, target = 7, Output: 6, Explanation: You throw two dice, each with 6 faces. There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
'''
#dp[i][j] represents the number of ways to achieve sum j using i dice (dice is plural form of die, or ଗୋଟି in Odia).
class Solution:

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        if n*k < target: #number of dice * Highest dice score < target
          return 0
          
        dp = [[-1] * (target + 1) for i in range(n + 1)]
        return self.solve(dp, n, k, target)

    def solve(self, dp, n, k, target):

            if target ==0 and n == 0: #If we want to achieve sum 0 using 0 dice, then there's one way only.
                return 1

            if target <= 0 or n == 0: #If our target goes below zero, or we have no dice left, there's no way of achieving the target.
                return 0

            if dp[n][target] != -1: #If target has been computed already, we retrieve from here. Ignore the modulo sign, it's not core to the problem.
                return dp[n][target]%(10**9 + 7)

            combs = 0 #Now, here we are calculating combinations for a valid combination of (target, n dices).

            for i in range(1,k+1): 
                combs += self.solve(dp, n-1, k, target-i) #Number of ways to achieve target-i using n-1 dice.
                combs = combs % (10**9 + 7) #Ignore this, not core to the algorithm

            dp[n][target] = combs % (10**9 + 7)
            return dp[n][target]    
