class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            k = haystack.index(needle)
        else:
            k = -1
        return k 
