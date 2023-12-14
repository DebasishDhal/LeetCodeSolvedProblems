'''
You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:

Let the number of ones in the ith row be onesRowi.
Let the number of ones in the jth column be onesColj.
Let the number of zeros in the ith row be zerosRowi.
Let the number of zeros in the jth column be zerosColj.
diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
Return the difference matrix diff.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
grid[i][j] is either 0 or 1.
'''

#Brute force method - Beats only 7% of users in runtime
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row_list = []
        col_list = []

        grid_len = len(grid)
        grid_width = len(grid[0])

        for i in range(grid_len):
            row_list.append([grid[i].count(0), grid[i].count(1)])

        for j in range(grid_width):
            col = [inner_list[j] for inner_list in grid]
            print(col)
            col_list.append([col.count(0), col.count(1)])

        res = []
        for i in range(grid_len):
            row = []
            for j in range(grid_width):
                element = row_list[i][1]+col_list[j][1]-row_list[i][0]-col_list[j][0]
                row.append(element)
            res.append(row)

        return res

#Optimized - Beats 80%. Since the grid has only 1's and 0's. We do not need to count 0 separately. And we do not create a new list to save space and time.
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        grid_len = len(grid)
        grid_width = len(grid[0])
        row_list = [0] * grid_len
        col_list = [0] * grid_width

        for i in range(grid_len):
            for j in range(grid_width):
                row_list[i] += grid[i][j]
                col_list[j] += grid[i][j]

        res = []
        for i in range(grid_len):
            for j in range(grid_width):
                grid[i][j] = 2*(row_list[i] + col_list[j]) - grid_len - grid_width

        return grid
            
