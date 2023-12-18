'''
The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.
Constraints:

4 <= nums.length <= 104
1 <= nums[i] <= 104 #This makes our job easier, by avoiding negative numbers

Beats 84% of users.
'''
#Most simple solution, although sorting takes the complexity to nlog(n). 
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)

        left1, left2 = 0, 1
        right1, right2 = len(nums) - 1, len(nums) - 2
        
        return nums[right1]*nums[right2] - nums[left1]*nums[left2]


#O(n) solution, beats 75% users only. It seems like since the we aren't making big loops here, eliminating explicit for loop doesn't cause much improvement
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:


        firstBig, secondBig = 0, 0 #always initialize opposite of what they should be. If numbers were not lower limited by 0, this'd have gone to - infinity instead ot zero.
        firstSmall, secondSmall = float('inf'), float('inf')

        for num in nums:
            if num > firstBig:
                firstBig, secondBig = num, firstBig
            
            elif num > secondBig:
                secondBig = num

            
            if num < secondSmall: #First small is larger
                firstSmall, secondSmall = secondSmall, num
            
            elif num < firstSmall:
                firstSmall = num

        return (firstBig*secondBig - firstSmall*secondSmall)
