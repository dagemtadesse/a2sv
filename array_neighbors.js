/**
 * @param {number[]} nums
 * @return {number[]}
 */
var rearrangeArray = function(nums) {
    while(true){
        let failed = false
        for(let i = 1; i< nums.length -1; i++){
            if((nums[i -1] + nums[i + 1])/ 2 === nums[i]){
                [nums[i + 1], nums[i]] = [nums[i], nums[i + 1]]
                failed = true
            }
        }
        if(!failed) break
    }
    return nums
};