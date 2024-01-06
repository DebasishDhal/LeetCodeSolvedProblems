'''
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].
You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.
If you choose a job that ends at time X you will be able to start another job that starts at time X.
'''

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        start_end = [[i,j,k] for i,j,k in zip(startTime,endTime, profit)]
        start_end.sort(key = lambda x:x[1]) #sorting by their finish time
        # print(start_end)

        finalProfit = [None]*n #Initialization of dynamic array
        finalProfit[0] = start_end[0][2] #First commit
        # print(finalProfit)

        for i in range(1,n):
            found = False
            low = 0
            high = i - 1

            while low <= high: #Using binary search, for each item, find the latest job which ends before the current job (corresponding to index i). Binary search is just for speed.
                mid = (low + high) // 2

                if start_end[mid][1] <= start_end[i][0]:
                    if start_end[mid + 1][1] <= start_end[i][0]:
                        low = mid + 1
                    else:
                        found = True
                        break
                else:
                    high = mid - 1

            if found:
                index = mid #If there's such an index whose finish time is less that our current start time, all good
            else:
                index = -1

            curr_profit = start_end[i][2]
            if index != -1:
                curr_profit = curr_profit + finalProfit[index]
            
            finalProfit[i] = max(curr_profit,finalProfit[i-1])
        # print(finalProfit)
        return finalProfit[-1]
