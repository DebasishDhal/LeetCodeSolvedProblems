'''
An array arr is a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.

99%
'''

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 0, len(arr)-1
        mid = (start+end)//2
        print(f"start = {start}, mid = {mid}, end = {end} ")
        while True:
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid

            if arr[mid]>arr[mid-1]:
                start = mid
                mid = (start+end)//2
                # print(f"start = {start}, mid = {mid}, end = {end} ")
            elif arr[mid] < arr[mid-1]:
                end = mid
                mid = (start+end)//2
                # print(f"start = {start}, mid = {mid}, end = {end} ")
            
            
