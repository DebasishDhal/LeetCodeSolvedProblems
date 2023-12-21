'''
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.

Constraints:

n == points.length
2 <= n <= 105
points[i].length == 2
0 <= xi, yi <= 109
'''
#My solution, beats 59%
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[0]) #Sorting on x-coordinates
        maxArea = 0
      
        for pos in range(len(points)-1):
            first,second = points[pos],points[pos+1]
            area = second[0]-first[0]
            maxArea = max(area,maxArea)

        return maxArea

#Elegant solution. You can't escape sorting the list.
from itertools import pairwise
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        return max((
            b - a
            for a, b in pairwise(sorted(x for x, _ in points))
        ), default=0)


