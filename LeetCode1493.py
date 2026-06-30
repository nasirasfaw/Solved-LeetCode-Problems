class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            longest = len(nums)-1
        else:
            gr = []
            i = 0
            for j in range(1, len(nums)):
                if nums[j] != nums[j-1]:
                    gr.append(nums[i:j])
                    i = j
            gr.append(nums[i:])
            
            longest = 0

            for i, g in enumerate(gr):
                if g[0] == 1:
                    longest = max(longest, len(g))
                elif len(g) == 1 and 0 < i < len(gr)-1:
                    longest = max(longest, len(gr[i-1]) + len(gr[i+1]))
        return longest
