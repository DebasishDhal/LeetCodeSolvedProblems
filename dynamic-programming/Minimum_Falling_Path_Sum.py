'''
Give a m * n list of lists. You start from top row and go to the bottomg, one row at a time. You're allowed to jump either left, right or stay on the same column, as you change rows.
This is known as falling path problem, used im image processing.
'''
#This was my first approach. Notice the problem? This is a Greedy approach to this problem and it risks being trapped in a local minima.
#Take this input - [[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]]. Optimal path is [-46,10,-51,51]. While jumping from col=0 to col=1, this algo picks -10 instead because it's min of -10,10,97.
#Minimum falling path sum is -36 = sum(-46,10,-51,51). My algo says it's -32. Need to fix this.

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        def low_neighbor_upToDown(i,j): #For every index, provide the index of minimum nearest index
            if i >= m-1:
                return (i,j)
            index_reach = [max(0,j-1),min(n-1,j+1)]
            neighbors = {(i+1, index):matrix[i+1][index] for index in index_reach}
            return min(neighbors, key=neighbors.get)

        def find_path(i,j): #Given an index, this finds all the index till the end of matrix so that all index are minimum
            if i == m-1:
                return [(i,j)]
            next_i, next_j = low_neighbor_upToDown(i,j)
            return [(i,j)] + find_path(next_i,next_j)

        beam_sum = []
        for y in range(n): #Doing this for every element of top row and then taking the min.
            path = find_path(0,y)
            curr_elm = [matrix[item[0]][item[1]] for item in path]
            print(matrix[0][y],curr_elm, sum(curr_elm))
            beam_sum.append(sum(curr_elm))

        return min(beam_sum)

#DP with bottom-to-top approach. DP stores sum of reaching to that cell from the bottom. 
#So, we begin from the lowest row. Bottom row remains unchanged because we're coming from bottom to top. Then you move to peultimate row. 
#There for every element, you get the lowest value for accessible cells [1 col left, 1 col right] in the last row, say min_sum. Replace every cell with value of that cell + min_sum.
#Repeat

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        if n == 1:
            return matrix[0][0]

        dp = [[0]*n for _ in range(n)]
        dp[-1] = matrix[-1]

        for i in range(n-2, -1, -1):
            for j in range(n):
                min_elm = min([dp[i+1][item] for item in range(max(0,j-1),min(n-1,j+1)+1)])
                dp[i][j] = matrix[i][j] + min_elm
                
        # print(dp)
        return min(dp[0])

#Same solution implemented in a top to bottom approach. 
class Solution:
  def minFallingPathSum(self, matrix: List[List[int]]) -> int:
      n = len(matrix)

      if n == 1:
          return matrix[0][0]

      dp = [[0]*n for _ in range(n)]
      dp[0] = matrix[0]

      for i in range(1, n, 1):
          for j in range(n):
              min_elm = min([dp[i-1][item] for item in range(max(0,j-1), min(n-1,j+1)+1)])
              dp[i][j] = min_elm + matrix[i][j]
            
      return min(dp[-1])#0
