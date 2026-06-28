class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == val and nums[j] != val:
                    nums[i], nums[j] = nums[j], nums[i]
        p = 0
        for x in nums:
            if x != val:
                p += 1
        return p
