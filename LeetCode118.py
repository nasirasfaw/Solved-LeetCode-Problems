class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        c = [[1]]

        for i in range(1, numRows):
            row = [1]
            
            for j in range(1, i):
                row.append(c[i-1][j-1] + c[i-1][j])
            
            row.append(1)
            c.append(row)

        return c
