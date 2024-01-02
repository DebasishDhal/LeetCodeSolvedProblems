/*
 * @param {number[]} nums
 * @return {number[][]}
You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.
 */
var findMatrix = function(nums) {
    let res = []

    for (const num of nums){
        let found = false
        for (let row of res){
            if (!row.includes(num)){
                found = true
                row.push(num)
                break
            }
        }
        if (!found){
            res.push([num])
        }
        
    }
    return res
};
