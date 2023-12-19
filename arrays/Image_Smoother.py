'''
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).

Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.

Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
'''
#Brute force method, beats 16% on runtime. 
#At first I wanted to do a try except method to catch out of bound errors, but that's not required.
#Scopes of improvement - Don't make lists and append new numbers to them. Adding number to number is faster.

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        smooth_img = []
        
        for row_no in range(len(img)):
            smooth_row = []
          
            for col_no in range(len(img[0])):
                valid_points = []
              
                for i in range(row_no-1,row_no+2):
                    for j in range(col_no-1,col_no+2):
                      
                        if i>=0 and i<len(img) and j>=0 and j<len(img[0]):
                            valid_points.append(img[i][j])
                          
                smooth_value = sum(valid_points)/len(valid_points)
                smooth_row.append(int(smooth_value))
            smooth_img.append(smooth_row)

        return smooth_img

#This one shows good improvement (48%). Reduced for loop by introducing max and min. Removed list appends and sum. Removed int(), instead using //
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        smooth_img = []
        m = len(img)
        n = len(img[0])
        for row_no in range(m):
            smooth_row = []
          
            for col_no in range(n):
                total = 0
                count = 0
              
                for i in range(max(row_no-1,0),min(row_no+2,m)):
                    for j in range(max(col_no-1,0),min(col_no+2,n)):
                        total += img[i][j]
                        count += 1

                # smooth_value = total//count
                smooth_row.append(total//count)
            smooth_img.append(smooth_row)

        return smooth_img

