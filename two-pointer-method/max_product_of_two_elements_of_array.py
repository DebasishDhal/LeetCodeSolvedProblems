'''Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
Constraints:

2 <= nums.length <= 500
1 <= nums[i] <= 10^3
'''

# Beats 65% of users in terms of speed and 10% in terms of memory
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        nums.sort()

        left = 0
        right = len(nums)-1

        res = 0
        while left<right:
            res_new = (nums[left]-1)*(nums[right]-1)

            if res_new < res:
                right -= 1
            else:
                left += 1
                res = res_new
        return res    


