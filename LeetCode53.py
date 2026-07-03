class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        current = nums[0]
        best = nums[0]

        for j in range(1, len(nums)):
            current = max(nums[j], current + nums[j])
            best = max(best, current)

        return best
      
      #Alternatively,
      #for x in nums[1:]:
        #current = max(x, current + x)
        #best = max(best, current)
