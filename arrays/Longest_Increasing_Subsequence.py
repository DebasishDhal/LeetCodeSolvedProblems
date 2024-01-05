'''
Given an integer array nums, return the length of the longest strictly increasing subsequence
Example 1: Input: nums = [10,9,2,5,3,7,101,18]. Output: 4. Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        lis = [nums[0]]

        for item in nums:
            if item>lis[-1]:
                lis.append(item)
            else: #Replace the smallest element greater
                left, right = 0, len(lis) - 1
                while right > left:
                    mid = left + (right-left)//2
                    if item > lis[mid]:
                        left = mid+1
                    else:
                        right = mid
                lis[left] = item
                # print(item, lis)
            print(item, lis)
        print(lis)                
        return len(lis)                        

#Another method includes dynamic programming
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
                            

'''Output

nums = [10,9,2,5,3,7,101,18]
10 [10]
9 [9] #Replaced 10.
2 [2] #Replaced 2
5 [2, 5] 
3 [2, 3] #Replaced 5
7 [2, 3, 7] 
101 [2, 3, 7, 101]
18 [2, 3, 7, 18] #Replaced 101
'''     
