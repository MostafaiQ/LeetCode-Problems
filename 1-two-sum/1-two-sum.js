/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let hashMap = new Map();
    
    for (var i = 0; i < nums.length; i++){
        var complement = target - nums[i]
        if (hashMap.has(complement)) {
            return [hashMap.get(complement),i];
        }
        else{
            hashMap.set(nums[i],i);
        }
    }
    return [];
};