/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
#Beats 28% of users only.
 */
var rotate = function(matrix) {
    const n = matrix.length

    let listOfLists = matrix.slice();
    
    for (let i = 0; i < n; i++) {
        listOfLists.push([...matrix[i]]);
    }

    for (let i = 0; i < n; i++) {
        const row = listOfLists.map(element => element[i]).reverse();
        matrix[i] = row;
    }
};
