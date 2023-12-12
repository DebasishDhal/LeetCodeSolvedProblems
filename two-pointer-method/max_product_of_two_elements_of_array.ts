function maxProduct(nums: number[]): number {
    let left = 0;
    let right = nums.length-1;

    let res = 0

    nums.sort((a,b) => a - b);
    
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
