/*
100th percentile

An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).

Constraints:

m == img.length
n == img[i].length
1 <= m, n <= 200
0 <= img[i][j] <= 255
*/
function imageSmoother(img: number[][]): number[][] {
    let smoothImg = []
    const rows = img.length
    const cols = img[0].length

    for (let i=0; i<rows; i++){
        let smoothRow = []
        for (let j=0; j<cols; j++){
            let total = 0
            let count = 0
            for (let row = Math.max(i-1,0); row<Math.min(i+2,rows); row++){
                for (let col = Math.max(j-1,0); col<Math.min(j+2,cols); col++){
                    total += img[row][col]
                    count += 1
                }
            }
            smoothRow.push(Math.floor(total/count))
        }
        smoothImg.push(smoothRow)
    }
    return smoothImg
};
