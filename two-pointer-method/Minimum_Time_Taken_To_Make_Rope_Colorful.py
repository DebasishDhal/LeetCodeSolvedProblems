'''
Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.
'''

#Logic - If we find 3 balloons of same colors, we simply remove everything apart from the balloon for which maximum time will be taken. 
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time_needed = []
        
        j = 0
        for i in range(len(colors)):
            if (colors[i] != colors[j]): #When a dissimilar balloon is found, stop. Before that all are of the same color
                equals = neededTime[j:i] #List of time taken to remove balloons of same color
                time_needed.append( sum(equals)-max(equals) ) #Remove all but the balloon with maximum time.
                j = i 

        time_needed.append(sum(neededTime[j:])- max(neededTime[j:])) #One more round needed for the end part.
        return sum(time_needed)
                
