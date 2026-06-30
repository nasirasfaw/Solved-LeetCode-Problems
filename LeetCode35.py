class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for i in range(1, len(nums)):
                if nums[i-1] < target and nums[i] > target:
                    return i
        if target < nums[0]:
            return 0
        elif target > nums[len(nums)-1]:
            return len(nums)
