class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        mid = len(nums) // 2
        right = len(nums) - 1
        while True:
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
                mid = (left + right) // 2
            elif target < nums[mid]:
                right = mid - 1
                mid = (left + right) // 2
            if left > mid or right < mid:
                return -1
                