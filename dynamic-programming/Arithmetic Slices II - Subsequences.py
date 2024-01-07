'''
Given an integer array nums, return the number of all the arithmetic subsequences of nums.
A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences. For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array. For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
The test cases are generated so that the answer fits in 32-bit integer.

Example 1: Input: nums = [2,4,6,8,10], Output: 7
Explanation: All arithmetic subsequence slices are:
[2,4,6],[4,6,8],[6,8,10],[2,4,6,8],[4,6,8,10],[2,4,6,8,10],[2,6,10]
'''
class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        totalCount = 0
         # initialize a list of dictionaries to store counts of subsequences
        dp = [{} for _ in range(n)]

        for i in range(0,n):
            for j in range(0,i):
                diff = nums[i] - nums[j]
                # get the count of subsequences with the same difference ending at nums[j]
                prevCount = dp[j].get(diff, 0) 
                # update count of subsequences ending at nums[i]
                dp[i][diff] = dp[i].get(diff, 0) + prevCount + 1
                print(f"i={i}, j={j}, elm_i={nums[i]}, elm_j={nums[j]}, diff={diff}, prevCount={prevCount}, dp={dp}")                
                # accumulate the previous count to the total count
                totalCount += prevCount

        return totalCount
s = Solution()

print(s.numberOfArithmeticSlices([2,4,6,8,10]))
