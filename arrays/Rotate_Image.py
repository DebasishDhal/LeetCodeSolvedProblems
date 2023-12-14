'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

#solution beats 71%% of users in Python.
Medium 
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        listOfLists = []
        for i in range(n):
            listOfLists.append(matrix[i])
        
        for i in range(n):
            row = [element[i] for element in listOfLists]
            row.reverse()
            matrix[i] = row

        
