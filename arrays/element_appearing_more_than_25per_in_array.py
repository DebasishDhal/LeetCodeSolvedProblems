class Solution:
    def findSpecialInteger(self, arr):
        import numpy as np
        nums, counts = np.unique(arr, return_counts=True)
        index = np.argmax(counts)
        return nums[index]
