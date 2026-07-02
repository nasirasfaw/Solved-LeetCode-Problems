class Solution:
    def reverseVowels(self, s: str) -> str:
        v = ["a", "e", "i", "o", "u"]
        pos = []
        sv = []
        for i in range(len(s)):
            if s[i].lower() in v:
                pos.append(i)
                sv.append(s[i])
        sv = sv[::-1]
        s = list(s)
        for pos, ch in zip(pos, sv):
            s[pos] = ch
        s = "".join(s)

        return s
