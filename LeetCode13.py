class Solution:
    def romanToInt(self, s: str) -> int:
        rom_values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000} 
        int_value = 0
        for i in range(len(s)):
            if i < len(s)-1 and rom_values[s[i]] < rom_values[s[i+1]]:
                int_value -= rom_values[s[i]]
            else:
                int_value += rom_values[s[i]]

        return int_value
