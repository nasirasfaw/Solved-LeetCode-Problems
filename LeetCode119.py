class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        from math import comb
        row = []
        for i in range(rowIndex+1):
            row.append(comb(rowIndex, i))

        return row
