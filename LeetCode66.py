class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dig = []

        for x in digits:
            dig.append(str(x))

        digits = "".join(dig)

        digits = int(digits) + 1

        n_nums = [d for d in str(digits)]
        n_nums = "".join(n_nums)
        n_nums = int(n_nums)
        n_nums = [int(x) for x in str(n_nums)]

        return n_nums
