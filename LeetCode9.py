class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1 = list(str(abs(x)))
        x1.reverse()
        x1 = "".join(x1)
        x1 = int(x1)
            
        return x == x1
        
