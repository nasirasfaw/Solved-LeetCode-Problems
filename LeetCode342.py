class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = any(4**k == n for k in range(16))  #the limits for n is <= 2**31 - 1 around ~ 4**15

        return x
