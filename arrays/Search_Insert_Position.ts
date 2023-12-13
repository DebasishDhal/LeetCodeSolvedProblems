/*
Beats 85% of users in runtime.
*/
function searchInsert(nums: number[], target: number): number {
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
        for (let i = 0; i<nums.length-1; i++){
            if (nums[i]<target && nums[i+1]>target){
                return i+1;
            }
        }
    }
};
