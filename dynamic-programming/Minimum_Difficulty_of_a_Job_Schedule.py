'''
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).
You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day. You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].
Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

In simple words, divide an array jobDifficulty into d chunks so that the sum of maximum of each chunk is the minimum. The ordering of array elements cannot be changed. 
'''

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        if n < d:
            return -1

        dp = [[float('inf')] * (n + 1) for _ in range(d + 1)]
        dp[0][0] = 0

        for days in range(1, d + 1):
            for i in range(1, n + 1):
                max_difficulty = 0
                for j in range(i, 0, -1):
                    max_difficulty = max(max_difficulty, jobDifficulty[j - 1])
                    dp[days][i] = min(dp[days][i], dp[days - 1][j - 1] + max_difficulty)

        result = dp[d][n]
        return result if result < float('inf') else -1
