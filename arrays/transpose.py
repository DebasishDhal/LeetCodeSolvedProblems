class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
      
        row_count = len(matrix)
        col_count = len(matrix[0])
        output = [[0]*row_count for i in range(col_count)]

        # matrix = np.array(matrix)
        for i in range(0,col_count):
            for j in range(0,row_count):
                output[i][j] = matrix[j][i]

        return output
        
