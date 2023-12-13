'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
'''

#Brute force method - Trash performance, beats 5% of users

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import numpy as np
        board = np.array(board)

        for i in range(0,9): #Check for each row and each col if count of number of elements which are repeated more than once is not more than 1. (1 is to accomodate the dots)
            row = board[i]
            col = board[:,i]

            items_row, counts_row = np.unique(row, return_counts = True)
            items_col, counts_col = np.unique(col, return_counts = True)

            if (counts_row>1).sum() > 1 or (counts_col>1).sum() > 1:
                print("Caught at row-col check")
                return False

            
        for i in range(0,9,3): #For each sub-table, check if number of elements which are repeated more than once is not more than 1.
            for j in range(0,9,3):
                smaller_board = board[i:i+3,j:j+3]

                items,counts = np.unique(smaller_board, return_counts = True)                

                if (counts>1).sum() > 1:
                    print("Caught at subbox check")
                    return False

        return True
      
#Elegant method

#Traverse the board using nested loop. For each valid element (!= '.'), append [row_num, col_num, (row_num // 3, col_num // 3)] to a list called elements. 
#Simply find if all the elements are unique or not, i.e. [row, number, (sub-board number)] must be unique, using set method
#Beats 90% of all users
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        elements = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    elements += [(i, element),(element, j),(i//3,j//3, element)]
        # print(type(elements))
        return len(elements) == len(set(elements))
