'''
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
'''
#Beats 98%. Simple sorting and optimized comparison.
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        totalCookies = []
        start = 0

        for greed in g:
            for index in range(start,len(s)):            
                if s[index] >= greed:
                    # totalCookies.append(s[index])
                    count += 1
                    start = index+1
                    break

        # print(totalCookies)
        # return len(totalCookies)
        return count

