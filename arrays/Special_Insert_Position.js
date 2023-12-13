/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 Beats 70% of users in runtime.
 */
var searchInsert = function(nums, target) {
    if (nums.includes(target)){
        return nums.indexOf(target)
    }

    else if (target<nums[0]){
        return 0
    }

    else if (target>nums[nums.length-1]){
        return nums.length
    }

    else {
        for (i = 0; i<nums.length-1; i++){
            if (nums[i]<target && nums[i+1]>target){
                return i+1;
            }
        }
    }

};
