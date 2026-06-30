class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ns = sorted(nums)
        tr = []
        for k in range(len(nums)-2):
            i = k+1 
            j = len(nums)-1
            while i < j:
                s = ns[k] + ns[i] + ns[j]
                if  s < 0:
                    i += 1
                elif s > 0:
                    j -= 1
                elif s == 0:
                    tr.append([ns[k], ns[i], ns[j]])
                    i += 1
                    j -= 1
        seen = set()
        for x in tr:
            seen.add(tuple(x))
        triplets = []
        for y in seen:
            triplets.append(list(y))
        return triplets
