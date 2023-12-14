/**
 * @param {number[][]} grid
 * @return {number[][]}
 You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:

Let the number of ones in the ith row be onesRowi.
Let the number of ones in the jth column be onesColj.
Let the number of zeros in the ith row be zerosRowi.
Let the number of zeros in the jth column be zerosColj.
diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
Return the difference matrix diff.

#Beats 100% of users in runtime.
 */
var onesMinusZeros = function(grid) {

    const len = grid.length
    const wid = grid[0].length

    let rows = Array(len).fill(0)
    let cols = Array(wid).fill(0)

    for (let i = 0; i < len; i++){
        for (let j = 0; j < wid; j++){
            rows[i] += grid[i][j]
            cols[j] += grid[i][j]
        }
    }

    for (let i = 0; i < len; i++){
        for (let j = 0; j < wid; j++){
            grid[i][j] = 2*(rows[i]+cols[j]) - len - wid
        }
    }

    return grid
};
