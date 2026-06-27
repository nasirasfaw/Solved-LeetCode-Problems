class Solution:
    def findComplement(self, num: int) -> int:
        b = bin(num)[2:]
        a = b.replace("0", "x").replace("1", "0").replace("x", "1")

        return int(a, 2)
