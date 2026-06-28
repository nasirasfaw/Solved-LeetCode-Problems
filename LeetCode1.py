class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sn = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in sn:
                return [sn[complement], i]
                break

            sn[num] = i
