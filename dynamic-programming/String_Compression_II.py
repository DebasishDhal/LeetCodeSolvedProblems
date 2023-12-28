'''
Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".

Notice that in this problem, we are not adding '1' after single characters. Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length. Find the minimum length of the run-length encoded version of s after deleting at most k characters.

Example 1: Input: s = "aaabcccd", k = 2, Output: 4
Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6. Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5, for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.
'''

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        self.n = len(s)
        self.dp = [[-1] * (k + 1) for _ in range(self.n)]
        return self.helper(0, k, s)

    def helper(self, i: int, k: int, s: str) -> int:
        if k < 0:
            return self.n
        if self.n <= i + k:
            return 0

        ans = self.dp[i][k]
        if ans != -1:
            return ans
        ans = self.helper(i + 1, k - 1, s)
        length, same, diff = 0, 0, 0

        for j in range(i, self.n):
            if diff > k:
                break
            if s[j] == s[i]:
                same += 1
                if same <= 2 or same == 10 or same == 100:
                    length += 1
            else:
                diff += 1
            ans = min(ans, length + self.helper(j + 1, k - diff, s))

        self.dp[i][k] = ans
        return ans
