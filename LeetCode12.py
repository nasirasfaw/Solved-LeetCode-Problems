class Solution:
    def intToRoman(self, num: int) -> str:
        r = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        d = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        rom = []
        for i in range(len(d)):
            while num >= d[i]:
                rom.append(r[i])
                num -= d[i]
        rom = "".join(rom)
        return rom
