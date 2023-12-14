/**
 Do not return anything, modify matrix in-place instead.
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
Beats 66% users in TS.
 */
function rotate(matrix: number[][]): void {
    const n = matrix.length

    let listOfLists = matrix.slice();

    for (let i = 0; i < n; i++) {
        const row = listOfLists.map(element => element[i]).reverse();
        matrix[i] = row;
    }
};
