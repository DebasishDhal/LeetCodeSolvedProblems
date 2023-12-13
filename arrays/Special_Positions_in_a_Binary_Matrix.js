/**
 * @param {number[][]} mat
 * @return {number}
 This works very fast in JavaScript, beats 88% of users.

 Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] is either 0 or 1.
 */

var numSpecial = function(mat) {
  let specialRows = []  
  let specialCols = []

  for (i = 0; i <mat.length; i++){
      let sum = mat[i].reduce((a,b) => a+b,0); //If sum of ith row is 0, add the row_number to the list
      if (sum==1){
          specialRows.push(i)
      }
  }


  for (i = 0; i <mat[0].length; i++){
      let sum = mat.reduce((a, b) => a + b[i], 0); //If sum of ith col is 0, add the col_number to the list
      if (sum == 1){
          specialCols.push(i)
      }
  }

  let selected = []

  for (i=0; i<specialRows.length; i++){ //For all row_number in specialRows, find which column of that row has element 1, and check if that element is in specialRows.
      let row = specialRows[i];
      let col = mat[row].indexOf(1)

      if (specialCols.includes(col)){
          selected.push([row, col])

      }

  }

  return selected.length
};
