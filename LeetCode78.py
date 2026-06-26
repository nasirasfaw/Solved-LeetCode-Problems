from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset = []
        for i in range(len(nums)+1):
            for subset in combinations(nums, i):
                powerset.append(list(subset))
        return powerset
