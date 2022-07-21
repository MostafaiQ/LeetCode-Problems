class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if nums[i] in hashTable:
                return [i, hashTable.get(nums[i])]
            else:
                hashTable[complement] = i
            