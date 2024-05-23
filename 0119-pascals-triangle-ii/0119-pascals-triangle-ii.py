class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        last = self.getRow(rowIndex-1)
        row = [1]
        for i in range(len(last)-1):
            row.append(last[i]+last[i+1])
        row.append(1)

        return row