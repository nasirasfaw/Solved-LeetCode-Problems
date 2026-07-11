class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s1 = []
        for i in range(len(s)):
            if i % k == 0:
                s1.append(s[i:i+k])
        for i in range(len(s1)):
            if i % 2 == 0:
                s1[i] = s1[i][::-1]
        s1 = "".join(s1)
        return s1
