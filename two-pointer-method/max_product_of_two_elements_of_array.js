/**
 * @param {number[]} nums
 * @return {number}
 Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

Constraints:
  2 <= nums.length <= 500
  1 <= nums[i] <= 10^3
 */


var maxProduct = function(nums) {
    nums.sort((a,b)=>a-b);

    let left = 0;
    let right = nums.length-1;

    let res = 0
    while (left<right) {

        let res_new = (nums[left]-1)*(nums[right]-1)

        if (res_new < res){
            right = right-1
        }

        else{
            left = left+1
            res = res_new
        }

    }
    return res;
};
