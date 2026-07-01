class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        common = ""
        
        m = min(len(x) for x in strs)
        for i in range(m):
            if all(x[i] == strs[0][i] for x in strs):
                common += strs[0][i]
            else:
                break

        return common
