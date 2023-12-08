'''
#Medium
https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description
Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: arr = [1,2,3,4], difference = 1
Output: 4
Explanation: The longest arithmetic subsequence is [1,2,3,4].
Example 2:

Input: arr = [1,3,5,7], difference = 1
Output: 1
Explanation: The longest arithmetic subsequence is any single element.
Example 3:

Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
Output: 4
Explanation: The longest arithmetic subsequence is [7,5,3,1].
'''
'''
This is bad solution with O(n*n) complexity.
class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        arr_len = []

        for i in range(0,len(arr)):
            ith_arr = []
            ith_arr.append(arr[i])
            for j in range(i+1, len(arr)):
                if arr[j] - ith_arr[-1] == difference:
                    ith_arr.append(arr[j])

            arr_len.append(len(ith_arr))
            print(ith_arr)
        
        return max(arr_len)
'''
#O(n) complexity.
class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        num_dict = {}
        for num in arr:
            count = 1
            if num-difference in num_dict:
                count = count + num_dict[num-difference]
            num_dict[num] = count

        return max(num_dict.values())
