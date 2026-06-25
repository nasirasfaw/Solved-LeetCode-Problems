class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            dg = [int(d) for d in str(n)]
            s = sum(k*k for k in dg)
            seen.add(n)
            n = s
            
        return n == 1
