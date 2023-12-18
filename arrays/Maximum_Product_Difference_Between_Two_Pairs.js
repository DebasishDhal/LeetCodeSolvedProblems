/*
The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.

Constraints:

4 <= nums.length <= 104
1 <= nums[i] <= 104
*/

/**
 * @param {number[]} nums
 * @return {number}
 */



//Horrible performance, beats only 5% of the users.
var maxProductDifference = function(nums) {
    let 
        firstBig = 0,
        secondBig = 0,
        firstSmall = Infinity,
        secondSmall = Infinity
        ;

    for (let num of nums){
        if (num > firstBig ){
            [firstBig, secondBig] = [num, firstBig]
        }
        else if (num > secondBig){
            secondBig = num
        }

        if (num < secondSmall) {
            [firstSmall,secondSmall] = [secondSmall, num]
        }

        else if (num < firstSmall){
            firstSmall = num
        }

        console.log(num, secondSmall, firstSmall, secondBig, firstBig)
    }

    return (firstBig*secondBig-firstSmall*secondSmall)
};

/**
 * @param {number[]} nums
 * @return {number}
 Beats 50% of users.
 */
var maxProductDifference = function(nums) {
    nums.sort((a,b)=>(a-b))
    len = nums.length
    return (nums[len-1]*nums[len-2]- nums[0]*nums[1])
};
