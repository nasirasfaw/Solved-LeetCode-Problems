class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s1 = int(a, 2)
        s2 = int(b, 2)
        s = s1 + s2
        c = bin(s)[2:]
        return c
