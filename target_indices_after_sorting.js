/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var targetIndices = function(nums, target) {
    const indices = []
    for(let i = 0; i < nums.length; i ++){
        for(let j = i; j < nums.length; j++){
            if(nums[i] > nums[j]) {
                [nums[i], nums[j]] = [nums[j], nums[i]]
            }
        }
        if(nums[i] == target) indices.push(i)
    }
    return indices
};