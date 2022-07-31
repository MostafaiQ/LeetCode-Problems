/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let hashMap = new Map();
    
    for (var i = 0; i < nums.length; i++){
        var complement = target - nums[i]
        if (!hashMap.get(nums[i])) {
            hashMap.set(complement, i);
        }
    }
    for (var i = 0; i < nums.length; i++) {
        if (hashMap.get(nums[i]) != undefined && (i != hashMap.get(nums[i]))){
            return [i,hashMap.get(nums[i])];
        }
    }
    return [];
};