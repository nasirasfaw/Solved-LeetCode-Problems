class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        from math import isqrt
        s = 1
        if num == 1:
            s = 0
        for i in range(2, isqrt(num) + 1):
            if num % i == 0:
                s += i
                if i != (num // i): # not to count isqr(n) twice     
                    s += (num // i)
        return s == num
