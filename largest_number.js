/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function (nums) {
    for(let i = 0; i < nums.length; i++){
        for(let j = 0; j < nums.length - 1; j++){
            if(`${nums[j]}${nums[j + 1]}` < `${nums[j + 1]}${nums[j]}`){
                [nums[j], nums[j + 1]] = [nums[j + 1], nums[j]]
            }
        }
    }
      let result = ""
    for(let num of nums){
        result += num
    }
    return Number(result)  == 0 ?  "0" : result
  }