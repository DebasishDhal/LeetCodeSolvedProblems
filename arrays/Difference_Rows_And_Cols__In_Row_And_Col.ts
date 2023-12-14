function onesMinusZeros(grid: number[][]): number[][] {
    let len = grid.length
    let wid = grid[0].length

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
