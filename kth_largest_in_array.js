/**
 * @param {string[]} nums
 * @param {number} k
 * @return {string}
 */
var kthLargestNumber = function(nums, k) {
    for(let i = 0; i < k; i++){
        let maxIndex = i;
        for(let j = i + 1; j < nums.length; j++){
            if(nums[maxIndex].length < nums[j].length || (nums[maxIndex].length == nums[j].length) && nums[maxIndex] < nums[j]){
                maxIndex = j
            }
        }
        [nums[maxIndex], nums[i]] = [nums[i], nums[maxIndex]]
    }
  
    return nums[k - 1]
  };