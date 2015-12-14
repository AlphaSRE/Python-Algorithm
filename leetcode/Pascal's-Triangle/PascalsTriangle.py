class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        row = [1]
        rowlist = [row]
        for i in range(1,numRows):
            row = map(lambda x,y: x+y, [0]+row, row+[0])
            rowlist.append(row)
        return rowlist[:numRows]