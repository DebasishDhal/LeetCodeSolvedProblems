'''
https://leetcode.com/problems/cyclically-rotating-a-grid/description/
You are given an m x n integer matrix grid​​​, where m and n are both even integers, and an integer k.

The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:

Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
Explanation: The figures above represent the grid at every state.

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 50
Both m and n are even integers.
1 <= grid[i][j] <= 5000
1 <= k <= 109

#This is one of the best solutions I have done. It beats 77% of the users. They key is to always take it simple, and break it into simple chunks. If you're thinking a complicated way, then 
most likely a simpler solution exists.
'''

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        layer = min( len(grid)/2, len(grid[0])/2 )

        m,n = len(grid), len(grid[0])
        layer = min(m, n)//2

        for i in range(0,layer): #Each layer get cycled independently. 
          #A grid consists of, first row, the last elements of middle row, the last row reversed and the first elements of the middle rows reversed.
            first_row = grid[i][i:n-i]
            row_length = len(first_row)
            last_elements_middle_rows = [row[n-i-1] for row in grid[i+1:m-i-1]]
            col_length = len(last_elements_middle_rows)
            last_row_reversed = grid[m-i-1][i:n-i][::-1]
            first_elements_middle_rows_reversed = [row[i] for row in grid[m-i-2:i:-1]]
            combined_list = first_row + last_elements_middle_rows + last_row_reversed + first_elements_middle_rows_reversed #This is the ith layer of the grid, starting from outermost layer
            shift_req = k%len(combined_list) #Because it k>len(combined_list), the shift function won't work.
            combined_list = combined_list[shift_req:]+combined_list[:shift_req] #We shift the elements k places to the left.

            first_row = combined_list[:row_length] #After shifting, the elements need to be reassigned their positions
            last_elements_middle_rows = combined_list[row_length:row_length+col_length]
            last_row_reversed = combined_list[row_length+col_length:row_length+col_length+row_length]
            first_elements_middle_rows_reversed = combined_list[row_length+col_length+row_length:]

            grid[i][i:n-i] = first_row #Working alright (First row)

            for j in range(i+1,m-i-1): ##Last elements of middle rows assignment
                grid[j][n-i-1] = last_elements_middle_rows[j-i-1] #Working alright

            grid[m-i-1][i:n-i] = last_row_reversed[::-1] #Working alright #The last row (reversed) assignment, that's why last_row_reversed is reversed using [::-1]
            
            for j in range(m-i-2,i,-1): #First elements of middle rows
                grid[j][i] = first_elements_middle_rows_reversed[m-i-2-j]

        return grid
