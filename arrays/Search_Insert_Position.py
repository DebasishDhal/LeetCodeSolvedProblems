'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

#This code has 0(n) complexity although. Need to employ binary search for O(logn)
#Beats 45% in runtime.
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # import numpy
        if target in nums:
            return nums.index(target)

        else:
            left = 0
            if nums[0]>target:
                return 0
                # nums.insert(0,target)

            elif target>nums[-1]:
                return len(nums)
                # nums.append(target)

            else:

                for i in range(len(nums)-1):
                    if nums[i]<target and nums[i+1]>target:
                        return i+1
                        # nums.insert(i+1,target)
                        break
            
