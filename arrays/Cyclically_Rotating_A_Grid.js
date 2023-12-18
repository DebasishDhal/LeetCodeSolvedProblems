/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number[][]}
 Beats 100%
 */
var rotateGrid = function(grid, k) {
    let layer = Math.min(grid.length / 2, grid[0].length / 2);
    const m = grid.length;
    const n = grid[0].length;
    layer = Math.min(m, n) / 2; //As evident from the example images, the number of layers depends on the min. of col_length and row_length

    //Each layer gets processed independently.
    for (let i = 0; i < layer; i++) {

        let firstRow = grid[i].slice(i, n - i);
        const rowLength = firstRow.length;

        let lastElementsMiddleRows = [];
        for (let j = i + 1; j < m - i - 1; j++) {
            lastElementsMiddleRows.push(grid[j][n - i - 1]);
        }
        const colLength = lastElementsMiddleRows.length;

        let lastRowReversed = grid[m - i - 1].slice(i, n - i).reverse();

        let firstElementsMiddleRowsReversed = [];
        for (let j = m - i - 2; j > i; j--) {
            firstElementsMiddleRowsReversed.push(grid[j][i]);
        }

        let combinedList = firstRow.concat(
            lastElementsMiddleRows,
            lastRowReversed,
            firstElementsMiddleRowsReversed
        );

        const shiftReq = k % combinedList.length; //This is very important, don't just shift it by k. If k>list length, it'll throw error
        combinedList = combinedList.slice(shiftReq).concat(combinedList.slice(0, shiftReq));

        // After shifting, the elements need to be reassigned their positions
        grid[i].splice(i, rowLength, ...combinedList.slice(0, rowLength)); // First row

        for (let j = i + 1; j < m - i - 1; j++) {
            grid[j][n - i - 1] = combinedList[rowLength + j - i - 1]; // Last elements of middle rows
        }

        grid[m - i - 1].splice(i, rowLength, ...combinedList.slice(rowLength + colLength, rowLength + colLength + rowLength).reverse()); // Last row

        for (let j = m - i - 2; j > i; j--) {
            grid[j][i] = combinedList[rowLength + colLength + rowLength + m - i - 2 - j]; // First elements of middle rows
        }
    }

    return grid;
};
