'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
'''

'''
1st approach - Brute force methd

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = []
        heightcopy = height
        for i in enumerate(height):
            for j in enumerate(heightcopy):
                length = abs(j[0] - i[0])
                height = min(j[1],i[1])
                area.append(length*height)

        return max(area)
#The answer is alright, but it couldn't get submitted. So I applied the double pointer method. Double pointer method is applicable here as the x-axis is sorted.
#Runtime lies in the median position
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 2:
            return min(height)

        start = 0
        end = len(height) - 1

        area = 0
        while start < end:
            length_new = end - start
            height_new = min(height[end], height[start])
            new_area = height_new * length_new
            
            area = max(area, new_area)

            if height[end] > height[start]:
                start += 1
            
            else:
                end -= 1


        return area

  
