class Solution:
    def isPalindrome(self, s: str) -> bool:

        s2 = ""

        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                s2 += s[i]
        for i in range(len(s2)):
            if s2[i].isalpha():
                s2 = s2.replace(s2[i], s2[i].lower())

        return s2 == s2[::-1]
