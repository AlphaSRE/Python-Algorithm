class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for i in range(1,rowIndex+1):
            row = map(lambda x,y: x+y, [0]+row, row+[0])
        return row