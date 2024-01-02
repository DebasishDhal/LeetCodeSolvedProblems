'''
You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:
The 2D array should contain only the elements of the array nums. Each row in the 2D array contains distinct integers. The number of rows in the 2D array should be minimal. Return the resulting array. If there are multiple answers, return any of them.
Note that the 2D array can have a different number of elements on each row.

 

Example 1:Input: nums = [1,3,4,1,2,3,1], Output: [[1,3,4,2],[1,3],[1]]. Explanation: We can create a 2D array that contains the following rows:
- 1,3,4,2
- 1,3
- 1
All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
It can be shown that we cannot have less than 3 rows in a valid array.
'''

class Solution: #Bottomg 5% percentile
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        # print(count)

        res = []

        while (all(value == 0 for value in count.values()) is False): #I resorted to this atrocity because you can't alter a dictionary during an iteration (this was new to me).
            new_row = []

            for key in count:
                if count[key] == 0:
                    continue
                new_row.append(key)
                count[key] -= 1

            res.append(new_row)

        return res

#Second attempt -  counting is not really necessary, so let's remove it

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        for num in nums:
            added = False

            for row in res:
                if num in row: #Since I'm putting a continue statement below, if not num in row is not necessary. This took me from bottomg percentile to 50%.
                    continue
                    
                row.append(num)
                added = True
                break
            
            if added is False:
                res.append([num])
            # print(num, res)
        return res                
 
