'''
Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] is either 0 or 1.
'''
#Quite bad performance in terms of memory. I convered the list into an array, I think delay is because of that.
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        import numpy as np
        special_rows = []
        special_cols = []
        mat = np.array(mat)
        for i in range(mat.shape[0]):
            if mat[i].sum() == 1:
                special_rows.append(i)

        for i in range(mat.shape[1]):
            if mat[:,i].sum() == 1:
                special_cols.append(i)

        selected = []

        for row in special_rows:
            col = np.where(mat[row]==1)[0][0]

            if col in special_cols:
                selected.append([row,col])

        return len(selected)
