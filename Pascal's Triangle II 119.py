class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        temp = []
        for j in range(rowIndex+1):
            temp.append(int(factorial(rowIndex)/(factorial(j)*factorial(rowIndex-j))))
        return temp