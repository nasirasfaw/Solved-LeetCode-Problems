class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    
        nums = list(set(nums))
        nums.sort()
        gr = []
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[j-1]+1:
                gr.append(nums[i:j])
                i = j
        gr.append(nums[i:])

        longest = max(len(x) for x in gr)

        return longest
